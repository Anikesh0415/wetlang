"""
WetLang Biocybersecurity Protections & Hardware Interlocks
Provides capability verification, water-window voltage clamp,
sliding charge balance watchdog, epileptiform runaway breaker,
and fail-safe interlock state management.
"""

from typing import List, Optional


class CapabilityVerifier:
    """
    Static and bytecode capability security verifier.
    Enforces that declared bytecode capability bitmasks cover all utilized opcodes.
    """

    def verify_capabilities(self, declared_caps: int, used_caps: int) -> bool:
        """
        Verifies that all used capability flags are authorized by declared_caps.
        Tier 0 compute (0x0000) is always authorized.
        """
        # All bits in used_caps must be present in declared_caps
        return (used_caps & ~declared_caps) == 0


class InterlockManager:
    """
    Hardware interlock manager simulating the cycle-accurate hardware watchdog.
    Tracks fail-safe lockout state, zeroes DAC voltages upon any safety trip,
    and produces post-mortem diagnostic telemetry.
    """

    STATE_OPERATIONAL = 0
    STATE_HALTED_SAFETY_LOCKOUT = 1

    def __init__(self, channel_count: int = 64):
        self.channel_count: int = channel_count
        self.state: int = self.STATE_OPERATIONAL
        self.dac_voltages: List[float] = [0.0] * channel_count
        self.diagnostic_report: str = "Interlocks normal. No safety trips."
        self.tripped_electrode: Optional[int] = None
        self.trip_reason: Optional[str] = None

    def get_state(self) -> int:
        """Returns the numeric interlock state (0 = OPERATIONAL, 1 = HALTED_SAFETY_LOCKOUT)."""
        return self.state

    def get_state_name(self) -> str:
        """Returns human-readable state string: 'OPERATIONAL' or 'HALTED_SAFETY_LOCKOUT'."""
        if self.state == self.STATE_OPERATIONAL:
            return "OPERATIONAL"
        return "HALTED_SAFETY_LOCKOUT"

    def trip_charge_imbalance(self, electrode: int) -> None:
        """
        Simulates sliding charge balance watchdog trip on specified electrode.
        Immediately zeroes all electrode DACs, transitions state to HALTED_SAFETY_LOCKOUT,
        and records post-mortem diagnostic report.
        """
        self.state = self.STATE_HALTED_SAFETY_LOCKOUT
        self.tripped_electrode = electrode
        self.trip_reason = "ERR_CHARGE_IMBALANCE"
        self.dac_voltages = [0.0] * self.channel_count
        self.diagnostic_report = (
            f"ERR_CHARGE_IMBALANCE: Net charge imbalance exceeded safety threshold (0.5 nC over 10 ms) "
            f"on electrode {electrode}. All 64 stimulation DACs forced to 0.0V fail-safe."
        )

    def trip_epileptiform_runaway(self) -> None:
        """
        Simulates epileptiform runaway breaker trip.
        Immediately zeroes all electrode DACs, transitions state to HALTED_SAFETY_LOCKOUT,
        and records post-mortem diagnostic report.
        """
        self.state = self.STATE_HALTED_SAFETY_LOCKOUT
        self.tripped_electrode = None
        self.trip_reason = "ERR_EPILEPTIFORM_RUNAWAY"
        self.dac_voltages = [0.0] * self.channel_count
        self.diagnostic_report = (
            "ERR_EPILEPTIFORM_RUNAWAY: Epileptiform runaway firing breaker tripped "
            "(>150 Hz on >35% channels for 50 ms). All 64 stimulation DACs forced to 0.0V fail-safe."
        )

    def get_dac_voltages(self) -> List[float]:
        """Returns instantaneous voltages across all electrode DACs."""
        return list(self.dac_voltages)

    def get_diagnostic_report(self) -> str:
        """Returns post-mortem diagnostics telemetry record upon interlock trip."""
        return self.diagnostic_report
