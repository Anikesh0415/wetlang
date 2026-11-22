#include "../include/wet_crt.h"
#include "../include/wet_hal.h"
#include "../include/wetvm_vm.h"
#include "../include/biophysics.h"

#if defined(_WIN32)
typedef union _LARGE_INTEGER {
    struct {
        uint32_t LowPart;
        int32_t  HighPart;
    } s;
    int64_t QuadPart;
} LARGE_INTEGER;

#ifdef __cplusplus
extern "C" {
#endif
int __stdcall QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount);
int __stdcall QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency);
#ifdef __cplusplus
}
#endif
#else
#include <time.h>
#endif

/* Monotonic time helper using genuine hardware high-resolution timing */
#if defined(_WIN32)
uint64_t wet_hal_get_time_us(void) {
    static LARGE_INTEGER s_freq;
    static int s_inited = 0;
    if (!s_inited) {
        QueryPerformanceFrequency(&s_freq);
        s_inited = 1;
    }
    LARGE_INTEGER counter;
    QueryPerformanceCounter(&counter);
    return (uint64_t)((counter.QuadPart * 1000000ULL) / s_freq.QuadPart);
}
#else
uint64_t wet_hal_get_time_us(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)(ts.tv_sec * 1000000ULL + ts.tv_nsec / 1000ULL);
}
#endif

/* =========================================================================
 * HAL Core Lifecycle Implementation
 * ========================================================================= */

wet_hal_context_t* wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config) {
    wet_hal_context_t* hal = (wet_hal_context_t*)calloc(1, sizeof(wet_hal_context_t));
    if (!hal) return NULL;

    hal->mode = mode;
    if (config) {
        hal->config = *config;
    } else {
        hal->config.mode = mode;
        hal->config.max_ephys_channels = 64;
        hal->config.num_pumps = 8;
        hal->config.num_valves = 8;
        hal->config.num_flow_sensors = 8;
        hal->config.enable_dead_head_protection = 1;
        hal->config.enable_crowbar_fastpath = 1;
        for (int i = 0; i < 8; ++i) {
            hal->config.valve_for_pump[i] = 0xFF;
        }
    }

    /* Open default valves 0..7 as open or closed */
    for (int i = 0; i < 8; ++i) {
        hal->valve_states[i] = 1; /* Default open for perfusion lines */
        hal->pump_rates_ul_min[i] = 0.0f;
        hal->flow_rates_ul_min[i] = 0.0;
    }

    return hal;
}

void wet_hal_destroy(wet_hal_context_t* hal) {
    if (!hal) return;

    /* Shutdown all registered drivers */
    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        if (hal->drivers[i] && hal->drivers[i]->ops && hal->drivers[i]->ops->shutdown) {
            hal->drivers[i]->ops->shutdown(hal->drivers[i]);
        }
    }

    free(hal);
}

wet_hal_status_t wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config) {
    if (!vm) return WET_HAL_ERR_NULL_PTR;

    wet_hal_context_t* hal = wet_hal_create(mode, config);
    if (!hal) return WET_HAL_ERR_IO;

    return wet_hal_attach(vm, hal);
}

wet_hal_status_t wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal) {
    if (!vm) return WET_HAL_ERR_NULL_PTR;

    vm->hal = hal;
    if (hal) {
        hal->vm = vm;
    }
    return WET_HAL_OK;
}

wet_hal_context_t* wet_hal_get_context(wet_vm_t* vm) {
    if (!vm) return NULL;
    return vm->hal;
}

wet_hal_status_t wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (mode > WET_HAL_MODE_HIL_LOOPBACK) return WET_HAL_ERR_INVALID_MODE;

    hal->mode = mode;
    hal->config.mode = mode;

    /* Propagate mode to all registered drivers */
    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        if (hal->drivers[i]) {
            hal->drivers[i]->mode = mode;
        }
    }
    return WET_HAL_OK;
}

wet_hal_mode_t wet_hal_get_mode(const wet_hal_context_t* hal) {
    if (!hal) return WET_HAL_MODE_SIMULATED;
    return hal->mode;
}

wet_hal_status_t wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver) {
    if (!hal || !driver) return WET_HAL_ERR_NULL_PTR;
    if (hal->driver_count >= WET_HAL_MAX_DRIVERS) return WET_HAL_ERR_BUFFER_FULL;

    /* Check for duplicate registration */
    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        if (hal->drivers[i] == driver) {
            return WET_HAL_OK;
        }
    }

    hal->drivers[hal->driver_count++] = driver;
    driver->mode = hal->mode;

    /* Bind fast direct routing slots */
    switch (driver->driver_type) {
        case WET_HAL_DRIVER_EPHYS:
            if (!hal->ephys_driver) hal->ephys_driver = driver;
            break;
        case WET_HAL_DRIVER_PUMP:
            if (!hal->pump_driver) hal->pump_driver = driver;
            break;
        case WET_HAL_DRIVER_VALVE:
            if (!hal->valve_driver) hal->valve_driver = driver;
            break;
        case WET_HAL_DRIVER_FLOW:
            if (!hal->flow_driver) hal->flow_driver = driver;
            break;
        case WET_HAL_DRIVER_CAN_BUS:
            if (!hal->can_driver) hal->can_driver = driver;
            break;
        default:
            break;
    }

    /* Initialize driver if not already initialized */
    if (!driver->is_initialized && driver->ops && driver->ops->init) {
        wet_hal_status_t st = driver->ops->init(driver, NULL);
        if (st == WET_HAL_OK) {
            driver->is_initialized = 1;
            driver->is_active = 1;
        }
        return st;
    }

    driver->is_active = 1;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver) {
    if (!hal || !driver) return WET_HAL_ERR_NULL_PTR;

    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        if (hal->drivers[i] == driver) {
            /* Clear specialized slot if matching */
            if (hal->ephys_driver == driver) hal->ephys_driver = NULL;
            if (hal->pump_driver == driver)  hal->pump_driver = NULL;
            if (hal->valve_driver == driver) hal->valve_driver = NULL;
            if (hal->flow_driver == driver)  hal->flow_driver = NULL;
            if (hal->can_driver == driver)   hal->can_driver = NULL;

            /* Shift array left */
            for (uint32_t j = i; j < hal->driver_count - 1; ++j) {
                hal->drivers[j] = hal->drivers[j + 1];
            }
            hal->drivers[hal->driver_count - 1] = NULL;
            hal->driver_count--;
            driver->is_active = 0;
            return WET_HAL_OK;
        }
    }
    return WET_HAL_ERR_DRIVER_NOT_FOUND;
}

wet_hal_driver_t* wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type) {
    if (!hal) return NULL;
    switch (type) {
        case WET_HAL_DRIVER_EPHYS:   return hal->ephys_driver;
        case WET_HAL_DRIVER_PUMP:    return hal->pump_driver;
        case WET_HAL_DRIVER_VALVE:   return hal->valve_driver;
        case WET_HAL_DRIVER_FLOW:    return hal->flow_driver;
        case WET_HAL_DRIVER_CAN_BUS: return hal->can_driver;
        default: break;
    }
    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        if (hal->drivers[i] && hal->drivers[i]->driver_type == type) {
            return hal->drivers[i];
        }
    }
    return NULL;
}

/* =========================================================================
 * Actuator & Sensor Routing Implementation
 * ========================================================================= */

wet_hal_status_t wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (pump_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;

    /* Check Dead-Head Overpressure Interlock: If valve is closed and rate > 0, reject immediately! */
    if (hal->config.enable_dead_head_protection && run_flag && rate_ul_min > 0.0) {
        uint8_t target_valve = pump_id;
        if (hal->config.valve_for_pump[pump_id] < 8) {
            target_valve = hal->config.valve_for_pump[pump_id];
        }
        if (hal->valve_states[target_valve] == 0) {
            return WET_HAL_ERR_DEAD_HEAD;
        }
    }

    hal->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
    hal->telemetry.total_rs232_commands++;

    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
        /* In simulated mode or no pump driver, update internal VM registers */
        if (hal->vm) {
            hal->vm->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
        }
        return WET_HAL_OK;
    }

    /* Dispatch to physical or HIL pump driver */
    if (hal->pump_driver->ops && hal->pump_driver->ops->write_pump) {
        return hal->pump_driver->ops->write_pump(hal->pump_driver, pump_id, rate_ul_min, run_flag);
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (pump_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;

    /* Dead-head protection check */
    if (hal->config.enable_dead_head_protection && volume_ul > 0.0) {
        uint8_t target_valve = pump_id;
        if (hal->config.valve_for_pump[pump_id] < 8) {
            target_valve = hal->config.valve_for_pump[pump_id];
        }
        if (hal->valve_states[target_valve] == 0) {
            return WET_HAL_ERR_DEAD_HEAD;
        }
    }

    hal->telemetry.total_rs232_commands++;
    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
        if (hal->vm) {
            hal->vm->pump_dispensed_ul[pump_id] += (float)volume_ul;
        }
        return WET_HAL_OK;
    }

    if (hal->pump_driver->ops && hal->pump_driver->ops->dispense_volume) {
        return hal->pump_driver->ops->dispense_volume(hal->pump_driver, pump_id, volume_ul);
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (valve_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;

    hal->valve_states[valve_id] = (state != 0) ? 1 : 0;
    if (hal->vm) {
        hal->vm->valve_states[valve_id] = hal->valve_states[valve_id];
    }

    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->valve_driver) {
        return WET_HAL_OK;
    }

    if (hal->valve_driver->ops && hal->valve_driver->ops->write_valve) {
        return hal->valve_driver->ops->write_valve(hal->valve_driver, valve_id, state);
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min) {
    if (!hal || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
    if (sensor_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;

    hal->telemetry.total_i2c_transactions++;
    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->flow_driver) {
        if (hal->vm) {
            *out_flow_ul_min = (double)hal->vm->fluid_flow_rate_ul_min[sensor_id];
        } else {
            *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
        }
        return WET_HAL_OK;
    }

    if (hal->flow_driver->ops && hal->flow_driver->ops->read_flow) {
        wet_hal_status_t st = hal->flow_driver->ops->read_flow(hal->flow_driver, sensor_id, out_flow_ul_min);
        if (st == WET_HAL_OK) {
            hal->flow_rates_ul_min[sensor_id] = *out_flow_ul_min;
            if (hal->vm) {
                hal->vm->fluid_flow_rate_ul_min[sensor_id] = (float)(*out_flow_ul_min);
            }
        }
        return st;
    }
    *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;

    hal->telemetry.total_spi_transactions++;
    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
        if (hal->vm) {
            /* Convert pA to uA for simulated biophysics: 1 uA = 1,000,000 pA */
            float current_ua = (float)current_pA / 1000000.0f;
            float dur_ms = (float)duration_us / 1000.0f;
            biophysics_schedule_stim_current(&hal->vm->bio, (uint8_t)channel, current_ua, dur_ms, dur_ms, 0.0f);
        }
        return WET_HAL_OK;
    }

    if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_current) {
        return hal->ephys_driver->ops->stim_current(hal->ephys_driver, channel, current_pA, duration_us);
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;

    hal->telemetry.total_spi_transactions++;
    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
        if (hal->vm) {
            biophysics_schedule_stim_ext(&hal->vm->bio, (uint8_t)channel, voltage_v, p1_ms, p2_ms, 0.0f);
        }
        return WET_HAL_OK;
    }

    if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_voltage) {
        return hal->ephys_driver->ops->stim_voltage(hal->ephys_driver, channel, voltage_v, p1_ms, p2_ms);
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag) {
    if (!hal || !out_spike_flag) return WET_HAL_ERR_NULL_PTR;
    if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;

    if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
        if (hal->vm) {
            *out_spike_flag = hal->vm->spikes[channel];
        } else {
            *out_spike_flag = hal->ephys_spikes[channel];
        }
        return WET_HAL_OK;
    }

    if (hal->ephys_driver->ops && hal->ephys_driver->ops->read_ephys) {
        float volts[64];
        uint8_t spks[64];
        wet_hal_status_t st = hal->ephys_driver->ops->read_ephys(hal->ephys_driver, volts, spks, 64);
        if (st == WET_HAL_OK) {
            *out_spike_flag = spks[channel];
        }
        return st;
    }
    *out_spike_flag = hal->ephys_spikes[channel];
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
    if (!hal || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
    if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;

    if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->measure_impedance) {
        return hal->ephys_driver->ops->measure_impedance(hal->ephys_driver, channel, freq_hz, out_mag_ohms, out_phase_rad);
    }

    /* Fallback default impedance model */
    *out_mag_ohms = 100000.0f; /* 100 kOhm baseline */
    *out_phase_rad = -0.785f;  /* -45 degrees */
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel) {
    if (!hal) return WET_HAL_ERR_NULL_PTR;
    if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;

    if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->active_discharge) {
        return hal->ephys_driver->ops->active_discharge(hal->ephys_driver, channel);
    }
    return WET_HAL_OK;
}

/* =========================================================================
 * Emergency Hardware Crowbar Fast-Path (<100 µs)
 * ========================================================================= */

void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason) {
    if (!vm) return;
    wet_hal_context_t* hal = vm->hal;
    if (!hal) return;

    uint64_t start_us = wet_hal_get_time_us();

    hal->crowbar_tripped = 1;
    hal->crowbar_reason = trip_reason;
    hal->crowbar_tick = vm->current_tick;
    hal->crowbar_timestamp_us = start_us;
    hal->telemetry.total_crowbar_events++;
    hal->telemetry.last_crowbar_reason = trip_reason;
    hal->telemetry.last_crowbar_timestamp_us = start_us;

    /* 1. Instantly zero all pump rates and flow sensor readouts */
    for (int i = 0; i < 8; ++i) {
        hal->pump_rates_ul_min[i] = 0.0f;
        hal->flow_rates_ul_min[i] = 0.0;
        vm->pump_rates_ul_min[i] = 0.0f;
        vm->fluid_flow_rate_ul_min[i] = 0.0f;
    }

    /* 2. Disarm all registered hardware drivers via emergency_stop callback */
    for (uint32_t i = 0; i < hal->driver_count; ++i) {
        wet_hal_driver_t* drv = hal->drivers[i];
        if (drv && drv->ops && drv->ops->emergency_stop) {
            drv->ops->emergency_stop(drv, trip_reason);
        }
    }

    /* 3. Execute active discharge across all ephys channels to clear Faradaic charge */
    for (uint16_t ch = 0; ch < 64; ++ch) {
        wet_hal_active_discharge(hal, ch);
        vm->discharge_charge_nc[ch] += vm->last_charge_nc[ch];
        vm->last_charge_nc[ch] = 0.0f;
        vm->voltages[ch] = 0.0f;
    }

    uint64_t end_us = wet_hal_get_time_us();
    hal->telemetry.crowbar_latency_us = (double)(end_us - start_us);
}

wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal) {
    if (!hal) return NULL;
    return &hal->telemetry;
}

void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id) {
    if (!hal || pump_id >= 8) return;
    hal->config.valve_for_pump[pump_id] = valve_id;
}
