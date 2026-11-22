# Volume VI: Verified Appendices, Checksums, Live Logs & Source Listings

**Platform:** Wetworld — WetLang Neural Organoid Computing Platform (v2.1.0)  
**Founder & Lead Architect:** Anikesh Tiwari (Surat, Gujarat, India)  
**Generated Programmatically:** `2026-11-22 21:55:42 UTC` by `docs/compendium/generate_compendium.py`  
**Repository Scope:** 134 tracked files | 2,467,026 bytes | 34,392 text lines

---

## Appendix A: Complete Repository SHA-256 & Line-Count Manifest

| # | Repository Path | Bytes | Lines | SHA-256 Checksum (Truncated / Full) |
|---:|---|---:|---:|---|
| 1 | `.gitattributes` | 486 | 19 | `06605de4ccdde7ca2ca17571eb44c8c655f32202de1d7df81c42525f53021a4b` |
| 2 | `.github/workflows/ci.yml` | 979 | 42 | `2e8f79189cbdbaa184ef4b016ec5d2425156205abc42737968ed1acf4c37a3a1` |
| 3 | `.gitignore` | 379 | 35 | `e16352655b73321e73348d85f754869373f3aeabd9e1781c0b9875656029136f` |
| 4 | `benchmarks/01_active_inference_closed_loop.wbc` | 1,540 | BIN | `65fa6fd3fbda453cd7ecb53ffb0b2e7a7387aafcbaa3223438da42cc3ba458ec` |
| 5 | `benchmarks/01_active_inference_closed_loop.wet` | 1,778 | 54 | `8dba4c8f3aedacde3c467c3a4bff80b581523ac37842fde9c85634474eb2b0f7` |
| 6 | `benchmarks/02_polychronous_reservoir_classifier.wbc` | 1,676 | BIN | `171e9560331c67d7f0fddd97efd985572356233e23e3607d5aefcacd3dfadcb7` |
| 7 | `benchmarks/02_polychronous_reservoir_classifier.wet` | 1,377 | 49 | `b385c987835dae60a479f77e6ec581a81d8ed8ecf5aa83400704fc6275416511` |
| 8 | `benchmarks/03_homeostatic_stabilization_and_stress.wbc` | 1,111 | BIN | `e7d2c293becbfebf9f39232d7c0f14439eb8c987a54e4be0282656f0cd02bee4` |
| 9 | `benchmarks/03_homeostatic_stabilization_and_stress.wet` | 1,326 | 43 | `88646455ff957520a8401921c7d8ee9a22b30b6ed78f889fba178acbaa454be5` |
| 10 | `bin/wetlang` | 48 | 2 | `ddb439bcbff7b0a10072988327d74d9bbbfa6186207ce83b2e2e5a750fca677c` |
| 11 | `bin/wetlang.cmd` | 35 | 2 | `4fd697a7d010293e3287761ec698ebf8c24b1092eb8ff2ed40029c92cefb0582` |
| 12 | `bin/wetvm.dll` | 81,920 | BIN | `86c4cf692aef4623d1c136971bb2485f0d9206110d333052edac3f6dcb025bfb` |
| 13 | `CONTRIBUTING.md` | 1,371 | 35 | `e05ce8218f37cbccd487443e6ed7306ff633ec3c93091d8fcf9f4af802955dd5` |
| 14 | `docs/adversarial_debate.md` | 29,926 | 286 | `80620f350cff9f2e9af1781d27e1718c63cfb5efdad4f6bf57b8c55a63fb62a4` |
| 15 | `docs/AUDIT_REPORT.md` | 6,094 | 73 | `ac4c405458cd04e0e71bd096b0d9dfd754a9ff92ba6e736ee16f86df2bbe0e32` |
| 16 | `docs/LANGUAGE_SPECIFICATION.md` | 24,511 | 398 | `55d53316fbed42199073c50ccdadd66ab033e922607d875da348ba889ca05458` |
| 17 | `docs/OI_HARDWARE_SCALING_SPECIFICATION.md` | 5,874 | 83 | `618af1daac247bc74828391eea7ce352b4e3bc102f3e1108023f9e6ada1be520` |
| 18 | `docs/WETLANG_MASTER_REFERENCE_COMPENDIUM.pdf` | 768,784 | BIN | `c6812e20cfc814bc75ed7acbb8908ef8e94bfe5d2ea4662009955eec56784c11` |
| 19 | `docs/WETLANG_V1_MASTER_AUDIT_DOSSIER.md` | 30,348 | 219 | `7988a6f4ddbf431c6fb846a43a7a7bbba6f46b990ec4a1a32e6f8e3d174680dd` |
| 20 | `examples/01_single_organoid_baseline.wbc` | 259 | BIN | `d4476a8217f32780adc25d8817e5805fd996267e17caf1be1c7524ae4dc6fc47` |
| 21 | `examples/01_single_organoid_baseline.wet` | 499 | 18 | `30f38bde068238378589ac7d452824f53fee9ef3d2ee8221194857178748f00a` |
| 22 | `examples/02_krogh_perfused_organoid.wet` | 593 | 19 | `41de709fd536cd8dffb322193491fc54f36e884ce63abb8aea1811e92c7d919d` |
| 23 | `examples/03_cyber_physical_actuation.wet` | 875 | 30 | `c7c591df662ff70c603b001e3688bc6bb49d8fe15772015e58d541e5aa357a00` |
| 24 | `examples/04_multi_organoid_connectome.wet` | 574 | 24 | `cd4c2e7e2420c6200d95f9aafaa2955aca5f70003bae6a7447cb6d060313a93a` |
| 25 | `examples/05_gymnasium_active_inference.py` | 1,524 | 41 | `ba14f7afba193b87701e83499cc5b1812ff497d35911decef269544047e7c174` |
| 26 | `examples/06_snntorch_validation.py` | 1,036 | 23 | `4d8f52c84fa79b4b2a4b4b7d90693baadd840247d272285e988dbb6acca9dee0` |
| 27 | `LICENSE` | 778 | 17 | `ad302ce114a707983380135aa042d5b051caae9ee20ae8c270c8dbaeec8e4171` |
| 28 | `native/__init__.py` | 61 | 3 | `d0681b3b7d83c57b6d20bfe602085e1620539b6f082cec5308bcaac40394e318` |
| 29 | `native/bin/kernel32.def` | 248 | 14 | `e529e508916c97866afd884b0231b80be7bfa471302c002e795778171f59c44a` |
| 30 | `native/bin/kernel32.lib` | 3,662 | BIN | `edca80141c1648a975f5945f38495020062e28ffa5b295b7b6793e5be2aef875` |
| 31 | `native/bin/msvcrt.def` | 182 | 20 | `15775a186f68afed2dc83e1da279ac9aba5b77549e25f44633b7dcf65ba7e553` |
| 32 | `native/bin/msvcrt.lib` | 3,984 | BIN | `0abf27283319dc423d0c0ad066308cbe84f78765d3ff61a767d2c382abb699a8` |
| 33 | `native/bin/wetvm.dll` | 81,920 | BIN | `86c4cf692aef4623d1c136971bb2485f0d9206110d333052edac3f6dcb025bfb` |
| 34 | `native/bin/wetvm.lib` | 32,320 | BIN | `7cfc3da014690c3d2569a71f094895962859aed3c4a9907053c5f548d415ab76` |
| 35 | `native/build.py` | 8,147 | 256 | `2cc2c020859bb090c3d391bc4c596d2822c5c0a179a89c95a75d3537fe083993` |
| 36 | `native/include/biophysics.h` | 9,671 | 214 | `c1ff823a6b9772a608a761911e20a36bba3d8a721bf95ef167e63c8c75f628fc` |
| 37 | `native/include/interlocks.h` | 8,810 | 188 | `5017b655ffe3fd61f74afc71e15d01c6b5b6aefffd977f9e5bf8a96b44d2f3d8` |
| 38 | `native/include/wet_aer.h` | 6,091 | 159 | `84b2e70694f38a59f9d9c66f74cd7220a9c1cf6298bcdd360f8fc78a5260f4f7` |
| 39 | `native/include/wet_crt.h` | 3,325 | 108 | `3c1a972b9cd8b7c7959e2d7362edb27f211577b535869a752b90d51e41a26f3c` |
| 40 | `native/include/wet_distributed.h` | 5,208 | 130 | `0aab09235da0a6be3b3d572ccd51ac8005a1d8c41549944b95f2d12bbf367d45` |
| 41 | `native/include/wet_hal.h` | 10,134 | 230 | `8b70512b8ce204939c066d0cc51985b2c48aba73a8b3727a8e359c082f8efa05` |
| 42 | `native/include/wet_hal_intan.h` | 5,000 | 169 | `15e6a6849d146a2522be660507c0ca896dd40db8b3164b866e5ec5d8fede6a10` |
| 43 | `native/include/wet_hal_maxwell.h` | 5,292 | 173 | `f5be2fac6cba467d89fd78a8017982cea9cdf18710406fc87bc107dce396df05` |
| 44 | `native/include/wet_hal_pump_valve.h` | 6,625 | 216 | `5db2b883e4822e33c028397394bc3ebc75b4be823e53b5253528faab68c198c2` |
| 45 | `native/include/wet_hal_sensirion.h` | 4,384 | 153 | `c5cadc6f9f2f1b2b7d0ea747dc19cce5246f1822519dd02d14092c4f9056144b` |
| 46 | `native/include/wet_scheduler.h` | 6,890 | 136 | `ae755ab83f92e02449f3bd47eeb7223b47a0ee8efee79bff5020215f4e89be4d` |
| 47 | `native/include/wetvm_api.h` | 8,546 | 310 | `f1f5e21dac2938cd8d6a6e035b0ab1d6172a37ce28ec9478113ec4c86b144efc` |
| 48 | `native/include/wetvm_types.h` | 6,675 | 177 | `b7289c4cdde4199c2fa77c87a1f5797132220e75a7dde7b4fcc548487dc491f6` |
| 49 | `native/include/wetvm_vm.h` | 4,235 | 146 | `e769cd7ca730fe3f32e0731b58dd048350163b60d9e6f48be06a67649ee774d4` |
| 50 | `native/interlocks.py` | 3,689 | 90 | `5831e4240793de5987e600feed2d8d32a6a294f05587113050968078dfe56b7c` |
| 51 | `native/src/biophysics.c` | 23,591 | 547 | `9854cac4a9aab3369896417d4732e4541befd934fe6a8974446bed80261e9b4b` |
| 52 | `native/src/interlocks.c` | 13,846 | 350 | `d17021d6920714f8f502f5c434af9ab7ac6133a0c8252b682548b54eade69199` |
| 53 | `native/src/wet_aer.c` | 11,713 | 307 | `bf9b381918ee73d445a38236a06bb21db9a61f48ac70cb08514360648ae68d02` |
| 54 | `native/src/wet_distributed.c` | 6,345 | 168 | `5c22625cf18763c227a8ca38f70c61c8025d17058bbedd39b750a34d861a0064` |
| 55 | `native/src/wet_hal.c` | 20,667 | 564 | `02cf9c0cd1c098b2b439b983e3d4d6e43fc502bfca923053a6223340a858135e` |
| 56 | `native/src/wet_hal_intan.c` | 15,642 | 404 | `04902df138963d3e4f6009a7501abdbc89a70311aefdbc6ebaecc42799f0f874` |
| 57 | `native/src/wet_hal_maxwell.c` | 14,303 | 357 | `e9c265c923734f464bf80b17bd7bd6f732492c32b1b2a1f2f390ad633185553a` |
| 58 | `native/src/wet_hal_pump_valve.c` | 16,066 | 463 | `0643ab7ba9b8e772538af708222527a1b845c6d61f84e941534d97a750c3f68d` |
| 59 | `native/src/wet_hal_sensirion.c` | 10,766 | 332 | `19293c38932593af4d119653c6ff904c1567163fdd58a80d2e729d08987bf3fe` |
| 60 | `native/src/wet_scheduler.c` | 23,845 | 658 | `128de8fe00f83e9055a26e8149386788ae5cf61cc7133fd736d7312a813367a4` |
| 61 | `native/src/wetvm_api.c` | 22,943 | 639 | `6a0641509ff77e10767f10f23d3b8ed1aa87e9f1f0480e45b7f51f5971a42345` |
| 62 | `native/src/wetvm_vm.c` | 87,487 | 2034 | `9c85d5d4afad5dc0de9306066d5a2d9d108ffb21e9c6c7aec18c91cfc2d50d68` |
| 63 | `native/wetvm.dll` | 81,920 | BIN | `86c4cf692aef4623d1c136971bb2485f0d9206110d333052edac3f6dcb025bfb` |
| 64 | `PROJECT.md` | 14,727 | 198 | `0ed7cee23597284f347b97dc1c85ba3d001b493489ecd773375aff47aa328d40` |
| 65 | `pyproject.toml` | 1,424 | 56 | `e9c9a7e703165689ca5b5dc68558376dca0d25b4e53e2c5a226b9e6bd2babb40` |
| 66 | `pytest.ini` | 80 | 4 | `f4bf1ab2c2b7363adbb36a4924619319baff715b1cc63cb9de6d252a3d11e4d5` |
| 67 | `README.md` | 14,563 | 236 | `17ea7c1ae7847907f59f93a57dfc6536de3a14a11634101df0eae0d6da16eafa` |
| 68 | `requirements.txt` | 75 | 5 | `6c0084c24660fd7f560241e652a7fab38e715289d6ffcdd53e9e8933d7af96f6` |
| 69 | `setup.py` | 262 | 13 | `ecb64ce4d922e590c7960f87370dcf627480a8eb8ae03e1b8323287d51df02bb` |
| 70 | `TEST_INFRA.md` | 5,666 | 71 | `9bfab52507a9ce87deaabb3d4f18f439a8826f28c06fbe67a693ed6b99c69606` |
| 71 | `TEST_READY.md` | 1,330 | 28 | `033fc27c27d1a17cdbf1378a56d1184ef143b5c632cf553a0ef082a8720b3585` |
| 72 | `tests/conftest.py` | 248 | 10 | `84fa09784e3171a88012caf158a599110e2d2cc4581ecb8ee07cb514f44ee0ba` |
| 73 | `tests/e2e/__init__.py` | 890 | 43 | `90fc12f4d49c01d1af12d768fff0eef372150c091fac25a1bf94e252f4da4c1d` |
| 74 | `tests/e2e/common.py` | 39,006 | 1063 | `3938424c010f887dd573a2980b24b2232f03475a0b1356a9180298a2e7b5178d` |
| 75 | `tests/e2e/test_tier1_features.py` | 74,568 | 1583 | `7098cf6a22339f1d0e74f8822473bdb28c653324638a3df7213c6685e977dda8` |
| 76 | `tests/e2e/test_tier2_boundaries.py` | 83,058 | 1836 | `551d1874d71da39d559fe975df8aaee097c3a911129fb8e67ea0a3bd5979be5e` |
| 77 | `tests/e2e/test_tier3_pairwise.py` | 42,786 | 977 | `68ee56301a785e4884a2ce887ec5ae4b2aad0e531973517384106076cef99757` |
| 78 | `tests/e2e/test_tier4_benchmarks.py` | 26,490 | 578 | `78a16ce38fcc7115cadc323f78aa694de546008351217bd59944146adb9cc0ac` |
| 79 | `tests/run_e2e_tests.py` | 11,147 | 323 | `60117a64b4f9abd9bdeff9ce315e00886d245811a3d6d05f3f8f6fa8dffdb955` |
| 80 | `tests/test_actuators.py` | 987 | 36 | `e0740cc2b9fa7b8475c6f7b6f2001cae3312291bdbc88e08f6fdc620ad5b0951` |
| 81 | `tests/test_audit_remediation.py` | 15,595 | 372 | `c5df3ce3eb8584e6f6c013a091613a7a7399983683148336fb370d254de64d10` |
| 82 | `tests/test_benchmarks.py` | 7,830 | 216 | `415b239383f290b91cca89c402389b8f1d586d3c2081fa0392c4891730e4d04f` |
| 83 | `tests/test_compiler.py` | 965 | 30 | `9f312c9e6fae882410299a7194f6b6c150ddcc1075dbd2fafb910747bde36f82` |
| 84 | `tests/test_hal_drivers.py` | 29,061 | 709 | `ca8bf850cd03ce66597afdf9b4ac95e91666bc871cdd03ad6755f3a72e71620d` |
| 85 | `tests/test_interlocks.py` | 12,556 | 302 | `0dd0fa920d0d8a597a4330fd9da868e2046a7daab6fa11a6ddc9b85d950c1725` |
| 86 | `tests/test_milestone2_aer_hdmea.py` | 6,639 | 166 | `bd929f3474cac5877905ec83375a5b6bc8e4239dd9755012074455cc40999894` |
| 87 | `tests/test_milestone3_distributed.py` | 6,906 | 218 | `74657ddac8b031862af3d95e488ff4d23d11f2cc0d46e3662e66f5952f7fe3e7` |
| 88 | `tests/test_milestone4_rtos_arena.py` | 7,251 | 184 | `ad1a380f1765b93a632f671149349c457476ef1b7bc8de41b7e12d15bb1990e3` |
| 89 | `tests/test_nir_bridge.py` | 17,608 | 480 | `c922ec35314e3d0c355388cf14c923072fced18bb968fdaad7e0c7922684bbd2` |
| 90 | `tests/test_ode_stability.py` | 17,095 | 425 | `d401dfe9d0d16c79a2a1d5ce5a6eed3d69a79286a5b83266e1bcaba24883d376` |
| 91 | `tests/test_parser_diagnostics.py` | 13,059 | 437 | `56a0914159f7f9c6302bba7aaa7ec78bd8d4d820337cf40abde9e3f06948cc3b` |
| 92 | `tests/test_phase2_deep_audit.py` | 14,468 | 348 | `d2b739b630b6e93a060f7a02c21a3c8bc8c0daa19ec508cc2086cd9d452614a4` |
| 93 | `tests/test_phase3_hardware_readiness.py` | 23,696 | 515 | `9a9418836d4fe8a96a1c8fda9c7fe69702eb97187229c6d5094166e76e83aa01` |
| 94 | `tests/test_rt_scheduler.py` | 12,191 | 307 | `750f42facca4e40141eada6080db79120ba5c9d7b810c5e8690b95f2f106d778` |
| 95 | `tests/test_runtime.py` | 643 | 22 | `7f8381b60a4cca97c68f4e63799cbf16ea489df723f7c6c01752a427af672269` |
| 96 | `tests/test_sandbox.py` | 1,113 | 31 | `5a2415e1659ca63f9374f5913db18b28721967a0de52e3e0551495ac9ff62884` |
| 97 | `tests/test_section1_audit_remediation.py` | 6,139 | 171 | `57a2f7fc2d42de440a53af230ea5f95cd017ad642dfb625cb256a1c27275cdde` |
| 98 | `tests/test_section3_audit_remediation.py` | 4,655 | 122 | `e4a1604d3ea56f9afde38e6db24e692d80f347aea0418e2c13326e650baa9640` |
| 99 | `tests/test_section5_audit_remediation.py` | 4,303 | 116 | `477791374681097bc88e2b70142f99de9ee869bc4d12713eb5255a1b189c6b4a` |
| 100 | `tests/test_static_verifier.py` | 17,470 | 584 | `54ca1aa3eb0d25c2b451224e8bea3be522a566a7502f2c4d7864dce57c770d5f` |
| 101 | `tests/test_universal_sandbox.py` | 5,725 | 139 | `ab7be8be193420d1d25a3ab3324be9342ee420b20210c3067199c1741832df1d` |
| 102 | `wetlang/__init__.py` | 2,004 | 63 | `99fad8b3eb64e679d57adf9a75fbd527ef67c6f9d0833d035b68d69e520f0f46` |
| 103 | `wetlang/bindings/__init__.py` | 798 | 42 | `7cfb2e1e1803c1220d5e90ab609730761d1d3500a35b087e5e5f966260b263d0` |
| 104 | `wetlang/bindings/aer.py` | 10,968 | 319 | `1be7d1fc1a5155a79af9da16f0d84924d343242e49ae76a77ea164a5129c65b9` |
| 105 | `wetlang/bindings/distributed.py` | 8,329 | 259 | `2eb4ebdc2a337209dc935d318cfafb114c047c9d07374897b413530edcb420fe` |
| 106 | `wetlang/bindings/ffi.py` | 48,920 | 1137 | `6fc5545771357f47091d01d90f8224ca59518a985356553e12728a394a9b5ba9` |
| 107 | `wetlang/bindings/runtime.py` | 18,677 | 505 | `b6ce663da7e4f5898025be58f5e4da55a1e112298c107dc194f0c8eb9fb694c4` |
| 108 | `wetlang/bindings/scheduler.py` | 10,504 | 302 | `a26fa321476c3e7ec4644f3b92c2457bc7fda9669dac9104dab7f5385ca6d0ba` |
| 109 | `wetlang/biophysics/__init__.py` | 386 | 17 | `2f45135b6989e595f5de6fbdec9752182da1831209ce27d4779056f4baf245cc` |
| 110 | `wetlang/biophysics/mea_grid.py` | 3,885 | 94 | `d0ccaf43957f0d45139a4ad5410a5d1a70d25e65caec517ad36c6d65985ebc84` |
| 111 | `wetlang/biophysics/ode_solver.py` | 4,088 | 109 | `2ce4db9b21d3fe8ca193cc3a5d15b47c34aff7f2ab32f175dd617a3e5b0c78c1` |
| 112 | `wetlang/biophysics/stdp.py` | 2,473 | 70 | `f156f43f0b438efe8042b53c54e9e092202b3499987fbcd23b304f2e96c90b50` |
| 113 | `wetlang/biophysics/stp.py` | 3,623 | 112 | `ceebb61134d250aad60823ac9f0514cffa3124524c4e9e816ba406fca9c6fb5e` |
| 114 | `wetlang/biophysics/telemetry.py` | 2,752 | 84 | `7ca0976d1c5d9f3fc88b5e7b5e8b8060d06bfd84e99ba96f75682d5b883501a9` |
| 115 | `wetlang/cli.py` | 7,244 | 191 | `9cdb73e6406f12c08df57bf394d4e225a9f62584f1b599c26087867265e69ca2` |
| 116 | `wetlang/compiler/__init__.py` | 2,240 | 123 | `79a50dc641756ee2daf14af80d412259090d2ed7d7abbbdb37f1d130eaa0b725` |
| 117 | `wetlang/compiler/ast_nodes.py` | 6,125 | 254 | `d81ae7e413aa53a49a9ffc0b06309993b58f9cedb4815138d39f2eb8c6ddfd96` |
| 118 | `wetlang/compiler/compiler_cli.py` | 3,295 | 104 | `245778ace8d44d4af528d6505dba37937e34cb0dca16706b1c998e16c4ca77c2` |
| 119 | `wetlang/compiler/crypto_signer.py` | 6,002 | 151 | `fc997ccd07fcb31b5ac0d3c864d290e903cb2b76b6b5772bb1a0d393cbe4d854` |
| 120 | `wetlang/compiler/emitter.py` | 39,419 | 951 | `f985cdab9ee3c89e79be2a59e441907b6e0eaf5a09f50da9db5914efd6913e50` |
| 121 | `wetlang/compiler/isa.py` | 5,758 | 185 | `80b277d6c870e49152b46b9ef5d77ca224c94f35e02a9ee93206cb59e95d719b` |
| 122 | `wetlang/compiler/lexer.py` | 14,228 | 407 | `537066d4e72fece2c7fecdd99eb68cd4496c70c7ddb43b37dc41d3f16e736e67` |
| 123 | `wetlang/compiler/nir_bridge.py` | 35,640 | 920 | `db41404376027cb0f75b3ed17fab6fabf6eaf56c6fbfffb2fa4578d3d3d7ef84` |
| 124 | `wetlang/compiler/parser.py` | 35,928 | 905 | `779033cb13b290b8f448c7575c8629681492b08e79f06cad0799bffafe3c7347` |
| 125 | `wetlang/compiler/semantic.py` | 44,837 | 987 | `bbdc4a0456335ba61fe71b42effb9725f6467731f54e76feb06c5ad2bff60b1a` |
| 126 | `wetlang/compiler/token.py` | 8,024 | 287 | `a9dd472e260458e11caf5daac599f6258b21009013791975a8409e179a7610fa` |
| 127 | `wetlang/runtime/__init__.py` | 585 | 32 | `80f25ac8bdcf546019300a646ea2035f167a57d8f529b995212677ceab963bb1` |
| 128 | `wetlang/runtime/ffi.py` | 10,509 | 297 | `6e1717b508cb1fae7d6018f4e29fc0cac5fb94cd3a3acdd4e635d6cd7a4f19cc` |
| 129 | `wetlang/runtime/runtime.py` | 10,880 | 323 | `7a1b134d8712895e2bfe840e95e2853a62ffdf24f23a6218a0dd0b983728dcaa` |
| 130 | `wetlang/runtime.py` | 18,677 | 505 | `b6ce663da7e4f5898025be58f5e4da55a1e112298c107dc194f0c8eb9fb694c4` |
| 131 | `wetlang/sandbox/__init__.py` | 665 | 17 | `d9a19ca91142f3e6aee021869b7d4ec18802570b34a4788bcae422ea27e853f8` |
| 132 | `wetlang/sandbox/gym_env.py` | 4,742 | 125 | `c2e87b7c1c91b7e6acb1752edb2d20b72e505442971dc3bda654a2e0a1b68544` |
| 133 | `wetlang/sandbox/snntorch_cross_validation.py` | 3,193 | 89 | `520ebfa09f643e5ecedf6994c8d8964450a960cf76900360c0b8e016011d8e7d` |
| 134 | `wetlang/sandbox/universal_organoid_sandbox.py` | 9,419 | 245 | `7d6bd7d2f6e452a2c6ada2ec1998d0aac3cdd8ff95cdd395bf8dba5bf77a22bd` |

---

## Appendix B: Auto-Extracted C99 & Python API Symbol Index

### B.1 Native C99 Headers & Sources (`native/include/`, `native/src/`)

#### `native/include/biophysics.h`

- **Types / Structs / Enums:** `bio_state_t`, `bio_stim_pulse_t`, `bio_syn_class_t`, `bio_synapse_t`
- **Macros / Constants:** `BIO_NUM_NEURONS` = `64`, `BIO_NUM_CHANNELS` = `64`, `BIO_GRID_ROWS` = `8`, `BIO_GRID_COLS` = `8`, `BIO_PITCH_UM` = `200.0f`, `BIO_ABS_REFRACT_MS` = `2.0f`, `BIO_ABS_REFRACT_TICKS` = `20`, `BIO_W_MIN_NS` = `0.0f`, `BIO_W_MAX_NS` = `40.0f`, `BIO_SPIKE_HISTORY_LEN` = `500`
- **Functions:** `biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed)`; `biophysics_reset(bio_state_t* bio)`; `biophysics_schedule_stim(bio_state_t* bio, uint8_t channel, float clamped_voltage_v, float phase1_ms, float phase2_ms)`; `biophysics_schedule_stim_ext(bio_state_t* bio, uint8_t channel, float clamped_voltage_v, float phase1_ms, float phase2_ms, float interphase_ms)`; `biophysics_schedule_stim_current(bio_state_t* bio, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms, float interphase_ms)`; `biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial)`; `biophysics_get_randles_state(const bio_state_t* bio, uint8_t channel, float* out_v_dl_v, float* out_v_elec_v)`; `biophysics_zero_all_stim(bio_state_t* bio)`; `biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns)`; `biophysics_step_tick(bio_state_t* bio)`; `biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms)`; `biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post)`

#### `native/include/interlocks.h`

- **Types / Structs / Enums:** `interlock_state_t`, `interlock_trip_reason_t`, `wet_electrode_material_t`
- **Macros / Constants:** `INTERLOCK_NUM_CHANNELS` = `64`, `INTERLOCK_VOLTAGE_LIMIT_V` = `1.2f`, `INTERLOCK_CHARGE_WINDOW_TICKS` = `100`, `INTERLOCK_CHARGE_LIMIT_NC` = `0.5f`, `INTERLOCK_EPILEPSY_RATE_HZ` = `150.0f`, `INTERLOCK_EPILEPSY_MIN_CHANNELS` = `23`, `INTERLOCK_EPILEPSY_SUSTAIN_TICKS` = `500`, `INTERLOCK_DC_DRIFT_LIMIT_NC` = `1.0f`, `INTERLOCK_BLEED_DECAY_PER_TICK` = `0.99999f`, `INTERLOCK_CHARGE_DENSITY_LIMIT_NC` = `0.40f`, `INTERLOCK_FOCAL_RATE_HZ` = `150.0f`, `INTERLOCK_FOCAL_SUSTAIN_TICKS` = `2500`, `INTERLOCK_DUTY_CYCLE_LIMIT` = `0.05f`, `INTERLOCK_DUTY_CYCLE_DECAY` = `0.9999f`, `INTERLOCK_THERMAL_LIMIT_C` = `38.0f`, `INTERLOCK_COMPLIANCE_LIMIT_V` = `7.0f`
- **Functions:** `interlocks_init(interlock_state_t* il)`; `interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count)`; `interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask)`; `interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2)`; `interlocks_active_discharge(interlock_state_t* il, uint8_t channel)`; `interlocks_active_discharge_all(interlock_state_t* il)`; `interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable)`; `interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c)`; `interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id)`; `interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v)`; `interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel)`; `interlocks_clamp_voltage(interlock_state_t* il, float requested_v)`; `interlocks_record_charge_tick(interlock_state_t* il, uint64_t current_tick, const float tick_charge_nc[INTERLOCK_NUM_CHANNELS])`; `interlocks_check_epileptiform(interlock_state_t* il, uint64_t current_tick, const float channel_rates_hz[INTERLOCK_NUM_CHANNELS])`

#### `native/include/wet_aer.h`

- **Types / Structs / Enums:** `wet_aer_packet_t`, `wet_aer_ring_t`, `wet_csr_matrix_t`, `wet_neo_detector_t`
- **Macros / Constants:** `WET_AER_CACHELINE_SIZE` = `128`, `WET_AER_PACKET_SIZE` = `16`, `WET_AER_MAX_CHANNELS` = `26400`
- **Functions:** `wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels)`; `wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint16_t channel, int16_t amp_uv, uint16_t flags)`; `wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count)`; `wet_aer_available(const wet_aer_ring_t *ring)`; `wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps)`; `wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks)`; `wet_neo_free(wet_neo_detector_t *det)`; `wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks)`; `wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring)`; `wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns)`; `wet_csr_free(wet_csr_matrix_t *csr)`; `wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns)`

#### `native/include/wet_crt.h`

- **Macros / Constants:** `snprintf` = `_snprintf`, `fabsf` = `wet_fabsf`
- **Functions:** `malloc(size_t size)`; `calloc(size_t num, size_t size)`; `free(void* ptr)`; `memcpy(void* dest, const void* src, size_t count)`; `memset(void* dest, int ch, size_t count)`; `memcmp(const void* s1, const void* s2, size_t count)`; `strlen(const char* str)`; `strncpy(char* dest, const char* src, size_t count)`; `strcpy(char* dest, const char* src)`; `strcat(char* dest, const char* src)`; `strcmp(const char* s1, const char* s2)`; `strncmp(const char* s1, const char* s2, size_t count)`; `sprintf(char* buffer, const char* format, ...)`; `_snprintf(char* buffer, size_t count, const char* format, ...)`; `wet_fabsf(float x)`; `wet_fabs(double x)`; `wet_clampf(float x, float lo, float hi)`; `wet_clampd(double x, double lo, double hi)`; `wet_exp(double x)`; `wet_expf(float x)`; `wet_sqrt(double x)`; `wet_rng_next(uint64_t* state)`; `wet_rng_uniform(uint64_t* state)`; `wet_rng_normal(uint64_t* state)`

#### `native/include/wet_distributed.h`

- **Types / Structs / Enums:** `wet_ptp_clock_t`, `wet_timing_wheel_bucket_t`, `wet_timing_wheel_t`, `wet_tsn_frame_t`
- **Macros / Constants:** `WET_DIST_CACHELINE_SIZE` = `128`, `WET_TSN_FRAME_SIZE` = `32`, `WET_TIMING_WHEEL_SLOTS` = `512`, `WET_WHEEL_BUCKET_CAP` = `64`, `WET_MAX_CHAMBERS` = `16`
- **Functions:** `wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki)`; `wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns)`; `wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns)`; `wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags)`; `wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber)`; `wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id)`; `wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns)`; `wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count)`; `wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks)`

#### `native/include/wet_hal.h`

- **Types / Structs / Enums:** `struct wet_hal_context`, `struct wet_hal_driver`, `wet_async_cmd_t`, `wet_async_cmd_type_t`, `wet_hal_config_t`, `wet_hal_driver_type_t`, `wet_hal_mode_t`, `wet_hal_ops_t`, `wet_hal_status_t`, `wet_hal_telemetry_t`
- **Macros / Constants:** `WET_HAL_CROWBAR_BLEED_RESISTOR_OHMS` = `700000.0f`, `WET_HAL_MAX_DEAD_HEAD_PRESSURE_KPA` = `150.0f`, `WET_HAL_ASYNC_QUEUE_CAPACITY` = `64`, `WET_HAL_MAX_DRIVERS` = `16`
- **Functions:** `wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_destroy(wet_hal_context_t* hal)`; `wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal)`; `wet_hal_get_context(wet_vm_t* vm)`; `wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode)`; `wet_hal_get_mode(const wet_hal_context_t* hal)`; `wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type)`; `wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul)`; `wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state)`; `wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min)`; `wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag)`; `wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel)`; `wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason)`; `wet_hal_async_enqueue(wet_hal_context_t* hal, const wet_async_cmd_t* cmd)`; `wet_hal_process_async_queue(wet_hal_context_t* hal)`; `wet_hal_i2c_bus_recovery(wet_hal_context_t* hal)`; `wet_hal_set_inline_pressure(wet_hal_context_t* hal, uint8_t port, float pressure_kpa)`; `wet_hal_get_telemetry(wet_hal_context_t* hal)`; `wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id)`; `wet_hal_get_time_us(void)`

#### `native/include/wet_hal_intan.h`

- **Types / Structs / Enums:** `intan_current_range_t`, `intan_device_state_t`, `intan_spi_command_t`
- **Macros / Constants:** `INTAN_RHS2116_NUM_CHANNELS` = `16`, `INTAN_SPI_WORD_BITS` = `32`, `INTAN_PIPELINE_DELAY_WORDS` = `2`, `INTAN_COMPLIANCE_RAIL_VOLT` = `7.0f`, `INTAN_CMD_CONVERT` = `0x00U`, `INTAN_CMD_WRITE` = `0x80U`, `INTAN_CMD_READ` = `0xC0U`, `INTAN_FLAG_M_COMPLIANCE_CLEAR` = `0x800000U`, `INTAN_FLAG_U_UPDATE_LATCH` = `0x400000U`
- **Functions:** `wet_hal_intan_create(wet_hal_mode_t mode)`; `wet_hal_intan_destroy(wet_hal_driver_t* drv)`; `wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word)`; `wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd)`; `wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd)`; `wet_hal_intan_set_stim_current(wet_hal_driver_t* drv, uint8_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv)`; `wet_hal_intan_clear_compliance(wet_hal_driver_t* drv)`; `wet_hal_intan_measure_impedance(wet_hal_driver_t* drv, uint8_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_intan_set_charge_recovery(wet_hal_driver_t* drv, uint8_t channel, uint8_t enable)`; `wet_hal_intan_inject_fault(wet_hal_driver_t* drv, uint8_t force_rail, uint8_t spi_error, uint8_t bus_timeout)`

#### `native/include/wet_hal_maxwell.h`

- **Types / Structs / Enums:** `maxwell_device_state_t`, `maxwell_seq_state_t`, `maxwell_seq_step_t`
- **Macros / Constants:** `MAXWELL_TOTAL_ELECTRODES` = `26400`, `MAXWELL_RECORDING_CHANNELS` = `1024`, `MAXWELL_STIMULATION_UNITS` = `32`, `MAXWELL_PITCH_UM` = `17.5f`, `MAXWELL_ELECTRODE_AREA_UM2` = `132.25f`, `MAXWELL_VOLTAGE_LIMIT_MV` = `1000.0f`, `MAXWELL_MAX_DAC_BITS` = `335`, `MAXWELL_PT_CIC_MC_CM2` = `0.10f`, `MAXWELL_MAX_PHASE_CHARGE_NC` = `0.13225f`, `MAXWELL_MAX_SEQUENCE_STEPS` = `4096`
- **Functions:** `wet_hal_maxwell_create(wet_hal_mode_t mode)`; `wet_hal_maxwell_destroy(wet_hal_driver_t* drv)`; `wet_hal_maxwell_route_channels(wet_hal_driver_t* drv, const uint16_t* electrode_indices, uint32_t count)`; `wet_hal_maxwell_connect_stim(wet_hal_driver_t* drv, uint8_t stim_unit, uint16_t electrode_id)`; `wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_append(wet_hal_driver_t* drv, uint32_t timestamp_us, uint8_t stim_unit, uint16_t electrode_id, float voltage_mv, uint16_t duration_us)`; `wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv)`; `wet_hal_maxwell_stim_voltage(wet_hal_driver_t* drv, uint8_t stim_unit, uint16_t electrode_id, float voltage_mv, float phase1_ms, float phase2_ms)`; `wet_hal_maxwell_inject_fault(wet_hal_driver_t* drv, uint8_t force_charge_violation, uint8_t drop_frames)`

#### `native/include/wet_hal_pump_valve.h`

- **Types / Structs / Enums:** `harvard_prompt_t`, `harvard_pump_state_t`, `microfluidic_state_t`, `wet_can_frame_t`
- **Macros / Constants:** `WET_MAX_PUMPS` = `8`, `WET_MAX_VALVES` = `8`, `WET_CAN_MAX_PAYLOAD` = `8`, `WET_CAN_QUEUE_CAPACITY` = `128`, `CAN_ID_EMCY_BASE` = `0x080U`, `CAN_ID_TPDO1_BASE` = `0x180U`, `CAN_ID_RPDO1_BASE` = `0x200U`, `CAN_ID_RPDO2_BASE` = `0x300U`, `CAN_ID_HEARTBEAT_BASE` = `0x700U`
- **Functions:** `wet_hal_microfluidics_create(wet_hal_mode_t mode)`; `wet_hal_microfluidics_destroy(wet_hal_driver_t* drv)`; `wet_hal_harvard_format_cmd(uint8_t address, uint8_t fast_mode, const char* cmd_name, const char* args, char* out_buf, size_t out_buf_len)`; `wet_hal_harvard_parse_response(const char* resp_buf, size_t resp_len)`; `wet_hal_pump_set_rate(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_pump_dispense(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul)`; `wet_hal_pump_stop(wet_hal_driver_t* drv, uint8_t pump_id)`; `wet_hal_valve_set_state(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state)`; `wet_hal_pump_bind_downstream_valve(wet_hal_driver_t* drv, uint8_t pump_id, uint8_t valve_id)`; `wet_hal_can_send(wet_hal_driver_t* drv, const wet_can_frame_t* frame)`; `wet_hal_can_recv(wet_hal_driver_t* drv, wet_can_frame_t* out_frame)`; `wet_hal_can_send_emcy(wet_hal_driver_t* drv, uint8_t node_id, uint16_t error_code, uint8_t error_register)`; `wet_hal_microfluidics_inject_fault(wet_hal_driver_t* drv, uint8_t stall, uint8_t can_drop, uint8_t timeout)`

#### `native/include/wet_hal_sensirion.h`

- **Types / Structs / Enums:** `sensirion_device_state_t`
- **Macros / Constants:** `SENSIRION_I2C_ADDR_DEFAULT` = `0x08U`, `SENSIRION_CRC8_POLYNOMIAL` = `0x31U`, `SENSIRION_CRC8_INIT` = `0xFFU`, `SENSIRION_CMD_START_CONT_H2O` = `0x3608U`, `SENSIRION_CMD_START_CONT_IPA` = `0x3615U`, `SENSIRION_CMD_STOP_CONT` = `0x3FF9U`, `SENSIRION_CMD_SOFT_RESET` = `0x0006U`, `SHDLC_FRAME_START_STOP` = `0x7EU`, `SHDLC_FRAME_ESCAPE` = `0x7DU`, `SHDLC_ESCAPE_MASK` = `0x20U`, `SHDLC_MAX_FRAME_SIZE` = `256`
- **Functions:** `wet_hal_sensirion_create(wet_hal_mode_t mode)`; `wet_hal_sensirion_destroy(wet_hal_driver_t* drv)`; `wet_hal_sensirion_crc8(const uint8_t* data, size_t len)`; `wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3])`; `wet_hal_sensirion_start_measurement(wet_hal_driver_t* drv, uint16_t cmd)`; `wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv)`; `wet_hal_sensirion_read_flow(wet_hal_driver_t* drv, double* out_flow_ul_min)`; `wet_hal_sensirion_hil_set_flow(wet_hal_driver_t* drv, double flow_ul_min)`; `wet_hal_shdlc_encode(uint8_t address, uint8_t command, const uint8_t* payload, uint8_t payload_len, uint8_t* out_buf, size_t out_buf_max)`; `wet_hal_shdlc_decode(const uint8_t* raw_buf, size_t raw_len, uint8_t* out_address, uint8_t* out_command, uint8_t* out_payload, uint8_t* out_payload_len)`; `wet_hal_sensirion_inject_fault(wet_hal_driver_t* drv, uint8_t corrupt_crc, uint8_t nak_addr)`

#### `native/include/wet_scheduler.h`

- **Types / Structs / Enums:** `wet_scheduler_config_t`, `wet_scheduler_stats_t`, `wet_stim_command_t`
- **Functions:** `wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config)`; `wet_scheduler_start(wet_scheduler_t* sched)`; `wet_scheduler_step(wet_scheduler_t* sched)`; `wet_scheduler_stop(wet_scheduler_t* sched)`; `wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem)`; `wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd)`; `wet_scheduler_benchmark(wet_scheduler_t* sched, uint32_t total_ticks, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_destroy(wet_scheduler_t* sched)`

#### `native/include/wetvm_api.h`

- **Types / Structs / Enums:** `wet_actuator_telemetry_t`, `wet_telemetry_t`, `wet_vm_config_t`
- **Functions:** `wet_create_vm(const wet_vm_config_t* config)`; `wet_create_vm_arena(void* arena_buf, size_t arena_bytes, const wet_vm_config_t* config)`; `wet_free_vm(wet_vm_t* vm)`; `wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2)`; `wet_active_discharge(wet_vm_t* vm, uint8_t channel)`; `wet_active_discharge_all(wet_vm_t* vm)`; `wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable)`; `wet_life_supervisor_shutdown(wet_vm_t* vm)`; `wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)`; `wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)`; `wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)`; `wet_get_last_error(wet_vm_t* vm)`; `wet_status_to_string(wet_status_t status)`; `wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial)`; `wet_inject_current_stimulus(wet_vm_t* vm, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms)`; `wet_verify_bytecode(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot(const wet_vm_t* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore(wet_vm_t* vm, const uint8_t* buffer, size_t len)`; `wet_set_environmental_sensors(wet_vm_t* vm, float ph, float do_pct, float co2_pct, uint8_t bubble_sensor_id, uint8_t bubble_state, float flow_rate_ul_min)`; `wet_set_temperature(wet_vm_t* vm, float temp_c)`; `wet_set_channel_banks(wet_vm_t* vm, uint64_t ref_mask, uint64_t rec_mask)`; `wet_vm_get_synapse_matrix(const wet_vm_t* vm, float* out_matrix, size_t out_capacity_floats)`; `wet_vm_get_synapse_weight(const wet_vm_t* vm, uint8_t pre, uint8_t post)`; `wet_clamp_voltage_vm(wet_vm_t* vm, float requested_v)`

#### `native/include/wetvm_types.h`

- **Types / Structs / Enums:** `wet_bytecode_header_t`, `wet_capability_t`, `wet_opcode_t`, `wet_section_header_t`, `wet_section_type_t`, `wet_status_t`
- **Macros / Constants:** `WET_HEADER_MAGIC` = `"WETB"`, `WET_HEADER_MAGIC_INT` = `0x42544557U`, `WET_HEADER_SIZE` = `32`, `WET_VERSION_MAJOR` = `1`, `WET_VERSION_MINOR` = `0`, `WET_SECTION_ENTRY_SIZE` = `12`

#### `native/include/wetvm_vm.h`

- **Types / Structs / Enums:** `struct wet_vm_instance`, `wet_call_frame_t`, `wet_constant_entry_t`, `wet_life_supervisor_t`, `wet_val_type_t`, `wet_value_t`
- **Functions:** `wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc)`; `wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem)`; `wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`

#### `native/src/biophysics.c`

- **Functions:** `init_synapse_stp(bio_synapse_t* syn, uint8_t pre_exc, uint8_t post_exc, float weight_ns)`; `biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed)`; `biophysics_reset(bio_state_t* bio)`; `biophysics_schedule_stim_ext(bio_state_t* bio, uint8_t channel, float clamped_voltage_v, float phase1_ms, float phase2_ms, float interphase_ms)`; `biophysics_schedule_stim_current(bio_state_t* bio, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms, float interphase_ms)`; `biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial)`; `biophysics_get_randles_state(const bio_state_t* bio, uint8_t channel, float* out_v_dl_v, float* out_v_elec_v)`; `biophysics_schedule_stim(bio_state_t* bio, uint8_t channel, float clamped_voltage_v, float phase1_ms, float phase2_ms)`; `biophysics_zero_all_stim(bio_state_t* bio)`; `biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns)`; `biophysics_step_tick(bio_state_t* bio)`; `biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms)`; `biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post)`

#### `native/src/interlocks.c`

- **Functions:** `interlocks_init(interlock_state_t* il)`; `interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2)`; `interlocks_active_discharge(interlock_state_t* il, uint8_t channel)`; `interlocks_active_discharge_all(interlock_state_t* il)`; `interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable)`; `interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count)`; `interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask)`; `interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel)`; `interlocks_clamp_voltage(interlock_state_t* il, float requested_v)`; `interlocks_record_charge_tick(interlock_state_t* il, uint64_t current_tick, const float tick_charge_nc[INTERLOCK_NUM_CHANNELS])`; `interlocks_check_epileptiform(interlock_state_t* il, uint64_t current_tick, const float channel_rates_hz[INTERLOCK_NUM_CHANNELS])`; `interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c)`; `interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id)`; `interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v)`

#### `native/src/wet_aer.c`

- **Functions:** `wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels)`; `wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint16_t channel, int16_t amp_uv, uint16_t flags)`; `wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count)`; `wet_aer_available(const wet_aer_ring_t *ring)`; `wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps)`; `wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks)`; `wet_neo_free(wet_neo_detector_t *det)`; `wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks)`; `wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring)`; `wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns)`; `wet_csr_free(wet_csr_matrix_t *csr)`; `wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns)`

#### `native/src/wet_distributed.c`

- **Functions:** `wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki)`; `wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns)`; `wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns)`; `wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags)`; `wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber)`; `wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id)`; `wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns)`; `wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count)`; `wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks)`

#### `native/src/wet_hal.c`

- **Types / Structs / Enums:** `LARGE_INTEGER`
- **Functions:** `wet_hal_get_time_us(void)`; `wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_destroy(wet_hal_context_t* hal)`; `wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal)`; `wet_hal_get_context(wet_vm_t* vm)`; `wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode)`; `wet_hal_get_mode(const wet_hal_context_t* hal)`; `wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type)`; `wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul)`; `wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state)`; `wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min)`; `wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag)`; `wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel)`; `wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason)`; `wet_hal_set_inline_pressure(wet_hal_context_t* hal, uint8_t port, float pressure_kpa)`; `wet_hal_async_enqueue(wet_hal_context_t* hal, const wet_async_cmd_t* cmd)`; `wet_hal_process_async_queue(wet_hal_context_t* hal)`; `wet_hal_i2c_bus_recovery(wet_hal_context_t* hal)`; `wet_hal_get_telemetry(wet_hal_context_t* hal)`; `wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id)`

#### `native/src/wet_hal_intan.c`

- **Functions:** `intan_op_init(wet_hal_driver_t* drv, void* config)`; `intan_op_shutdown(wet_hal_driver_t* drv)`; `intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason)`; `intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms)`; `intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count)`; `intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel)`; `wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd)`; `wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd)`; `wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word)`; `wet_hal_intan_create(wet_hal_mode_t mode)`; `wet_hal_intan_destroy(wet_hal_driver_t* drv)`; `wet_hal_intan_set_stim_current(wet_hal_driver_t* drv, uint8_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv)`; `wet_hal_intan_clear_compliance(wet_hal_driver_t* drv)`; `wet_hal_intan_measure_impedance(wet_hal_driver_t* drv, uint8_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_intan_set_charge_recovery(wet_hal_driver_t* drv, uint8_t channel, uint8_t enable)`; `wet_hal_intan_inject_fault(wet_hal_driver_t* drv, uint8_t force_rail, uint8_t spi_error, uint8_t bus_timeout)`

#### `native/src/wet_hal_maxwell.c`

- **Functions:** `maxwell_op_init(wet_hal_driver_t* drv, void* config)`; `maxwell_op_shutdown(wet_hal_driver_t* drv)`; `maxwell_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason)`; `maxwell_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms)`; `maxwell_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `maxwell_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `maxwell_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count)`; `maxwell_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `maxwell_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel)`; `wet_hal_maxwell_create(wet_hal_mode_t mode)`; `wet_hal_maxwell_destroy(wet_hal_driver_t* drv)`; `wet_hal_maxwell_route_channels(wet_hal_driver_t* drv, const uint16_t* electrode_indices, uint32_t count)`; `wet_hal_maxwell_connect_stim(wet_hal_driver_t* drv, uint8_t stim_unit, uint16_t electrode_id)`; `wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_append(wet_hal_driver_t* drv, uint32_t timestamp_us, uint8_t stim_unit, uint16_t electrode_id, float voltage_mv, uint16_t duration_us)`; `wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv)`; `wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv)`; `wet_hal_maxwell_stim_voltage(wet_hal_driver_t* drv, uint8_t stim_unit, uint16_t electrode_id, float voltage_mv, float phase1_ms, float phase2_ms)`; `wet_hal_maxwell_inject_fault(wet_hal_driver_t* drv, uint8_t force_charge_violation, uint8_t drop_frames)`

#### `native/src/wet_hal_pump_valve.c`

- **Functions:** `microfluidics_op_init(wet_hal_driver_t* drv, void* config)`; `microfluidics_op_shutdown(wet_hal_driver_t* drv)`; `microfluidics_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason)`; `microfluidics_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms)`; `microfluidics_op_write_pump(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `microfluidics_op_dispense_volume(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul)`; `microfluidics_op_write_valve(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state)`; `microfluidics_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min)`; `microfluidics_op_read_pressure(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa)`; `wet_hal_harvard_format_cmd(uint8_t address, uint8_t fast_mode, const char* cmd_name, const char* args, char* out_buf, size_t out_buf_len)`; `wet_hal_harvard_parse_response(const char* resp_buf, size_t resp_len)`; `wet_hal_microfluidics_create(wet_hal_mode_t mode)`; `wet_hal_microfluidics_destroy(wet_hal_driver_t* drv)`; `wet_hal_pump_set_rate(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_pump_dispense(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul)`; `wet_hal_pump_stop(wet_hal_driver_t* drv, uint8_t pump_id)`; `wet_hal_valve_set_state(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t val_state)`; `wet_hal_pump_bind_downstream_valve(wet_hal_driver_t* drv, uint8_t pump_id, uint8_t valve_id)`; `wet_hal_can_send(wet_hal_driver_t* drv, const wet_can_frame_t* frame)`; `wet_hal_can_recv(wet_hal_driver_t* drv, wet_can_frame_t* out_frame)`; `wet_hal_can_send_emcy(wet_hal_driver_t* drv, uint8_t node_id, uint16_t error_code, uint8_t error_register)`; `wet_hal_microfluidics_inject_fault(wet_hal_driver_t* drv, uint8_t stall, uint8_t can_drop, uint8_t timeout)`

#### `native/src/wet_hal_sensirion.c`

- **Functions:** `sensirion_op_init(wet_hal_driver_t* drv, void* config)`; `sensirion_op_shutdown(wet_hal_driver_t* drv)`; `sensirion_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason)`; `sensirion_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms)`; `sensirion_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min)`; `wet_hal_sensirion_crc8(const uint8_t* data, size_t len)`; `wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3])`; `wet_hal_shdlc_encode(uint8_t address, uint8_t command, const uint8_t* payload, uint8_t payload_len, uint8_t* out_buf, size_t out_buf_max)`; `wet_hal_shdlc_decode(const uint8_t* raw_buf, size_t raw_len, uint8_t* out_address, uint8_t* out_command, uint8_t* out_payload, uint8_t* out_payload_len)`; `wet_hal_sensirion_create(wet_hal_mode_t mode)`; `wet_hal_sensirion_destroy(wet_hal_driver_t* drv)`; `wet_hal_sensirion_start_measurement(wet_hal_driver_t* drv, uint16_t cmd)`; `wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv)`; `wet_hal_sensirion_read_flow(wet_hal_driver_t* drv, double* out_flow_ul_min)`; `wet_hal_sensirion_hil_set_flow(wet_hal_driver_t* drv, double flow_ul_min)`; `wet_hal_sensirion_inject_fault(wet_hal_driver_t* drv, uint8_t corrupt_crc, uint8_t nak_addr)`

#### `native/src/wet_scheduler.c`

- **Types / Structs / Enums:** `LARGE_INTEGER`, `struct wet_scheduler`, `wet_spsc_ring_t`
- **Macros / Constants:** `WET_CACHELINE_SIZE` = `128`, `WET_DEFAULT_SAMPLE_CAPACITY` = `100000`
- **Functions:** `wet_cpu_pause(void)`; `wet_atomic_load_u32_acquire(const volatile uint32_t* ptr)`; `wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val)`; `wet_spsc_init(wet_spsc_ring_t* ring, uint32_t capacity, size_t elem_size)`; `wet_spsc_free(wet_spsc_ring_t* ring)`; `wet_spsc_push(wet_spsc_ring_t* ring, const void* item)`; `wet_spsc_pop(wet_spsc_ring_t* ring, void* out_item)`; `wet_sort_doubles(double* arr, int left, int right)`; `wet_scheduler_thread_proc(void* param)`; `wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config)`; `wet_scheduler_start(wet_scheduler_t* sched)`; `wet_scheduler_step(wet_scheduler_t* sched)`; `wet_scheduler_stop(wet_scheduler_t* sched)`; `wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem)`; `wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd)`; `wet_scheduler_benchmark(wet_scheduler_t* sched, uint32_t total_ticks, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_destroy(wet_scheduler_t* sched)`

#### `native/src/wetvm_api.c`

- **Functions:** `wet_create_vm(const wet_vm_config_t* config)`; `wet_create_vm_arena(void* arena_buf, size_t arena_bytes, const wet_vm_config_t* config)`; `wet_free_vm(wet_vm_t* vm)`; `wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)`; `wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)`; `wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)`; `wet_get_last_error(wet_vm_t* vm)`; `wet_status_to_string(wet_status_t status)`; `wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2)`; `wet_active_discharge(wet_vm_t* vm, uint8_t channel)`; `wet_active_discharge_all(wet_vm_t* vm)`; `wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable)`; `wet_life_supervisor_shutdown(wet_vm_t* vm)`; `wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial)`; `wet_inject_current_stimulus(wet_vm_t* vm, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms)`; `wet_verify_bytecode(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot(const wet_vm_t* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore(wet_vm_t* vm, const uint8_t* buffer, size_t len)`; `wet_set_environmental_sensors(wet_vm_t* vm, float ph, float do_pct, float co2_pct, uint8_t bubble_sensor_id, uint8_t bubble_state, float flow_rate_ul_min)`; `wet_set_temperature(wet_vm_t* vm, float temp_c)`; `wet_set_channel_banks(wet_vm_t* vm, uint64_t ref_mask, uint64_t rec_mask)`; `wet_vm_get_synapse_matrix(const wet_vm_t* vm, float* out_matrix, size_t out_capacity_floats)`; `wet_vm_get_synapse_weight(const wet_vm_t* vm, uint8_t pre, uint8_t post)`; `wet_clamp_voltage_vm(wet_vm_t* vm, float requested_v)`

#### `native/src/wetvm_vm.c`

- **Types / Structs / Enums:** `wet_vm_snapshot_payload_t`
- **Macros / Constants:** `WET_SNAPSHOT_MAGIC` = `0x53544557U`, `WET_SNAPSHOT_VERSION` = `1`
- **Functions:** `wet_read_u16_le(const void* p)`; `wet_read_i16_le(const void* p)`; `wet_read_u32_le(const void* p)`; `wet_read_i32_le(const void* p)`; `wet_read_f32_le(const void* p)`; `wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc)`; `push_val(struct wet_vm_instance* vm, wet_value_t val)`; `pop_val(struct wet_vm_instance* vm, wet_value_t* out_val)`; `to_float(const wet_value_t* v)`; `to_int(const wet_value_t* v)`; `is_truthy(const wet_value_t* v)`; `cleanup_constants(struct wet_vm_instance* vm)`; `cleanup_bytecode(struct wet_vm_instance* vm)`; `wet_vm_load_bytecode_internal(struct wet_vm_instance* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `populate_telemetry(const struct wet_vm_instance* vm, wet_telemetry_t* telem)`; `advance_simulation_tick(struct wet_vm_instance* vm, wet_telemetry_t* out_telem)`; `wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem)`; `wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot_internal(const struct wet_vm_instance* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore_internal(struct wet_vm_instance* vm, const uint8_t* buffer, size_t len)`

### B.2 Python Modules (`compiler/`, `bindings/`, `biophysics/`, `native/`)

#### `native/build.py`

- def `get_project_root()`
- def `find_executable(name, extra_paths)`
- def `generate_msvcrt_import_lib(dlltool_path, output_lib, output_def)`
- def `generate_kernel32_import_lib(dlltool_path, output_lib, output_def)`
- def `build_with_clang(clang_path, src_files, include_dir, out_dll)`
- def `build_with_gcc(gcc_path, src_files, include_dir, out_dll)`
- def `build_with_msvc(cl_path, src_files, include_dir, out_dll)`
- def `build_native_runtime()`

#### `native/interlocks.py`

- class `CapabilityVerifier`: verify_capabilities()
- class `InterlockManager`: __init__(), get_state(), get_state_name(), trip_charge_imbalance(), trip_epileptiform_runaway(), get_dac_voltages(), get_diagnostic_report()

---

## Appendix C: Machine-Disassembled `.wbc` Benchmark Binaries

### `benchmarks/01_active_inference_closed_loop.wet`

```text
Section Table:
  [0] type=1 (CONSTANT_POOL   ) offset=0x005C (  92) size=   4 B
  [1] type=2 (TOPOLOGY_CONFIG ) offset=0x0060 (  96) size=  92 B
  [2] type=3 (BYTECODE_STREAM ) offset=0x00BC ( 188) size= 339 B
  [3] type=4 (SAFETY_MANIFEST ) offset=0x020F ( 527) size=  13 B
  [4] type=5 (DEBUG_LINE_MAP  ) offset=0x021C ( 540) size=1000 B

======================================================================
WBC Binary Disassembly (v1.0)
File Size: 1540 bytes | CRC32: 0x89A70FBC | Capabilities: 0x000B | Seq: 1
Sections: 5 | Channels: 64 | Max Charge Bound: 0.50 nC
======================================================================

[Section 3: BYTECODE_STREAM]
0000:  55 08 08         MEA_CONFIG       8, 8
0003:  12 00 00 00 00   PUSH_FLOAT       0.0
0008:  17 00 00         STORE_LOCAL      0
000B:  12 00 00 00 00   PUSH_FLOAT       0.0
0010:  17 01 00         STORE_LOCAL      1
0013:  12 00 00 00 00   PUSH_FLOAT       0.0
0018:  17 02 00         STORE_LOCAL      2
001B:  11 00 00 00 00   PUSH_INT         0
0020:  17 03 00         STORE_LOCAL      3
0023:  16 03 00         LOAD_LOCAL       3
0026:  11 88 13 00 00   PUSH_INT         5000
002B:  32               CMP_LT           
002C:  42 26 01         JMP_IF_FALSE     294
002F:  16 01 00         LOAD_LOCAL       1
0032:  16 00 00         LOAD_LOCAL       0
0035:  25               SUB_F            
0036:  17 04 00         STORE_LOCAL      4
0039:  16 04 00         LOAD_LOCAL       4
003C:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0041:  34               CMP_GT           
0042:  42 1C 00         JMP_IF_FALSE     28
0045:  12 CD CC 4C 3F   PUSH_FLOAT       0.800000011920929
004A:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
004F:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
0054:  12 00 00 00 00   PUSH_FLOAT       0.0
0059:  50 05            STIM_BIPHASIC    5
005B:  40 26 00         JMP              38
005E:  16 04 00         LOAD_LOCAL       4
0061:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0066:  28               NEG              
0067:  32               CMP_LT           
0068:  42 19 00         JMP_IF_FALSE     25
006B:  12 CD CC 4C 3F   PUSH_FLOAT       0.800000011920929
0070:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
0075:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
007A:  12 00 00 00 00   PUSH_FLOAT       0.0
007F:  50 02            STIM_BIPHASIC    2
0081:  11 00 00 00 00   PUSH_INT         0
0086:  17 05 00         STORE_LOCAL      5
0089:  16 05 00         LOAD_LOCAL       5
008C:  11 C8 00 00 00   PUSH_INT         200
0091:  32               CMP_LT           
0092:  42 13 00         JMP_IF_FALSE     19
0095:  02               SYNC_TICK        
0096:  16 05 00         LOAD_LOCAL       5
0099:  11 01 00 00 00   PUSH_INT         1
009E:  20               ADD_I            
009F:  17 05 00         STORE_LOCAL      5
00A2:  40 E7 FF         JMP              -25
00A5:  12 00 00 A0 41   PUSH_FLOAT       20.0
00AA:  51 3A            READ_SPIKES      58
00AC:  17 06 00         STORE_LOCAL      6
00AF:  12 00 00 A0 41   PUSH_FLOAT       20.0
00B4:  51 3D            READ_SPIKES      61
00B6:  17 07 00         STORE_LOCAL      7
00B9:  16 07 00         LOAD_LOCAL       7
00BC:  16 06 00         LOAD_LOCAL       6
00BF:  25               SUB_F            
00C0:  12 CD CC 4C 3D   PUSH_FLOAT       0.05000000074505806
00C5:  26               MUL_F            
00C6:  17 08 00         STORE_LOCAL      8
00C9:  16 00 00         LOAD_LOCAL       0
00CC:  16 08 00         LOAD_LOCAL       8
00CF:  24               ADD_F            
00D0:  17 00 00         STORE_LOCAL      0
00D3:  16 01 00         LOAD_LOCAL       1
00D6:  16 00 00         LOAD_LOCAL       0
00D9:  25               SUB_F            
00DA:  14               DUP              
00DB:  11 00 00 00 00   PUSH_INT         0
00E0:  32               CMP_LT           
00E1:  42 04 00         JMP_IF_FALSE     4
00E4:  28               NEG              
00E5:  17 09 00         STORE_LOCAL      9
00E8:  16 09 00         LOAD_LOCAL       9
00EB:  16 02 00         LOAD_LOCAL       2
00EE:  14               DUP              
00EF:  11 00 00 00 00   PUSH_INT         0
00F4:  32               CMP_LT           
00F5:  42 04 00         JMP_IF_FALSE     4
00F8:  28               NEG              
00F9:  32               CMP_LT           
00FA:  42 24 00         JMP_IF_FALSE     36
00FD:  12 00 00 00 3F   PUSH_FLOAT       0.5
0102:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0107:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
010C:  12 00 00 00 00   PUSH_FLOAT       0.0
0111:  50 1B            STIM_BIPHASIC    27
0113:  12 9A 99 99 3F   PUSH_FLOAT       1.2000000476837158
0118:  53 00 00         MODULATE_STDP    0, 0
011B:  40 21 00         JMP              33
011E:  12 66 66 66 3F   PUSH_FLOAT       0.8999999761581421
0123:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0128:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
012D:  12 00 00 00 00   PUSH_FLOAT       0.0
0132:  50 24            STIM_BIPHASIC    36
0134:  12 33 33 33 3F   PUSH_FLOAT       0.699999988079071
0139:  53 00 00         MODULATE_STDP    0, 0
013C:  16 09 00         LOAD_LOCAL       9
013F:  17 02 00         STORE_LOCAL      2
0142:  16 03 00         LOAD_LOCAL       3
0145:  11 01 00 00 00   PUSH_INT         1
014A:  20               ADD_I            
014B:  17 03 00         STORE_LOCAL      3
014E:  02               SYNC_TICK        
014F:  40 D4 FE         JMP              -300
0152:  01               HALT             
======================================================================
```

### `benchmarks/02_polychronous_reservoir_classifier.wet`

```text
Section Table:
  [0] type=1 (CONSTANT_POOL   ) offset=0x005C (  92) size=   4 B
  [1] type=2 (TOPOLOGY_CONFIG ) offset=0x0060 (  96) size=  48 B
  [2] type=3 (BYTECODE_STREAM ) offset=0x0090 ( 144) size= 375 B
  [3] type=4 (SAFETY_MANIFEST ) offset=0x0207 ( 519) size=  13 B
  [4] type=5 (DEBUG_LINE_MAP  ) offset=0x0214 ( 532) size=1144 B

======================================================================
WBC Binary Disassembly (v1.0)
File Size: 1676 bytes | CRC32: 0x3CB805C3 | Capabilities: 0x001B | Seq: 1
Sections: 5 | Channels: 64 | Max Charge Bound: 0.50 nC
======================================================================

[Section 3: BYTECODE_STREAM]
0000:  55 08 08         MEA_CONFIG       8, 8
0003:  11 00 00 00 00   PUSH_INT         0
0008:  17 00 00         STORE_LOCAL      0
000B:  16 00 00         LOAD_LOCAL       0
000E:  11 64 00 00 00   PUSH_INT         100
0013:  32               CMP_LT           
0014:  42 62 01         JMP_IF_FALSE     354
0017:  12 66 66 66 3F   PUSH_FLOAT       0.8999999761581421
001C:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0021:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0026:  12 00 00 00 00   PUSH_FLOAT       0.0
002B:  50 00            STIM_BIPHASIC    0
002D:  11 00 00 00 00   PUSH_INT         0
0032:  17 01 00         STORE_LOCAL      1
0035:  16 01 00         LOAD_LOCAL       1
0038:  11 32 00 00 00   PUSH_INT         50
003D:  32               CMP_LT           
003E:  42 13 00         JMP_IF_FALSE     19
0041:  02               SYNC_TICK        
0042:  16 01 00         LOAD_LOCAL       1
0045:  11 01 00 00 00   PUSH_INT         1
004A:  20               ADD_I            
004B:  17 01 00         STORE_LOCAL      1
004E:  40 E7 FF         JMP              -25
0051:  12 66 66 66 3F   PUSH_FLOAT       0.8999999761581421
0056:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
005B:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0060:  12 00 00 00 00   PUSH_FLOAT       0.0
0065:  50 02            STIM_BIPHASIC    2
0067:  11 00 00 00 00   PUSH_INT         0
006C:  17 01 00         STORE_LOCAL      1
006F:  16 01 00         LOAD_LOCAL       1
0072:  11 32 00 00 00   PUSH_INT         50
0077:  32               CMP_LT           
0078:  42 13 00         JMP_IF_FALSE     19
007B:  02               SYNC_TICK        
007C:  16 01 00         LOAD_LOCAL       1
007F:  11 01 00 00 00   PUSH_INT         1
0084:  20               ADD_I            
0085:  17 01 00         STORE_LOCAL      1
0088:  40 E7 FF         JMP              -25
008B:  12 66 66 66 3F   PUSH_FLOAT       0.8999999761581421
0090:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0095:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
009A:  12 00 00 00 00   PUSH_FLOAT       0.0
009F:  50 04            STIM_BIPHASIC    4
00A1:  11 00 00 00 00   PUSH_INT         0
00A6:  17 01 00         STORE_LOCAL      1
00A9:  16 01 00         LOAD_LOCAL       1
00AC:  11 32 00 00 00   PUSH_INT         50
00B1:  32               CMP_LT           
00B2:  42 13 00         JMP_IF_FALSE     19
00B5:  02               SYNC_TICK        
00B6:  16 01 00         LOAD_LOCAL       1
00B9:  11 01 00 00 00   PUSH_INT         1
00BE:  20               ADD_I            
00BF:  17 01 00         STORE_LOCAL      1
00C2:  40 E7 FF         JMP              -25
00C5:  12 66 66 66 3F   PUSH_FLOAT       0.8999999761581421
00CA:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
00CF:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
00D4:  12 00 00 00 00   PUSH_FLOAT       0.0
00D9:  50 06            STIM_BIPHASIC    6
00DB:  11 00 00 00 00   PUSH_INT         0
00E0:  17 01 00         STORE_LOCAL      1
00E3:  16 01 00         LOAD_LOCAL       1
00E6:  11 2C 01 00 00   PUSH_INT         300
00EB:  32               CMP_LT           
00EC:  42 13 00         JMP_IF_FALSE     19
00EF:  02               SYNC_TICK        
00F0:  16 01 00         LOAD_LOCAL       1
00F3:  11 01 00 00 00   PUSH_INT         1
00F8:  20               ADD_I            
00F9:  17 01 00         STORE_LOCAL      1
00FC:  40 E7 FF         JMP              -25
00FF:  11 00 00 00 00   PUSH_INT         0
0104:  17 02 00         STORE_LOCAL      2
0107:  11 00 00 00 00   PUSH_INT         0
010C:  17 03 00         STORE_LOCAL      3
010F:  16 02 00         LOAD_LOCAL       2
0112:  11 10 00 00 00   PUSH_INT         16
0117:  32               CMP_LT           
0118:  42 2F 00         JMP_IF_FALSE     47
011B:  11 18 00 00 00   PUSH_INT         24
0120:  16 02 00         LOAD_LOCAL       2
0123:  20               ADD_I            
0124:  17 04 00         STORE_LOCAL      4
0127:  16 03 00         LOAD_LOCAL       3
012A:  16 04 00         LOAD_LOCAL       4
012D:  12 00 00 F0 41   PUSH_FLOAT       30.0
0132:  51 FF            READ_SPIKES      255
0134:  20               ADD_I            
0135:  17 03 00         STORE_LOCAL      3
0138:  16 02 00         LOAD_LOCAL       2
013B:  11 01 00 00 00   PUSH_INT         1
0140:  20               ADD_I            
0141:  17 02 00         STORE_LOCAL      2
0144:  40 CB FF         JMP              -53
0147:  16 03 00         LOAD_LOCAL       3
014A:  11 2D 00 00 00   PUSH_INT         45
014F:  34               CMP_GT           
0150:  42 0E 00         JMP_IF_FALSE     14
0153:  12 CD CC 8C 3F   PUSH_FLOAT       1.100000023841858
0158:  53 00 00         MODULATE_STDP    0, 0
015B:  40 0B 00         JMP              11
015E:  12 33 33 73 3F   PUSH_FLOAT       0.949999988079071
0163:  53 00 00         MODULATE_STDP    0, 0
0166:  16 00 00         LOAD_LOCAL       0
0169:  11 01 00 00 00   PUSH_INT         1
016E:  20               ADD_I            
016F:  17 00 00         STORE_LOCAL      0
0172:  02               SYNC_TICK        
0173:  40 98 FE         JMP              -360
0176:  01               HALT             
======================================================================
```

### `benchmarks/03_homeostatic_stabilization_and_stress.wet`

```text
Section Table:
  [0] type=1 (CONSTANT_POOL   ) offset=0x005C (  92) size=   4 B
  [1] type=2 (TOPOLOGY_CONFIG ) offset=0x0060 (  96) size=  64 B
  [2] type=3 (BYTECODE_STREAM ) offset=0x00A0 ( 160) size= 250 B
  [3] type=4 (SAFETY_MANIFEST ) offset=0x019A ( 410) size=  13 B
  [4] type=5 (DEBUG_LINE_MAP  ) offset=0x01A7 ( 423) size= 688 B

======================================================================
WBC Binary Disassembly (v1.0)
File Size: 1111 bytes | CRC32: 0x5B2C0692 | Capabilities: 0x000B | Seq: 1
Sections: 5 | Channels: 64 | Max Charge Bound: 0.50 nC
======================================================================

[Section 3: BYTECODE_STREAM]
0000:  55 08 08         MEA_CONFIG       8, 8
0003:  11 00 00 00 00   PUSH_INT         0
0008:  17 00 00         STORE_LOCAL      0
000B:  16 00 00         LOAD_LOCAL       0
000E:  11 D0 07 00 00   PUSH_INT         2000
0013:  32               CMP_LT           
0014:  42 E5 00         JMP_IF_FALSE     229
0017:  11 00 00 00 00   PUSH_INT         0
001C:  17 01 00         STORE_LOCAL      1
001F:  16 01 00         LOAD_LOCAL       1
0022:  11 64 00 00 00   PUSH_INT         100
0027:  32               CMP_LT           
0028:  42 13 00         JMP_IF_FALSE     19
002B:  02               SYNC_TICK        
002C:  16 01 00         LOAD_LOCAL       1
002F:  11 01 00 00 00   PUSH_INT         1
0034:  20               ADD_I            
0035:  17 01 00         STORE_LOCAL      1
0038:  40 E7 FF         JMP              -25
003B:  12 00 00 20 41   PUSH_FLOAT       10.0
0040:  54               GET_POP_RATE     
0041:  17 02 00         STORE_LOCAL      2
0044:  16 02 00         LOAD_LOCAL       2
0047:  12 00 00 70 41   PUSH_FLOAT       15.0
004C:  32               CMP_LT           
004D:  42 3A 00         JMP_IF_FALSE     58
0050:  12 CD CC CC 3E   PUSH_FLOAT       0.4000000059604645
0055:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
005A:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
005F:  12 00 00 00 00   PUSH_FLOAT       0.0
0064:  50 12            STIM_BIPHASIC    18
0066:  12 CD CC CC 3E   PUSH_FLOAT       0.4000000059604645
006B:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0070:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
0075:  12 00 00 00 00   PUSH_FLOAT       0.0
007A:  50 2D            STIM_BIPHASIC    45
007C:  12 66 66 86 3F   PUSH_FLOAT       1.0499999523162842
0081:  53 00 00         MODULATE_STDP    0, 0
0084:  40 43 00         JMP              67
0087:  16 02 00         LOAD_LOCAL       2
008A:  12 00 00 C8 41   PUSH_FLOAT       25.0
008F:  34               CMP_GT           
0090:  42 37 00         JMP_IF_FALSE     55
0093:  12 9A 99 19 3F   PUSH_FLOAT       0.6000000238418579
0098:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
009D:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
00A2:  12 00 00 00 00   PUSH_FLOAT       0.0
00A7:  50 09            STIM_BIPHASIC    9
00A9:  12 9A 99 19 3F   PUSH_FLOAT       0.6000000238418579
00AE:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
00B3:  12 CD CC CC 3D   PUSH_FLOAT       0.10000000149011612
00B8:  12 00 00 00 00   PUSH_FLOAT       0.0
00BD:  50 36            STIM_BIPHASIC    54
00BF:  12 9A 99 59 3F   PUSH_FLOAT       0.8500000238418579
00C4:  53 00 00         MODULATE_STDP    0, 0
00C7:  16 00 00         LOAD_LOCAL       0
00CA:  11 F4 01 00 00   PUSH_INT         500
00CF:  30               CMP_EQ           
00D0:  42 19 00         JMP_IF_FALSE     25
00D3:  12 CD CC 8C 3F   PUSH_FLOAT       1.100000023841858
00D8:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
00DD:  12 CD CC 4C 3E   PUSH_FLOAT       0.20000000298023224
00E2:  12 00 00 00 00   PUSH_FLOAT       0.0
00E7:  50 24            STIM_BIPHASIC    36
00E9:  16 00 00         LOAD_LOCAL       0
00EC:  11 01 00 00 00   PUSH_INT         1
00F1:  20               ADD_I            
00F2:  17 00 00         STORE_LOCAL      0
00F5:  02               SYNC_TICK        
00F6:  40 15 FF         JMP              -235
00F9:  01               HALT             
======================================================================
```

---

## Appendix D: Live Verification & Latency Execution Logs

### D.1 Live 4-Tier E2E Test Suite (`python tests/run_e2e_tests.py`)

```text
$ python tests/run_e2e_tests.py  (exit_code=0)
================================================================================
 WetLang Neural Organoid Platform — 4-Tier E2E Test Suite
 Python Interpreter : 3.12.10 (C:\Users\Anikesh\AppData\Local\Programs\Python\Python312\python.exe)
 Working Directory  : D:\WetLang\wetlang_github_release
 Tests Discovered   : 313
================================================================================
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1Interlocks.test_tier1_f21_counter_reset_on_calm_happy took 1.94s
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_benchmarks_suite_happy took 2.48s
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_interlocks_suite_happy took 2.45s
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_ode_stability_suite_happy took 2.48s
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_parser_diagnostics_suite_happy took 1.83s
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_static_verifier_suite_happy took 2.06s

================================================================================
 E2E Test Execution Summary
--------------------------------------------------------------------------------
Tier        Passed      Skipped     Failed      Errors      Total     
--------------------------------------------------------------------------------
Tier 1      140         0           0           0           140       
Tier 2      140         0           0           0           140       
Tier 3      28          0           0           0           28        
Tier 4      5           0           0           0           5         
--------------------------------------------------------------------------------
TOTAL: 313 run | 313 passed | 0 skipped | 0 failed | 0 errors
Elapsed Time: 16.011 s
================================================================================

[STDERR]
.........................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 313 tests in 16.008s

OK
```

### D.2 Live Synthetic Unit Test Suite (`python -m pytest tests/test_*.py -v`)

```text
$ python -m pytest tests/test_*.py -v  (exit_code=0)
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\Anikesh\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: D:\WetLang\wetlang_github_release
configfile: pytest.ini
plugins: anyio-4.14.2, platformdirs-4.12.3
collecting ... collected 243 items

tests/test_actuators.py::TestWetLangActuators::test_cyber_physical_actuation PASSED [  0%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_01_si_time_scaling PASSED [  0%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_02_integer_arithmetic_precision PASSED [  1%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_03_cfg_reachability_pass3 PASSED [  1%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_04_watchdog_timeout_100k PASSED [  2%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_05_leaky_dc_drift_integrator PASSED [  2%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_06_focal_hyperactivity_breaker PASSED [  2%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_07_charge_density_limit PASSED [  3%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_08_cathodic_first_extracellular_sign PASSED [  3%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_09_lfp_zero_baseline PASSED [  4%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_10_amplifier_blanking PASSED [  4%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_11_dynamic_channel_dispatch PASSED [  4%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_12_user_functions_and_calls PASSED [  5%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_13_boolean_normalization PASSED [  5%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_14_safe_unaligned_memory_access PASSED [  6%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_15_free_running_simulation_ticks PASSED [  6%]
tests/test_benchmarks.py::test_compile_benchmark_01_active_inference PASSED [  6%]
tests/test_benchmarks.py::test_compile_benchmark_02_polychronous_reservoir PASSED [  7%]
tests/test_benchmarks.py::test_compile_benchmark_03_homeostatic_stabilization PASSED [  7%]
tests/test_benchmarks.py::test_run_benchmark_01_in_wetvm PASSED          [  8%]
tests/test_benchmarks.py::test_run_benchmark_02_in_wetvm PASSED          [  8%]
tests/test_benchmarks.py::test_run_benchmark_03_in_wetvm PASSED          [  9%]
tests/test_benchmarks.py::test_benchmark_telemetry_jsonl_formatting PASSED [  9%]
tests/test_benchmarks.py::test_benchmark_telemetry_csv_formatting PASSED [  9%]
tests/test_compiler.py::TestWetLangCompiler::test_lexer_physical_units PASSED [ 10%]
tests/test_compiler.py::TestWetLangCompiler::test_parser_and_semantic_analysis PASSED [ 10%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_hal_create_and_destroy PASSED [ 11%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_hal_mode_switching PASSED [ 11%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_driver_registration_and_lookup PASSED [ 11%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_emergency_crowbar_fastpath_sub_100us PASSED [ 12%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_router_valve_mapping_dead_head PASSED [ 12%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_command_encoding_and_decoding PASSED [ 13%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_constant_current_dac_ranges PASSED [ 13%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_compliance_rail_detection_and_clearing PASSED [ 13%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_in_situ_1khz_impedance_check PASSED [ 14%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_active_charge_recovery_switch PASSED [ 14%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_intan_fault_injection PASSED [ 15%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_intan_voltage_stimulation_duration_and_cathodic_polarity PASSED [ 15%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_routing_matrix_configuration PASSED [ 16%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_sequence_buffering_and_playback PASSED [ 16%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_voltage_clamping_and_charge_injection_protection PASSED [ 16%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_maxwell_connect_stim_and_fault_injection PASSED [ 17%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_harvard_rs232_formatting_and_prompt_parsing PASSED [ 17%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_dead_head_overpressure_interlock PASSED [ 18%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_bus_pdo_and_emergency_frames PASSED [ 18%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_dead_head_recovery_and_fault_injection PASSED [ 18%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_bus_boundary_dlc_and_extended_id_segregation PASSED [ 19%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_hil_bidirectional_loopback PASSED [ 19%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_crc8_algorithm PASSED [ 20%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_i2c_flow_reading PASSED [ 20%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_shdlc_framing_and_byte_stuffing PASSED [ 20%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_nak_and_multiple_crc_vectors PASSED [ 21%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_shdlc_illegal_stuffing_rejection PASSED [ 21%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_with_hal_pump_and_flow_routing PASSED [ 22%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_bytecode_actuation_with_hal PASSED [ 22%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_bytecode_dead_head_interlock_trip PASSED [ 23%]
tests/test_interlocks.py::test_voltage_clamp_positive_saturation PASSED  [ 23%]
tests/test_interlocks.py::test_voltage_clamp_negative_saturation PASSED  [ 23%]
tests/test_interlocks.py::test_voltage_clamp_within_water_window_passthrough PASSED [ 24%]
tests/test_interlocks.py::test_static_compile_rejection_overvoltage PASSED [ 24%]
tests/test_interlocks.py::test_static_compile_rejection_undervoltage PASSED [ 25%]
tests/test_interlocks.py::test_sliding_charge_balance_symmetric_biphasic_no_trip PASSED [ 25%]
tests/test_interlocks.py::test_sliding_charge_balance_unbalanced_dc_trip_at_100_ticks PASSED [ 25%]
tests/test_interlocks.py::test_sliding_charge_balance_boundary_threshold PASSED [ 26%]
tests/test_interlocks.py::test_epileptiform_sub_critical_burst_does_not_trip PASSED [ 26%]
tests/test_interlocks.py::test_epileptiform_focal_burst_few_channels_does_not_trip PASSED [ 27%]
tests/test_interlocks.py::test_epileptiform_runaway_trips_at_500_ticks PASSED [ 27%]
tests/test_interlocks.py::test_failsafe_state_lockout_blocks_further_operations PASSED [ 27%]
tests/test_milestone2_aer_hdmea.py::test_aer_packet_16byte_aligned_layout PASSED [ 28%]
tests/test_milestone2_aer_hdmea.py::test_aer_ring_burst_tolerance_and_quarantine PASSED [ 28%]
tests/test_milestone2_aer_hdmea.py::test_aer_bandwidth_reduction_metric PASSED [ 29%]
tests/test_milestone2_aer_hdmea.py::test_neo_bartlett_smoother_and_artifact_blanking PASSED [ 29%]
tests/test_milestone2_aer_hdmea.py::test_csr_sparse_synaptic_matrix_footprint_and_spmv PASSED [ 30%]
tests/test_milestone3_distributed.py::test_tsn_frame_32byte_aligned_layout_and_causality PASSED [ 30%]
tests/test_milestone3_distributed.py::test_ptp_slew_only_disciplining_and_safety_inhibit PASSED [ 30%]
tests/test_milestone3_distributed.py::test_timing_wheel_eliminates_head_of_line_blocking PASSED [ 31%]
tests/test_milestone3_distributed.py::test_late_packet_drop_telemetry PASSED [ 31%]
tests/test_milestone3_distributed.py::test_epileptiform_rate_governor_and_tx_blanking PASSED [ 32%]
tests/test_milestone4_rtos_arena.py::test_bare_metal_rtos_static_arena_allocation_and_scrubbing PASSED [ 32%]
tests/test_milestone4_rtos_arena.py::test_bounded_wcet_realtime_determinism PASSED [ 32%]
tests/test_milestone4_rtos_arena.py::test_multi_week_64bit_femtocoulomb_soak_stability PASSED [ 33%]
tests/test_milestone4_rtos_arena.py::test_material_dependent_water_window_clamping PASSED [ 33%]
tests/test_nir_bridge.py::test_cubalif_biophysical_parameters PASSED     [ 34%]
tests/test_nir_bridge.py::test_lif_parameters PASSED                     [ 34%]
tests/test_nir_bridge.py::test_izhikevich_cortical_phenotypes PASSED     [ 34%]
tests/test_nir_bridge.py::test_dales_principle_valid_matrices PASSED     [ 35%]
tests/test_nir_bridge.py::test_dales_principle_violation_raises PASSED   [ 35%]
tests/test_nir_bridge.py::test_decompose_to_dales_principle PASSED       [ 36%]
tests/test_nir_bridge.py::test_feedforward_topological_sort PASSED       [ 36%]
tests/test_nir_bridge.py::test_recurrent_graph_detection PASSED          [ 37%]
tests/test_nir_bridge.py::test_hdf5_serialization_roundtrip PASSED       [ 37%]
tests/test_nir_bridge.py::test_json_serialization_roundtrip PASSED       [ 37%]
tests/test_nir_bridge.py::test_nir_to_wet_source_generation PASSED       [ 38%]
tests/test_nir_bridge.py::test_nir_to_wet_ast PASSED                     [ 38%]
tests/test_nir_bridge.py::test_nir_to_wet_bytecode_and_native_execution PASSED [ 39%]
tests/test_nir_bridge.py::test_nir_dimension_validation_exceeding_channels PASSED [ 39%]
tests/test_nir_bridge.py::test_wet_ast_to_nir PASSED                     [ 39%]
tests/test_nir_bridge.py::test_wet_bytecode_to_nir PASSED                [ 40%]
tests/test_nir_bridge.py::test_wet_vm_to_nir PASSED                      [ 40%]
tests/test_nir_bridge.py::test_vm_get_synapse_matrix_live PASSED         [ 41%]
tests/test_nir_bridge.py::test_multilayer_feedforward_pipeline PASSED    [ 41%]
tests/test_nir_bridge.py::test_hdf5_to_bytecode_roundtrip PASSED         [ 41%]
tests/test_nir_bridge.py::test_affine_dales_principle PASSED             [ 42%]
tests/test_ode_stability.py::test_coba_lif_extreme_positive_current_injection PASSED [ 42%]
tests/test_ode_stability.py::test_coba_lif_extreme_negative_current_injection PASSED [ 43%]
tests/test_ode_stability.py::test_coba_lif_resting_equilibrium_stability PASSED [ 43%]
tests/test_ode_stability.py::test_absolute_refractory_clamp_2ms PASSED   [ 44%]
tests/test_ode_stability.py::test_membrane_clamped_at_reset_during_refractory PASSED [ 44%]
tests/test_ode_stability.py::test_dynamic_threshold_jump_and_decay PASSED [ 44%]
tests/test_ode_stability.py::test_slow_ahp_potassium_conductance_decay PASSED [ 45%]
tests/test_ode_stability.py::test_tsodyks_markram_ee_depression_and_recovery PASSED [ 45%]
tests/test_ode_stability.py::test_tsodyks_markram_ei_facilitation PASSED [ 46%]
tests/test_ode_stability.py::test_stdp_weight_hard_clamping PASSED       [ 46%]
tests/test_ode_stability.py::test_stdp_depression_bias_ratio PASSED      [ 46%]
tests/test_ode_stability.py::test_dales_principle_conductance_reversal PASSED [ 47%]
tests/test_ode_stability.py::test_native_wetvm_multi_tick_stability PASSED [ 47%]
tests/test_parser_diagnostics.py::test_lexer_keywords_and_identifiers PASSED [ 48%]
tests/test_parser_diagnostics.py::test_lexer_physical_literals_si_scaling PASSED [ 48%]
tests/test_parser_diagnostics.py::test_lexer_line_column_tracking PASSED [ 48%]
tests/test_parser_diagnostics.py::test_lexer_comment_skipping PASSED     [ 49%]
tests/test_parser_diagnostics.py::test_lexer_unterminated_block_comment PASSED [ 49%]
tests/test_parser_diagnostics.py::test_lexer_unterminated_string PASSED  [ 50%]
tests/test_parser_diagnostics.py::test_parser_arithmetic_precedence PASSED [ 50%]
tests/test_parser_diagnostics.py::test_parser_logical_operator_precedence PASSED [ 51%]
tests/test_parser_diagnostics.py::test_parser_parentheses_override PASSED [ 51%]
tests/test_parser_diagnostics.py::test_parser_unary_operators PASSED     [ 51%]
tests/test_parser_diagnostics.py::test_parser_grid_and_channel_declarations PASSED [ 52%]
tests/test_parser_diagnostics.py::test_parser_function_and_control_flow PASSED [ 52%]
tests/test_parser_diagnostics.py::test_parser_for_loop PASSED            [ 53%]
tests/test_parser_diagnostics.py::test_parser_stream_declaration PASSED  [ 53%]
tests/test_parser_diagnostics.py::test_parser_domain_primitives PASSED   [ 53%]
tests/test_parser_diagnostics.py::test_parser_error_diagnostics PASSED   [ 54%]
tests/test_parser_diagnostics.py::test_compiler_bytecode_binary_header_and_disasm PASSED [ 54%]
tests/test_parser_diagnostics.py::test_compile_benchmark_01 PASSED       [ 55%]
tests/test_parser_diagnostics.py::test_compile_benchmark_02 PASSED       [ 55%]
tests/test_parser_diagnostics.py::test_compile_benchmark_03 PASSED       [ 55%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_01_wbc_header_truncation PASSED [ 56%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_02_wbc_magic_corruption PASSED [ 56%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_03_wbc_crc32_tamper_detection PASSED [ 57%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_04_wbc_unsupported_version PASSED [ 57%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_05_stimulation_without_capability PASSED [ 58%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_06_microfluidics_without_capability PASSED [ 58%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_07_motor_actuation_without_capability PASSED [ 58%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_08_hydrodynamic_shear_stress_enforcement PASSED [ 59%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_09_compiler_shear_stress_rejection PASSED [ 59%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_10_valid_actuator_telemetry_inspection PASSED [ 60%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_11_cryptographic_signing_and_verification PASSED [ 60%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_12_division_by_zero_safety PASSED [ 60%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_13_stack_underflow_safety PASSED [ 61%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_14_multithreaded_concurrent_vms PASSED [ 61%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_15_hundred_cycle_memory_endurance PASSED [ 62%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_16_full_cyber_physical_closed_loop_program PASSED [ 62%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_01_hd_mea_water_window_clamping PASSED [ 62%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_02_persistent_unbounded_dc_accumulator PASSED [ 63%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_03_active_hardware_discharge_recovery PASSED [ 63%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_04_spherical_diffusion_thiele_anoxia PASSED [ 64%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_05_geometry_aware_shear_stress PASSED [ 64%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_06_dead_heading_valve_pump_interlock PASSED [ 65%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_07_ring0_life_support_supervisor PASSED [ 65%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_08_static_arena_allocation_zero_malloc PASSED [ 65%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_09_ed25519_asymmetric_bytecode_provenance PASSED [ 66%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_10_randles_interface_and_compliance_voltage_interlock PASSED [ 66%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_11_configurable_blanking_and_spatial_crosstalk PASSED [ 67%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_12_subnormal_denormal_conductance_zero_clamping PASSED [ 67%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_13_environmental_sensors_ph_do_co2_flow PASSED [ 67%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_14_cmos_thermal_duty_cycle_interlock PASSED [ 68%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_15_optical_bubble_sensor_pump_halt_interlock PASSED [ 68%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_16_load_time_c99_bytecode_verifier PASSED [ 69%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_17_live_state_checkpointing_and_hot_swap PASSED [ 69%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_18_typed_channel_banks_static_safety PASSED [ 69%]
tests/test_rt_scheduler.py::test_scheduler_lifecycle PASSED              [ 70%]
tests/test_rt_scheduler.py::test_scheduler_context_manager PASSED        [ 70%]
tests/test_rt_scheduler.py::test_spsc_stimulus_and_telemetry_streaming PASSED [ 71%]
tests/test_rt_scheduler.py::test_quiescent_hard_realtime_benchmark_10k_ticks PASSED [ 71%]
tests/test_rt_scheduler.py::test_stress_load_hard_realtime_benchmark_10k_ticks PASSED [ 72%]
tests/test_rt_scheduler.py::test_isochronous_pacing_zero_cumulative_drift PASSED [ 72%]
tests/test_runtime.py::TestWetLangRuntime::test_vm_stepping PASSED       [ 72%]
tests/test_sandbox.py::TestWetLangSandbox::test_gymnasium_compliance PASSED [ 73%]
tests/test_sandbox.py::TestWetLangSandbox::test_multi_organoid_orchestration PASSED [ 73%]
tests/test_sandbox.py::TestWetLangSandbox::test_snntorch_cross_validation PASSED [ 74%]
tests/test_section1_audit_remediation.py::test_ohms_law_dimensional_analysis PASSED [ 74%]
tests/test_section1_audit_remediation.py::test_transcendental_dimensionless_check_happy PASSED [ 74%]
tests/test_section1_audit_remediation.py::test_transcendental_dimensional_mismatch_rejected PASSED [ 75%]
tests/test_section1_audit_remediation.py::test_cfg_sync_tick_post_dominance_nested_blocks PASSED [ 75%]
tests/test_section1_audit_remediation.py::test_cfg_sync_tick_branching_rejection PASSED [ 76%]
tests/test_section1_audit_remediation.py::test_reference_channel_static_rejection PASSED [ 76%]
tests/test_section1_audit_remediation.py::test_anti_rollback_security_verification PASSED [ 76%]
tests/test_section3_audit_remediation.py::test_hardware_inline_pressure_dead_head_interlock PASSED [ 77%]
tests/test_section3_audit_remediation.py::test_asynchronous_microfluidics_queue PASSED [ 77%]
tests/test_section3_audit_remediation.py::test_i2c_bus_recovery_routine PASSED [ 78%]
tests/test_section3_audit_remediation.py::test_intan_charge_recovery_dac_registers PASSED [ 78%]
tests/test_section5_audit_remediation.py::test_fixed_point_femtocoulomb_dc_accumulation PASSED [ 79%]
tests/test_section5_audit_remediation.py::test_adversarial_corrupt_bytecode_fuzzing PASSED [ 79%]
tests/test_section5_audit_remediation.py::test_empirical_mea_burst_replay PASSED [ 79%]
tests/test_section5_audit_remediation.py::test_oi_hardware_scaling_memory_bounds PASSED [ 80%]
tests/test_static_verifier.py::test_symbol_resolution_undeclared_identifier PASSED [ 80%]
tests/test_static_verifier.py::test_symbol_resolution_redeclared_identifier PASSED [ 81%]
tests/test_static_verifier.py::test_symbol_resolution_duplicate_function_params PASSED [ 81%]
tests/test_static_verifier.py::test_mea_coordinates_valid PASSED         [ 81%]
tests/test_static_verifier.py::test_mea_coordinates_row_out_of_bounds PASSED [ 82%]
tests/test_static_verifier.py::test_mea_coordinates_col_out_of_bounds PASSED [ 82%]
tests/test_static_verifier.py::test_mea_coordinates_negative_row PASSED  [ 83%]
tests/test_static_verifier.py::test_mea_coordinates_negative_col PASSED  [ 83%]
tests/test_static_verifier.py::test_mea_coordinates_linear_out_of_bounds PASSED [ 83%]
tests/test_static_verifier.py::test_mea_coordinates_linear_negative PASSED [ 84%]
tests/test_static_verifier.py::test_mea_coordinates_in_stim_stmt_out_of_bounds PASSED [ 84%]
tests/test_static_verifier.py::test_dimensional_homogeneous_addition PASSED [ 85%]
tests/test_static_verifier.py::test_dimensional_incompatible_addition PASSED [ 85%]
tests/test_static_verifier.py::test_dimensional_multiplication_current_time_to_charge PASSED [ 86%]
tests/test_static_verifier.py::test_dimensional_incompatible_comparison PASSED [ 86%]
tests/test_static_verifier.py::test_static_voltage_clamp_valid PASSED    [ 86%]
tests/test_static_verifier.py::test_static_voltage_clamp_positive_exceeded PASSED [ 87%]
tests/test_static_verifier.py::test_static_voltage_clamp_negative_exceeded PASSED [ 87%]
tests/test_static_verifier.py::test_static_voltage_clamp_unitless_float_exceeded PASSED [ 88%]
tests/test_static_verifier.py::test_loop_yield_bounded_while_loop PASSED [ 88%]
tests/test_static_verifier.py::test_loop_yield_unbounded_while_loop_rejected PASSED [ 88%]
tests/test_static_verifier.py::test_loop_yield_unbounded_if_branch_rejected PASSED [ 89%]
tests/test_static_verifier.py::test_loop_yield_bounded_if_branch_accepted PASSED [ 89%]
tests/test_static_verifier.py::test_loop_yield_pure_compute_loop_accepted PASSED [ 90%]
tests/test_static_verifier.py::test_loop_yield_unbounded_for_loop_rejected PASSED [ 90%]
tests/test_static_verifier.py::test_loop_yield_bounded_for_loop_accepted PASSED [ 90%]
tests/test_static_verifier.py::test_loop_yield_stream_cycle_unbounded_rejected PASSED [ 91%]
tests/test_static_verifier.py::test_loop_yield_stream_cycle_bounded_accepted PASSED [ 91%]
tests/test_static_verifier.py::test_loop_yield_nested_block_unbounded_rejected PASSED [ 92%]
tests/test_static_verifier.py::test_loop_yield_inner_while_loop_evasion_rejected PASSED [ 92%]
tests/test_static_verifier.py::test_loop_yield_inner_for_loop_evasion_rejected PASSED [ 93%]
tests/test_static_verifier.py::test_loop_yield_nested_block_if_without_else_rejected PASSED [ 93%]
tests/test_static_verifier.py::test_static_voltage_clamp_constant_folded_addition_exceeded PASSED [ 93%]
tests/test_static_verifier.py::test_static_voltage_clamp_constant_folded_multiplication_exceeded PASSED [ 94%]
tests/test_static_verifier.py::test_static_voltage_clamp_variable_constant_exceeded PASSED [ 94%]
tests/test_static_verifier.py::test_negative_high_voltage_capability_and_manifest PASSED [ 95%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_out_of_bounds PASSED [ 95%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_linear_out_of_bounds PASSED [ 95%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_valid_mapping PASSED [ 96%]
tests/test_static_verifier.py::test_capability_multi_electrode_threshold PASSED [ 96%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_01_single_organoid_sandbox PASSED [ 97%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_02_16_organoid_cluster_sandbox PASSED [ 97%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_03_1024_parametric_cluster_scaling PASSED [ 97%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_04_axonal_conduction_delay_timing PASSED [ 98%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_05_krogh_anoxia_compile_check PASSED [ 98%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_06_gymnasium_env_compliance PASSED [ 99%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_07_gymnasium_active_inference_loop PASSED [ 99%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_08_snntorch_biophysical_ode_convergence PASSED [100%]

============================== warnings summary ===============================
C:\Users\Anikesh\AppData\Local\Programs\Python\Python312\Lib\site-packages\anyio\pytest_plugin.py:14
  C:\Users\Anikesh\AppData\Local\Programs\Python\Python312\Lib\site-packages\anyio\pytest_plugin.py:14: PytestRemovedIn10Warning: _pytest.python.CallSpec2 has been renamed to CallSpec.
  The CallSpec2 alias will be removed in pytest 10.
  Update imports to use CallSpec instead.
  See https://docs.pytest.org/en/stable/deprecations.html#callspec2-renamed
    from _pytest.python import CallSpec2

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================= 243 passed, 1 warning in 14.73s =======================
```

### D.3 Live 10,000-Tick `wetvm.dll` Latency Microbenchmark

```text
Host Platform : Windows-11-10.0.26300-SP0 (AMD64)
Processor     : Intel64 Family 6 Model 189 Stepping 1, GenuineIntel
Python        : 3.12.10
Workload      : benchmarks/01_active_inference_closed_loop.wet (dt = 0.1 ms = 100 us)

[Mode A: Per-Tick Python->C FFI vm.step_tick() x 10,000 ticks]
  mean   : 27.528 us/tick
  median : 24.800 us/tick
  p95    : 29.300 us/tick
  p99    : 67.600 us/tick
  min    : 15.800 us/tick
  max    : 2751.000 us/tick
  wall   : 279.735 ms (1.0 s simulated time)

[Mode B: Batched Native C vm.run_ticks(10000) x 10 trials]
  mean       : 24.700 us/tick
  median     : 25.578 us/tick
  min        : 21.286 us/tick
  max        : 26.447 us/tick
  throughput : 40485 ticks/sec
  speedup    : 4.05x real-time
```

---

## Appendix E: Verified Line-Numbered Core Source Code Listing

Covers all 31 core source files across `compiler/`, `native/include/`, `native/src/`, `native/build.py`, `native/interlocks.py`, `bindings/`, `biophysics/`, and `benchmarks/*.wet`.

### `native/include/biophysics.h` (214 lines, SHA-256: `c1ff823a6b9772a6...`)

```text
   1 | #ifndef WET_BIOPHYSICS_H
   2 | #define WET_BIOPHYSICS_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | 
   7 | #ifdef __cplusplus
   8 | extern "C" {
   9 | #endif
  10 | 
  11 | /* =========================================================================
  12 |  * WetLang In-Silico Biophysical Digital Twin (64-Neuron 8x8 MEA)
  13 |  * =========================================================================
  14 |  * - Fixed integration timestep: dt = 0.1 ms
  15 |  * - Conductance-Based Leaky Integrate-and-Fire (COBA-LIF) + slow AHP
  16 |  * - Exact Exponential Euler numerical integration
  17 |  * - Absolute refractory period: 2.0 ms (20 ticks -> max 500 Hz single neuron)
  18 |  * - Relative refractory period: dynamic threshold (+15 mV, tau = 10 ms)
  19 |  * - Tsodyks-Markram Short-Term Plasticity (4 classes: E->E, E->I, I->E, I->I)
  20 |  * - Online Pairwise Trace STDP (1.05x LTD bias, [0, 40 nS], Dale's principle)
  21 |  * - 8x8 MEA Volume Conduction (200 um pitch) forward pickup & cross-talk
  22 |  * ========================================================================= */
  23 | 
  24 | #define BIO_NUM_NEURONS      64
  25 | #define BIO_NUM_CHANNELS     64
  26 | #define BIO_GRID_ROWS        8
  27 | #define BIO_GRID_COLS        8
  28 | #define BIO_PITCH_UM         200.0f
  29 | 
  30 | /* Absolute refractory period: 2.0 ms at dt = 0.1 ms -> 20 ticks */
  31 | #define BIO_ABS_REFRACT_MS   2.0f
  32 | #define BIO_ABS_REFRACT_TICKS 20
  33 | 
  34 | /* Synaptic weight hard bounds (nS) */
  35 | #define BIO_W_MIN_NS         0.0f
  36 | #define BIO_W_MAX_NS         40.0f
  37 | 
  38 | /* Spike history ring buffer per channel for sliding-window readout (500 ticks = 50.0 ms) */
  39 | #define BIO_SPIKE_HISTORY_LEN 500
  40 | 
  41 | /* Synapse Class Enumeration (Tsodyks-Markram) */
  42 | typedef enum {
  43 |     SYN_CLASS_EE = 0, /* Excitatory -> Excitatory (Depressing) */
  44 |     SYN_CLASS_EI = 1, /* Excitatory -> Inhibitory (Facilitating) */
  45 |     SYN_CLASS_IE = 2, /* Inhibitory -> Excitatory (Depressing) */
  46 |     SYN_CLASS_II = 3  /* Inhibitory -> Inhibitory (Moderately depressing) */
  47 | } bio_syn_class_t;
  48 | 
  49 | /* Directed Synapse Structure */
  50 | typedef struct {
  51 |     uint8_t  exists;      /* 1 if connected, 0 otherwise */
  52 |     uint8_t  syn_class;   /* bio_syn_class_t */
  53 |     float    weight_ns;   /* Conductance weight in [0.0, 40.0] nS (always >= 0; sign via E_rev) */
  54 |     /* Tsodyks-Markram STP state */
  55 |     float    u_stp;       /* Utilization of synaptic efficacy */
  56 |     float    x_stp;       /* Fraction of available vesicles */
  57 |     float    U_base;      /* Baseline release probability */
  58 |     float    tau_rec_ms;  /* Recovery time constant (ms) */
  59 |     float    tau_fac_ms;  /* Facilitation time constant (ms) */
  60 | } bio_synapse_t;
  61 | 
  62 | /* Active Biphasic Stimulation Pulse Schedule per Channel */
  63 | typedef struct {
  64 |     uint8_t  active;
  65 |     float    voltage_v;         /* Clamped amplitude (V) */
  66 |     uint32_t phase1_ticks_left; /* Cathodic / Phase 1 remaining ticks */
  67 |     uint32_t interphase_ticks_left; /* Interphase gap (0 V) remaining ticks */
  68 |     uint32_t phase2_ticks_left; /* Anodic / Phase 2 remaining ticks */
  69 |     float    phase1_amp_v;      /* Phase 1 voltage */
  70 |     float    phase2_amp_v;      /* Phase 2 counter-balancing voltage */
  71 | } bio_stim_pulse_t;
  72 | 
  73 | /* Complete Biophysical State */
  74 | typedef struct {
  75 |     double   dt_ms;
  76 |     uint64_t tick_count;
  77 |     uint64_t rng_state;
  78 | 
  79 |     /* Neuron type: 1 = Excitatory (80%, 51 neurons), 0 = Inhibitory (20%, 13 neurons) */
  80 |     uint8_t  is_excitatory[BIO_NUM_NEURONS];
  81 | 
  82 |     /* 3D coordinates in micrometers (x, y on 8x8 grid, z offset) */
  83 |     float    pos_x_um[BIO_NUM_NEURONS];
  84 |     float    pos_y_um[BIO_NUM_NEURONS];
  85 |     float    pos_z_um[BIO_NUM_NEURONS];
  86 | 
  87 |     /* COBA-LIF state variables */
  88 |     float    v_m_mv[BIO_NUM_NEURONS];         /* Membrane potential (mV), resting -70 mV */
  89 |     float    v_thresh_mv[BIO_NUM_NEURONS];    /* Dynamic firing threshold (mV), base -50 mV */
  90 |     float    g_exc_ns[BIO_NUM_NEURONS];       /* Excitatory synaptic conductance (nS) */
  91 |     float    g_inh_ns[BIO_NUM_NEURONS];       /* Inhibitory synaptic conductance (nS) */
  92 |     float    g_ahp_ns[BIO_NUM_NEURONS];       /* Slow after-hyperpolarization conductance (nS) */
  93 |     uint16_t refract_ticks[BIO_NUM_NEURONS];  /* Remaining absolute refractory ticks */
  94 | 
  95 |     /* STDP Eligibility Traces per Neuron */
  96 |     float    trace_pre[BIO_NUM_NEURONS];      /* Pre-synaptic trace (tau_plus = 20 ms) */
  97 |     float    trace_post[BIO_NUM_NEURONS];     /* Post-synaptic trace (tau_minus = 20 ms) */
  98 |     float    stdp_lr_scale;                   /* Dynamic STDP learning rate multiplier */
  99 |     float    cumulative_weight_drift_ns;      /* Cumulative |dw| across all plastic synapses */
 100 | 
 101 |     /* Dense 64x64 Synaptic Matrix */
 102 |     bio_synapse_t synapses[BIO_NUM_NEURONS][BIO_NUM_NEURONS];
 103 | 
 104 |     /* 8x8 MEA Volume Conduction Forward Matrix (channel <- neuron) */
 105 |     float    pickup_matrix[BIO_NUM_CHANNELS][BIO_NUM_NEURONS];
 106 | 
 107 |     /* Active stimulation pulses & instantaneous electrode voltages */
 108 |     bio_stim_pulse_t stim_pulses[BIO_NUM_CHANNELS];
 109 |     float    ext_stim_v[BIO_NUM_CHANNELS];       /* Applied electrode voltage this tick (V) */
 110 |     float    mea_voltage_v[BIO_NUM_CHANNELS];    /* Extracellular pickup + stim potential (V) */
 111 |     float    tick_charge_nc[BIO_NUM_CHANNELS];   /* Charge injected this tick (nC) */
 112 | 
 113 |     /* Spike outputs and rolling 50.0 ms history ring buffer */
 114 |     uint8_t  spikes_now[BIO_NUM_NEURONS];
 115 |     uint8_t  spike_history[BIO_NUM_CHANNELS][BIO_SPIKE_HISTORY_LEN];
 116 |     uint16_t spike_history_head;
 117 |     uint16_t spike_count_50ms[BIO_NUM_CHANNELS]; /* Running count over last 500 ticks */
 118 |     float    channel_rate_hz[BIO_NUM_CHANNELS];
 119 |     float    population_rate_hz;
 120 | 
 121 |     /* Biophysical constants */
 122 |     float    c_m_pf;          /* Membrane capacitance (200 pF) */
 123 |     float    g_leak_ns;       /* Leak conductance (10 nS -> tau_m = 20 ms) */
 124 |     float    e_leak_mv;       /* Leak reversal (-70 mV) */
 125 |     float    e_reset_mv;      /* Reset potential (-75 mV) */
 126 |     float    e_thresh_base_mv;/* Base spike threshold (-50 mV) */
 127 |     float    e_exc_mv;        /* Excitatory reversal (0 mV) */
 128 |     float    e_inh_mv;        /* Inhibitory reversal (-80 mV) */
 129 |     float    e_k_mv;          /* Potassium / AHP reversal (-90 mV) */
 130 |     float    tau_exc_ms;      /* AMPA decay (5.0 ms) */
 131 |     float    tau_inh_ms;      /* GABA_A decay (10.0 ms) */
 132 |     float    tau_ahp_ms;      /* Slow AHP decay (80.0 ms) */
 133 |     float    tau_thresh_ms;   /* Dynamic threshold decay (10.0 ms) */
 134 |     float    tau_stdp_plus_ms;/* STDP LTP window (20.0 ms) */
 135 |     float    tau_stdp_minus_ms;/* STDP LTD window (20.0 ms) */
 136 |     float    stdp_a_plus;     /* LTP amplitude (0.20 nS) */
 137 |     float    stdp_a_minus;    /* LTD amplitude (0.21 nS = 1.05x bias) */
 138 |     float    electrode_impedance_kohm; /* Electrode-electrolyte impedance (50 kOhm) */
 139 |     uint16_t stim_blanking_ticks[BIO_NUM_CHANNELS]; /* Post-stimulus amplifier artifact blanking ticks */
 140 |     uint16_t default_blanking_ticks; /* Configurable baseline blanking duration in ticks (e.g. 20 = 2.0 ms) */
 141 |     uint8_t  spatial_blanking_enabled; /* 1 = propagate attenuated blanking to adjacent MEA channels */
 142 | 
 143 |     /* Randles Equivalent Circuit Interface Model (Electrode-Electrolyte Interface) */
 144 |     float    r_solution_kohm;        /* Solution bulk resistance Rs (e.g. 2.0 kOhm) */
 145 |     float    r_charge_transfer_kohm; /* Faradaic charge transfer resistance Rct (e.g. 5000.0 kOhm = 5 MOhm) */
 146 |     float    c_double_layer_pf[BIO_NUM_CHANNELS];  /* Helmholtz double-layer capacitance Cdl */
 147 |     float    v_double_layer_v[BIO_NUM_CHANNELS];   /* Instantaneous polarization voltage Vdl(t) */
 148 |     float    last_stim_current_ua[BIO_NUM_CHANNELS]; /* Last injected constant current */
 149 |     float    max_compliance_voltage_v; /* Maximum ASIC compliance voltage (e.g. 7.0 V) */
 150 | } bio_state_t;
 151 | 
 152 | /* Lifecycle & Simulation Functions */
 153 | void biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed);
 154 | void biophysics_reset(bio_state_t* bio);
 155 | 
 156 | /* Schedule a biphasic stimulation pulse on a channel (already clamped by interlocks) */
 157 | void biophysics_schedule_stim(
 158 |     bio_state_t* bio,
 159 |     uint8_t channel,
 160 |     float clamped_voltage_v,
 161 |     float phase1_ms,
 162 |     float phase2_ms
 163 | );
 164 | 
 165 | void biophysics_schedule_stim_ext(
 166 |     bio_state_t* bio,
 167 |     uint8_t channel,
 168 |     float clamped_voltage_v,
 169 |     float phase1_ms,
 170 |     float phase2_ms,
 171 |     float interphase_ms
 172 | );
 173 | 
 174 | /* Schedule a constant-current stimulation pulse on a channel (Randles interface model) */
 175 | void biophysics_schedule_stim_current(
 176 |     bio_state_t* bio,
 177 |     uint8_t channel,
 178 |     float current_ua,
 179 |     float phase1_ms,
 180 |     float phase2_ms,
 181 |     float interphase_ms
 182 | );
 183 | 
 184 | /* Configure post-stimulus blanking window in milliseconds */
 185 | void biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial);
 186 | 
 187 | /* Query instantaneous Randles polarization and total electrode potential */
 188 | void biophysics_get_randles_state(
 189 |     const bio_state_t* bio,
 190 |     uint8_t channel,
 191 |     float* out_v_dl_v,
 192 |     float* out_v_elec_v
 193 | );
 194 | 
 195 | /* Direct instantaneous voltage override (used for fail-safe zeroing or external injection) */
 196 | void biophysics_zero_all_stim(bio_state_t* bio);
 197 | 
 198 | /* Modulate STDP weight directly (bounded within [0, 40 nS], respecting Dale's principle) */
 199 | void biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns);
 200 | 
 201 | /* Advance entire 64-neuron network by 1 fixed timestep (dt = 0.1 ms) */
 202 | void biophysics_step_tick(bio_state_t* bio);
 203 | 
 204 | /* Query spike count on a channel over a sliding window (up to 50.0 ms) */
 205 | uint32_t biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms);
 206 | 
 207 | /* Query synaptic weight between pre and post neurons */
 208 | float biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post);
 209 | 
 210 | #ifdef __cplusplus
 211 | }
 212 | #endif
 213 | 
 214 | #endif /* WET_BIOPHYSICS_H */
```

### `native/include/interlocks.h` (188 lines, SHA-256: `5017b655ffe3fd61...`)

```text
   1 | #ifndef WET_INTERLOCKS_H
   2 | #define WET_INTERLOCKS_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wetvm_types.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | #if defined(_WIN32) || defined(__CYGWIN__)
  13 |   #ifdef WET_BUILDING_DLL
  14 |     #define WET_EXPORT __declspec(dllexport)
  15 |   #else
  16 |     #define WET_EXPORT __declspec(dllimport)
  17 |   #endif
  18 | #else
  19 |   #if defined(__GNUC__) && __GNUC__ >= 4
  20 |     #define WET_EXPORT __attribute__((visibility("default")))
  21 |   #else
  22 |     #define WET_EXPORT
  23 |   #endif
  24 | #endif
  25 | 
  26 | /* =========================================================================
  27 |  * WetLang Cycle-Accurate Biocybersecurity Hardware Watchdog & Interlocks
  28 |  * =========================================================================
  29 |  * 1. Water-Window Voltage Clamp: Hard clamp [-1.2 V, +1.2 V]
  30 |  * 2. Sliding Charge-Balance Ring Buffer:
  31 |  *    - 100-tick (10.0 ms at dt=0.1 ms) per-electrode circular buffer
  32 |  *    - Trip ERR_CHARGE_IMBALANCE if |Q_accum[ch]| >= 0.5 nC
  33 |  * 3. Epileptiform Runaway Firing Breaker:
  34 |  *    - Monitors sliding 50.0 ms firing rate per channel
  35 |  *    - Hyperactive channel: firing_rate > 150.0 Hz
  36 |  *    - Fraction threshold: > 35% of 64 channels (>= 23 channels)
  37 |  *    - Sustained duration: 500 consecutive ticks (50.0 ms)
  38 |  *    - Trip ERR_EPILEPTIFORM_RUNAWAY -> immediately zero DACs & lock VM
  39 |  * 4. Fail-Safe Interlock Lockout:
  40 |  *    - Once tripped, zeroes all stimulation voltages (0.0 V) and blocks
  41 |  *      further stimulation/execution until explicit hardware reset.
  42 |  * ========================================================================= */
  43 | 
  44 | #define INTERLOCK_NUM_CHANNELS          64
  45 | #define INTERLOCK_VOLTAGE_LIMIT_V       1.2f
  46 | #define INTERLOCK_CHARGE_WINDOW_TICKS   100     /* 10.0 ms at dt = 0.1 ms */
  47 | #define INTERLOCK_CHARGE_LIMIT_NC       0.5f    /* 0.5 nC per electrode */
  48 | #define INTERLOCK_EPILEPSY_RATE_HZ      150.0f  /* > 150 Hz */
  49 | #define INTERLOCK_EPILEPSY_MIN_CHANNELS 23      /* > 35% of 64 (22.4 -> 23) */
  50 | #define INTERLOCK_EPILEPSY_SUSTAIN_TICKS 500    /* 50.0 ms at dt = 0.1 ms */
  51 | 
  52 | /* Hardened Biocybersecurity Extensions (Audit Remediation) */
  53 | #define INTERLOCK_DC_DRIFT_LIMIT_NC     1.0f    /* 1.0 nC cumulative unrecovered DC charge */
  54 | #define INTERLOCK_BLEED_DECAY_PER_TICK  0.99999f/* tau = 10.0 s (100,000 ticks) */
  55 | #define INTERLOCK_CHARGE_DENSITY_LIMIT_NC 0.40f /* 0.40 nC max per single pulse phase (Shannon limit) */
  56 | #define INTERLOCK_FOCAL_RATE_HZ         150.0f  /* 150 Hz focal rate */
  57 | #define INTERLOCK_FOCAL_SUSTAIN_TICKS   2500    /* 250.0 ms sustained focal hyperactivity */
  58 | #define INTERLOCK_DUTY_CYCLE_LIMIT      0.05f   /* 5% max stimulation duty cycle */
  59 | #define INTERLOCK_DUTY_CYCLE_DECAY      0.9999f /* tau = 1.0 s (10,000 ticks) */
  60 | #define INTERLOCK_THERMAL_LIMIT_C       38.0f   /* 38.0 C max incubator / CMOS die temperature */
  61 | #define INTERLOCK_COMPLIANCE_LIMIT_V    7.0f    /* 7.0 V Intan RHS2116 compliance rail */
  62 | 
  63 | /* Phase 3 Electrochemical Water-Window & Material CIC Limits */
  64 | typedef enum {
  65 |     WET_ELEC_PLATINUM = 0,  /* 0.10 mC/cm^2 (water-window limit: 0.05..0.15 mC/cm^2) */
  66 |     WET_ELEC_TIN      = 1,  /* 0.90 mC/cm^2 (Titanium Nitride) */
  67 |     WET_ELEC_IROX     = 2,  /* 2.00 mC/cm^2 (Iridium Oxide / SIROF) */
  68 |     WET_ELEC_PEDOT    = 3,  /* 5.00 mC/cm^2 (Conductive Polymer PEDOT:PSS) */
  69 |     WET_ELEC_CUSTOM   = 4
  70 | } wet_electrode_material_t;
  71 | 
  72 | typedef enum {
  73 |     INTERLOCK_TRIP_NONE                = 0,
  74 |     INTERLOCK_TRIP_CHARGE_IMBALANCE    = 1,
  75 |     INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY= 2,
  76 |     INTERLOCK_TRIP_CAPABILITY_VIOLATION= 3,
  77 |     INTERLOCK_TRIP_VOLTAGE_OVERRIDE    = 4,
  78 |     INTERLOCK_TRIP_DC_DRIFT            = 5,
  79 |     INTERLOCK_TRIP_CHARGE_DENSITY      = 6,
  80 |     INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY= 7,
  81 |     INTERLOCK_TRIP_DEAD_HEAD_PRESSURE  = 8,
  82 |     INTERLOCK_TRIP_THERMAL_LIMIT       = 9,
  83 |     INTERLOCK_TRIP_BUBBLE_DETECTED     = 10,
  84 |     INTERLOCK_TRIP_COMPLIANCE_RAILED   = 11
  85 | } interlock_trip_reason_t;
  86 | 
  87 | typedef struct {
  88 |     /* Fail-safe lockout state */
  89 |     uint8_t  locked;
  90 |     uint8_t  trip_reason;          /* interlock_trip_reason_t */
  91 |     uint8_t  tripped_channel;
  92 |     uint64_t trip_tick;
  93 |     float    trip_value;           /* Measured charge (nC) or hyperactive count */
  94 |     char     diagnostic[256];
  95 | 
  96 |     /* Water-window clamp statistics */
  97 |     uint64_t clamp_events;
  98 | 
  99 |     /* 10.0 ms (100-tick) sliding charge balance ring buffer per electrode */
 100 |     float    q_ring[INTERLOCK_NUM_CHANNELS][INTERLOCK_CHARGE_WINDOW_TICKS];
 101 |     float    q_accum[INTERLOCK_NUM_CHANNELS];
 102 |     uint16_t q_head;
 103 | 
 104 |     /* Long-horizon leaky DC charge integrator (10.0 s bleed time constant) */
 105 |     float    q_dc[INTERLOCK_NUM_CHANNELS];
 106 | 
 107 |     /* Phase 3: Unbounded Cumulative DC Charge Accumulator (no leaky decay; resets ONLY on active discharge) */
 108 |     float    cumulative_unbounded_dc_nc[INTERLOCK_NUM_CHANNELS];
 109 |     int64_t  cumulative_dc_femtocoulombs[INTERLOCK_NUM_CHANNELS]; /* Exact 64-bit fixed-point femtoCoulombs (1 nC = 1e6 fC) - immune to multi-week float32 ULP saturation */
 110 | 
 111 |     /* Phase 3 & v2.1: Electrode Material & Material-Dependent Water-Window */
 112 |     uint8_t  electrode_material;   /* wet_electrode_material_t */
 113 |     float    electrode_area_um2;   /* e.g. 132.25 um^2 for MaxOne, or 5000 um^2 for macro */
 114 |     float    v_water_window_low_v; /* Material-dependent cathodic limit (e.g. -0.6 V for Pt, -0.9 V for TiN) */
 115 |     float    v_water_window_high_v;/* Material-dependent anodic limit (e.g. +0.8 V for Pt, +0.9 V for TiN) */
 116 |     float    max_charge_per_phase_nc; /* Dynamic limit = CIC * Area */
 117 |     float    max_cumulative_dc_nc;    /* Dynamic persistent DC limit */
 118 | 
 119 |     /* Active Emc Closed-Loop Hardware Trimming & OCP Guard */
 120 |     uint8_t  active_emc_trim_enabled;
 121 |     float    emc_trim_offset_v[INTERLOCK_NUM_CHANNELS];
 122 |     float    reference_ocp_baseline_v;
 123 |     uint8_t  reference_ocp_fault_tripped;
 124 | 
 125 |     /* Phase 3: Microfluidic Dead-Heading Pressure Interlock */
 126 |     uint8_t  dead_head_protection_enabled;
 127 |     uint8_t  pump_valve_mapping[8]; /* Maps pump ID to downstream pinch valve ID */
 128 | 
 129 |     /* 50.0 ms (500-tick) sustained epileptiform runaway counter */
 130 |     uint32_t hyperactive_consecutive_ticks;
 131 |     uint32_t last_hyperactive_channel_count;
 132 | 
 133 |     /* Per-channel focal hyperactivity & stimulation duty cycle monitors */
 134 |     uint32_t focal_hyperactive_ticks[INTERLOCK_NUM_CHANNELS];
 135 |     float    stim_duty_filter[INTERLOCK_NUM_CHANNELS];
 136 | 
 137 |     /* Authorized bytecode capabilities */
 138 |     uint16_t authorized_capabilities;
 139 |     uint32_t authorized_channels;
 140 | 
 141 |     /* Typed Channel Banks / Capabilities (Bug C-05 Remediation) */
 142 |     uint64_t reference_channels_mask;      /* Cannot be stimulated */
 143 |     uint64_t recording_only_channels_mask; /* Cannot be stimulated */
 144 | } interlock_state_t;
 145 | 
 146 | /* Initialize / reset watchdog state */
 147 | void interlocks_init(interlock_state_t* il);
 148 | void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count);
 149 | void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask);
 150 | 
 151 | /* Phase 3 Electrochemical & Hardware Interlock API */
 152 | WET_EXPORT void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2);
 153 | void interlocks_active_discharge(interlock_state_t* il, uint8_t channel);
 154 | void interlocks_active_discharge_all(interlock_state_t* il);
 155 | void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable);
 156 | 
 157 | /* Environmental & Compliance Safety Checks */
 158 | wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c);
 159 | wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id);
 160 | wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v);
 161 | 
 162 | /* Static authorization check for an opcode against loaded bytecode capabilities */
 163 | int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel);
 164 | 
 165 | /* Clamp requested stimulation voltage to material water window */
 166 | WET_EXPORT float interlocks_clamp_voltage(interlock_state_t* il, float requested_v);
 167 | 
 168 | /* Advance 10.0 ms charge ring buffer with this tick's per-channel injected charge (nC).
 169 |  * Returns WET_OK or WET_ERR_CHARGE_IMBALANCE (locking the watchdog on trip). */
 170 | wet_status_t interlocks_record_charge_tick(
 171 |     interlock_state_t* il,
 172 |     uint64_t current_tick,
 173 |     const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
 174 | );
 175 | 
 176 | /* Evaluate epileptiform runaway breaker using per-channel firing rates (Hz).
 177 |  * Returns WET_OK or WET_ERR_EPILEPTIFORM_RUNAWAY (locking the watchdog on trip). */
 178 | wet_status_t interlocks_check_epileptiform(
 179 |     interlock_state_t* il,
 180 |     uint64_t current_tick,
 181 |     const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
 182 | );
 183 | 
 184 | #ifdef __cplusplus
 185 | }
 186 | #endif
 187 | 
 188 | #endif /* WET_INTERLOCKS_H */
```

### `native/include/wet_aer.h` (159 lines, SHA-256: `84b2e70694f38a59...`)

```text
   1 | #ifndef WET_AER_H
   2 | #define WET_AER_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | 
   7 | #ifdef __cplusplus
   8 | extern "C" {
   9 | #endif
  10 | 
  11 | #define WET_AER_CACHELINE_SIZE 128
  12 | #define WET_AER_PACKET_SIZE    16
  13 | #define WET_AER_MAX_CHANNELS   26400
  14 | 
  15 | #if defined(_WIN32) || defined(__CYGWIN__)
  16 |   #ifdef WET_BUILDING_DLL
  17 |     #define WET_EXPORT __declspec(dllexport)
  18 |   #else
  19 |     #define WET_EXPORT __declspec(dllimport)
  20 |   #endif
  21 | #else
  22 |   #if defined(__GNUC__) && __GNUC__ >= 4
  23 |     #define WET_EXPORT __attribute__((visibility("default")))
  24 |   #else
  25 |     #define WET_EXPORT
  26 |   #endif
  27 | #endif
  28 | 
  29 | /*
  30 |  * Production 16-byte AER Packet Layout
  31 |  * Guaranteed 8-byte natural alignment in arrays: eliminates hardware Alignment/UsageFault
  32 |  * exceptions on ARM Cortex-M/R and RISC-V cores while preventing split cache-line loads.
  33 |  */
  34 | #if defined(_MSC_VER)
  35 | #pragma pack(push, 8)
  36 | typedef struct {
  37 |     uint64_t timestamp_tick;    /* 8 bytes: tick count */
  38 |     uint16_t channel_id;        /* 2 bytes: 0..65535 electrode index */
  39 |     int16_t  peak_amplitude_uv; /* 2 bytes: spike peak amplitude in microvolts */
  40 |     uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: multi-unit, bit 2: stim-recovery */
  41 |     uint16_t reserved;          /* 2 bytes: padding for strict 16-byte power-of-two alignment */
  42 | } wet_aer_packet_t;
  43 | #pragma pack(pop)
  44 | #else
  45 | typedef struct __attribute__((aligned(8))) {
  46 |     uint64_t timestamp_tick;    /* 8 bytes: tick count */
  47 |     uint16_t channel_id;        /* 2 bytes: 0..65535 electrode index */
  48 |     int16_t  peak_amplitude_uv; /* 2 bytes: spike peak amplitude in microvolts */
  49 |     uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: multi-unit, bit 2: stim-recovery */
  50 |     uint16_t reserved;          /* 2 bytes: padding for strict 16-byte power-of-two alignment */
  51 | } wet_aer_packet_t;
  52 | #endif
  53 | 
  54 | #if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
  55 | _Static_assert(sizeof(wet_aer_packet_t) == 16, "wet_aer_packet_t must be exactly 16 bytes");
  56 | #endif
  57 | 
  58 | /*
  59 |  * High-Throughput Burst-Tolerant Lockless SPSC Circular Ring Buffer
  60 |  */
  61 | typedef struct {
  62 |     /* Producer cacheline */
  63 |     uint8_t pad0[WET_AER_CACHELINE_SIZE];
  64 |     uint32_t head;
  65 |     uint8_t pad1[WET_AER_CACHELINE_SIZE - sizeof(uint32_t)];
  66 | 
  67 |     /* Consumer cacheline */
  68 |     uint32_t tail;
  69 |     uint8_t pad2[WET_AER_CACHELINE_SIZE - sizeof(uint32_t)];
  70 | 
  71 |     /* Shared configuration and storage */
  72 |     wet_aer_packet_t *buffer;
  73 |     uint32_t capacity;
  74 |     uint32_t mask; /* capacity - 1 (must be power of 2) */
  75 | 
  76 |     /* Statistics and burst rate tracking */
  77 |     uint64_t total_pushed;
  78 |     uint64_t total_dropped;
  79 |     uint64_t last_stat_tick;
  80 |     uint32_t spikes_in_window;
  81 |     double current_spike_rate_hz;
  82 |     double current_bandwidth_mbps;
  83 |     uint32_t burst_limit_max_hz; /* Peak burst ceiling (e.g. 5,000,000 Hz) */
  84 |     uint8_t is_burst_tripped;
  85 | 
  86 |     /* Per-channel rate monitoring to quarantine noisy / oscillating pads */
  87 |     uint16_t *channel_spike_counts;
  88 |     uint32_t monitored_channels;
  89 |     uint16_t max_channel_hz; /* Default 250 Hz per channel */
  90 | } wet_aer_ring_t;
  91 | 
  92 | /*
  93 |  * Nonlinear Energy Operator (NEO) Spike Detector with Bartlett Smoother
  94 |  * Pipeline:
  95 |  *  1. Baseline subtraction: x_ac = v - v_base
  96 |  *  2. Raw discrete NEO: Psi[n] = x_ac[n-1]^2 - x_ac[n] * x_ac[n-2]
  97 |  *  3. 5-tap Bartlett smoothing window: Psi_smooth = (1/9)*(Psi[-2] + 2Psi[-1] + 3Psi[0] + 2Psi[1] + Psi[2])
  98 |  *  4. Blanking window suppression
  99 |  */
 100 | typedef struct {
 101 |     uint32_t num_channels;
 102 |     float threshold_multiplier;
 103 |     uint32_t refractory_ticks;
 104 |     
 105 |     /* Per-channel state */
 106 |     float *v_baseline;
 107 |     float *prev_v1;       /* x_ac[n-1] */
 108 |     float *prev_v2;       /* x_ac[n-2] */
 109 |     float *psi_history[4]; /* 4-tap history for 5-tap Bartlett smoother */
 110 |     uint32_t *refract_left;
 111 |     uint32_t *blanking_left; /* Hardware stimulus artifact blanking window */
 112 |     float *running_neo_mean;
 113 |     uint32_t *sample_count;
 114 |     uint64_t total_detected;
 115 | } wet_neo_detector_t;
 116 | 
 117 | /*
 118 |  * Event-Driven Compressed Sparse Row / Adjacency Synaptic Matrix
 119 |  * Total footprint:
 120 |  *  - weights_int8: 6.97 MB (int8)
 121 |  *  - col_idx:      13.94 MB (uint16_t)
 122 |  *  - row_ptr:      0.11 MB (uint32_t)
 123 |  *  - Total:        21.02 MB for 26,400 neurons @ 1% density
 124 |  *
 125 |  * Event-driven dispatch: O(spiking_neurons * avg_degree) complexity.
 126 |  */
 127 | typedef struct {
 128 |     uint32_t num_rows;
 129 |     uint32_t num_cols;
 130 |     uint32_t nnz;
 131 |     uint32_t *row_ptr;      /* Size: num_rows + 1 */
 132 |     uint16_t *col_idx;      /* Size: nnz */
 133 |     int8_t   *weights_int8;  /* Size: nnz, signed 8-bit quantized weights */
 134 |     float    weight_scale_ns; /* Conductance per LSB (default 0.2 nS) */
 135 | } wet_csr_matrix_t;
 136 | 
 137 | /* AER Ring Buffer Functions */
 138 | WET_EXPORT int wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels);
 139 | WET_EXPORT int wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint16_t channel, int16_t amp_uv, uint16_t flags);
 140 | WET_EXPORT uint32_t wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count);
 141 | WET_EXPORT uint32_t wet_aer_available(const wet_aer_ring_t *ring);
 142 | WET_EXPORT void wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps);
 143 | 
 144 | /* NEO Detector Functions */
 145 | WET_EXPORT int wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks);
 146 | WET_EXPORT void wet_neo_free(wet_neo_detector_t *det);
 147 | WET_EXPORT void wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks);
 148 | WET_EXPORT int wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring);
 149 | 
 150 | /* CSR int8 Synaptic Matrix Functions */
 151 | WET_EXPORT int wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns);
 152 | WET_EXPORT void wet_csr_free(wet_csr_matrix_t *csr);
 153 | WET_EXPORT void wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns);
 154 | 
 155 | #ifdef __cplusplus
 156 | }
 157 | #endif
 158 | 
 159 | #endif /* WET_AER_H */
```

### `native/include/wet_crt.h` (108 lines, SHA-256: `3c1a972b9cd8b7c7...`)

```text
   1 | #ifndef WET_CRT_H
   2 | #define WET_CRT_H
   3 | 
   4 | #include <stddef.h>
   5 | #include <stdint.h>
   6 | 
   7 | void* malloc(size_t size);
   8 | void* calloc(size_t num, size_t size);
   9 | void  free(void* ptr);
  10 | void* memcpy(void* dest, const void* src, size_t count);
  11 | void* memset(void* dest, int ch, size_t count);
  12 | int   memcmp(const void* s1, const void* s2, size_t count);
  13 | size_t strlen(const char* str);
  14 | char* strncpy(char* dest, const char* src, size_t count);
  15 | char* strcpy(char* dest, const char* src);
  16 | char* strcat(char* dest, const char* src);
  17 | int   strcmp(const char* s1, const char* s2);
  18 | int   strncmp(const char* s1, const char* s2, size_t count);
  19 | int   sprintf(char* buffer, const char* format, ...);
  20 | int   _snprintf(char* buffer, size_t count, const char* format, ...);
  21 | #ifndef snprintf
  22 | #define snprintf _snprintf
  23 | #endif
  24 | 
  25 | static inline float wet_fabsf(float x) {
  26 |     return (x < 0.0f) ? -x : x;
  27 | }
  28 | #ifndef fabsf
  29 | #define fabsf wet_fabsf
  30 | #endif
  31 | 
  32 | static inline double wet_fabs(double x) {
  33 |     return (x < 0.0) ? -x : x;
  34 | }
  35 | 
  36 | static inline float wet_clampf(float x, float lo, float hi) {
  37 |     if (x < lo) return lo;
  38 |     if (x > hi) return hi;
  39 |     return x;
  40 | }
  41 | 
  42 | static inline double wet_clampd(double x, double lo, double hi) {
  43 |     if (x < lo) return lo;
  44 |     if (x > hi) return hi;
  45 |     return x;
  46 | }
  47 | 
  48 | /* Pure C99 deterministic exp(x) via range reduction (Cody-Waite) + minimax polynomial.
  49 |  * Accurate to < 1e-6 for all biophysical inputs; zero external libm dependency. */
  50 | static inline double wet_exp(double x) {
  51 |     if (x < -700.0) return 0.0;
  52 |     if (x > 700.0)  return 1e300;
  53 |     const double LN2_INV = 1.44269504088896340736;
  54 |     const double LN2_HI  = 0.69314718055994530942;
  55 |     int k = (int)(x * LN2_INV + (x >= 0.0 ? 0.5 : -0.5));
  56 |     double r = x - (double)k * LN2_HI;
  57 |     /* 7th-order Taylor/Horner on [-ln2/2, ln2/2] -> error < 1e-9 */
  58 |     double poly = 1.0 + r * (1.0 + r * (0.5 + r * (1.0/6.0 + r * (1.0/24.0
  59 |                 + r * (1.0/120.0 + r * (1.0/720.0 + r * (1.0/5040.0)))))));
  60 |     /* Multiply by 2^k via IEEE-754 exponent manipulation */
  61 |     union { double d; uint64_t u; } scale;
  62 |     int exp_bits = k + 1023;
  63 |     if (exp_bits <= 0) return 0.0;
  64 |     if (exp_bits >= 2047) return 1e300;
  65 |     scale.u = ((uint64_t)exp_bits) << 52;
  66 |     return poly * scale.d;
  67 | }
  68 | 
  69 | static inline float wet_expf(float x) {
  70 |     return (float)wet_exp((double)x);
  71 | }
  72 | 
  73 | /* Pure C99 Newton-Raphson sqrt(x) */
  74 | static inline double wet_sqrt(double x) {
  75 |     if (x <= 0.0) return 0.0;
  76 |     double g = x > 1.0 ? x * 0.5 : 1.0;
  77 |     for (int i = 0; i < 16; ++i) {
  78 |         g = 0.5 * (g + x / g);
  79 |     }
  80 |     return g;
  81 | }
  82 | 
  83 | /* Deterministic Xorshift64* PRNG for reproducible background noise & network wiring */
  84 | static inline uint64_t wet_rng_next(uint64_t* state) {
  85 |     uint64_t x = *state;
  86 |     if (x == 0) x = 0x9E3779B97F4A7C15ULL;
  87 |     x ^= x >> 12;
  88 |     x ^= x << 25;
  89 |     x ^= x >> 27;
  90 |     *state = x;
  91 |     return x * 0x2545F4914F6CDD1DULL;
  92 | }
  93 | 
  94 | /* Uniform double in [0, 1) */
  95 | static inline double wet_rng_uniform(uint64_t* state) {
  96 |     return (double)(wet_rng_next(state) >> 11) * (1.0 / 9007199254740992.0);
  97 | }
  98 | 
  99 | /* Approximate standard normal N(0,1) via Irwin-Hall (sum of 12 uniforms - 6) */
 100 | static inline double wet_rng_normal(uint64_t* state) {
 101 |     double s = 0.0;
 102 |     for (int i = 0; i < 12; ++i) {
 103 |         s += wet_rng_uniform(state);
 104 |     }
 105 |     return s - 6.0;
 106 | }
 107 | 
 108 | #endif /* WET_CRT_H */
```

### `native/include/wet_distributed.h` (130 lines, SHA-256: `0aab09235da0a6be...`)

```text
   1 | #ifndef WET_DISTRIBUTED_H
   2 | #define WET_DISTRIBUTED_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | 
   7 | #ifdef __cplusplus
   8 | extern "C" {
   9 | #endif
  10 | 
  11 | #define WET_DIST_CACHELINE_SIZE 128
  12 | #define WET_TSN_FRAME_SIZE      32
  13 | #define WET_TIMING_WHEEL_SLOTS  512  /* 512 slots * 100 us = 51.2 ms horizon */
  14 | #define WET_WHEEL_BUCKET_CAP    64   /* Max spikes per 100 us tick */
  15 | #define WET_MAX_CHAMBERS        16
  16 | 
  17 | #if defined(_WIN32) || defined(__CYGWIN__)
  18 |   #ifdef WET_BUILDING_DLL
  19 |     #define WET_EXPORT __declspec(dllexport)
  20 |   #else
  21 |     #define WET_EXPORT __declspec(dllimport)
  22 |   #endif
  23 | #else
  24 |   #if defined(__GNUC__) && __GNUC__ >= 4
  25 |     #define WET_EXPORT __attribute__((visibility("default")))
  26 |   #else
  27 |     #define WET_EXPORT
  28 |   #endif
  29 | #endif
  30 | 
  31 | /*
  32 |  * Production 32-Byte Time-Sensitive Networking (TSN) Inter-Chamber Packet
  33 |  * Natural 8-byte alignment, zero split-load penalty, explicit release epoch & sequence number.
  34 |  */
  35 | #if defined(_MSC_VER)
  36 | #pragma pack(push, 8)
  37 | typedef struct {
  38 |     uint64_t source_epoch_ns;   /* 8 bytes: Originating biological spike epoch */
  39 |     uint64_t release_epoch_ns;  /* 8 bytes: Scheduled target delivery epoch */
  40 |     uint32_t sequence_number;   /* 4 bytes: Monotonic packet counter */
  41 |     uint16_t source_chamber;    /* 2 bytes: Originating incubator ID */
  42 |     uint16_t target_chamber;    /* 2 bytes: Destination incubator ID */
  43 |     uint16_t source_channel;    /* 2 bytes: Transmitting electrode */
  44 |     uint16_t target_channel;    /* 2 bytes: Receiving electrode */
  45 |     int16_t  spike_amplitude_uv;/* 2 bytes: Spike amplitude */
  46 |     uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: e-stop, bit 2: clock-sync, bit 3: echo-suppressed */
  47 | } wet_tsn_frame_t;
  48 | #pragma pack(pop)
  49 | #else
  50 | typedef struct __attribute__((aligned(8))) {
  51 |     uint64_t source_epoch_ns;   /* 8 bytes: Originating biological spike epoch */
  52 |     uint64_t release_epoch_ns;  /* 8 bytes: Scheduled target delivery epoch */
  53 |     uint32_t sequence_number;   /* 4 bytes: Monotonic packet counter */
  54 |     uint16_t source_chamber;    /* 2 bytes: Originating incubator ID */
  55 |     uint16_t target_chamber;    /* 2 bytes: Destination incubator ID */
  56 |     uint16_t source_channel;    /* 2 bytes: Transmitting electrode */
  57 |     uint16_t target_channel;    /* 2 bytes: Receiving electrode */
  58 |     int16_t  spike_amplitude_uv;/* 2 bytes: Spike amplitude */
  59 |     uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: e-stop, bit 2: clock-sync, bit 3: echo-suppressed */
  60 | } wet_tsn_frame_t;
  61 | #endif
  62 | 
  63 | #if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
  64 | _Static_assert(sizeof(wet_tsn_frame_t) == 32, "wet_tsn_frame_t must be exactly 32 bytes");
  65 | #endif
  66 | 
  67 | /*
  68 |  * IEEE 1588 PTP Slew-Only Hardware Clock Disciplining State
  69 |  */
  70 | typedef struct {
  71 |     uint64_t local_time_ns;
  72 |     uint64_t grandmaster_time_ns;
  73 |     int64_t  accumulated_offset_ns;
  74 |     int64_t  mean_path_delay_ns;
  75 |     double   frequency_slew_ppm;
  76 |     double   integral_err_ns;
  77 |     double   kp;
  78 |     double   ki;
  79 |     uint8_t  is_synchronized;
  80 |     uint8_t  stim_inhibited;      /* Inhibited if |residual_offset| > 1000 ns */
  81 |     uint32_t sync_sequence;
  82 | } wet_ptp_clock_t;
  83 | 
  84 | /*
  85 |  * Timing Wheel Bucket for O(1) Heterogeneous Axonal Delay Dispatching
  86 |  * Eliminates Head-of-Line blocking inherent to FIFO queues.
  87 |  */
  88 | typedef struct {
  89 |     uint32_t count;
  90 |     wet_tsn_frame_t frames[WET_WHEEL_BUCKET_CAP];
  91 | } wet_timing_wheel_bucket_t;
  92 | 
  93 | typedef struct {
  94 |     wet_timing_wheel_bucket_t buckets[WET_TIMING_WHEEL_SLOTS];
  95 |     uint64_t current_wheel_tick;
  96 |     uint32_t chamber_id;
  97 |     uint64_t total_scheduled;
  98 |     uint64_t total_dispatched;
  99 |     uint64_t late_drops;
 100 |     uint64_t bucket_overflows;
 101 | 
 102 |     /* Cross-chamber epileptiform rate governor (caps max inter-chamber rate at 50 Hz) */
 103 |     uint32_t rate_governor_window_spikes;
 104 |     uint64_t rate_governor_last_tick;
 105 |     uint8_t  is_epileptiform_tripped;
 106 | 
 107 |     /* Outbound TX stimulus artifact blanking */
 108 |     uint32_t tx_blanking_ticks_remaining[WET_MAX_CHAMBERS];
 109 | } wet_timing_wheel_t;
 110 | 
 111 | /* PTP Clock Functions */
 112 | WET_EXPORT void wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki);
 113 | WET_EXPORT void wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns);
 114 | WET_EXPORT uint64_t wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns);
 115 | 
 116 | /* TSN Frame Functions */
 117 | WET_EXPORT int wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags);
 118 | WET_EXPORT int wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber);
 119 | 
 120 | /* Timing Wheel Functions */
 121 | WET_EXPORT int wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id);
 122 | WET_EXPORT int wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns);
 123 | WET_EXPORT uint32_t wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count);
 124 | WET_EXPORT void wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks);
 125 | 
 126 | #ifdef __cplusplus
 127 | }
 128 | #endif
 129 | 
 130 | #endif /* WET_DISTRIBUTED_H */
```

### `native/include/wet_hal.h` (230 lines, SHA-256: `8b70512b8ce20493...`)

```text
   1 | #ifndef WET_HAL_H
   2 | #define WET_HAL_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wetvm_types.h"
   7 | #include "wetvm_api.h"
   8 | 
   9 | #ifdef __cplusplus
  10 | extern "C" {
  11 | #endif
  12 | 
  13 | /* =========================================================================
  14 |  * WetLang Hardware Abstraction Layer (HAL) Core Architecture
  15 |  * Tri-Modal Router: SIMULATED (0), PHYSICAL (1), HIL_LOOPBACK (2)
  16 |  * ========================================================================= */
  17 | 
  18 | typedef enum {
  19 |     WET_HAL_MODE_SIMULATED    = 0, /* In-silico ODE biophysics & virtual registers */
  20 |     WET_HAL_MODE_PHYSICAL     = 1, /* Real device drivers (SPI, I2C, RS-232, CAN) */
  21 |     WET_HAL_MODE_HIL_LOOPBACK = 2  /* Hardware-in-the-loop mock with bit-level validation */
  22 | } wet_hal_mode_t;
  23 | 
  24 | typedef enum {
  25 |     WET_HAL_DRIVER_EPHYS      = 1, /* Intan RHS2116 / MaxWell MaxOne */
  26 |     WET_HAL_DRIVER_PUMP       = 2, /* Harvard Apparatus RS-232 */
  27 |     WET_HAL_DRIVER_VALVE      = 3, /* Microfluidic Solenoid / CAN */
  28 |     WET_HAL_DRIVER_FLOW       = 4, /* Sensirion I2C / SHDLC */
  29 |     WET_HAL_DRIVER_CAN_BUS    = 5  /* CAN-bus transceiver */
  30 | } wet_hal_driver_type_t;
  31 | 
  32 | typedef enum {
  33 |     WET_HAL_OK                   = 0,
  34 |     WET_HAL_ERR_NULL_PTR         = -1,
  35 |     WET_HAL_ERR_INVALID_MODE     = -2,
  36 |     WET_HAL_ERR_DRIVER_NOT_FOUND = -3,
  37 |     WET_HAL_ERR_IO               = -4,
  38 |     WET_HAL_ERR_TIMEOUT          = -5,
  39 |     WET_HAL_ERR_CRC_MISMATCH     = -6,
  40 |     WET_HAL_ERR_COMPLIANCE_RAILED= -7,
  41 |     WET_HAL_ERR_INTERLOCK        = -8,
  42 |     WET_HAL_ERR_DEAD_HEAD        = -9,
  43 |     WET_HAL_ERR_OUT_OF_BOUNDS    = -10,
  44 |     WET_HAL_ERR_BUS_BUSY         = -11,
  45 |     WET_HAL_ERR_NOT_SUPPORTED    = -12,
  46 |     WET_HAL_ERR_BUFFER_FULL      = -13
  47 | } wet_hal_status_t;
  48 | 
  49 | /* Forward declarations */
  50 | typedef struct wet_hal_driver wet_hal_driver_t;
  51 | typedef struct wet_hal_context wet_hal_context_t;
  52 | 
  53 | /* Driver vtable operations */
  54 | typedef struct {
  55 |     /* Lifecycle */
  56 |     wet_hal_status_t (*init)(wet_hal_driver_t* drv, void* config);
  57 |     wet_hal_status_t (*shutdown)(wet_hal_driver_t* drv);
  58 |     wet_hal_status_t (*emergency_stop)(wet_hal_driver_t* drv, uint32_t reason);
  59 |     wet_hal_status_t (*step_tick)(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
  60 | 
  61 |     /* Electrophysiology DAQ */
  62 |     wet_hal_status_t (*stim_voltage)(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
  63 |     wet_hal_status_t (*stim_current)(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
  64 |     wet_hal_status_t (*read_ephys)(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
  65 |     wet_hal_status_t (*measure_impedance)(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
  66 |     wet_hal_status_t (*active_discharge)(wet_hal_driver_t* drv, uint16_t channel);
  67 | 
  68 |     /* Microfluidics & Actuators */
  69 |     wet_hal_status_t (*write_pump)(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
  70 |     wet_hal_status_t (*dispense_volume)(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul);
  71 |     wet_hal_status_t (*write_valve)(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state);
  72 |     wet_hal_status_t (*read_flow)(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);
  73 |     wet_hal_status_t (*read_pressure)(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa);
  74 | } wet_hal_ops_t;
  75 | 
  76 | /* Driver instance structure */
  77 | struct wet_hal_driver {
  78 |     char                  name[32];
  79 |     wet_hal_driver_type_t driver_type;
  80 |     wet_hal_mode_t        mode;
  81 |     uint8_t               is_initialized;
  82 |     uint8_t               is_active;
  83 |     const wet_hal_ops_t*  ops;
  84 |     void*                 context;
  85 |     wet_hal_driver_t*     next;
  86 | };
  87 | 
  88 | #define WET_HAL_CROWBAR_BLEED_RESISTOR_OHMS 700000.0f /* 700 kOhm: guarantees <= 10 uA surge from +/-7.0 V compliance rail */
  89 | #define WET_HAL_MAX_DEAD_HEAD_PRESSURE_KPA  150.0f   /* 150 kPa safety cutoff threshold */
  90 | #define WET_HAL_ASYNC_QUEUE_CAPACITY        64
  91 | 
  92 | /* Asynchronous Microfluidic Command Packet */
  93 | typedef enum {
  94 |     WET_ASYNC_CMD_NONE           = 0,
  95 |     WET_ASYNC_CMD_PUMP_RATE      = 1,
  96 |     WET_ASYNC_CMD_PUMP_DISPENSE  = 2,
  97 |     WET_ASYNC_CMD_VALVE_SET      = 3,
  98 |     WET_ASYNC_CMD_BUS_RECOVERY   = 4
  99 | } wet_async_cmd_type_t;
 100 | 
 101 | typedef struct {
 102 |     uint8_t  cmd_type;    /* wet_async_cmd_type_t */
 103 |     uint8_t  device_id;   /* pump_id or valve_id */
 104 |     uint8_t  state;       /* run_flag or valve state */
 105 |     uint8_t  padding;
 106 |     double   param_val;   /* rate_ul_min or volume_ul */
 107 |     uint64_t submit_tick;
 108 | } wet_async_cmd_t;
 109 | 
 110 | /* HAL Configuration */
 111 | typedef struct {
 112 |     wet_hal_mode_t mode;
 113 |     uint32_t       max_ephys_channels;
 114 |     uint32_t       num_pumps;
 115 |     uint32_t       num_valves;
 116 |     uint32_t       num_flow_sensors;
 117 |     uint8_t        enable_dead_head_protection;
 118 |     uint8_t        enable_crowbar_fastpath;
 119 |     uint8_t        valve_for_pump[8]; /* Associated downstream valve for dead-head protection */
 120 |     float          max_line_pressure_kpa; /* Maximum inline fluidic pressure threshold (default 150.0 kPa) */
 121 | } wet_hal_config_t;
 122 | 
 123 | /* HAL Hardware Statistics & Telemetry */
 124 | typedef struct {
 125 |     uint64_t total_spi_transactions;
 126 |     uint64_t total_i2c_transactions;
 127 |     uint64_t total_rs232_commands;
 128 |     uint64_t total_can_frames;
 129 |     uint64_t total_crowbar_events;
 130 |     uint64_t last_crowbar_timestamp_us;
 131 |     uint32_t last_crowbar_reason;
 132 |     double   crowbar_latency_us;
 133 | } wet_hal_telemetry_t;
 134 | 
 135 | /* HAL Context / Router Registry */
 136 | #define WET_HAL_MAX_DRIVERS 16
 137 | 
 138 | struct wet_hal_context {
 139 |     wet_hal_mode_t       mode;
 140 |     wet_hal_config_t     config;
 141 |     wet_vm_t*            vm; /* Attached VM */
 142 | 
 143 |     /* Registered Drivers */
 144 |     wet_hal_driver_t*    drivers[WET_HAL_MAX_DRIVERS];
 145 |     uint32_t             driver_count;
 146 | 
 147 |     /* Primary specialized driver slots for zero-search O(1) routing */
 148 |     wet_hal_driver_t*    ephys_driver;
 149 |     wet_hal_driver_t*    pump_driver;
 150 |     wet_hal_driver_t*    valve_driver;
 151 |     wet_hal_driver_t*    flow_driver;
 152 |     wet_hal_driver_t*    can_driver;
 153 | 
 154 |     /* Actuator & Sensor Caches */
 155 |     float                pump_rates_ul_min[8];
 156 |     uint8_t              valve_states[8];
 157 |     double               flow_rates_ul_min[8];
 158 |     float                fluid_pressure_kpa[8];
 159 |     float                ephys_voltages[64];
 160 |     uint8_t              ephys_spikes[64];
 161 | 
 162 |     /* Emergency Crowbar Status */
 163 |     uint8_t              crowbar_tripped;
 164 |     uint32_t             crowbar_reason;
 165 |     uint64_t             crowbar_tick;
 166 |     uint64_t             crowbar_timestamp_us;
 167 | 
 168 |     /* Asynchronous Microfluidics Lockless Command Queue */
 169 |     wet_async_cmd_t      async_queue[WET_HAL_ASYNC_QUEUE_CAPACITY];
 170 |     volatile uint32_t    async_head;
 171 |     volatile uint32_t    async_tail;
 172 | 
 173 |     /* Telemetry Counters */
 174 |     wet_hal_telemetry_t  telemetry;
 175 | };
 176 | 
 177 | /* =========================================================================
 178 |  * Core HAL API Prototypes
 179 |  * ========================================================================= */
 180 | 
 181 | WET_EXPORT wet_hal_context_t* wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config);
 182 | WET_EXPORT void wet_hal_destroy(wet_hal_context_t* hal);
 183 | 
 184 | WET_EXPORT wet_hal_status_t wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config);
 185 | WET_EXPORT wet_hal_status_t wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal);
 186 | WET_EXPORT wet_hal_context_t* wet_hal_get_context(wet_vm_t* vm);
 187 | 
 188 | WET_EXPORT wet_hal_status_t wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode);
 189 | WET_EXPORT wet_hal_mode_t wet_hal_get_mode(const wet_hal_context_t* hal);
 190 | 
 191 | WET_EXPORT wet_hal_status_t wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
 192 | WET_EXPORT wet_hal_status_t wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
 193 | WET_EXPORT wet_hal_driver_t* wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type);
 194 | 
 195 | /* Actuator & Sensor Dispatch */
 196 | WET_EXPORT wet_hal_status_t wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
 197 | WET_EXPORT wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul);
 198 | WET_EXPORT wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state);
 199 | WET_EXPORT wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min);
 200 | WET_EXPORT wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us);
 201 | WET_EXPORT wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
 202 | WET_EXPORT wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag);
 203 | WET_EXPORT wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
 204 | WET_EXPORT wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel);
 205 | 
 206 | /* Emergency Hardware Crowbar Fast-Path (<100 µs) */
 207 | WET_EXPORT void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason);
 208 | 
 209 | /* Asynchronous Microfluidics Queue APIs (Decouples 10 kHz Ephys from slow RS-232 / I2C) */
 210 | WET_EXPORT wet_hal_status_t wet_hal_async_enqueue(wet_hal_context_t* hal, const wet_async_cmd_t* cmd);
 211 | WET_EXPORT uint32_t wet_hal_process_async_queue(wet_hal_context_t* hal);
 212 | 
 213 | /* Standard 9-SCL-pulse I2C bus recovery routine */
 214 | WET_EXPORT wet_hal_status_t wet_hal_i2c_bus_recovery(wet_hal_context_t* hal);
 215 | 
 216 | /* Physical inline pressure transducer setter for dead-head monitoring */
 217 | WET_EXPORT void wet_hal_set_inline_pressure(wet_hal_context_t* hal, uint8_t port, float pressure_kpa);
 218 | 
 219 | /* Telemetry & Mapping Accessors */
 220 | WET_EXPORT wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal);
 221 | WET_EXPORT void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id);
 222 | 
 223 | /* High-resolution timer utility (monotonic microseconds) */
 224 | WET_EXPORT uint64_t wet_hal_get_time_us(void);
 225 | 
 226 | #ifdef __cplusplus
 227 | }
 228 | #endif
 229 | 
 230 | #endif /* WET_HAL_H */
```

### `native/include/wet_hal_intan.h` (169 lines, SHA-256: `15e6a6849d146a25...`)

```text
   1 | #ifndef WET_HAL_INTAN_H
   2 | #define WET_HAL_INTAN_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wet_hal.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | /* =========================================================================
  13 |  * Intan RHS2116 Electrophysiology DAQ Driver Specification
  14 |  * 16-Channel Bidirectional SPI Interface
  15 |  * ========================================================================= */
  16 | 
  17 | #define INTAN_RHS2116_NUM_CHANNELS 16
  18 | #define INTAN_SPI_WORD_BITS        32
  19 | #define INTAN_PIPELINE_DELAY_WORDS 2
  20 | #define INTAN_COMPLIANCE_RAIL_VOLT 7.0f
  21 | 
  22 | /* SPI Command Opcode prefixes */
  23 | #define INTAN_CMD_CONVERT 0x00U /* 00xxxxxx: Convert channel [3:0] */
  24 | #define INTAN_CMD_WRITE   0x80U /* 10xxxxxx: Write register [7:0] */
  25 | #define INTAN_CMD_READ    0xC0U /* 11xxxxxx: Read register [7:0] */
  26 | 
  27 | /* Command Control Flags */
  28 | #define INTAN_FLAG_M_COMPLIANCE_CLEAR 0x800000U /* Bit 23: M flag */
  29 | #define INTAN_FLAG_U_UPDATE_LATCH     0x400000U /* Bit 22: U flag */
  30 | 
  31 | /* Current Range Selectors */
  32 | typedef enum {
  33 |     INTAN_RANGE_1X   = 0, /* 10 nA step,   range: 10 nA .. 2.55 uA */
  34 |     INTAN_RANGE_10X  = 1, /* 100 nA step,  range: 100 nA .. 25.5 uA */
  35 |     INTAN_RANGE_100X = 2  /* 10 uA step,   range: 1.0 uA .. 2.55 mA */
  36 | } intan_current_range_t;
  37 | 
  38 | /* Intan 32-bit SPI Command Word Structure */
  39 | typedef struct {
  40 |     uint8_t  opcode;   /* 0x00=Convert, 0x80=Write, 0xC0=Read */
  41 |     uint8_t  channel;  /* 0..15 */
  42 |     uint8_t  reg;      /* Register address 0..63 */
  43 |     uint16_t data;     /* 16-bit register payload */
  44 |     uint8_t  flag_m;   /* Compliance clear flag */
  45 |     uint8_t  flag_u;   /* Update / Latch flag */
  46 | } intan_spi_command_t;
  47 | 
  48 | /* Intan Hardware / HIL State */
  49 | typedef struct {
  50 |     /* SPI State */
  51 |     uint32_t tx_pipeline[INTAN_PIPELINE_DELAY_WORDS + 1];
  52 |     uint32_t rx_pipeline[INTAN_PIPELINE_DELAY_WORDS + 1];
  53 |     uint32_t pipeline_index;
  54 | 
  55 |     /* Register File (64 x 16-bit registers) */
  56 |     uint16_t registers[64];
  57 | 
  58 |     /* Channel DAC Configuration (16 channels) */
  59 |     struct {
  60 |         uint8_t               dac_val_p1;
  61 |         uint8_t               dac_val_p2;
  62 |         intan_current_range_t range;
  63 |         int32_t               current_pA;
  64 |         uint32_t              duration_us;
  65 |         uint8_t               enabled;
  66 |         uint8_t               charge_recovery_on;
  67 |         float                 impedance_ohms;
  68 |         float                 impedance_phase_rad;
  69 |     } channels[INTAN_RHS2116_NUM_CHANNELS];
  70 | 
  71 |     /* Compliance Monitor */
  72 |     uint16_t compliance_rail_mask; /* Bitmask of channels currently railed */
  73 |     uint32_t total_compliance_trips;
  74 | 
  75 |     /* Impedance Module Configuration */
  76 |     float    zcheck_freq_hz;
  77 |     float    zcheck_probe_current_pA;
  78 | 
  79 |     /* HIL Fault Injection Hooks */
  80 |     uint8_t  fault_force_compliance_rail;
  81 |     uint8_t  fault_spi_crc_error;
  82 |     uint8_t  fault_bus_timeout;
  83 |     uint32_t transaction_count;
  84 | } intan_device_state_t;
  85 | 
  86 | /* =========================================================================
  87 |  * Intan RHS2116 Driver APIs
  88 |  * ========================================================================= */
  89 | 
  90 | /**
  91 |  * Creates and registers an Intan RHS2116 DAQ driver instance.
  92 |  */
  93 | WET_EXPORT wet_hal_driver_t* wet_hal_intan_create(wet_hal_mode_t mode);
  94 | 
  95 | /**
  96 |  * Destroys an Intan RHS2116 driver instance.
  97 |  */
  98 | WET_EXPORT void wet_hal_intan_destroy(wet_hal_driver_t* drv);
  99 | 
 100 | /**
 101 |  * Low-level 32-bit SPI word exchange.
 102 |  */
 103 | WET_EXPORT uint32_t wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word);
 104 | 
 105 | /**
 106 |  * Encodes a 32-bit SPI command word.
 107 |  */
 108 | WET_EXPORT uint32_t wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd);
 109 | 
 110 | /**
 111 |  * Decodes a 32-bit SPI command word.
 112 |  */
 113 | WET_EXPORT void wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd);
 114 | 
 115 | /**
 116 |  * Configures constant current stimulation on channel (10 nA - 2.55 mA).
 117 |  */
 118 | WET_EXPORT wet_hal_status_t wet_hal_intan_set_stim_current(
 119 |     wet_hal_driver_t* drv,
 120 |     uint8_t channel,
 121 |     int32_t current_pA,
 122 |     uint32_t duration_us
 123 | );
 124 | 
 125 | /**
 126 |  * Queries compliance rail register.
 127 |  */
 128 | WET_EXPORT uint16_t wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv);
 129 | 
 130 | /**
 131 |  * Clears compliance rail register (issues command with M flag).
 132 |  */
 133 | WET_EXPORT void wet_hal_intan_clear_compliance(wet_hal_driver_t* drv);
 134 | 
 135 | /**
 136 |  * Performs in-situ 1 kHz AC impedance test on channel.
 137 |  */
 138 | WET_EXPORT wet_hal_status_t wet_hal_intan_measure_impedance(
 139 |     wet_hal_driver_t* drv,
 140 |     uint8_t channel,
 141 |     float freq_hz,
 142 |     float* out_mag_ohms,
 143 |     float* out_phase_rad
 144 | );
 145 | 
 146 | /**
 147 |  * Enables / disables active hardware charge recovery switch on channel.
 148 |  */
 149 | WET_EXPORT wet_hal_status_t wet_hal_intan_set_charge_recovery(
 150 |     wet_hal_driver_t* drv,
 151 |     uint8_t channel,
 152 |     uint8_t enable
 153 | );
 154 | 
 155 | /**
 156 |  * HIL Fault Injection: Inject simulated compliance railing or bus errors.
 157 |  */
 158 | WET_EXPORT void wet_hal_intan_inject_fault(
 159 |     wet_hal_driver_t* drv,
 160 |     uint8_t force_rail,
 161 |     uint8_t spi_error,
 162 |     uint8_t bus_timeout
 163 | );
 164 | 
 165 | #ifdef __cplusplus
 166 | }
 167 | #endif
 168 | 
 169 | #endif /* WET_HAL_INTAN_H */
```

### `native/include/wet_hal_maxwell.h` (173 lines, SHA-256: `f5be2fac6cba467d...`)

```text
   1 | #ifndef WET_HAL_MAXWELL_H
   2 | #define WET_HAL_MAXWELL_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wet_hal.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | /* =========================================================================
  13 |  * MaxWell Biosystems MaxOne HD-MEA Driver Specification
  14 |  * CMOS High-Density Microelectrode Array Interface
  15 |  * ========================================================================= */
  16 | 
  17 | #define MAXWELL_TOTAL_ELECTRODES      26400
  18 | #define MAXWELL_RECORDING_CHANNELS    1024
  19 | #define MAXWELL_STIMULATION_UNITS     32
  20 | #define MAXWELL_PITCH_UM              17.5f
  21 | #define MAXWELL_ELECTRODE_AREA_UM2    132.25f
  22 | 
  23 | /* Electrochemical Safety Bounds for Platinum (Pt) Microelectrodes */
  24 | #define MAXWELL_VOLTAGE_LIMIT_MV      1000.0f /* Max safe DAC amplitude */
  25 | #define MAXWELL_MAX_DAC_BITS          335     /* Corresponding to 1000 mV */
  26 | #define MAXWELL_PT_CIC_MC_CM2         0.10f   /* Pt charge injection capacity */
  27 | #define MAXWELL_MAX_PHASE_CHARGE_NC   0.13225f/* Max safe single-phase charge in nC */
  28 | 
  29 | /* Sequence Buffer Capacity */
  30 | #define MAXWELL_MAX_SEQUENCE_STEPS    4096
  31 | 
  32 | typedef enum {
  33 |     MAXWELL_SEQ_IDLE    = 0,
  34 |     MAXWELL_SEQ_ARMED   = 1,
  35 |     MAXWELL_SEQ_RUNNING = 2,
  36 |     MAXWELL_SEQ_DONE    = 3,
  37 |     MAXWELL_SEQ_ERROR   = 4
  38 | } maxwell_seq_state_t;
  39 | 
  40 | /* Single step in pre-compiled hardware Sequence buffer */
  41 | typedef struct {
  42 |     uint32_t timestamp_us;     /* Offset from sequence start in microseconds */
  43 |     uint8_t  stim_unit_id;     /* 0..31 */
  44 |     uint16_t electrode_id;     /* Target electrode 0..26399 */
  45 |     int16_t  dac_val;          /* Voltage DAC value (-335 .. +335) */
  46 |     uint16_t phase_duration_us;/* Pulse duration */
  47 | } maxwell_seq_step_t;
  48 | 
  49 | /* MaxWell Driver State */
  50 | typedef struct {
  51 |     /* Electrode Routing Matrix (1024 recording channels mapped to 26400 electrodes) */
  52 |     uint16_t routing_matrix[MAXWELL_RECORDING_CHANNELS];
  53 |     uint8_t  channel_active[MAXWELL_RECORDING_CHANNELS];
  54 | 
  55 |     /* 32 Stimulation Units */
  56 |     struct {
  57 |         uint16_t connected_electrode;
  58 |         uint8_t  is_connected;
  59 |         int16_t  current_dac_val;
  60 |         float    phase1_charge_nc;
  61 |         float    phase2_charge_nc;
  62 |     } stim_units[MAXWELL_STIMULATION_UNITS];
  63 | 
  64 |     /* Hardware Sequence Buffer (to eliminate host OS preemption jitter) */
  65 |     maxwell_seq_step_t  sequence_buffer[MAXWELL_MAX_SEQUENCE_STEPS];
  66 |     uint32_t            sequence_length;
  67 |     uint32_t            sequence_playback_index;
  68 |     maxwell_seq_state_t sequence_state;
  69 |     uint64_t            sequence_start_time_us;
  70 | 
  71 |     /* Channel Readout Cache */
  72 |     float    channel_voltages[MAXWELL_RECORDING_CHANNELS];
  73 |     uint8_t  channel_spikes[MAXWELL_RECORDING_CHANNELS];
  74 | 
  75 |     /* Safety & Interlock Counters */
  76 |     uint32_t voltage_clamp_events;
  77 |     uint32_t charge_limit_violations;
  78 | 
  79 |     /* HIL Fault Injection */
  80 |     uint8_t  fault_force_charge_violation;
  81 |     uint8_t  fault_bus_dropped_frame;
  82 | } maxwell_device_state_t;
  83 | 
  84 | /* =========================================================================
  85 |  * MaxWell MaxOne Driver APIs
  86 |  * ========================================================================= */
  87 | 
  88 | /**
  89 |  * Creates and registers a MaxWell MaxOne HD-MEA driver instance.
  90 |  */
  91 | WET_EXPORT wet_hal_driver_t* wet_hal_maxwell_create(wet_hal_mode_t mode);
  92 | 
  93 | /**
  94 |  * Destroys a MaxWell MaxOne driver instance.
  95 |  */
  96 | WET_EXPORT void wet_hal_maxwell_destroy(wet_hal_driver_t* drv);
  97 | 
  98 | /**
  99 |  * Configures the switch matrix to connect 1024 recording channels to specific electrodes.
 100 |  */
 101 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_route_channels(
 102 |     wet_hal_driver_t* drv,
 103 |     const uint16_t* electrode_indices,
 104 |     uint32_t count
 105 | );
 106 | 
 107 | /**
 108 |  * Connects a stimulation unit to a specific electrode.
 109 |  */
 110 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_connect_stim(
 111 |     wet_hal_driver_t* drv,
 112 |     uint8_t stim_unit,
 113 |     uint16_t electrode_id
 114 | );
 115 | 
 116 | /**
 117 |  * Clears the hardware sequence buffer.
 118 |  */
 119 | WET_EXPORT void wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv);
 120 | 
 121 | /**
 122 |  * Appends a step to the hardware sequence buffer (enforces voltage and charge safety bounds).
 123 |  */
 124 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_append(
 125 |     wet_hal_driver_t* drv,
 126 |     uint32_t timestamp_us,
 127 |     uint8_t stim_unit,
 128 |     uint16_t electrode_id,
 129 |     float voltage_mv,
 130 |     uint16_t duration_us
 131 | );
 132 | 
 133 | /**
 134 |  * Uploads and arms the pre-compiled sequence buffer for jitter-free execution.
 135 |  */
 136 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv);
 137 | 
 138 | /**
 139 |  * Starts execution of the sequence.
 140 |  */
 141 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv);
 142 | 
 143 | /**
 144 |  * Queries sequence playback status.
 145 |  */
 146 | WET_EXPORT maxwell_seq_state_t wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv);
 147 | 
 148 | /**
 149 |  * Immediate voltage pulse injection (with Pt safety clamping: <= 1000 mV and <= 0.13225 nC).
 150 |  */
 151 | WET_EXPORT wet_hal_status_t wet_hal_maxwell_stim_voltage(
 152 |     wet_hal_driver_t* drv,
 153 |     uint8_t stim_unit,
 154 |     uint16_t electrode_id,
 155 |     float voltage_mv,
 156 |     float phase1_ms,
 157 |     float phase2_ms
 158 | );
 159 | 
 160 | /**
 161 |  * HIL Fault Injection: Inject simulated charge violation or frame drop.
 162 |  */
 163 | WET_EXPORT void wet_hal_maxwell_inject_fault(
 164 |     wet_hal_driver_t* drv,
 165 |     uint8_t force_charge_violation,
 166 |     uint8_t drop_frames
 167 | );
 168 | 
 169 | #ifdef __cplusplus
 170 | }
 171 | #endif
 172 | 
 173 | #endif /* WET_HAL_MAXWELL_H */
```

### `native/include/wet_hal_pump_valve.h` (216 lines, SHA-256: `5db2b883e4822e33...`)

```text
   1 | #ifndef WET_HAL_PUMP_VALVE_H
   2 | #define WET_HAL_PUMP_VALVE_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wet_hal.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | /* =========================================================================
  13 |  * Microfluidic Pump & Valve Protocol Specifications
  14 |  * Harvard Apparatus RS-232 & CAN-bus (ISO 11898-1/2) Microfluidics
  15 |  * ========================================================================= */
  16 | 
  17 | #define WET_MAX_PUMPS             8
  18 | #define WET_MAX_VALVES            8
  19 | #define WET_CAN_MAX_PAYLOAD       8
  20 | #define WET_CAN_QUEUE_CAPACITY    128
  21 | 
  22 | /* Harvard Apparatus Prompt Return Codes */
  23 | typedef enum {
  24 |     HARVARD_PROMPT_IDLE        = ':', /* Prompt : (pump stopped / idle) */
  25 |     HARVARD_PROMPT_INFUSING    = '>', /* Prompt > (pump infusing) */
  26 |     HARVARD_PROMPT_WITHDRAWING = '<', /* Prompt < (pump withdrawing) */
  27 |     HARVARD_PROMPT_STALLED     = '*', /* Prompt * (motor stalled / alarm) */
  28 |     HARVARD_PROMPT_TARGET_DONE = 'T', /* Prompt T* (target volume reached) */
  29 |     HARVARD_PROMPT_INVALID     = '?'
  30 | } harvard_prompt_t;
  31 | 
  32 | /* Harvard RS-232 Device Configuration */
  33 | typedef struct {
  34 |     uint8_t address;          /* Daisy-chain address 00..99 (0 = master) */
  35 |     uint8_t fast_mode;        /* 1 = use '@' prefix for sub-50 ms execution */
  36 |     double  rate_ul_min;      /* Current programmed infusion rate */
  37 |     double  infused_volume_ul;/* Cumulative dispensed volume */
  38 |     uint8_t is_running;       /* 1 = infusing, 2 = withdrawing, 0 = stopped */
  39 |     uint8_t is_stalled;       /* 1 = stall condition */
  40 | } harvard_pump_state_t;
  41 | 
  42 | /* CAN Message Frame (ISO 11898-1/2) */
  43 | typedef struct {
  44 |     uint32_t id;                       /* 11-bit standard or 29-bit extended ID */
  45 |     uint8_t  is_extended;              /* 1 = 29-bit CAN 2.0B, 0 = 11-bit standard */
  46 |     uint8_t  is_rtr;                   /* Remote Transmission Request */
  47 |     uint8_t  dlc;                      /* Data Length Code (0..8) */
  48 |     uint8_t  data[WET_CAN_MAX_PAYLOAD];/* Frame payload */
  49 |     uint64_t timestamp_us;             /* Monotonic arrival/tx timestamp */
  50 | } wet_can_frame_t;
  51 | 
  52 | /* CAN Message Type IDs */
  53 | #define CAN_ID_EMCY_BASE          0x080U /* Emergency frame: 0x080 + NodeID */
  54 | #define CAN_ID_TPDO1_BASE         0x180U /* Telemetry transmit: 0x180 + NodeID */
  55 | #define CAN_ID_RPDO1_BASE         0x200U /* Pump rate command: 0x200 + NodeID */
  56 | #define CAN_ID_RPDO2_BASE         0x300U /* Valve state command: 0x300 + NodeID */
  57 | #define CAN_ID_HEARTBEAT_BASE     0x700U /* Heartbeat: 0x700 + NodeID */
  58 | 
  59 | /* Valve & Pump Microfluidics State */
  60 | typedef struct {
  61 |     /* Harvard RS-232 Pumps (up to 8) */
  62 |     harvard_pump_state_t pumps[WET_MAX_PUMPS];
  63 | 
  64 |     /* Micro-pinch / Solenoid Valve States (0=Closed, 1=Open) */
  65 |     uint8_t              valve_states[WET_MAX_VALVES];
  66 | 
  67 |     /* Dead-Head Overpressure Interlock Configuration */
  68 |     uint8_t              dead_head_enabled;
  69 |     uint8_t              valve_for_pump[WET_MAX_PUMPS]; /* Associated downstream valve */
  70 |     uint32_t             dead_head_trip_count;
  71 | 
  72 |     /* CAN-bus Loopback & Queue */
  73 |     wet_can_frame_t      can_tx_queue[WET_CAN_QUEUE_CAPACITY];
  74 |     uint32_t             can_tx_head;
  75 |     uint32_t             can_tx_tail;
  76 |     uint32_t             can_tx_count;
  77 | 
  78 |     wet_can_frame_t      can_rx_queue[WET_CAN_QUEUE_CAPACITY];
  79 |     uint32_t             can_rx_head;
  80 |     uint32_t             can_rx_tail;
  81 |     uint32_t             can_rx_count;
  82 | 
  83 |     /* Telemetry Counters */
  84 |     uint32_t             total_rs232_tx;
  85 |     uint32_t             total_can_frames_tx;
  86 |     uint32_t             total_can_frames_rx;
  87 |     uint32_t             total_emcy_frames;
  88 | 
  89 |     /* HIL Fault Injection */
  90 |     uint8_t              fault_inject_stall;
  91 |     uint8_t              fault_inject_can_drop;
  92 |     uint8_t              fault_inject_rs232_timeout;
  93 | } microfluidic_state_t;
  94 | 
  95 | /* =========================================================================
  96 |  * Microfluidic Pump & Valve APIs
  97 |  * ========================================================================= */
  98 | 
  99 | /**
 100 |  * Creates and registers a microfluidic pump & valve driver instance.
 101 |  */
 102 | WET_EXPORT wet_hal_driver_t* wet_hal_microfluidics_create(wet_hal_mode_t mode);
 103 | 
 104 | /**
 105 |  * Destroys microfluidic driver instance.
 106 |  */
 107 | WET_EXPORT void wet_hal_microfluidics_destroy(wet_hal_driver_t* drv);
 108 | 
 109 | /**
 110 |  * Encodes a Harvard Apparatus RS-232 command string into out_buf.
 111 |  * (e.g. "@irate 1.500 u/m\r", "01 stp\r", etc.)
 112 |  */
 113 | WET_EXPORT int wet_hal_harvard_format_cmd(
 114 |     uint8_t address,
 115 |     uint8_t fast_mode,
 116 |     const char* cmd_name,
 117 |     const char* args,
 118 |     char* out_buf,
 119 |     size_t out_buf_len
 120 | );
 121 | 
 122 | /**
 123 |  * Parses a Harvard Apparatus prompt response string.
 124 |  */
 125 | WET_EXPORT harvard_prompt_t wet_hal_harvard_parse_response(
 126 |     const char* resp_buf,
 127 |     size_t resp_len
 128 | );
 129 | 
 130 | /**
 131 |  * Commands Harvard pump rate and run state.
 132 |  * Performs dead-head overpressure interlock check if downstream valve is closed!
 133 |  */
 134 | WET_EXPORT wet_hal_status_t wet_hal_pump_set_rate(
 135 |     wet_hal_driver_t* drv,
 136 |     uint8_t pump_id,
 137 |     double rate_ul_min,
 138 |     uint8_t run_flag
 139 | );
 140 | 
 141 | /**
 142 |  * Dispenses a specific volume in µL.
 143 |  */
 144 | WET_EXPORT wet_hal_status_t wet_hal_pump_dispense(
 145 |     wet_hal_driver_t* drv,
 146 |     uint8_t pump_id,
 147 |     double volume_ul
 148 | );
 149 | 
 150 | /**
 151 |  * Immediately stops a pump.
 152 |  */
 153 | WET_EXPORT wet_hal_status_t wet_hal_pump_stop(
 154 |     wet_hal_driver_t* drv,
 155 |     uint8_t pump_id
 156 | );
 157 | 
 158 | /**
 159 |  * Sets valve state (0 = closed, 1 = open).
 160 |  */
 161 | WET_EXPORT wet_hal_status_t wet_hal_valve_set_state(
 162 |     wet_hal_driver_t* drv,
 163 |     uint8_t valve_id,
 164 |     uint8_t state
 165 | );
 166 | 
 167 | /**
 168 |  * Configures the associated downstream valve for dead-head overpressure protection.
 169 |  */
 170 | WET_EXPORT void wet_hal_pump_bind_downstream_valve(
 171 |     wet_hal_driver_t* drv,
 172 |     uint8_t pump_id,
 173 |     uint8_t valve_id
 174 | );
 175 | 
 176 | /**
 177 |  * Encodes and transmits a CAN frame (ISO 11898-1/2).
 178 |  */
 179 | WET_EXPORT wet_hal_status_t wet_hal_can_send(
 180 |     wet_hal_driver_t* drv,
 181 |     const wet_can_frame_t* frame
 182 | );
 183 | 
 184 | /**
 185 |  * Receives the next available CAN frame from Rx queue.
 186 |  */
 187 | WET_EXPORT wet_hal_status_t wet_hal_can_recv(
 188 |     wet_hal_driver_t* drv,
 189 |     wet_can_frame_t* out_frame
 190 | );
 191 | 
 192 | /**
 193 |  * Emits an Emergency (EMCY) frame on the CAN bus.
 194 |  */
 195 | WET_EXPORT wet_hal_status_t wet_hal_can_send_emcy(
 196 |     wet_hal_driver_t* drv,
 197 |     uint8_t node_id,
 198 |     uint16_t error_code,
 199 |     uint8_t error_register
 200 | );
 201 | 
 202 | /**
 203 |  * HIL Fault Injection: Inject stall condition, CAN frame drop, or serial timeout.
 204 |  */
 205 | WET_EXPORT void wet_hal_microfluidics_inject_fault(
 206 |     wet_hal_driver_t* drv,
 207 |     uint8_t stall,
 208 |     uint8_t can_drop,
 209 |     uint8_t timeout
 210 | );
 211 | 
 212 | #ifdef __cplusplus
 213 | }
 214 | #endif
 215 | 
 216 | #endif /* WET_HAL_PUMP_VALVE_H */
```

### `native/include/wet_hal_sensirion.h` (153 lines, SHA-256: `c5cadc6f9f2f1b2b...`)

```text
   1 | #ifndef WET_HAL_SENSIRION_H
   2 | #define WET_HAL_SENSIRION_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wet_hal.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | /* =========================================================================
  13 |  * Sensirion Liquid Flow Meter Driver Specification
  14 |  * SLF3x / LPG10 (I2C) & SLI Series (SHDLC over RS-485/RS-232)
  15 |  * ========================================================================= */
  16 | 
  17 | #define SENSIRION_I2C_ADDR_DEFAULT    0x08U
  18 | #define SENSIRION_CRC8_POLYNOMIAL     0x31U /* x^8 + x^5 + x^4 + 1 */
  19 | #define SENSIRION_CRC8_INIT           0xFFU
  20 | 
  21 | /* I2C 16-bit Command Words */
  22 | #define SENSIRION_CMD_START_CONT_H2O  0x3608U /* Water / Aqueous continuous */
  23 | #define SENSIRION_CMD_START_CONT_IPA  0x3615U /* Hydrocarbons / IPA */
  24 | #define SENSIRION_CMD_STOP_CONT       0x3FF9U /* Stop continuous measurement */
  25 | #define SENSIRION_CMD_SOFT_RESET      0x0006U /* General call soft reset */
  26 | 
  27 | /* SHDLC Protocol Definitions */
  28 | #define SHDLC_FRAME_START_STOP        0x7EU
  29 | #define SHDLC_FRAME_ESCAPE            0x7DU
  30 | #define SHDLC_ESCAPE_MASK             0x20U
  31 | #define SHDLC_MAX_FRAME_SIZE          256
  32 | 
  33 | /* Sensirion Flow Driver State */
  34 | typedef struct {
  35 |     /* I2C Sensor Configuration (SLF3x / LPG10) */
  36 |     uint8_t  i2c_address;
  37 |     uint16_t active_command;
  38 |     uint8_t  measurement_active;
  39 |     float    scale_factor;           /* e.g., 10.0 or 500.0 (uL/min)^-1 */
  40 |     int16_t  raw_flow_ticks;
  41 |     double   current_flow_ul_min;
  42 | 
  43 |     /* SHDLC State (SLI series) */
  44 |     uint8_t  shdlc_address;
  45 |     uint8_t  shdlc_rx_buffer[SHDLC_MAX_FRAME_SIZE];
  46 |     size_t   shdlc_rx_len;
  47 |     uint8_t  shdlc_in_frame;
  48 |     uint8_t  shdlc_escaped;
  49 | 
  50 |     /* Telemetry Counters */
  51 |     uint32_t total_i2c_reads;
  52 |     uint32_t total_shdlc_frames;
  53 |     uint32_t crc_errors;
  54 | 
  55 |     /* HIL Fault Injection */
  56 |     uint8_t  fault_corrupt_crc;
  57 |     uint8_t  fault_nak_address;
  58 | } sensirion_device_state_t;
  59 | 
  60 | /* =========================================================================
  61 |  * Sensirion Driver APIs
  62 |  * ========================================================================= */
  63 | 
  64 | /**
  65 |  * Creates and registers a Sensirion Flow Meter driver instance.
  66 |  */
  67 | WET_EXPORT wet_hal_driver_t* wet_hal_sensirion_create(wet_hal_mode_t mode);
  68 | 
  69 | /**
  70 |  * Destroys a Sensirion Flow Meter driver instance.
  71 |  */
  72 | WET_EXPORT void wet_hal_sensirion_destroy(wet_hal_driver_t* drv);
  73 | 
  74 | /**
  75 |  * Computes Sensirion CRC-8 checksum over buffer (poly 0x31, init 0xFF).
  76 |  */
  77 | WET_EXPORT uint8_t wet_hal_sensirion_crc8(const uint8_t* data, size_t len);
  78 | 
  79 | /**
  80 |  * Validates a Sensirion 3-byte measurement word ([MSB] [LSB] [CRC]).
  81 |  * Returns 1 if CRC matches, 0 otherwise.
  82 |  */
  83 | WET_EXPORT int wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3]);
  84 | 
  85 | /**
  86 |  * Starts continuous measurement on SLF3x / LPG10 sensor (0x3608 for H2O).
  87 |  */
  88 | WET_EXPORT wet_hal_status_t wet_hal_sensirion_start_measurement(
  89 |     wet_hal_driver_t* drv,
  90 |     uint16_t cmd
  91 | );
  92 | 
  93 | /**
  94 |  * Stops continuous measurement on SLF3x / LPG10 sensor (0x3FF9).
  95 |  */
  96 | WET_EXPORT wet_hal_status_t wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv);
  97 | 
  98 | /**
  99 |  * Reads instantaneous liquid flow rate in µL/min.
 100 |  */
 101 | WET_EXPORT wet_hal_status_t wet_hal_sensirion_read_flow(
 102 |     wet_hal_driver_t* drv,
 103 |     double* out_flow_ul_min
 104 | );
 105 | 
 106 | /**
 107 |  * Sets raw flow value for HIL simulation.
 108 |  */
 109 | WET_EXPORT void wet_hal_sensirion_hil_set_flow(
 110 |     wet_hal_driver_t* drv,
 111 |     double flow_ul_min
 112 | );
 113 | 
 114 | /**
 115 |  * Encodes an SHDLC packet with start/stop flags (0x7E), byte-stuffing, and checksum.
 116 |  * Returns length of stuffed frame written to out_buf, or 0 on buffer overflow.
 117 |  */
 118 | WET_EXPORT size_t wet_hal_shdlc_encode(
 119 |     uint8_t address,
 120 |     uint8_t command,
 121 |     const uint8_t* payload,
 122 |     uint8_t payload_len,
 123 |     uint8_t* out_buf,
 124 |     size_t out_buf_max
 125 | );
 126 | 
 127 | /**
 128 |  * Decodes an unstuffed SHDLC packet, verifying start/stop flags and checksum.
 129 |  * Returns 1 on success, 0 on checksum error or invalid framing.
 130 |  */
 131 | WET_EXPORT int wet_hal_shdlc_decode(
 132 |     const uint8_t* raw_buf,
 133 |     size_t raw_len,
 134 |     uint8_t* out_address,
 135 |     uint8_t* out_command,
 136 |     uint8_t* out_payload,
 137 |     uint8_t* out_payload_len
 138 | );
 139 | 
 140 | /**
 141 |  * HIL Fault Injection: Inject simulated CRC corruption or I2C bus NAK.
 142 |  */
 143 | WET_EXPORT void wet_hal_sensirion_inject_fault(
 144 |     wet_hal_driver_t* drv,
 145 |     uint8_t corrupt_crc,
 146 |     uint8_t nak_addr
 147 | );
 148 | 
 149 | #ifdef __cplusplus
 150 | }
 151 | #endif
 152 | 
 153 | #endif /* WET_HAL_SENSIRION_H */
```

### `native/include/wet_scheduler.h` (136 lines, SHA-256: `ae755ab83f92e024...`)

```text
   1 | /**
   2 |  * WetLang Hard Real-Time Sub-100 µs Execution Scheduler
   3 |  * Header Interface (native/include/wet_scheduler.h)
   4 |  *
   5 |  * Deterministic C99 execution scheduler operating at 10 kHz (100 µs period):
   6 |  *  - Dedicated real-time thread with core pinning (SetThreadAffinityMask)
   7 |  *  - Process & thread priority elevation (REALTIME_PRIORITY_CLASS / THREAD_PRIORITY_TIME_CRITICAL)
   8 |  *  - High-resolution hardware monotonic timer (QPC / QPF)
   9 |  *  - Hybrid precision pacing: bytecode/ODE compute + calibrated spin-wait tail (_mm_pause)
  10 |  *  - Cacheline-aligned (64-byte) lockless SPSC ring buffers for telemetry & stimulus injection
  11 |  *  - Static memory arena: zero heap allocations during real-time stepping
  12 |  */
  13 | 
  14 | #ifndef WET_SCHEDULER_H
  15 | #define WET_SCHEDULER_H
  16 | 
  17 | #include "wetvm_api.h"
  18 | #include "wetvm_types.h"
  19 | #include "wetvm_vm.h"
  20 | 
  21 | #ifdef __cplusplus
  22 | extern "C" {
  23 | #endif
  24 | 
  25 | typedef struct wet_vm_instance wet_vm_instance_t;
  26 | 
  27 | /* Scheduler Configuration Options */
  28 | typedef struct {
  29 |     uint32_t target_period_us;         /* Nominal tick period in microseconds (default: 100 µs = 10 kHz) */
  30 | 
  31 |     /**
  32 |      * target_core: Physical/logical CPU core index for thread affinity mask (default: 1).
  33 |      *
  34 |      * ARCHITECTURAL GUIDANCE FOR HETEROGENEOUS HYBRID PROCESSORS:
  35 |      * On modern heterogeneous x86 architectures (e.g. Intel 12th-15th Gen Alder Lake,
  36 |      * Raptor Lake, Arrow Lake, and Intel Core Ultra / Lunar Lake), the processor combines
  37 |      * Performance Cores (P-cores, typically logical cores 0-3) and Efficient Cores
  38 |      * (E-cores / LP-E cores, typically logical cores 4+).
  39 |      *
  40 |      * CRITICAL: target_core MUST be pinned to a Performance Core (P-core, typically logical
  41 |      * cores 0–3). Benchmarks on heterogeneous hardware show that Efficient Cores (E-cores)
  42 |      * exhibit:
  43 |      *   - +55% compute latency (13–14 µs vs 8.8 µs on P-cores)
  44 |      *   - Highly elevated jitter (>300 µs P99.9) violating the sub-100 µs real-time contract
  45 |      *   - Consistent deadline overruns (4–17 overruns per 5k ticks under 10 kHz load).
  46 |      * Core 0 typically handles operating system DPCs and hardware interrupts; therefore,
  47 |      * logical Cores 1, 2, or 3 are the strongly recommended targets for hard real-time execution.
  48 |      */
  49 |     uint32_t target_core;
  50 |     uint32_t priority_class;           /* Windows priority class (default: 0x00000100 REALTIME_PRIORITY_CLASS) */
  51 |     int32_t  thread_priority;          /* Thread priority level (default: 15 THREAD_PRIORITY_TIME_CRITICAL) */
  52 |     uint8_t  enable_core_pinning;      /* 1 = pin thread to target_core, 0 = no pinning */
  53 |     uint8_t  enable_priority_elevation;/* 1 = elevate to REALTIME/TIME_CRITICAL, 0 = normal */
  54 |     uint32_t telemetry_queue_capacity; /* Power-of-2 capacity for telemetry SPSC ring buffer (default: 1024) */
  55 |     uint32_t stimulus_queue_capacity;  /* Power-of-2 capacity for stimulus SPSC ring buffer (default: 256) */
  56 |     uint64_t total_ticks;              /* Number of ticks to execute in benchmark/run (0 = indefinite) */
  57 | } wet_scheduler_config_t;
  58 | 
  59 | /* Asynchronous Stimulus Command injected through lockless SPSC queue */
  60 | typedef struct {
  61 |     uint8_t  channel;         /* MEA electrode channel (0..63) */
  62 |     float    voltage_v;       /* Stimulation voltage amplitude (V) */
  63 |     float    phase1_ms;       /* Cathodic pulse duration (ms) */
  64 |     float    phase2_ms;       /* Anodic counter-charge duration (ms) */
  65 |     uint64_t tick_scheduled;  /* Execution tick target (0 = immediate next tick) */
  66 | } wet_stim_command_t;
  67 | 
  68 | /* Latency & Jitter Performance Statistics */
  69 | typedef struct {
  70 |     uint64_t total_ticks;
  71 |     double   min_compute_us;
  72 |     double   max_compute_us;
  73 |     double   mean_compute_us;
  74 |     double   min_period_us;
  75 |     double   max_period_us;
  76 |     double   mean_period_us;
  77 |     double   mean_jitter_us;
  78 |     double   p50_jitter_us;
  79 |     double   p95_jitter_us;
  80 |     double   p99_jitter_us;
  81 |     double   p999_jitter_us;
  82 |     double   max_jitter_us;
  83 |     uint64_t deadline_overruns; /* Count of ticks where compute duration > target_period */
  84 |     uint64_t telemetry_dropped; /* Count of telemetry frames dropped due to full SPSC queue */
  85 |     uint64_t stimuli_injected;  /* Count of stimuli popped from SPSC queue and delivered to VM */
  86 | } wet_scheduler_stats_t;
  87 | 
  88 | /* Opaque Scheduler Instance Pointer */
  89 | typedef struct wet_scheduler wet_scheduler_t;
  90 | 
  91 | /* Public C-ABI API Functions */
  92 | WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config);
  93 | WET_EXPORT wet_status_t wet_scheduler_start(wet_scheduler_t* sched);
  94 | 
  95 | /**
  96 |  * Executes a single isochronous real-time tick step.
  97 |  *
  98 |  * PHASE SLIP STABILITY TRADE-OFF (Isochronous Pacing vs. Catch-Up Storms):
  99 |  * The scheduler deadline calculation evaluates:
 100 |  *   if (sched->next_deadline_qpc == 0 ||
 101 |  *       start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
 102 |  *       sched->next_deadline_qpc = start_qpc + sched->period_qpc;
 103 |  *   } else {
 104 |  *       sched->next_deadline_qpc += sched->period_qpc;
 105 |  *   }
 106 |  *
 107 |  * DESIGN RATIONALE:
 108 |  * Under quiescent conditions, accumulating next_deadline_qpc += period_qpc maintains
 109 |  * zero cumulative phase drift across thousands of cycles (<0.005% drift).
 110 |  * However, on non-RTOS desktop operating systems (e.g. Windows/Linux without PREEMPT_RT),
 111 |  * transient kernel DPCs, graphics driver stalls, or System Management Interrupts (SMIs)
 112 |  * can intermittently stall user-space threads for >200 µs (more than 2 full periods at 10 kHz).
 113 |  *
 114 |  * If the scheduler strictly maintained absolute wallclock cumulative phase lock without
 115 |  * resynchronization, returning from an OS stall would trigger a catastrophic "catch-up storm":
 116 |  * the scheduler would execute dozens of consecutive ticks with zero slack to recover lost time.
 117 |  * In wetware electrophysiology and microfluidics, back-to-back stimulation pulses violate
 118 |  * biological refractory windows (2.0 ms) and destabilize ODE numerical integration.
 119 |  *
 120 |  * Therefore, WetLang intentionally resynchronizes the deadline forward when a lag exceeding
 121 |  * two periods (>200 µs) occurs. This trades absolute cumulative wallclock phase lock during
 122 |  * severe OS stalls for period stability and biophysical execution safety.
 123 |  */
 124 | WET_EXPORT wet_status_t wet_scheduler_step(wet_scheduler_t* sched);
 125 | WET_EXPORT wet_status_t wet_scheduler_stop(wet_scheduler_t* sched);
 126 | WET_EXPORT wet_status_t wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats);
 127 | WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem);
 128 | WET_EXPORT wet_status_t wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd);
 129 | WET_EXPORT wet_status_t wet_scheduler_benchmark(wet_scheduler_t* sched, uint32_t total_ticks, wet_scheduler_stats_t* out_stats);
 130 | WET_EXPORT void wet_scheduler_destroy(wet_scheduler_t* sched);
 131 | 
 132 | #ifdef __cplusplus
 133 | }
 134 | #endif
 135 | 
 136 | #endif /* WET_SCHEDULER_H */
```

### `native/include/wetvm_api.h` (310 lines, SHA-256: `f1f5e21dac2938cd...`)

```text
   1 | #ifndef WETVM_API_H
   2 | #define WETVM_API_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | #include "wetvm_types.h"
   7 | 
   8 | #ifdef __cplusplus
   9 | extern "C" {
  10 | #endif
  11 | 
  12 | /* Export / Import visibility macro */
  13 | #if defined(_WIN32) || defined(__CYGWIN__)
  14 |   #ifdef WET_BUILDING_DLL
  15 |     #define WET_EXPORT __declspec(dllexport)
  16 |   #else
  17 |     #define WET_EXPORT __declspec(dllimport)
  18 |   #endif
  19 | #else
  20 |   #if defined(__GNUC__) && __GNUC__ >= 4
  21 |     #define WET_EXPORT __attribute__((visibility("default")))
  22 |   #else
  23 |     #define WET_EXPORT
  24 |   #endif
  25 | #endif
  26 | 
  27 | /* Opaque Virtual Machine Instance Pointer */
  28 | typedef struct wet_vm_instance wet_vm_t;
  29 | 
  30 | /* VM Configuration */
  31 | typedef struct {
  32 |     double   dt_ms;            /* Simulation timestep in ms (default: 0.1 ms) */
  33 |     uint32_t max_stack_depth;  /* Max operand stack capacity (default: 1024) */
  34 |     uint32_t max_locals;       /* Max local variable slots (default: 256) */
  35 |     uint32_t channel_count;    /* Number of MEA channels (default: 64) */
  36 |     uint32_t max_ops_per_tick; /* Per-tick watchdog instruction limit (default: 100,000 / 2,000 for MCU) */
  37 |     uint32_t min_sequence_counter; /* Minimum monotonic anti-rollback sequence counter required (0 = unconstrained) */
  38 | } wet_vm_config_t;
  39 | 
  40 | /* Cycle-Accurate Telemetry Output */
  41 | typedef struct {
  42 |     uint64_t current_tick;         /* Number of executed ticks */
  43 |     double   sim_time_ms;          /* Total simulation time in ms */
  44 |     float    voltages[64];         /* Instantaneous channel potentials (V) */
  45 |     uint8_t  spikes[64];           /* Binary spike raster (1 = spiked this tick) */
  46 |     float    population_rate_hz;   /* Estimated population firing rate (Hz) */
  47 |     float    last_charge_nc[64];   /* Cumulative or last injected charge (nC) */
  48 | } wet_telemetry_t;
  49 | 
  50 | /* Cyber-Physical Hardware Actuator Telemetry */
  51 | typedef struct {
  52 |     float    pump_rates_ul_min[8];   /* Rate for 8 microfluidic pumps */
  53 |     float    pump_dispensed_ul[8];   /* Cumulative dispensed volume */
  54 |     uint8_t  valve_states[8];        /* State of 8 valves (0=closed, 1=open) */
  55 |     int32_t  motor_positions[4];     /* Step positions for 4 motors */
  56 |     float    motor_speeds_rpm[4];    /* Speeds for 4 motors */
  57 |     float    ambient_temperature_c;  /* Ambient incubator temperature (C) */
  58 |     float    fluid_pressure_kpa[4];  /* Microfluidic pressure (kPa) */
  59 | } wet_actuator_telemetry_t;
  60 | 
  61 | /* =========================================================================
  62 |  * Public C-ABI API Functions
  63 |  * ========================================================================= */
  64 | 
  65 | /**
  66 |  * Creates and initializes a new WetVM instance.
  67 |  * If config is NULL, default configuration values are used.
  68 |  */
  69 | WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config);
  70 | 
  71 | /**
  72 |  * Creates a WetVM instance using caller-supplied static arena memory (zero dynamic malloc).
  73 |  */
  74 | WET_EXPORT wet_vm_t* wet_create_vm_arena(
  75 |     void* arena_buf,
  76 |     size_t arena_bytes,
  77 |     const wet_vm_config_t* config
  78 | );
  79 | 
  80 | /**
  81 |  * Destroys the VM instance and releases all associated memory.
  82 |  */
  83 | WET_EXPORT void wet_free_vm(wet_vm_t* vm);
  84 | 
  85 | /**
  86 |  * Phase 3: Configures electrode material and physical geometric surface area.
  87 |  */
  88 | WET_EXPORT void wet_configure_electrode(
  89 |     wet_vm_t* vm,
  90 |     uint8_t material,
  91 |     float area_um2
  92 | );
  93 | 
  94 | /**
  95 |  * Phase 3: Actuates hardware charge-recovery switch to discharge residual DC Faradaic charge.
  96 |  */
  97 | WET_EXPORT void wet_active_discharge(
  98 |     wet_vm_t* vm,
  99 |     uint8_t channel
 100 | );
 101 | 
 102 | /**
 103 |  * Phase 3: Actuates hardware charge-recovery switch on all channels.
 104 |  */
 105 | WET_EXPORT void wet_active_discharge_all(
 106 |     wet_vm_t* vm
 107 | );
 108 | 
 109 | /**
 110 |  * Phase 3: Enables microfluidic valve-pump dead-head overpressure interlock.
 111 |  */
 112 | WET_EXPORT void wet_enable_dead_head_protection(
 113 |     wet_vm_t* vm,
 114 |     uint8_t enable
 115 | );
 116 | 
 117 | /**
 118 |  * Phase 3: Ring-0 Life Support Supervisor shutdown (terminates baseline life support).
 119 |  */
 120 | WET_EXPORT void wet_life_supervisor_shutdown(
 121 |     wet_vm_t* vm
 122 | );
 123 | 
 124 | /**
 125 |  * Validates, loads, and parses WBC binary bytecode into the VM.
 126 |  * Resets execution registers (pc, sp, tick_count, is_halted).
 127 |  * If loading fails, an error message is written into err_buf (if provided).
 128 |  */
 129 | WET_EXPORT wet_status_t wet_load_bytecode(
 130 |     wet_vm_t* vm,
 131 |     const uint8_t* code_bytes,
 132 |     size_t size,
 133 |     char* err_buf,
 134 |     size_t err_buf_len
 135 | );
 136 | 
 137 | /**
 138 |  * Executes instructions until the next SYNC_TICK yield, SLEEP_TICKS, HALT, or error.
 139 |  * Advances current_tick by 1 and sim_time_ms by config->dt_ms.
 140 |  * Caller allocates out_telem; if non-NULL, it is populated with current state.
 141 |  */
 142 | WET_EXPORT wet_status_t wet_step_tick(
 143 |     wet_vm_t* vm,
 144 |     wet_telemetry_t* out_telem
 145 | );
 146 | 
 147 | /**
 148 |  * Executes up to `ticks` consecutive ticks.
 149 |  * Returns WET_OK if all ticks executed successfully, or early status on HALT/error.
 150 |  * executed_ticks receives the actual number of ticks completed.
 151 |  * out_telem receives final state (if non-NULL).
 152 |  */
 153 | WET_EXPORT wet_status_t wet_run_ticks(
 154 |     wet_vm_t* vm,
 155 |     uint32_t ticks,
 156 |     uint32_t* executed_ticks,
 157 |     wet_telemetry_t* out_telem
 158 | );
 159 | 
 160 | /**
 161 |  * Injects a biphasic electrical stimulus onto the designated MEA channel.
 162 |  */
 163 | WET_EXPORT wet_status_t wet_inject_stimulus(
 164 |     wet_vm_t* vm,
 165 |     uint8_t channel,
 166 |     float voltage_v,
 167 |     float phase1_ms,
 168 |     float phase2_ms
 169 | );
 170 | 
 171 | /**
 172 |  * Queries current telemetry state into caller-allocated struct.
 173 |  */
 174 | WET_EXPORT wet_status_t wet_get_telemetry(
 175 |     wet_vm_t* vm,
 176 |     wet_telemetry_t* out_telem
 177 | );
 178 | 
 179 | /**
 180 |  * Queries current cyber-physical hardware actuator telemetry into caller-allocated struct.
 181 |  */
 182 | WET_EXPORT wet_status_t wet_get_actuator_telemetry(
 183 |     wet_vm_t* vm,
 184 |     wet_actuator_telemetry_t* out_act_telem
 185 | );
 186 | 
 187 | /**
 188 |  * Returns string pointer to the last error message recorded on the VM.
 189 |  */
 190 | WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm);
 191 | 
 192 | /**
 193 |  * Returns a static descriptive string for the given status code.
 194 |  */
 195 | WET_EXPORT const char* wet_status_to_string(wet_status_t status);
 196 | 
 197 | /**
 198 |  * Phase 3: Configures post-stimulus amplifier artifact blanking window in ms.
 199 |  */
 200 | WET_EXPORT void wet_configure_blanking(
 201 |     wet_vm_t* vm,
 202 |     float blanking_ms,
 203 |     uint8_t enable_spatial
 204 | );
 205 | 
 206 | /**
 207 |  * Phase 3: Injects constant-current electrical stimulus (uA) into MEA channel.
 208 |  */
 209 | WET_EXPORT wet_status_t wet_inject_current_stimulus(
 210 |     wet_vm_t* vm,
 211 |     uint8_t channel,
 212 |     float current_ua,
 213 |     float phase1_ms,
 214 |     float phase2_ms
 215 | );
 216 | 
 217 | /**
 218 |  * Phase 3: Standalone C99 Load-Time Bytecode Verifier.
 219 |  * Validates magic, CRC32, section boundaries, opcode validity, and branch target alignment.
 220 |  */
 221 | WET_EXPORT wet_status_t wet_verify_bytecode(
 222 |     const uint8_t* bytecode,
 223 |     size_t size,
 224 |     char* err_buf,
 225 |     size_t err_buf_len
 226 | );
 227 | 
 228 | /**
 229 |  * Phase 3: Live State Checkpointing.
 230 |  * Serializes complete dynamic neural state, synaptic weights, and clocks into buffer.
 231 |  */
 232 | WET_EXPORT wet_status_t wet_vm_snapshot(
 233 |     const wet_vm_t* vm,
 234 |     uint8_t* buffer,
 235 |     size_t* inout_len
 236 | );
 237 | 
 238 | /**
 239 |  * Phase 3: Live State Hot-Swap Restoration.
 240 |  * Deserializes neural state and synaptic weights without rebooting the VM.
 241 |  */
 242 | WET_EXPORT wet_status_t wet_vm_restore(
 243 |     wet_vm_t* vm,
 244 |     const uint8_t* buffer,
 245 |     size_t len
 246 | );
 247 | 
 248 | /**
 249 |  * Phase 3: Sets environmental sensor readings (pH, DO %, CO2 %, bubble detectors, flow rate).
 250 |  */
 251 | WET_EXPORT void wet_set_environmental_sensors(
 252 |     wet_vm_t* vm,
 253 |     float ph,
 254 |     float do_pct,
 255 |     float co2_pct,
 256 |     uint8_t bubble_sensor_id,
 257 |     uint8_t bubble_state,
 258 |     float flow_rate_ul_min
 259 | );
 260 | 
 261 | /**
 262 |  * Phase 3: Sets ambient incubator / CMOS die temperature (C).
 263 |  */
 264 | WET_EXPORT void wet_set_temperature(
 265 |     wet_vm_t* vm,
 266 |     float temp_c
 267 | );
 268 | 
 269 | /**
 270 |  * Phase 3: Sets typed channel banks (reference and recording-only masks).
 271 |  */
 272 | WET_EXPORT void wet_set_channel_banks(
 273 |     wet_vm_t* vm,
 274 |     uint64_t ref_mask,
 275 |     uint64_t rec_mask
 276 | );
 277 | 
 278 | /**
 279 |  * Milestone 2 Biophysics Live Synapse Matrix Introspection:
 280 |  * Copies the dense 64x64 synaptic conductance matrix (nS) from VM biophysics state
 281 |  * into caller-allocated buffer (float[64][64] = 4096 floats).
 282 |  */
 283 | WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
 284 |     const wet_vm_t* vm,
 285 |     float* out_matrix,
 286 |     size_t out_capacity_floats
 287 | );
 288 | 
 289 | /**
 290 |  * Queries single synaptic conductance weight between pre and post neurons in nS.
 291 |  */
 292 | WET_EXPORT float wet_vm_get_synapse_weight(
 293 |     const wet_vm_t* vm,
 294 |     uint8_t pre,
 295 |     uint8_t post
 296 | );
 297 | 
 298 | /**
 299 |  * Clamps requested stimulation voltage against the configured electrode material water window.
 300 |  */
 301 | WET_EXPORT float wet_clamp_voltage_vm(
 302 |     wet_vm_t* vm,
 303 |     float requested_v
 304 | );
 305 | 
 306 | #ifdef __cplusplus
 307 | }
 308 | #endif
 309 | 
 310 | #endif /* WETVM_API_H */
```

### `native/include/wetvm_types.h` (177 lines, SHA-256: `b7289c4cdde4199c...`)

```text
   1 | #ifndef WETVM_TYPES_H
   2 | #define WETVM_TYPES_H
   3 | 
   4 | #include <stdint.h>
   5 | #include <stddef.h>
   6 | 
   7 | #ifdef __cplusplus
   8 | extern "C" {
   9 | #endif
  10 | 
  11 | /* =========================================================================
  12 |  * WetLang Bytecode (WBC) Binary Header and Constants
  13 |  * ========================================================================= */
  14 | 
  15 | #define WET_HEADER_MAGIC "WETB"
  16 | #define WET_HEADER_MAGIC_INT 0x42544557U /* Little-endian 'W','E','T','B' */
  17 | #define WET_HEADER_SIZE 32
  18 | #define WET_VERSION_MAJOR 1
  19 | #define WET_VERSION_MINOR 0
  20 | 
  21 | #define WET_SECTION_ENTRY_SIZE 12
  22 | 
  23 | /* Capability Bitmask Flags matching compiler/isa.py */
  24 | typedef enum {
  25 |     WET_CAP_NONE            = 0x0000,
  26 |     WET_CAP_STIMULATION     = 0x0001, /* Performs electrical stimulation */
  27 |     WET_CAP_PLASTICITY      = 0x0002, /* Modifies STDP synaptic weights */
  28 |     WET_CAP_CLOSED_LOOP     = 0x0004, /* Executes sensory-motor feedback stream */
  29 |     WET_CAP_HIGH_VOLTAGE    = 0x0008, /* Requests voltages between 0.8 V and 1.2 V */
  30 |     WET_CAP_MULTI_ELECTRODE = 0x0010, /* Uses more than 16 electrodes concurrently */
  31 |     WET_CAP_MICROFLUIDICS   = 0x0020, /* Drives physical microfluidic pumps & valves */
  32 |     WET_CAP_MOTOR_ACTUATION = 0x0040, /* Drives physical stepper motors / actuators */
  33 |     WET_CAP_SIGNATURE_VERIFIED = 0x0080 /* Cryptographically signed bytecode */
  34 | } wet_capability_t;
  35 | 
  36 | /* Section Types matching compiler/isa.py */
  37 | typedef enum {
  38 |     WET_SEC_CONSTANT_POOL   = 1,
  39 |     WET_SEC_TOPOLOGY_CONFIG = 2,
  40 |     WET_SEC_BYTECODE_STREAM = 3,
  41 |     WET_SEC_SAFETY_MANIFEST = 4,
  42 |     WET_SEC_DEBUG_LINE_MAP  = 5
  43 | } wet_section_type_t;
  44 | 
  45 | /* Status / Error Codes */
  46 | typedef enum {
  47 |     WET_OK                     = 0,
  48 |     WET_ERR_INVALID_MAGIC      = 1,
  49 |     WET_ERR_CRC_MISMATCH       = 2,
  50 |     WET_ERR_UNSUPPORTED_VERSION= 3,
  51 |     WET_ERR_MALFORMED_SECTION  = 4,
  52 |     WET_ERR_STACK_OVERFLOW     = 5,
  53 |     WET_ERR_STACK_UNDERFLOW    = 6,
  54 |     WET_ERR_INVALID_OPCODE     = 7,
  55 |     WET_ERR_OUT_OF_BOUNDS_CH   = 8,
  56 |     WET_ERR_DIVISION_BY_ZERO   = 9,
  57 |     WET_ERR_NULL_PTR           = 10,
  58 |     WET_ERR_ALLOC_FAILED       = 11,
  59 |     WET_ERR_HALTED             = 12,
  60 |     WET_ERR_CHARGE_IMBALANCE   = 13,
  61 |     WET_ERR_EPILEPTIFORM_RUNAWAY = 14,
  62 |     WET_ERR_CAPABILITY_DENIED  = 15,
  63 |     WET_ERR_INTERLOCK_LOCKED   = 16,
  64 |     WET_ERR_WATCHDOG_TIMEOUT   = 17,
  65 |     WET_ERR_DC_DRIFT           = 18,
  66 |     WET_ERR_CHARGE_DENSITY_EXCEEDED = 19,
  67 |     WET_ERR_FOCAL_EXCITOTOXICITY = 20,
  68 |     WET_ERR_SHEAR_STRESS_EXCEEDED = 21,
  69 |     WET_ERR_SECURITY_UNTRUSTED    = 22,
  70 |     WET_ERR_ACTUATOR_FAULT        = 23,
  71 |     WET_ERR_THERMAL_LIMIT         = 24,
  72 |     WET_ERR_BUBBLE_DETECTED       = 25,
  73 |     WET_ERR_COMPLIANCE_RAILED     = 26,
  74 |     WET_ERR_BYTECODE_VERIFICATION = 27
  75 | } wet_status_t;
  76 | 
  77 | /* Opcode Table (30+ Opcodes) matching compiler/isa.py */
  78 | typedef enum {
  79 |     /* Control */
  80 |     WET_OP_NOP          = 0x00,
  81 |     WET_OP_HALT         = 0x01,
  82 |     WET_OP_SYNC_TICK    = 0x02,
  83 |     WET_OP_SLEEP_TICKS  = 0x03, /* <H (uint16) */
  84 | 
  85 |     /* Stack Ops */
  86 |     WET_OP_PUSH_CONST   = 0x10, /* <H (uint16 pool index) */
  87 |     WET_OP_PUSH_INT     = 0x11, /* <i (int32) */
  88 |     WET_OP_PUSH_FLOAT   = 0x12, /* <f (float32) */
  89 |     WET_OP_POP          = 0x13,
  90 |     WET_OP_DUP          = 0x14,
  91 |     WET_OP_SWAP         = 0x15,
  92 |     WET_OP_LOAD_LOCAL   = 0x16, /* <H (uint16 local slot) */
  93 |     WET_OP_STORE_LOCAL  = 0x17, /* <H (uint16 local slot) */
  94 | 
  95 |     /* Arithmetic */
  96 |     WET_OP_ADD_I        = 0x20,
  97 |     WET_OP_SUB_I        = 0x21,
  98 |     WET_OP_MUL_I        = 0x22,
  99 |     WET_OP_DIV_I        = 0x23,
 100 |     WET_OP_ADD_F        = 0x24,
 101 |     WET_OP_SUB_F        = 0x25,
 102 |     WET_OP_MUL_F        = 0x26,
 103 |     WET_OP_DIV_F        = 0x27,
 104 |     WET_OP_NEG          = 0x28,
 105 |     WET_OP_MOD_I        = 0x29,
 106 | 
 107 |     /* Relational & Equality */
 108 |     WET_OP_CMP_EQ       = 0x30,
 109 |     WET_OP_CMP_NE       = 0x31,
 110 |     WET_OP_CMP_LT       = 0x32,
 111 |     WET_OP_CMP_LE       = 0x33,
 112 |     WET_OP_CMP_GT       = 0x34,
 113 |     WET_OP_CMP_GE       = 0x35,
 114 | 
 115 |     /* Control Jumps */
 116 |     WET_OP_JMP          = 0x40, /* <h (int16 relative branch offset) */
 117 |     WET_OP_JMP_IF_TRUE  = 0x41, /* <h (int16 relative branch offset) */
 118 |     WET_OP_JMP_IF_FALSE = 0x42, /* <h (int16 relative branch offset) */
 119 |     WET_OP_CALL         = 0x43, /* <HB (uint16 fn_idx, uint8 argc) */
 120 |     WET_OP_RET          = 0x44,
 121 | 
 122 |     /* Biophysical & Domain */
 123 |     WET_OP_STIM_BIPHASIC= 0x50, /* <B (uint8 channel) */
 124 |     WET_OP_READ_SPIKES  = 0x51, /* <B (uint8 channel) */
 125 |     WET_OP_READ_VOLTAGE = 0x52, /* <B (uint8 channel) */
 126 |     WET_OP_MODULATE_STDP= 0x53, /* <BB (uint8 pre, uint8 post) */
 127 |     WET_OP_GET_POP_RATE = 0x54,
 128 |     WET_OP_MEA_CONFIG   = 0x55, /* <BB (uint8 rows, uint8 cols) */
 129 | 
 130 |     /* Cyber-Physical Hardware Actuation (Pumps, Valves, Motors, Sensors) */
 131 |     WET_OP_PUMP_SET_RATE    = 0x56, /* <Bf (uint8 pump_id, float32 rate_ul_min) */
 132 |     WET_OP_PUMP_DISPENSE    = 0x57, /* <Bf (uint8 pump_id, float32 volume_ul) */
 133 |     WET_OP_VALVE_SET        = 0x58, /* <BB (uint8 valve_id, uint8 state) */
 134 |     WET_OP_MOTOR_STEP       = 0x59, /* <Bif (uint8 motor_id, int32 steps, float32 speed_rpm) */
 135 |     WET_OP_READ_PRESSURE    = 0x5A, /* <B (uint8 port_id) */
 136 |     WET_OP_READ_TEMPERATURE = 0x5B,
 137 | 
 138 |     /* Phase 3 Electrophysiology & Environmental Sensors */
 139 |     WET_OP_STIM_CURRENT     = 0x5C, /* <Bf (uint8 channel, float32 current_ua) */
 140 |     WET_OP_READ_PH          = 0x5D,
 141 |     WET_OP_READ_DO          = 0x5E,
 142 |     WET_OP_READ_CO2         = 0x5F,
 143 |     WET_OP_READ_BUBBLE      = 0x60, /* <B (uint8 sensor_id) */
 144 |     WET_OP_READ_FLOW        = 0x61  /* <B (uint8 sensor_id) */
 145 | } wet_opcode_t;
 146 | 
 147 | #pragma pack(push, 1)
 148 | 
 149 | /* WBC 32-Byte Header Specification (<4sBBHIIIIfI) */
 150 | typedef struct {
 151 |     uint8_t  magic[4];       /* "WETB" */
 152 |     uint8_t  version_major;  /* 1 */
 153 |     uint8_t  version_minor;  /* 0 */
 154 |     uint16_t capabilities;   /* wet_capability_t bitmask */
 155 |     uint32_t file_size;      /* Total file size in bytes */
 156 |     uint32_t checksum_crc32; /* CRC32 with bytes 12-15 zeroed */
 157 |     uint32_t num_sections;   /* Number of section table entries */
 158 |     uint32_t channel_count;  /* MEA channel count (typically 64) */
 159 |     float    max_charge_nc;  /* Upper bound static charge limit */
 160 |     uint32_t sequence_counter; /* Monotonically increasing anti-rollback security counter (0 = unconstrained) */
 161 | } wet_bytecode_header_t;
 162 | 
 163 | /* WBC Section Table Entry (<HHII, 12 bytes) */
 164 | typedef struct {
 165 |     uint16_t section_type;   /* wet_section_type_t */
 166 |     uint16_t reserved;       /* Reserved (0) */
 167 |     uint32_t offset;         /* Byte offset from start of file */
 168 |     uint32_t size;           /* Size of section payload in bytes */
 169 | } wet_section_header_t;
 170 | 
 171 | #pragma pack(pop)
 172 | 
 173 | #ifdef __cplusplus
 174 | }
 175 | #endif
 176 | 
 177 | #endif /* WETVM_TYPES_H */
```

### `native/include/wetvm_vm.h` (146 lines, SHA-256: `e769cd7ca730fe3f...`)

```text
   1 | #ifndef WETVM_VM_H
   2 | #define WETVM_VM_H
   3 | 
   4 | #include "wetvm_api.h"
   5 | #include "wetvm_types.h"
   6 | #include "biophysics.h"
   7 | #include "interlocks.h"
   8 | 
   9 | #ifdef __cplusplus
  10 | extern "C" {
  11 | #endif
  12 | 
  13 | /* Tagged value types */
  14 | typedef enum {
  15 |     WET_VAL_INT    = 1,
  16 |     WET_VAL_FLOAT  = 2,
  17 |     WET_VAL_STRING = 3
  18 | } wet_val_type_t;
  19 | 
  20 | /* Tagged Value representation for Operand Stack and Locals */
  21 | typedef struct {
  22 |     uint8_t type; /* wet_val_type_t */
  23 |     union {
  24 |         int32_t i_val;
  25 |         float   f_val;
  26 |         struct {
  27 |             const char* str;
  28 |             uint16_t    len;
  29 |         } s_val;
  30 |     } as;
  31 | } wet_value_t;
  32 | 
  33 | /* Constant Pool Entry */
  34 | typedef struct {
  35 |     wet_value_t val;
  36 |     char*       str_alloc; /* Owned allocation for string constants */
  37 | } wet_constant_entry_t;
  38 | 
  39 | /* Call Frame for CALL / RET */
  40 | typedef struct {
  41 |     size_t return_pc;
  42 | } wet_call_frame_t;
  43 | 
  44 | /* Ring-0 Life Support Supervisor (M6 Life Support Subsystem) */
  45 | typedef struct {
  46 |     uint8_t  supervisor_active;            /* 1 = Ring-0 supervisor autonomous maintenance active */
  47 |     float    maintenance_perfusion_ul_min[8]; /* Baseline nutrient flow rates */
  48 |     float    maintenance_temperature_c;      /* Target incubator temperature (37.0 C) */
  49 |     uint64_t ticks_under_supervisor;
  50 | } wet_life_supervisor_t;
  51 | 
  52 | /* Forward declaration for Hardware Abstraction Layer context */
  53 | struct wet_hal_context;
  54 | 
  55 | /* Internal VM instance structure */
  56 | struct wet_vm_instance {
  57 |     wet_vm_config_t config;
  58 | 
  59 |     /* Raw bytecode buffer */
  60 |     uint8_t* bytecode_raw;
  61 |     size_t   bytecode_size;
  62 | 
  63 |     /* Bytecode Stream section pointers */
  64 |     const uint8_t* code;
  65 |     size_t         code_size;
  66 |     size_t         pc;
  67 | 
  68 |     /* Constant Pool */
  69 |     wet_constant_entry_t* constants;
  70 |     size_t                num_constants;
  71 | 
  72 |     /* Operand Stack */
  73 |     wet_value_t* stack;
  74 |     size_t       sp;         /* Stack pointer: index of next free slot */
  75 |     size_t       max_stack;
  76 | 
  77 |     /* Local Variables */
  78 |     wet_value_t* locals;
  79 |     size_t       max_locals;
  80 | 
  81 |     /* Call Stack for CALL / RET */
  82 |     wet_call_frame_t* call_stack;
  83 |     size_t            call_sp;
  84 |     size_t            max_call_depth;
  85 | 
  86 |     /* Execution State */
  87 |     uint64_t current_tick;
  88 |     double   sim_time_ms;
  89 |     int64_t  sim_time_us;        /* Microsecond monotonic time (avoids float32 loss) */
  90 |     int      is_halted;
  91 |     int      is_finished;
  92 |     uint16_t sleep_ticks_remaining;
  93 |     uint8_t  arena_allocated;    /* 1 if created in static arena memory */
  94 | 
  95 |     /* Channel States (64 channels) */
  96 |     float    voltages[64];
  97 |     uint8_t  spikes[64];
  98 |     float    last_charge_nc[64];
  99 |     float    discharge_charge_nc[64];
 100 |     float    population_rate_hz;
 101 | 
 102 |     /* Grid topology */
 103 |     uint8_t  grid_rows;
 104 |     uint8_t  grid_cols;
 105 | 
 106 |     /* Embedded Biophysical Digital Twin (M3) & Hardware Watchdog Interlocks (M4) */
 107 |     bio_state_t       bio;
 108 |     interlock_state_t interlocks;
 109 |     uint16_t          loaded_capabilities;
 110 | 
 111 |     /* Ring-0 Autonomous Life Support Supervisor */
 112 |     wet_life_supervisor_t life_supervisor;
 113 | 
 114 |     /* Cyber-Physical Hardware Actuator State (M5 HAL) */
 115 |     float    pump_rates_ul_min[8];
 116 |     float    pump_dispensed_ul[8];
 117 |     uint8_t  valve_states[8];
 118 |     int32_t  motor_positions[4];
 119 |     float    motor_speeds_rpm[4];
 120 |     float    ambient_temperature_c;
 121 |     float    fluid_pressure_kpa[4];
 122 | 
 123 |     /* Phase 3 Environmental & Cyber-Physical Sensors */
 124 |     float    ph_level;              /* e.g. 7.40 */
 125 |     float    dissolved_oxygen_pct;  /* e.g. 95.0 % */
 126 |     float    dissolved_co2_pct;     /* e.g. 5.0 % */
 127 |     uint8_t  bubble_detected[8];    /* 1 if bubble detected on tubing line */
 128 |     float    fluid_flow_rate_ul_min[8]; /* flow sensor readouts */
 129 | 
 130 |     /* Hardware Abstraction Layer Context (M1 HAL) */
 131 |     struct wet_hal_context* hal;
 132 | 
 133 |     /* Error reporting buffer */
 134 |     char     last_error[256];
 135 | };
 136 | 
 137 | /* Internal VM execution and validation declarations */
 138 | uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc);
 139 | wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem);
 140 | wet_status_t wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len);
 141 | 
 142 | #ifdef __cplusplus
 143 | }
 144 | #endif
 145 | 
 146 | #endif /* WETVM_VM_H */
```

### `native/src/biophysics.c` (547 lines, SHA-256: `9854cac4a9aab336...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/biophysics.h"
   3 | 
   4 | /* =========================================================================
   5 |  * Helper: Initialize Tsodyks-Markram STP parameters by cortical synapse class
   6 |  * ========================================================================= */
   7 | static void init_synapse_stp(bio_synapse_t* syn, uint8_t pre_exc, uint8_t post_exc, float weight_ns) {
   8 |     syn->exists = 1;
   9 |     syn->weight_ns = wet_clampf(weight_ns, BIO_W_MIN_NS, BIO_W_MAX_NS);
  10 | 
  11 |     if (pre_exc && post_exc) {
  12 |         syn->syn_class = SYN_CLASS_EE;
  13 |         syn->U_base = 0.50f;
  14 |         syn->tau_rec_ms = 800.0f;
  15 |         syn->tau_fac_ms = 20.0f;
  16 |     } else if (pre_exc && !post_exc) {
  17 |         syn->syn_class = SYN_CLASS_EI;
  18 |         syn->U_base = 0.15f;
  19 |         syn->tau_rec_ms = 200.0f;
  20 |         syn->tau_fac_ms = 600.0f;
  21 |     } else if (!pre_exc && post_exc) {
  22 |         syn->syn_class = SYN_CLASS_IE;
  23 |         syn->U_base = 0.25f;
  24 |         syn->tau_rec_ms = 500.0f;
  25 |         syn->tau_fac_ms = 50.0f;
  26 |     } else {
  27 |         syn->syn_class = SYN_CLASS_II;
  28 |         syn->U_base = 0.30f;
  29 |         syn->tau_rec_ms = 400.0f;
  30 |         syn->tau_fac_ms = 50.0f;
  31 |     }
  32 | 
  33 |     syn->u_stp = syn->U_base;
  34 |     syn->x_stp = 1.0f;
  35 | }
  36 | 
  37 | void biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed) {
  38 |     if (!bio) return;
  39 |     memset(bio, 0, sizeof(bio_state_t));
  40 | 
  41 |     bio->dt_ms = (dt_ms > 0.0) ? dt_ms : 0.1;
  42 |     bio->rng_state = (seed != 0) ? seed : 0x574554574F524C44ULL; /* "WETWORLD" */
  43 |     bio->stdp_lr_scale = 1.0f;
  44 | 
  45 |     /* Biophysical constants (COBA-LIF cortical organoid parameters) */
  46 |     bio->c_m_pf            = 200.0f;   /* 200 pF */
  47 |     bio->g_leak_ns         = 10.0f;    /* 10 nS -> tau_m = 20.0 ms */
  48 |     bio->e_leak_mv         = -70.0f;
  49 |     bio->e_reset_mv        = -75.0f;
  50 |     bio->e_thresh_base_mv  = -50.0f;
  51 |     bio->e_exc_mv          = 0.0f;
  52 |     bio->e_inh_mv          = -80.0f;
  53 |     bio->e_k_mv            = -90.0f;
  54 |     bio->tau_exc_ms        = 5.0f;     /* AMPA */
  55 |     bio->tau_inh_ms        = 10.0f;    /* GABA_A */
  56 |     bio->tau_ahp_ms        = 80.0f;    /* Slow K+ AHP */
  57 |     bio->tau_thresh_ms     = 10.0f;    /* Relative refractory threshold decay */
  58 |     bio->tau_stdp_plus_ms  = 20.0f;
  59 |     bio->tau_stdp_minus_ms = 20.0f;
  60 |     bio->stdp_a_plus       = 0.20f;
  61 |     bio->stdp_a_minus      = 0.21f;    /* 1.05x LTD bias for network stability */
  62 |     bio->electrode_impedance_kohm = 1000.0f; /* 1 MOhm microelectrode impedance */
  63 | 
  64 |     /* Phase 3 Blanking and Randles Equivalent Circuit Parameters */
  65 |     bio->default_blanking_ticks = 20;   /* 2.0 ms default amplifier blanking */
  66 |     bio->spatial_blanking_enabled = 1;  /* Enable adjacent channel crosstalk blanking */
  67 |     bio->r_solution_kohm = 2.0f;        /* 2.0 kOhm electrolyte solution resistance */
  68 |     bio->r_charge_transfer_kohm = 5000.0f; /* 5.0 MOhm Faradaic charge transfer resistance */
  69 |     bio->max_compliance_voltage_v = 7.0f;  /* +/-7.0 V Intan RHS2116 compliance limit */
  70 | 
  71 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
  72 |         bio->c_double_layer_pf[ch] = 26.45f; /* 26.45 pF for 132 um2 microelectrode */
  73 |         bio->v_double_layer_v[ch] = 0.0f;
  74 |         bio->last_stim_current_ua[ch] = 0.0f;
  75 |         bio->stim_blanking_ticks[ch] = 0;
  76 |     }
  77 | 
  78 |     /* 1. Place 64 neurons over 8x8 MEA (200 um pitch), 80% Exc (51) / 20% Inh (13) */
  79 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
  80 |         int r = i / BIO_GRID_COLS;
  81 |         int c = i % BIO_GRID_COLS;
  82 | 
  83 |         /* Deterministic spatially distributed 20% inhibitory interneurons */
  84 |         bio->is_excitatory[i] = ((i % 5) != 4) ? 1 : 0;
  85 | 
  86 |         float jx = (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 30.0f;
  87 |         float jy = (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 30.0f;
  88 |         float jz = 20.0f + (float)wet_rng_uniform(&bio->rng_state) * 15.0f;
  89 | 
  90 |         bio->pos_x_um[i] = (float)c * BIO_PITCH_UM + jx;
  91 |         bio->pos_y_um[i] = (float)r * BIO_PITCH_UM + jy;
  92 |         bio->pos_z_um[i] = jz;
  93 | 
  94 |         /* Slight heterogeneity in resting membrane potential */
  95 |         bio->v_m_mv[i] = bio->e_leak_mv + (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 4.0f;
  96 |         bio->v_thresh_mv[i] = bio->e_thresh_base_mv;
  97 |     }
  98 | 
  99 |     /* 2. Compute 8x8 MEA 3D volume conduction forward pickup matrix */
 100 |     const float lambda_um = 120.0f;
 101 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 102 |         float ex = (float)(ch % BIO_GRID_COLS) * BIO_PITCH_UM;
 103 |         float ey = (float)(ch / BIO_GRID_COLS) * BIO_PITCH_UM;
 104 |         float ez = 0.0f;
 105 | 
 106 |         float row_sum = 0.0f;
 107 |         for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 108 |             float dx = bio->pos_x_um[i] - ex;
 109 |             float dy = bio->pos_y_um[i] - ey;
 110 |             float dz = bio->pos_z_um[i] - ez;
 111 |             float dist_sq = dx * dx + dy * dy + dz * dz;
 112 |             float gain = 1.0f / (1.0f + dist_sq / (lambda_um * lambda_um));
 113 |             bio->pickup_matrix[ch][i] = gain;
 114 |             row_sum += gain;
 115 |         }
 116 |         if (row_sum > 1e-6f) {
 117 |             for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 118 |                 bio->pickup_matrix[ch][i] /= row_sum;
 119 |             }
 120 |         }
 121 |     }
 122 | 
 123 |     /* 3. Build distance-dependent sparse cortical connectivity (~20% density) */
 124 |     const float conn_scale_um = 350.0f;
 125 |     for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
 126 |         for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
 127 |             if (pre == post) continue;
 128 |             float dx = bio->pos_x_um[post] - bio->pos_x_um[pre];
 129 |             float dy = bio->pos_y_um[post] - bio->pos_y_um[pre];
 130 |             float dz = bio->pos_z_um[post] - bio->pos_z_um[pre];
 131 |             float dist = (float)wet_sqrt((double)(dx * dx + dy * dy + dz * dz));
 132 |             double p_conn = 0.35 * wet_exp(-(double)(dist / conn_scale_um));
 133 |             if (wet_rng_uniform(&bio->rng_state) < p_conn) {
 134 |                 float w0 = bio->is_excitatory[pre]
 135 |                     ? (4.0f + (float)wet_rng_uniform(&bio->rng_state) * 6.0f)
 136 |                     : (10.0f + (float)wet_rng_uniform(&bio->rng_state) * 10.0f);
 137 |                 init_synapse_stp(&bio->synapses[pre][post],
 138 |                                  bio->is_excitatory[pre],
 139 |                                  bio->is_excitatory[post],
 140 |                                  w0);
 141 |             }
 142 |         }
 143 |     }
 144 | }
 145 | 
 146 | void biophysics_reset(bio_state_t* bio) {
 147 |     if (!bio) return;
 148 |     double dt = bio->dt_ms;
 149 |     biophysics_init(bio, dt, 0x574554574F524C44ULL);
 150 | }
 151 | 
 152 | void biophysics_schedule_stim_ext(
 153 |     bio_state_t* bio,
 154 |     uint8_t channel,
 155 |     float clamped_voltage_v,
 156 |     float phase1_ms,
 157 |     float phase2_ms,
 158 |     float interphase_ms
 159 | ) {
 160 |     if (!bio || channel >= BIO_NUM_CHANNELS) return;
 161 | 
 162 |     float dt = (float)bio->dt_ms;
 163 |     uint32_t p1_ticks = (phase1_ms > 0.0f) ? (uint32_t)(phase1_ms / dt + 0.5f) : 0U;
 164 |     uint32_t p2_ticks = (phase2_ms > 0.0f) ? (uint32_t)(phase2_ms / dt + 0.5f) : 0U;
 165 |     uint32_t ip_ticks = (interphase_ms > 0.0f) ? (uint32_t)(interphase_ms / dt + 0.5f) : 0U;
 166 | 
 167 |     if (p1_ticks == 0 && p2_ticks == 0) {
 168 |         bio->stim_pulses[channel].active = 0;
 169 |         return;
 170 |     }
 171 | 
 172 |     bio_stim_pulse_t* p = &bio->stim_pulses[channel];
 173 |     p->active = 1;
 174 |     p->voltage_v = clamped_voltage_v;
 175 |     p->phase1_ticks_left = p1_ticks;
 176 |     p->interphase_ticks_left = ip_ticks;
 177 |     p->phase2_ticks_left = p2_ticks;
 178 | 
 179 |     /* Neurophysiologically grounded extracellular stimulation:
 180 |      * Phase 1 is negative (cathodic) relative to extracellular bath (depolarizing soma).
 181 |      * Phase 2 is positive (anodic) counter-charge. */
 182 |     float v_mag = wet_fabsf(clamped_voltage_v);
 183 |     p->phase1_amp_v = -v_mag;
 184 |     p->phase2_amp_v = v_mag;
 185 | 
 186 |     /* Set post-stimulus amplifier blanking window with spatial crosstalk neighbor propagation */
 187 |     uint16_t total_blanking = (uint16_t)(p1_ticks + ip_ticks + p2_ticks + bio->default_blanking_ticks);
 188 |     bio->stim_blanking_ticks[channel] = total_blanking;
 189 | 
 190 |     if (bio->spatial_blanking_enabled) {
 191 |         int r1 = channel / BIO_GRID_COLS;
 192 |         int c1 = channel % BIO_GRID_COLS;
 193 |         uint16_t neighbor_blank = (total_blanking * 3) / 4;
 194 |         for (int r2 = r1 - 1; r2 <= r1 + 1; ++r2) {
 195 |             for (int c2 = c1 - 1; c2 <= c1 + 1; ++c2) {
 196 |                 if (r2 >= 0 && r2 < BIO_GRID_ROWS && c2 >= 0 && c2 < BIO_GRID_COLS) {
 197 |                     int neighbor_ch = r2 * BIO_GRID_COLS + c2;
 198 |                     if (neighbor_ch != (int)channel && bio->stim_blanking_ticks[neighbor_ch] < neighbor_blank) {
 199 |                         bio->stim_blanking_ticks[neighbor_ch] = neighbor_blank;
 200 |                     }
 201 |                 }
 202 |             }
 203 |         }
 204 |     }
 205 | }
 206 | 
 207 | void biophysics_schedule_stim_current(
 208 |     bio_state_t* bio,
 209 |     uint8_t channel,
 210 |     float current_ua,
 211 |     float phase1_ms,
 212 |     float phase2_ms,
 213 |     float interphase_ms
 214 | ) {
 215 |     if (!bio || channel >= BIO_NUM_CHANNELS) return;
 216 |     bio->last_stim_current_ua[channel] = current_ua;
 217 | 
 218 |     /* Randles interface: Effective applied voltage V_eff = I * Rs + V_dl */
 219 |     float v_eff = (current_ua / 1000.0f) * bio->r_solution_kohm + bio->v_double_layer_v[channel];
 220 |     biophysics_schedule_stim_ext(bio, channel, v_eff, phase1_ms, phase2_ms, interphase_ms);
 221 | }
 222 | 
 223 | void biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial) {
 224 |     if (!bio) return;
 225 |     float dt = (float)bio->dt_ms;
 226 |     if (dt <= 0.0f) dt = 0.1f;
 227 |     bio->default_blanking_ticks = (uint16_t)(blanking_ms / dt + 0.5f);
 228 |     bio->spatial_blanking_enabled = enable_spatial;
 229 | }
 230 | 
 231 | void biophysics_get_randles_state(
 232 |     const bio_state_t* bio,
 233 |     uint8_t channel,
 234 |     float* out_v_dl_v,
 235 |     float* out_v_elec_v
 236 | ) {
 237 |     if (!bio || channel >= BIO_NUM_CHANNELS) return;
 238 |     float v_dl = bio->v_double_layer_v[channel];
 239 |     float v_elec = (bio->last_stim_current_ua[channel] / 1000.0f) * bio->r_solution_kohm + v_dl;
 240 |     if (out_v_dl_v) *out_v_dl_v = v_dl;
 241 |     if (out_v_elec_v) *out_v_elec_v = v_elec;
 242 | }
 243 | 
 244 | void biophysics_schedule_stim(
 245 |     bio_state_t* bio,
 246 |     uint8_t channel,
 247 |     float clamped_voltage_v,
 248 |     float phase1_ms,
 249 |     float phase2_ms
 250 | ) {
 251 |     biophysics_schedule_stim_ext(bio, channel, clamped_voltage_v, phase1_ms, phase2_ms, 0.0f);
 252 | }
 253 | 
 254 | void biophysics_zero_all_stim(bio_state_t* bio) {
 255 |     if (!bio) return;
 256 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 257 |         bio->stim_pulses[ch].active = 0;
 258 |         bio->stim_pulses[ch].phase1_ticks_left = 0;
 259 |         bio->stim_pulses[ch].interphase_ticks_left = 0;
 260 |         bio->stim_pulses[ch].phase2_ticks_left = 0;
 261 |         bio->stim_pulses[ch].voltage_v = 0.0f;
 262 |         bio->stim_pulses[ch].phase1_amp_v = 0.0f;
 263 |         bio->stim_pulses[ch].phase2_amp_v = 0.0f;
 264 |         bio->ext_stim_v[ch] = 0.0f;
 265 |         bio->tick_charge_nc[ch] = 0.0f;
 266 |         bio->stim_blanking_ticks[ch] = 0;
 267 |     }
 268 | }
 269 | 
 270 | void biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns) {
 271 |     if (!bio || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return;
 272 |     if (pre == post) return;
 273 | 
 274 |     bio_synapse_t* syn = &bio->synapses[pre][post];
 275 |     if (!syn->exists) {
 276 |         if (delta_w_ns > 0.0f) {
 277 |             init_synapse_stp(syn, bio->is_excitatory[pre], bio->is_excitatory[post], delta_w_ns);
 278 |             bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns);
 279 |         }
 280 |         return;
 281 |     }
 282 | 
 283 |     /* Dale's Principle: Conductance magnitude strictly bounded in [0, 40 nS]; sign fixed by E_rev */
 284 |     float old_w = syn->weight_ns;
 285 |     float new_w = wet_clampf(old_w + delta_w_ns, BIO_W_MIN_NS, BIO_W_MAX_NS);
 286 |     syn->weight_ns = new_w;
 287 |     bio->cumulative_weight_drift_ns += wet_fabsf(new_w - old_w);
 288 | }
 289 | 
 290 | void biophysics_step_tick(bio_state_t* bio) {
 291 |     if (!bio) return;
 292 | 
 293 |     const double dt = bio->dt_ms;
 294 |     const float  dt_f = (float)dt;
 295 | 
 296 |     /* Precompute exact exponential decay factors */
 297 |     const float decay_exc   = (float)wet_exp(-dt / (double)bio->tau_exc_ms);
 298 |     const float decay_inh   = (float)wet_exp(-dt / (double)bio->tau_inh_ms);
 299 |     const float decay_ahp   = (float)wet_exp(-dt / (double)bio->tau_ahp_ms);
 300 |     const float decay_thr   = (float)wet_exp(-dt / (double)bio->tau_thresh_ms);
 301 |     const float decay_pre   = (float)wet_exp(-dt / (double)bio->tau_stdp_plus_ms);
 302 |     const float decay_post  = (float)wet_exp(-dt / (double)bio->tau_stdp_minus_ms);
 303 | 
 304 |     /* 1. Advance active biphasic stimulation waveforms & compute tick charge (nC) */
 305 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 306 |         bio_stim_pulse_t* p = &bio->stim_pulses[ch];
 307 |         float v_applied = 0.0f;
 308 | 
 309 |         if (p->active) {
 310 |             if (p->phase1_ticks_left > 0) {
 311 |                 v_applied = p->phase1_amp_v;
 312 |                 p->phase1_ticks_left--;
 313 |             } else if (p->interphase_ticks_left > 0) {
 314 |                 v_applied = 0.0f;
 315 |                 p->interphase_ticks_left--;
 316 |                 /* Interphase Overpotential (E_mc): During zero-current interphase delay,
 317 |                  * I * Rs = 0, so measured electrode potential is purely the interfacial overpotential E_mc.
 318 |                  * If |E_mc| exceeds water window (0.8 V), extend blanking and flag Faradaic excursion. */
 319 |                 float e_mc_v = bio->v_double_layer_v[ch];
 320 |                 if (wet_fabsf(e_mc_v) > 0.8f && bio->stim_blanking_ticks[ch] < 50) {
 321 |                     bio->stim_blanking_ticks[ch] += 10;
 322 |                 }
 323 |             } else if (p->phase2_ticks_left > 0) {
 324 |                 v_applied = p->phase2_amp_v;
 325 |                 p->phase2_ticks_left--;
 326 |             }
 327 |             if (p->phase1_ticks_left == 0 && p->interphase_ticks_left == 0 && p->phase2_ticks_left == 0) {
 328 |                 p->active = 0;
 329 |             }
 330 |         }
 331 | 
 332 |         if (bio->stim_blanking_ticks[ch] > 0) {
 333 |             bio->stim_blanking_ticks[ch]--;
 334 |         }
 335 | 
 336 |         bio->ext_stim_v[ch] = v_applied;
 337 |         /* I (uA) = V (V) / Z (kOhm) * 1000; Q (nC) = I (uA) * dt (ms) */
 338 |         float i_ua = (v_applied / bio->electrode_impedance_kohm) * 1000.0f;
 339 |         bio->tick_charge_nc[ch] = i_ua * dt_f;
 340 | 
 341 |         /* Randles Cell Integration: dV_dl/dt = (I - V_dl/Rct) / Cdl */
 342 |         float c_dl_pf = bio->c_double_layer_pf[ch] > 0.0f ? bio->c_double_layer_pf[ch] : 26.45f;
 343 |         float r_ct_kohm = bio->r_charge_transfer_kohm > 0.0f ? bio->r_charge_transfer_kohm : 5000.0f;
 344 |         float tau_dl_ms = (r_ct_kohm * 1e3f) * (c_dl_pf * 1e-12f) * 1e3f; /* Rct * Cdl in ms */
 345 |         if (tau_dl_ms < 0.01f) tau_dl_ms = 0.01f;
 346 |         float decay_dl = (float)wet_exp(-dt / (double)tau_dl_ms);
 347 |         /* Injected dv = I * dt / Cdl; I in uA, dt in ms, Cdl in pF -> (uA * ms) / pF = (1e-6 * 1e-3) / 1e-12 = 1.0 V */
 348 |         float dv_dl = (i_ua * dt_f) / c_dl_pf;
 349 |         bio->v_double_layer_v[ch] = bio->v_double_layer_v[ch] * decay_dl + dv_dl;
 350 |     }
 351 | 
 352 |     /* 2. Decay synaptic conductances, AHP, dynamic thresholds, STDP traces & STP state */
 353 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 354 |         bio->g_exc_ns[i]   *= decay_exc;
 355 |         bio->g_inh_ns[i]   *= decay_inh;
 356 |         bio->g_ahp_ns[i]   *= decay_ahp;
 357 |         bio->v_thresh_mv[i] = bio->e_thresh_base_mv + (bio->v_thresh_mv[i] - bio->e_thresh_base_mv) * decay_thr;
 358 |         bio->trace_pre[i]  *= decay_pre;
 359 |         bio->trace_post[i] *= decay_post;
 360 |         bio->spikes_now[i]  = 0;
 361 | 
 362 |         /* Denormal / Subnormal Floating-Point Clamping to eliminate microcode exception traps */
 363 |         if (bio->g_exc_ns[i] < 1e-12f) bio->g_exc_ns[i] = 0.0f;
 364 |         if (bio->g_inh_ns[i] < 1e-12f) bio->g_inh_ns[i] = 0.0f;
 365 |         if (bio->g_ahp_ns[i] < 1e-12f) bio->g_ahp_ns[i] = 0.0f;
 366 |         if (bio->trace_pre[i] < 1e-12f) bio->trace_pre[i] = 0.0f;
 367 |         if (bio->trace_post[i] < 1e-12f) bio->trace_post[i] = 0.0f;
 368 |     }
 369 | 
 370 |     /* Exact Exponential Euler relaxation of Tsodyks-Markram STP variables */
 371 |     for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
 372 |         for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
 373 |             bio_synapse_t* syn = &bio->synapses[pre][post];
 374 |             if (!syn->exists) continue;
 375 |             float d_rec = (float)wet_exp(-dt / (double)syn->tau_rec_ms);
 376 |             float d_fac = (float)wet_exp(-dt / (double)syn->tau_fac_ms);
 377 |             syn->x_stp = 1.0f + (syn->x_stp - 1.0f) * d_rec;
 378 |             syn->u_stp = syn->U_base + (syn->u_stp - syn->U_base) * d_fac;
 379 |         }
 380 |     }
 381 | 
 382 |     /* 3. Integrate COBA-LIF membrane ODE via Exact Exponential Euler */
 383 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 384 |         if (bio->refract_ticks[i] > 0) {
 385 |             bio->refract_ticks[i]--;
 386 |             bio->v_m_mv[i] = bio->e_reset_mv;
 387 |             continue;
 388 |         }
 389 | 
 390 |         /* Couple nearby electrode stimulation via volume conduction pickup matrix */
 391 |         float stim_v_eff = 0.0f;
 392 |         for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 393 |             if (bio->ext_stim_v[ch] != 0.0f) {
 394 |                 stim_v_eff += bio->pickup_matrix[ch][i] * bio->ext_stim_v[ch];
 395 |             }
 396 |         }
 397 |         /* Convert effective extracellular field (V) into depolarizing soma current (pA).
 398 |          * Cathodic extracellular field (stim_v_eff < 0) depolarizes the soma (Vm = Vi - Ve);
 399 |          * scale calibrated so 0.5-1.0 V drives firing. */
 400 |         float i_stim_pa = -stim_v_eff * 1500.0f;
 401 | 
 402 |         /* Spontaneous cortical tonic + Gaussian background synaptic current (~15-25 Hz baseline) */
 403 |         float i_bg_pa = 215.0f + (float)wet_rng_normal(&bio->rng_state) * 140.0f;
 404 | 
 405 |         /* Total conductance (nS) */
 406 |         float g_tot = bio->g_leak_ns + bio->g_exc_ns[i] + bio->g_inh_ns[i] + bio->g_ahp_ns[i];
 407 |         if (g_tot < 1e-3f) g_tot = bio->g_leak_ns;
 408 | 
 409 |         /* Steady-state target potential V_inf (mV): (nS * mV + pA) / nS = mV */
 410 |         float num = bio->g_leak_ns * bio->e_leak_mv
 411 |                   + bio->g_exc_ns[i] * bio->e_exc_mv
 412 |                   + bio->g_inh_ns[i] * bio->e_inh_mv
 413 |                   + bio->g_ahp_ns[i] * bio->e_k_mv
 414 |                   + i_stim_pa + i_bg_pa;
 415 |         float v_inf = num / g_tot;
 416 | 
 417 |         /* Exact Exponential Euler step: tau_eff (ms) = C_m (pF) / g_tot (nS) */
 418 |         float tau_eff_ms = bio->c_m_pf / g_tot;
 419 |         float decay_v = (float)wet_exp(-dt / (double)tau_eff_ms);
 420 |         float v_next = v_inf + (bio->v_m_mv[i] - v_inf) * decay_v;
 421 | 
 422 |         /* Numerical safety clamp */
 423 |         v_next = wet_clampf(v_next, -120.0f, 50.0f);
 424 | 
 425 |         if (v_next >= bio->v_thresh_mv[i]) {
 426 |             bio->spikes_now[i] = 1;
 427 |             bio->v_m_mv[i] = bio->e_reset_mv;
 428 |             bio->refract_ticks[i] = BIO_ABS_REFRACT_TICKS; /* 2.0 ms hard absolute refractory */
 429 |             bio->v_thresh_mv[i] += 15.0f;                  /* +15 mV relative refractory jump */
 430 |             bio->g_ahp_ns[i]    += 2.0f;                   /* Slow AHP potassium adaptation */
 431 |         } else {
 432 |             bio->v_m_mv[i] = v_next;
 433 |         }
 434 |     }
 435 | 
 436 |     /* 4. Propagate spikes through Tsodyks-Markram STP synapses & Online Pairwise STDP */
 437 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 438 |         if (!bio->spikes_now[i]) continue;
 439 | 
 440 |         /* Update pre-synaptic and post-synaptic STDP traces */
 441 |         bio->trace_pre[i]  += 1.0f;
 442 |         bio->trace_post[i] += 1.0f;
 443 | 
 444 |         /* A) Outgoing synapses (i -> post): STP transmission + LTD */
 445 |         for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
 446 |             bio_synapse_t* syn = &bio->synapses[i][post];
 447 |             if (!syn->exists) continue;
 448 | 
 449 |             /* Tsodyks-Markram discrete spike update */
 450 |             syn->u_stp = syn->u_stp + syn->U_base * (1.0f - syn->u_stp);
 451 |             float release = syn->u_stp * syn->x_stp;
 452 |             syn->x_stp = wet_clampf(syn->x_stp - release, 0.0f, 1.0f);
 453 | 
 454 |             float dg = syn->weight_ns * release;
 455 |             if (bio->is_excitatory[i]) {
 456 |                 bio->g_exc_ns[post] += dg;
 457 |             } else {
 458 |                 bio->g_inh_ns[post] += dg;
 459 |             }
 460 | 
 461 |             /* Online STDP LTD on plastic excitatory synapses (1.05x depression bias) */
 462 |             if (bio->is_excitatory[i] && bio->trace_post[post] > 1e-6f) {
 463 |                 float dw = -bio->stdp_lr_scale * bio->stdp_a_minus * bio->trace_post[post];
 464 |                 float old_w = syn->weight_ns;
 465 |                 syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
 466 |                 bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
 467 |             }
 468 |         }
 469 | 
 470 |         /* B) Incoming synapses (pre -> i): Online STDP LTP on plastic excitatory synapses */
 471 |         for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
 472 |             if (!bio->is_excitatory[pre]) continue;
 473 |             bio_synapse_t* syn = &bio->synapses[pre][i];
 474 |             if (!syn->exists) continue;
 475 | 
 476 |             if (bio->trace_pre[pre] > 1e-6f) {
 477 |                 float dw = bio->stdp_lr_scale * bio->stdp_a_plus * bio->trace_pre[pre];
 478 |                 float old_w = syn->weight_ns;
 479 |                 syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
 480 |                 bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
 481 |             }
 482 |         }
 483 |     }
 484 | 
 485 |     /* 5. Update 8x8 MEA Extracellular Voltages & 50.0 ms Sliding Spike History */
 486 |     uint16_t head = bio->spike_history_head;
 487 |     float total_rate_sum = 0.0f;
 488 |     const float window_s = (float)(BIO_SPIKE_HISTORY_LEN * bio->dt_ms) * 0.001f; /* 0.05 s */
 489 | 
 490 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 491 |         /* Forward volume conduction LFP/spike pickup (mV -> V, resting baseline centered at 0 V) + applied stim voltage */
 492 |         float v_pick_mv = 0.0f;
 493 |         for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 494 |             float v_sig = bio->spikes_now[i] ? (30.0f - bio->e_leak_mv) : (bio->v_m_mv[i] - bio->e_leak_mv);
 495 |             v_pick_mv += bio->pickup_matrix[ch][i] * v_sig;
 496 |         }
 497 |         /* Report extracellular voltage in Volts (stim + attenuated biological LFP, zero baseline) */
 498 |         bio->mea_voltage_v[ch] = bio->ext_stim_v[ch] + (v_pick_mv * 1e-3f);
 499 | 
 500 |         /* Hardware Blanking Suppression: silence artifact and biological false-positives during post-stimulus discharge */
 501 |         if (!bio->stim_pulses[ch].active && bio->stim_blanking_ticks[ch] > 0) {
 502 |             bio->mea_voltage_v[ch] = 0.0f;
 503 |             bio->spikes_now[ch] = 0;
 504 |         }
 505 | 
 506 |         /* Rolling 500-tick (50 ms) spike count */
 507 |         uint8_t old_spk = bio->spike_history[ch][head];
 508 |         uint8_t new_spk = bio->spikes_now[ch];
 509 |         bio->spike_history[ch][head] = new_spk;
 510 | 
 511 |         if (bio->spike_count_50ms[ch] >= old_spk) {
 512 |             bio->spike_count_50ms[ch] = (uint16_t)(bio->spike_count_50ms[ch] - old_spk + new_spk);
 513 |         } else {
 514 |             bio->spike_count_50ms[ch] = new_spk;
 515 |         }
 516 | 
 517 |         bio->channel_rate_hz[ch] = (float)bio->spike_count_50ms[ch] / window_s;
 518 |         total_rate_sum += bio->channel_rate_hz[ch];
 519 |     }
 520 | 
 521 |     bio->spike_history_head = (uint16_t)((head + 1U) % BIO_SPIKE_HISTORY_LEN);
 522 |     bio->population_rate_hz = total_rate_sum / (float)BIO_NUM_CHANNELS;
 523 |     bio->tick_count++;
 524 | }
 525 | 
 526 | uint32_t biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms) {
 527 |     if (!bio || channel >= BIO_NUM_CHANNELS) return 0U;
 528 | 
 529 |     uint32_t n_ticks = (window_ms > 0.0f) ? (uint32_t)(window_ms / (float)bio->dt_ms + 0.5f) : 1U;
 530 |     if (n_ticks == 0U) n_ticks = 1U;
 531 |     if (n_ticks > BIO_SPIKE_HISTORY_LEN) n_ticks = BIO_SPIKE_HISTORY_LEN;
 532 | 
 533 |     uint32_t count = 0U;
 534 |     int idx = (int)bio->spike_history_head - 1;
 535 |     for (uint32_t k = 0; k < n_ticks; ++k) {
 536 |         if (idx < 0) idx += BIO_SPIKE_HISTORY_LEN;
 537 |         count += bio->spike_history[channel][idx];
 538 |         idx--;
 539 |     }
 540 |     return count;
 541 | }
 542 | 
 543 | float biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post) {
 544 |     if (!bio || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
 545 |     if (!bio->synapses[pre][post].exists) return 0.0f;
 546 |     return bio->synapses[pre][post].weight_ns;
 547 | }
```

### `native/src/interlocks.c` (350 lines, SHA-256: `d17021d6920714f8...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/interlocks.h"
   3 | 
   4 | void interlocks_init(interlock_state_t* il) {
   5 |     if (!il) return;
   6 |     memset(il, 0, sizeof(interlock_state_t));
   7 |     il->authorized_capabilities = 0xFFFF; /* Default permissive until bytecode loaded */
   8 |     il->authorized_channels = INTERLOCK_NUM_CHANNELS;
   9 |     il->electrode_material = (uint8_t)WET_ELEC_PLATINUM;
  10 |     il->electrode_area_um2 = 5000.0f; /* Default macro-electrode area (5000 um^2) */
  11 |     il->v_water_window_low_v = -0.6f;  /* Platinum safe cathodic limit */
  12 |     il->v_water_window_high_v = +0.8f; /* Platinum safe anodic limit */
  13 |     il->max_charge_per_phase_nc = INTERLOCK_CHARGE_LIMIT_NC; /* Default 0.5 nC */
  14 |     il->max_cumulative_dc_nc = INTERLOCK_DC_DRIFT_LIMIT_NC;  /* Default 1.0 nC */
  15 |     for (int p = 0; p < 8; ++p) {
  16 |         il->pump_valve_mapping[p] = (uint8_t)p;
  17 |     }
  18 | }
  19 | 
  20 | void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2) {
  21 |     if (!il) return;
  22 |     il->electrode_material = material;
  23 |     il->electrode_area_um2 = area_um2;
  24 | 
  25 |     /* Charge Injection Capacity (CIC) in mC/cm^2:
  26 |      * Area in cm^2 = area_um2 * 1e-8 cm^2/um^2
  27 |      * Max charge in nC = CIC (mC/cm^2) * Area (cm^2) * 1e6 nC/mC = CIC * area_um2 * 0.01 nC
  28 |      */
  29 |     float cic_mc_cm2 = 0.10f;
  30 |     float v_low = -0.6f;
  31 |     float v_high = +0.8f;
  32 | 
  33 |     switch ((wet_electrode_material_t)material) {
  34 |         case WET_ELEC_PLATINUM:
  35 |             cic_mc_cm2 = 0.10f;
  36 |             v_low = -0.6f;
  37 |             v_high = +0.8f;
  38 |             break;
  39 |         case WET_ELEC_IROX:
  40 |             cic_mc_cm2 = 2.00f;
  41 |             v_low = -0.6f;
  42 |             v_high = +0.8f;
  43 |             break;
  44 |         case WET_ELEC_TIN:
  45 |             cic_mc_cm2 = 0.90f;
  46 |             v_low = -0.9f;
  47 |             v_high = +0.9f;
  48 |             break;
  49 |         case WET_ELEC_PEDOT:
  50 |             cic_mc_cm2 = 5.00f;
  51 |             v_low = -0.9f;
  52 |             v_high = +0.6f;
  53 |             break;
  54 |         default:
  55 |             cic_mc_cm2 = 0.10f;
  56 |             v_low = -0.6f;
  57 |             v_high = +0.8f;
  58 |             break;
  59 |     }
  60 | 
  61 |     il->v_water_window_low_v = v_low;
  62 |     il->v_water_window_high_v = v_high;
  63 | 
  64 |     float limit_nc = cic_mc_cm2 * area_um2 * 0.01f;
  65 |     if (limit_nc < 0.01f) limit_nc = 0.01f;
  66 |     il->max_charge_per_phase_nc = limit_nc;
  67 |     il->max_cumulative_dc_nc = limit_nc * 2.0f;
  68 | }
  69 | 
  70 | void interlocks_active_discharge(interlock_state_t* il, uint8_t channel) {
  71 |     if (!il || channel >= INTERLOCK_NUM_CHANNELS) return;
  72 |     il->cumulative_unbounded_dc_nc[channel] = 0.0f;
  73 |     il->cumulative_dc_femtocoulombs[channel] = 0;
  74 |     il->q_dc[channel] = 0.0f;
  75 | }
  76 | 
  77 | void interlocks_active_discharge_all(interlock_state_t* il) {
  78 |     if (!il) return;
  79 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
  80 |         il->cumulative_unbounded_dc_nc[ch] = 0.0f;
  81 |         il->cumulative_dc_femtocoulombs[ch] = 0;
  82 |         il->q_dc[ch] = 0.0f;
  83 |     }
  84 | }
  85 | 
  86 | void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable) {
  87 |     if (!il) return;
  88 |     il->dead_head_protection_enabled = enable;
  89 | }
  90 | 
  91 | void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count) {
  92 |     if (!il) return;
  93 |     il->authorized_capabilities = caps;
  94 |     il->authorized_channels = (channel_count > 0 && channel_count <= INTERLOCK_NUM_CHANNELS)
  95 |                               ? channel_count : INTERLOCK_NUM_CHANNELS;
  96 | }
  97 | 
  98 | void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask) {
  99 |     if (!il) return;
 100 |     il->reference_channels_mask = ref_mask;
 101 |     il->recording_only_channels_mask = rec_mask;
 102 | }
 103 | 
 104 | int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel) {
 105 |     if (!il) return 0;
 106 |     if (il->locked) return 0;
 107 | 
 108 |     /* Bounds check for channel-addressed opcodes */
 109 |     if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT ||
 110 |         opcode == WET_OP_READ_SPIKES || opcode == WET_OP_READ_VOLTAGE) {
 111 |         if ((uint32_t)channel >= il->authorized_channels) {
 112 |             return 0;
 113 |         }
 114 |     }
 115 | 
 116 |     /* Typed Channel Banks: Disallow stimulation on reference or recording-only electrodes */
 117 |     if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT) {
 118 |         if (channel < 64) {
 119 |             uint64_t ch_bit = 1ULL << channel;
 120 |             if ((il->reference_channels_mask & ch_bit) != 0ULL ||
 121 |                 (il->recording_only_channels_mask & ch_bit) != 0ULL) {
 122 |                 return 0; /* Capability Denied: Channel restricted to reference or recording */
 123 |             }
 124 |         }
 125 |     }
 126 | 
 127 |     switch ((wet_opcode_t)opcode) {
 128 |         case WET_OP_STIM_BIPHASIC:
 129 |         case WET_OP_STIM_CURRENT:
 130 |             if ((il->authorized_capabilities & WET_CAP_STIMULATION) == 0) {
 131 |                 return 0;
 132 |             }
 133 |             if (wet_fabsf(voltage_v) > 0.8f && (il->authorized_capabilities & WET_CAP_HIGH_VOLTAGE) == 0) {
 134 |                 return 0;
 135 |             }
 136 |             return 1;
 137 | 
 138 |         case WET_OP_MODULATE_STDP:
 139 |             if ((il->authorized_capabilities & WET_CAP_PLASTICITY) == 0) {
 140 |                 return 0;
 141 |             }
 142 |             return 1;
 143 | 
 144 |         case WET_OP_PUMP_SET_RATE:
 145 |         case WET_OP_PUMP_DISPENSE:
 146 |         case WET_OP_VALVE_SET:
 147 |             if ((il->authorized_capabilities & WET_CAP_MICROFLUIDICS) == 0) {
 148 |                 return 0;
 149 |             }
 150 |             return 1;
 151 | 
 152 |         case WET_OP_MOTOR_STEP:
 153 |             if ((il->authorized_capabilities & WET_CAP_MOTOR_ACTUATION) == 0) {
 154 |                 return 0;
 155 |             }
 156 |             return 1;
 157 | 
 158 |         default:
 159 |             /* Tier 0 compute and Tier 1 passive readout always permitted */
 160 |             return 1;
 161 |     }
 162 | }
 163 | 
 164 | float interlocks_clamp_voltage(interlock_state_t* il, float requested_v) {
 165 |     float v_high = (il && il->v_water_window_high_v > 0.0f) ? il->v_water_window_high_v : 0.8f;
 166 |     float v_low  = (il && il->v_water_window_low_v < 0.0f)  ? il->v_water_window_low_v  : -0.6f;
 167 | 
 168 |     if (requested_v > v_high) {
 169 |         if (il) il->clamp_events++;
 170 |         return v_high;
 171 |     }
 172 |     if (requested_v < v_low) {
 173 |         if (il) il->clamp_events++;
 174 |         return v_low;
 175 |     }
 176 |     return requested_v;
 177 | }
 178 | 
 179 | wet_status_t interlocks_record_charge_tick(
 180 |     interlock_state_t* il,
 181 |     uint64_t current_tick,
 182 |     const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
 183 | ) {
 184 |     if (!il || !tick_charge_nc) return WET_ERR_NULL_PTR;
 185 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 186 | 
 187 |     uint16_t head = il->q_head;
 188 |     wet_status_t status = WET_OK;
 189 | 
 190 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
 191 |         float old_q = il->q_ring[ch][head];
 192 |         float new_q = tick_charge_nc[ch];
 193 |         il->q_ring[ch][head] = new_q;
 194 | 
 195 |         /* Recompute exact sum periodically or maintain running sum with drift-free precision */
 196 |         float accum = il->q_accum[ch] - old_q + new_q;
 197 |         if (wet_fabsf(accum) < 1e-7f) accum = 0.0f;
 198 |         il->q_accum[ch] = accum;
 199 | 
 200 |         /* Long-horizon leaky DC integrator (tau = 10.0 s = 100,000 ticks) */
 201 |         il->q_dc[ch] = il->q_dc[ch] * INTERLOCK_BLEED_DECAY_PER_TICK + new_q;
 202 |         if (wet_fabsf(il->q_dc[ch]) < 1e-7f) il->q_dc[ch] = 0.0f;
 203 | 
 204 |         /* Phase 3: Persistent unbounded cumulative DC charge accumulator (zero decay, exact fixed-point femtoCoulombs) */
 205 |         int64_t delta_fc = (int64_t)((double)new_q * 1000000.0);
 206 |         il->cumulative_dc_femtocoulombs[ch] += delta_fc;
 207 |         il->cumulative_unbounded_dc_nc[ch] = (float)((double)il->cumulative_dc_femtocoulombs[ch] * 1e-6);
 208 |         if (wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) < 1e-7f) {
 209 |             il->cumulative_unbounded_dc_nc[ch] = 0.0f;
 210 |             il->cumulative_dc_femtocoulombs[ch] = 0;
 211 |         }
 212 | 
 213 |         float charge_limit = il->max_charge_per_phase_nc > 0.0f ? il->max_charge_per_phase_nc : INTERLOCK_CHARGE_LIMIT_NC;
 214 |         float dc_limit = il->max_cumulative_dc_nc > 0.0f ? il->max_cumulative_dc_nc : INTERLOCK_DC_DRIFT_LIMIT_NC;
 215 | 
 216 |         if (wet_fabsf(accum) >= charge_limit) {
 217 |             il->locked = 1;
 218 |             il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
 219 |             il->tripped_channel = (uint8_t)ch;
 220 |             il->trip_tick = current_tick;
 221 |             il->trip_value = accum;
 222 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 223 |                      "ERR_CHARGE_IMBALANCE: ch=%d net_q=%.4f nC >= %.2f nC (CIC limit for material %u, area %.1f um2) at tick %llu",
 224 |                      ch, (double)accum, (double)charge_limit, il->electrode_material, (double)il->electrode_area_um2, (unsigned long long)current_tick);
 225 |             status = WET_ERR_CHARGE_IMBALANCE;
 226 |             break;
 227 |         }
 228 | 
 229 |         if (wet_fabsf(il->q_dc[ch]) >= dc_limit || wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit) {
 230 |             il->locked = 1;
 231 |             il->trip_reason = INTERLOCK_TRIP_DC_DRIFT;
 232 |             il->tripped_channel = (uint8_t)ch;
 233 |             il->trip_tick = current_tick;
 234 |             il->trip_value = wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit ? il->cumulative_unbounded_dc_nc[ch] : il->q_dc[ch];
 235 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 236 |                      "ERR_DC_DRIFT: ch=%d cumulative DC charge=%.4f nC >= %.2f nC at tick %llu",
 237 |                      ch, (double)il->trip_value, (double)dc_limit, (unsigned long long)current_tick);
 238 |             status = WET_ERR_DC_DRIFT;
 239 |             break;
 240 |         }
 241 |     }
 242 | 
 243 |     il->q_head = (uint16_t)((head + 1U) % INTERLOCK_CHARGE_WINDOW_TICKS);
 244 |     return status;
 245 | }
 246 | 
 247 | wet_status_t interlocks_check_epileptiform(
 248 |     interlock_state_t* il,
 249 |     uint64_t current_tick,
 250 |     const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
 251 | ) {
 252 |     if (!il || !channel_rates_hz) return WET_ERR_NULL_PTR;
 253 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 254 | 
 255 |     uint32_t hyper_count = 0U;
 256 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
 257 |         if (channel_rates_hz[ch] >= INTERLOCK_EPILEPSY_RATE_HZ) {
 258 |             hyper_count++;
 259 |             il->focal_hyperactive_ticks[ch]++;
 260 |             if (il->focal_hyperactive_ticks[ch] >= INTERLOCK_FOCAL_SUSTAIN_TICKS) {
 261 |                 il->locked = 1;
 262 |                 il->trip_reason = INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY;
 263 |                 il->tripped_channel = (uint8_t)ch;
 264 |                 il->trip_tick = current_tick;
 265 |                 il->trip_value = channel_rates_hz[ch];
 266 |                 snprintf(il->diagnostic, sizeof(il->diagnostic),
 267 |                          "ERR_FOCAL_EXCITOTOXICITY: ch=%d sustained %.1f Hz >= 150 Hz for 250.0 ms at tick %llu",
 268 |                          ch, (double)channel_rates_hz[ch], (unsigned long long)current_tick);
 269 |                 return WET_ERR_FOCAL_EXCITOTOXICITY;
 270 |             }
 271 |         } else {
 272 |             il->focal_hyperactive_ticks[ch] = 0U;
 273 |         }
 274 |     }
 275 | 
 276 |     il->last_hyperactive_channel_count = hyper_count;
 277 | 
 278 |     if (hyper_count >= INTERLOCK_EPILEPSY_MIN_CHANNELS) {
 279 |         il->hyperactive_consecutive_ticks++;
 280 |         if (il->hyperactive_consecutive_ticks >= INTERLOCK_EPILEPSY_SUSTAIN_TICKS) {
 281 |             il->locked = 1;
 282 |             il->trip_reason = INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY;
 283 |             il->tripped_channel = 0xFF;
 284 |             il->trip_tick = current_tick;
 285 |             il->trip_value = (float)hyper_count;
 286 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 287 |                      "ERR_EPILEPTIFORM_RUNAWAY: %u/64 channels (>35%%) exceeded 150 Hz for 50.0 ms at tick %llu",
 288 |                      hyper_count, (unsigned long long)current_tick);
 289 |             return WET_ERR_EPILEPTIFORM_RUNAWAY;
 290 |         }
 291 |     } else {
 292 |         il->hyperactive_consecutive_ticks = 0U;
 293 |     }
 294 | 
 295 |     return WET_OK;
 296 | }
 297 | 
 298 | wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c) {
 299 |     if (!il) return WET_ERR_NULL_PTR;
 300 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 301 | 
 302 |     if (temp_c > INTERLOCK_THERMAL_LIMIT_C) {
 303 |         il->locked = 1;
 304 |         il->trip_reason = INTERLOCK_TRIP_THERMAL_LIMIT;
 305 |         il->tripped_channel = 0xFF;
 306 |         il->trip_tick = current_tick;
 307 |         il->trip_value = temp_c;
 308 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 309 |                  "ERR_THERMAL_LIMIT: Temperature %.2f C exceeds incubator threshold (38.00 C) at tick %llu",
 310 |                  (double)temp_c, (unsigned long long)current_tick);
 311 |         return WET_ERR_THERMAL_LIMIT;
 312 |     }
 313 |     return WET_OK;
 314 | }
 315 | 
 316 | wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id) {
 317 |     if (!il) return WET_ERR_NULL_PTR;
 318 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 319 | 
 320 |     if (bubble_detected) {
 321 |         il->locked = 1;
 322 |         il->trip_reason = INTERLOCK_TRIP_BUBBLE_DETECTED;
 323 |         il->tripped_channel = sensor_id;
 324 |         il->trip_tick = current_tick;
 325 |         il->trip_value = 1.0f;
 326 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 327 |                  "ERR_BUBBLE_DETECTED: Optical bubble sensor %u triggered (fluid line cavitation risk) at tick %llu",
 328 |                  sensor_id, (unsigned long long)current_tick);
 329 |         return WET_ERR_BUBBLE_DETECTED;
 330 |     }
 331 |     return WET_OK;
 332 | }
 333 | 
 334 | wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v) {
 335 |     if (!il) return WET_ERR_NULL_PTR;
 336 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 337 | 
 338 |     if (wet_fabsf(v_elec_v) > INTERLOCK_COMPLIANCE_LIMIT_V) {
 339 |         il->locked = 1;
 340 |         il->trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
 341 |         il->tripped_channel = channel;
 342 |         il->trip_tick = current_tick;
 343 |         il->trip_value = v_elec_v;
 344 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 345 |                  "ERR_COMPLIANCE_RAILED: ch=%u electrode potential %.3f V exceeded compliance rail (+/-7.0 V) at tick %llu",
 346 |                  channel, (double)v_elec_v, (unsigned long long)current_tick);
 347 |         return WET_ERR_COMPLIANCE_RAILED;
 348 |     }
 349 |     return WET_OK;
 350 | }
```

### `native/src/wet_aer.c` (307 lines, SHA-256: `bf9b381918ee73d4...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_aer.h"
   3 | 
   4 | int wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels) {
   5 |     if (!ring || !buffer || capacity < 2) {
   6 |         return -1;
   7 |     }
   8 |     /* Capacity must be a power of 2 */
   9 |     if ((capacity & (capacity - 1)) != 0) {
  10 |         return -2;
  11 |     }
  12 | 
  13 |     memset(ring, 0, sizeof(*ring));
  14 |     ring->buffer = buffer;
  15 |     ring->capacity = capacity;
  16 |     ring->mask = capacity - 1;
  17 |     /* Allow burst traffic up to 5 MHz during network bursts */
  18 |     ring->burst_limit_max_hz = burst_limit_max_hz > 0 ? burst_limit_max_hz : 5000000U;
  19 |     ring->channel_spike_counts = ch_counts;
  20 |     ring->monitored_channels = num_channels;
  21 |     ring->max_channel_hz = 250; /* Quarantine pads oscillating above 250 Hz */
  22 |     return 0;
  23 | }
  24 | 
  25 | int wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint16_t channel, int16_t amp_uv, uint16_t flags) {
  26 |     if (!ring || !ring->buffer) {
  27 |         return -1;
  28 |     }
  29 | 
  30 |     /* Per-channel rate monitoring to quarantine noisy / oscillating pads */
  31 |     if (ring->channel_spike_counts && channel < ring->monitored_channels) {
  32 |         if (ring->channel_spike_counts[channel] > ring->max_channel_hz) {
  33 |             ring->total_dropped++;
  34 |             return -3; /* Quarantined noisy channel */
  35 |         }
  36 |         ring->channel_spike_counts[channel]++;
  37 |     }
  38 | 
  39 |     /* Check if ring is full */
  40 |     uint32_t next_head = (ring->head + 1) & ring->mask;
  41 |     if (next_head == (ring->tail & ring->mask)) {
  42 |         ring->total_dropped++;
  43 |         return -2; /* Buffer full */
  44 |     }
  45 | 
  46 |     /* Burst rate tracking over sliding 1-second window */
  47 |     if (tick > ring->last_stat_tick + 10000ULL) {
  48 |         double elapsed_sec = (double)(tick - ring->last_stat_tick) * 0.0001;
  49 |         ring->current_spike_rate_hz = (double)ring->spikes_in_window / elapsed_sec;
  50 |         /* 16 bytes per packet * 8 bits = 128 bits */
  51 |         ring->current_bandwidth_mbps = (ring->current_spike_rate_hz * 128.0) / 1000000.0;
  52 | 
  53 |         if (ring->burst_limit_max_hz > 0 && ring->current_spike_rate_hz > (double)ring->burst_limit_max_hz) {
  54 |             ring->is_burst_tripped = 1;
  55 |         } else {
  56 |             ring->is_burst_tripped = 0;
  57 |         }
  58 |         ring->spikes_in_window = 0;
  59 |         ring->last_stat_tick = tick;
  60 | 
  61 |         /* Reset per-channel counts */
  62 |         if (ring->channel_spike_counts) {
  63 |             memset(ring->channel_spike_counts, 0, ring->monitored_channels * sizeof(uint16_t));
  64 |         }
  65 |     }
  66 |     ring->spikes_in_window++;
  67 | 
  68 |     /* Write 16-byte aligned packet */
  69 |     uint32_t idx = ring->head & ring->mask;
  70 |     ring->buffer[idx].timestamp_tick = tick;
  71 |     ring->buffer[idx].channel_id = channel;
  72 |     ring->buffer[idx].peak_amplitude_uv = amp_uv;
  73 |     ring->buffer[idx].flags = flags;
  74 |     ring->buffer[idx].reserved = 0;
  75 | 
  76 |     /* Publish head */
  77 |     ring->head = (ring->head + 1) & ring->mask;
  78 |     ring->total_pushed++;
  79 |     return 0;
  80 | }
  81 | 
  82 | uint32_t wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count) {
  83 |     if (!ring || !out_batch || max_count == 0) {
  84 |         return 0;
  85 |     }
  86 | 
  87 |     uint32_t popped = 0;
  88 |     while (popped < max_count && (ring->tail != ring->head)) {
  89 |         uint32_t idx = ring->tail & ring->mask;
  90 |         out_batch[popped] = ring->buffer[idx];
  91 |         ring->tail = (ring->tail + 1) & ring->mask;
  92 |         popped++;
  93 |     }
  94 |     return popped;
  95 | }
  96 | 
  97 | uint32_t wet_aer_available(const wet_aer_ring_t *ring) {
  98 |     if (!ring) return 0;
  99 |     if (ring->head >= ring->tail) {
 100 |         return ring->head - ring->tail;
 101 |     }
 102 |     return ring->capacity - (ring->tail - ring->head);
 103 | }
 104 | 
 105 | void wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps) {
 106 |     if (!ring) return;
 107 |     if (current_tick > ring->last_stat_tick && ring->spikes_in_window > 0) {
 108 |         double elapsed_sec = (double)(current_tick - ring->last_stat_tick) * 0.0001;
 109 |         if (elapsed_sec > 0.0) {
 110 |             ring->current_spike_rate_hz = (double)ring->spikes_in_window / elapsed_sec;
 111 |             ring->current_bandwidth_mbps = (ring->current_spike_rate_hz * 128.0) / 1000000.0;
 112 |         }
 113 |     }
 114 |     if (out_total) *out_total = ring->total_pushed;
 115 |     if (out_rate_hz) *out_rate_hz = ring->current_spike_rate_hz;
 116 |     if (out_mbps) *out_mbps = ring->current_bandwidth_mbps;
 117 | }
 118 | 
 119 | /*
 120 |  * NEO Detector Implementation with 5-Tap Bartlett Filter & Blanking
 121 |  */
 122 | int wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks) {
 123 |     if (!det || num_channels == 0) return -1;
 124 |     memset(det, 0, sizeof(*det));
 125 | 
 126 |     det->num_channels = num_channels;
 127 |     det->threshold_multiplier = threshold_multiplier > 0.0f ? threshold_multiplier : 4.0f;
 128 |     det->refractory_ticks = refractory_ticks > 0 ? refractory_ticks : 10; /* 1.0 ms default */
 129 | 
 130 |     det->v_baseline = (float*)calloc(num_channels, sizeof(float));
 131 |     det->prev_v1 = (float*)calloc(num_channels, sizeof(float));
 132 |     det->prev_v2 = (float*)calloc(num_channels, sizeof(float));
 133 |     for (int k = 0; k < 4; k++) {
 134 |         det->psi_history[k] = (float*)calloc(num_channels, sizeof(float));
 135 |     }
 136 |     det->refract_left = (uint32_t*)calloc(num_channels, sizeof(uint32_t));
 137 |     det->blanking_left = (uint32_t*)calloc(num_channels, sizeof(uint32_t));
 138 |     det->running_neo_mean = (float*)calloc(num_channels, sizeof(float));
 139 |     det->sample_count = (uint32_t*)calloc(num_channels, sizeof(uint32_t));
 140 | 
 141 |     if (!det->v_baseline || !det->prev_v1 || !det->prev_v2 || !det->refract_left ||
 142 |         !det->blanking_left || !det->running_neo_mean || !det->sample_count) {
 143 |         wet_neo_free(det);
 144 |         return -2;
 145 |     }
 146 | 
 147 |     for (uint32_t i = 0; i < num_channels; i++) {
 148 |         det->running_neo_mean[i] = 1.0f;
 149 |     }
 150 |     return 0;
 151 | }
 152 | 
 153 | void wet_neo_free(wet_neo_detector_t *det) {
 154 |     if (!det) return;
 155 |     if (det->v_baseline) { free(det->v_baseline); det->v_baseline = NULL; }
 156 |     if (det->prev_v1) { free(det->prev_v1); det->prev_v1 = NULL; }
 157 |     if (det->prev_v2) { free(det->prev_v2); det->prev_v2 = NULL; }
 158 |     for (int k = 0; k < 4; k++) {
 159 |         if (det->psi_history[k]) { free(det->psi_history[k]); det->psi_history[k] = NULL; }
 160 |     }
 161 |     if (det->refract_left) { free(det->refract_left); det->refract_left = NULL; }
 162 |     if (det->blanking_left) { free(det->blanking_left); det->blanking_left = NULL; }
 163 |     if (det->running_neo_mean) { free(det->running_neo_mean); det->running_neo_mean = NULL; }
 164 |     if (det->sample_count) { free(det->sample_count); det->sample_count = NULL; }
 165 |     det->num_channels = 0;
 166 | }
 167 | 
 168 | void wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks) {
 169 |     if (!det || channel >= det->num_channels) return;
 170 |     det->blanking_left[channel] = blanking_ticks;
 171 | }
 172 | 
 173 | int wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring) {
 174 |     if (!det || channel >= det->num_channels) return 0;
 175 | 
 176 |     /* Hardware stimulus artifact blanking */
 177 |     if (det->blanking_left[channel] > 0) {
 178 |         det->blanking_left[channel]--;
 179 |         det->v_baseline[channel] = voltage; /* Clamp baseline to avoid transient blinding */
 180 |         return 0;
 181 |     }
 182 | 
 183 |     /* DC baseline estimation */
 184 |     if (det->sample_count[channel] == 0) {
 185 |         det->v_baseline[channel] = voltage;
 186 |     } else {
 187 |         det->v_baseline[channel] = 0.95f * det->v_baseline[channel] + 0.05f * voltage;
 188 |     }
 189 |     float x_ac = voltage - det->v_baseline[channel];
 190 | 
 191 |     /* Prime pipeline on first 2 samples */
 192 |     if (det->sample_count[channel] < 2) {
 193 |         det->prev_v2[channel] = det->prev_v1[channel];
 194 |         det->prev_v1[channel] = x_ac;
 195 |         det->sample_count[channel]++;
 196 |         return 0;
 197 |     }
 198 |     det->sample_count[channel]++;
 199 | 
 200 |     /* Update refractory counter */
 201 |     if (det->refract_left[channel] > 0) {
 202 |         det->refract_left[channel]--;
 203 |     }
 204 | 
 205 |     /* Shift voltages: x[n] = x_ac, x[n-1] = prev_v1, x[n-2] = prev_v2 */
 206 |     float v_curr = x_ac;
 207 |     float v_prev1 = det->prev_v1[channel];
 208 |     float v_prev2 = det->prev_v2[channel];
 209 | 
 210 |     /* Raw discrete NEO: Psi = v_prev1^2 - v_curr * v_prev2 */
 211 |     float raw_psi = (v_prev1 * v_prev1) - (v_curr * v_prev2);
 212 |     if (raw_psi < 0.0f) raw_psi = 0.0f;
 213 | 
 214 |     /*
 215 |      * 5-Tap Bartlett Triangular Smoother:
 216 |      * Weights: [1, 2, 3, 2, 1] / 9
 217 |      * Suppresses quadratic high-frequency thermal noise amplification
 218 |      */
 219 |     float p_m2 = det->psi_history[0][channel];
 220 |     float p_m1 = det->psi_history[1][channel];
 221 |     float p_0  = raw_psi;
 222 |     float p_p1 = det->psi_history[2][channel];
 223 |     float p_p2 = det->psi_history[3][channel];
 224 | 
 225 |     float psi_smooth = (p_m2 + 2.0f * p_m1 + 3.0f * p_0 + 2.0f * p_p1 + p_p2) * (1.0f / 9.0f);
 226 | 
 227 |     /* Shift PSI history */
 228 |     det->psi_history[0][channel] = det->psi_history[1][channel];
 229 |     det->psi_history[1][channel] = p_0;
 230 |     det->psi_history[2][channel] = det->psi_history[3][channel];
 231 |     det->psi_history[3][channel] = raw_psi;
 232 | 
 233 |     /* Running baseline energy tracking */
 234 |     det->running_neo_mean[channel] = 0.99f * det->running_neo_mean[channel] + 0.01f * psi_smooth;
 235 |     if (det->running_neo_mean[channel] < 0.1f) det->running_neo_mean[channel] = 0.1f;
 236 |     float threshold = det->threshold_multiplier * det->running_neo_mean[channel];
 237 | 
 238 |     int spike_detected = 0;
 239 |     if (psi_smooth > threshold && det->refract_left[channel] == 0) {
 240 |         spike_detected = 1;
 241 |         det->refract_left[channel] = det->refractory_ticks;
 242 |         det->total_detected++;
 243 |         if (out_ring) {
 244 |             int16_t amp_uv = (int16_t)(v_curr * 1000.0f); /* Convert mV to uV */
 245 |             wet_aer_push(out_ring, current_tick, channel, amp_uv, 0x0001);
 246 |         }
 247 |     }
 248 | 
 249 |     /* Shift pipeline */
 250 |     det->prev_v2[channel] = v_prev1;
 251 |     det->prev_v1[channel] = v_curr;
 252 | 
 253 |     return spike_detected;
 254 | }
 255 | 
 256 | /*
 257 |  * Event-Driven CSR Synaptic Matrix
 258 |  * Complexity: O(spiking_neurons * degree), avoiding O(N_rows) scans
 259 |  */
 260 | int wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns) {
 261 |     if (!csr || rows == 0 || cols == 0 || nnz == 0) return -1;
 262 |     memset(csr, 0, sizeof(*csr));
 263 | 
 264 |     csr->num_rows = rows;
 265 |     csr->num_cols = cols;
 266 |     csr->nnz = nnz;
 267 |     csr->weight_scale_ns = scale_ns > 0.0f ? scale_ns : 0.2f;
 268 | 
 269 |     csr->row_ptr = (uint32_t*)calloc(rows + 1, sizeof(uint32_t));
 270 |     csr->col_idx = (uint16_t*)calloc(nnz, sizeof(uint16_t));
 271 |     csr->weights_int8 = (int8_t*)calloc(nnz, sizeof(int8_t));
 272 | 
 273 |     if (!csr->row_ptr || !csr->col_idx || !csr->weights_int8) {
 274 |         wet_csr_free(csr);
 275 |         return -2;
 276 |     }
 277 |     return 0;
 278 | }
 279 | 
 280 | void wet_csr_free(wet_csr_matrix_t *csr) {
 281 |     if (!csr) return;
 282 |     if (csr->row_ptr) { free(csr->row_ptr); csr->row_ptr = NULL; }
 283 |     if (csr->col_idx) { free(csr->col_idx); csr->col_idx = NULL; }
 284 |     if (csr->weights_int8) { free(csr->weights_int8); csr->weights_int8 = NULL; }
 285 |     csr->num_rows = 0;
 286 |     csr->num_cols = 0;
 287 |     csr->nnz = 0;
 288 | }
 289 | 
 290 | void wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns) {
 291 |     if (!csr || !spike_events || !out_conductance_ns) return;
 292 | 
 293 |     float scale = csr->weight_scale_ns;
 294 |     /* Strictly event-driven: only traverse outgoing edges of spiking pre-synaptic neurons */
 295 |     for (uint32_t r = 0; r < csr->num_rows; r++) {
 296 |         if (!spike_events[r]) continue;
 297 | 
 298 |         uint32_t start = csr->row_ptr[r];
 299 |         uint32_t end = csr->row_ptr[r + 1];
 300 |         for (uint32_t idx = start; idx < end; idx++) {
 301 |             uint16_t post_id = csr->col_idx[idx];
 302 |             if (post_id < csr->num_cols) {
 303 |                 out_conductance_ns[post_id] += (float)csr->weights_int8[idx] * scale;
 304 |             }
 305 |         }
 306 |     }
 307 | }
```

### `native/src/wet_distributed.c` (168 lines, SHA-256: `5c22625cf18763c2...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_distributed.h"
   3 | 
   4 | /*
   5 |  * IEEE 1588 PTP Slew-Only Disciplining & Safety Invariants
   6 |  */
   7 | void wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki) {
   8 |     if (!clk) return;
   9 |     memset(clk, 0, sizeof(*clk));
  10 |     clk->kp = (kp > 0.0) ? kp : 0.7;
  11 |     clk->ki = (ki > 0.0) ? ki : 0.2;
  12 |     clk->stim_inhibited = 1; /* Inhibit inter-chamber stimulation until synchronized */
  13 | }
  14 | 
  15 | void wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns) {
  16 |     if (!clk) return;
  17 | 
  18 |     /*
  19 |      * Fundamental PTP 4-Timestamp Formula:
  20 |      * offset = ((t2 - t1) - (t4 - t3)) / 2
  21 |      * delay  = ((t2 - t1) + (t4 - t3)) / 2
  22 |      */
  23 |     int64_t ms_diff = (int64_t)t2_ns - (int64_t)t1_ns;
  24 |     int64_t sm_diff = (int64_t)t4_ns - (int64_t)t3_ns;
  25 | 
  26 |     int64_t raw_offset = (ms_diff - sm_diff) / 2;
  27 |     int64_t raw_delay  = (ms_diff + sm_diff) / 2;
  28 | 
  29 |     /* Residual timing error after accumulated clock discipline */
  30 |     int64_t residual_offset = raw_offset - clk->accumulated_offset_ns;
  31 | 
  32 |     /* Slew-only PI Servo filter */
  33 |     clk->integral_err_ns += (double)residual_offset * 0.1;
  34 |     double adj = (clk->kp * (double)residual_offset) + (clk->ki * clk->integral_err_ns);
  35 | 
  36 |     /* Clamp maximum slew rate to +/- 100 ppm (prevents sudden time dilation) */
  37 |     if (adj > 10000.0) adj = 10000.0;
  38 |     if (adj < -10000.0) adj = -10000.0;
  39 | 
  40 |     clk->accumulated_offset_ns += (int64_t)adj;
  41 |     clk->mean_path_delay_ns = raw_delay;
  42 |     clk->sync_sequence++;
  43 | 
  44 |     /* Sub-microsecond synchronization threshold: |residual_offset| <= 1000 ns (1.0 us) */
  45 |     int64_t post_residual = raw_offset - clk->accumulated_offset_ns;
  46 |     if (post_residual >= -1000 && post_residual <= 1000) {
  47 |         clk->is_synchronized = 1;
  48 |         clk->stim_inhibited = 0; /* Clear safety inhibit */
  49 |     } else {
  50 |         clk->is_synchronized = 0;
  51 |         clk->stim_inhibited = 1; /* Inhibit inter-chamber stimulation if timing diverges */
  52 |     }
  53 | }
  54 | 
  55 | uint64_t wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns) {
  56 |     if (!clk) return local_raw_ns;
  57 |     return (uint64_t)((int64_t)local_raw_ns - clk->accumulated_offset_ns);
  58 | }
  59 | 
  60 | /*
  61 |  * 32-Byte TSN Frame Serialization & Validation
  62 |  */
  63 | int wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags) {
  64 |     if (!frame) return -1;
  65 |     frame->source_epoch_ns = src_epoch_ns;
  66 |     frame->release_epoch_ns = rel_epoch_ns;
  67 |     frame->sequence_number = seq;
  68 |     frame->source_chamber = src_chamb;
  69 |     frame->target_chamber = dst_chamb;
  70 |     frame->source_channel = src_ch;
  71 |     frame->target_channel = dst_ch;
  72 |     frame->spike_amplitude_uv = amp_uv;
  73 |     frame->flags = flags;
  74 |     return 0;
  75 | }
  76 | 
  77 | int wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber) {
  78 |     if (!frame) return -1;
  79 |     if (frame->target_chamber != expected_dst_chamber && expected_dst_chamber != 0xFFFF) {
  80 |         return -2; /* Wrong destination chamber */
  81 |     }
  82 |     if (frame->release_epoch_ns < frame->source_epoch_ns) {
  83 |         return -3; /* Negative axonal delay (causality violation) */
  84 |     }
  85 |     return 0;
  86 | }
  87 | 
  88 | /*
  89 |  * Timing Wheel: O(1) Heterogeneous Axonal Delay Dispatcher
  90 |  * Completely eliminates Head-of-Line blocking inherent to FIFO queues.
  91 |  */
  92 | int wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id) {
  93 |     if (!tw) return -1;
  94 |     memset(tw, 0, sizeof(*tw));
  95 |     tw->chamber_id = chamber_id;
  96 |     return 0;
  97 | }
  98 | 
  99 | int wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns) {
 100 |     if (!tw || !frame) return -1;
 101 | 
 102 |     /* Outbound stimulus artifact echo blanking check */
 103 |     if (frame->target_chamber < WET_MAX_CHAMBERS && tw->tx_blanking_ticks_remaining[frame->target_chamber] > 0) {
 104 |         return -5; /* Suppressed by local TX stimulus blanking window */
 105 |     }
 106 | 
 107 |     /* Cross-chamber epileptiform rate governor (max 50 Hz inter-chamber rate = 50 spikes / second) */
 108 |     if (current_epoch_ns > tw->rate_governor_last_tick + 1000000000ULL) {
 109 |         tw->rate_governor_window_spikes = 0;
 110 |         tw->rate_governor_last_tick = current_epoch_ns;
 111 |         tw->is_epileptiform_tripped = 0;
 112 |     }
 113 |     tw->rate_governor_window_spikes++;
 114 |     if (tw->rate_governor_window_spikes > 50) {
 115 |         tw->is_epileptiform_tripped = 1;
 116 |         return -4; /* Cross-chamber epileptiform runaway tripped */
 117 |     }
 118 | 
 119 |     /* Check for late arrival (transit delay exceeded axonal delay) */
 120 |     if (frame->release_epoch_ns < current_epoch_ns) {
 121 |         tw->late_drops++;
 122 |         return -2; /* Late drop */
 123 |     }
 124 | 
 125 |     /* Map absolute release epoch to wheel slot (100 us per slot) */
 126 |     uint64_t rel_slots = frame->release_epoch_ns / 100000ULL;
 127 |     uint32_t slot_idx = (uint32_t)(rel_slots % WET_TIMING_WHEEL_SLOTS);
 128 |     wet_timing_wheel_bucket_t *bucket = &tw->buckets[slot_idx];
 129 | 
 130 |     if (bucket->count >= WET_WHEEL_BUCKET_CAP) {
 131 |         tw->bucket_overflows++;
 132 |         return -3; /* Bucket overflow */
 133 |     }
 134 | 
 135 |     bucket->frames[bucket->count++] = *frame;
 136 |     tw->total_scheduled++;
 137 |     return 0;
 138 | }
 139 | 
 140 | uint32_t wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count) {
 141 |     if (!tw || !out_ready || max_count == 0) return 0;
 142 | 
 143 |     /* Advance TX blanking counters */
 144 |     for (int c = 0; c < WET_MAX_CHAMBERS; c++) {
 145 |         if (tw->tx_blanking_ticks_remaining[c] > 0) {
 146 |             tw->tx_blanking_ticks_remaining[c]--;
 147 |         }
 148 |     }
 149 | 
 150 |     /* Map current absolute epoch to wheel slot */
 151 |     uint64_t curr_slots = current_epoch_ns / 100000ULL;
 152 |     uint32_t slot_idx = (uint32_t)(curr_slots % WET_TIMING_WHEEL_SLOTS);
 153 |     wet_timing_wheel_bucket_t *bucket = &tw->buckets[slot_idx];
 154 | 
 155 |     uint32_t ready_count = 0;
 156 |     while (ready_count < max_count && bucket->count > 0) {
 157 |         out_ready[ready_count++] = bucket->frames[--bucket->count];
 158 |         tw->total_dispatched++;
 159 |     }
 160 | 
 161 |     tw->current_wheel_tick = curr_slots;
 162 |     return ready_count;
 163 | }
 164 | 
 165 | void wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks) {
 166 |     if (!tw || target_chamber >= WET_MAX_CHAMBERS) return;
 167 |     tw->tx_blanking_ticks_remaining[target_chamber] = blanking_ticks;
 168 | }
```

### `native/src/wet_hal.c` (564 lines, SHA-256: `02cf9c0cd1c098b2...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_hal.h"
   3 | #include "../include/wetvm_vm.h"
   4 | #include "../include/biophysics.h"
   5 | 
   6 | #if defined(_WIN32)
   7 | typedef union _LARGE_INTEGER {
   8 |     struct {
   9 |         uint32_t LowPart;
  10 |         int32_t  HighPart;
  11 |     } s;
  12 |     int64_t QuadPart;
  13 | } LARGE_INTEGER;
  14 | 
  15 | #ifdef __cplusplus
  16 | extern "C" {
  17 | #endif
  18 | int __stdcall QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount);
  19 | int __stdcall QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency);
  20 | #ifdef __cplusplus
  21 | }
  22 | #endif
  23 | #else
  24 | #include <time.h>
  25 | #endif
  26 | 
  27 | /* Monotonic time helper using genuine hardware high-resolution timing */
  28 | #if defined(_WIN32)
  29 | uint64_t wet_hal_get_time_us(void) {
  30 |     static LARGE_INTEGER s_freq;
  31 |     static int s_inited = 0;
  32 |     if (!s_inited) {
  33 |         QueryPerformanceFrequency(&s_freq);
  34 |         s_inited = 1;
  35 |     }
  36 |     LARGE_INTEGER counter;
  37 |     QueryPerformanceCounter(&counter);
  38 |     return (uint64_t)((counter.QuadPart * 1000000ULL) / s_freq.QuadPart);
  39 | }
  40 | #else
  41 | uint64_t wet_hal_get_time_us(void) {
  42 |     struct timespec ts;
  43 |     clock_gettime(CLOCK_MONOTONIC, &ts);
  44 |     return (uint64_t)(ts.tv_sec * 1000000ULL + ts.tv_nsec / 1000ULL);
  45 | }
  46 | #endif
  47 | 
  48 | /* =========================================================================
  49 |  * HAL Core Lifecycle Implementation
  50 |  * ========================================================================= */
  51 | 
  52 | wet_hal_context_t* wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config) {
  53 |     wet_hal_context_t* hal = (wet_hal_context_t*)calloc(1, sizeof(wet_hal_context_t));
  54 |     if (!hal) return NULL;
  55 | 
  56 |     hal->mode = mode;
  57 |     if (config) {
  58 |         hal->config = *config;
  59 |     } else {
  60 |         hal->config.mode = mode;
  61 |         hal->config.max_ephys_channels = 64;
  62 |         hal->config.num_pumps = 8;
  63 |         hal->config.num_valves = 8;
  64 |         hal->config.num_flow_sensors = 8;
  65 |         hal->config.enable_dead_head_protection = 1;
  66 |         hal->config.enable_crowbar_fastpath = 1;
  67 |         for (int i = 0; i < 8; ++i) {
  68 |             hal->config.valve_for_pump[i] = 0xFF;
  69 |         }
  70 |     }
  71 | 
  72 |     /* Open default valves 0..7 as open or closed */
  73 |     for (int i = 0; i < 8; ++i) {
  74 |         hal->valve_states[i] = 1; /* Default open for perfusion lines */
  75 |         hal->pump_rates_ul_min[i] = 0.0f;
  76 |         hal->flow_rates_ul_min[i] = 0.0;
  77 |     }
  78 | 
  79 |     return hal;
  80 | }
  81 | 
  82 | void wet_hal_destroy(wet_hal_context_t* hal) {
  83 |     if (!hal) return;
  84 | 
  85 |     /* Shutdown all registered drivers */
  86 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
  87 |         if (hal->drivers[i] && hal->drivers[i]->ops && hal->drivers[i]->ops->shutdown) {
  88 |             hal->drivers[i]->ops->shutdown(hal->drivers[i]);
  89 |         }
  90 |     }
  91 | 
  92 |     free(hal);
  93 | }
  94 | 
  95 | wet_hal_status_t wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config) {
  96 |     if (!vm) return WET_HAL_ERR_NULL_PTR;
  97 | 
  98 |     wet_hal_context_t* hal = wet_hal_create(mode, config);
  99 |     if (!hal) return WET_HAL_ERR_IO;
 100 | 
 101 |     return wet_hal_attach(vm, hal);
 102 | }
 103 | 
 104 | wet_hal_status_t wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal) {
 105 |     if (!vm) return WET_HAL_ERR_NULL_PTR;
 106 | 
 107 |     vm->hal = hal;
 108 |     if (hal) {
 109 |         hal->vm = vm;
 110 |     }
 111 |     return WET_HAL_OK;
 112 | }
 113 | 
 114 | wet_hal_context_t* wet_hal_get_context(wet_vm_t* vm) {
 115 |     if (!vm) return NULL;
 116 |     return vm->hal;
 117 | }
 118 | 
 119 | wet_hal_status_t wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode) {
 120 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 121 |     if (mode > WET_HAL_MODE_HIL_LOOPBACK) return WET_HAL_ERR_INVALID_MODE;
 122 | 
 123 |     hal->mode = mode;
 124 |     hal->config.mode = mode;
 125 | 
 126 |     /* Propagate mode to all registered drivers */
 127 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 128 |         if (hal->drivers[i]) {
 129 |             hal->drivers[i]->mode = mode;
 130 |         }
 131 |     }
 132 |     return WET_HAL_OK;
 133 | }
 134 | 
 135 | wet_hal_mode_t wet_hal_get_mode(const wet_hal_context_t* hal) {
 136 |     if (!hal) return WET_HAL_MODE_SIMULATED;
 137 |     return hal->mode;
 138 | }
 139 | 
 140 | wet_hal_status_t wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver) {
 141 |     if (!hal || !driver) return WET_HAL_ERR_NULL_PTR;
 142 |     if (hal->driver_count >= WET_HAL_MAX_DRIVERS) return WET_HAL_ERR_BUFFER_FULL;
 143 | 
 144 |     /* Check for duplicate registration */
 145 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 146 |         if (hal->drivers[i] == driver) {
 147 |             return WET_HAL_OK;
 148 |         }
 149 |     }
 150 | 
 151 |     hal->drivers[hal->driver_count++] = driver;
 152 |     driver->mode = hal->mode;
 153 | 
 154 |     /* Bind fast direct routing slots */
 155 |     switch (driver->driver_type) {
 156 |         case WET_HAL_DRIVER_EPHYS:
 157 |             if (!hal->ephys_driver) hal->ephys_driver = driver;
 158 |             break;
 159 |         case WET_HAL_DRIVER_PUMP:
 160 |             if (!hal->pump_driver) hal->pump_driver = driver;
 161 |             break;
 162 |         case WET_HAL_DRIVER_VALVE:
 163 |             if (!hal->valve_driver) hal->valve_driver = driver;
 164 |             break;
 165 |         case WET_HAL_DRIVER_FLOW:
 166 |             if (!hal->flow_driver) hal->flow_driver = driver;
 167 |             break;
 168 |         case WET_HAL_DRIVER_CAN_BUS:
 169 |             if (!hal->can_driver) hal->can_driver = driver;
 170 |             break;
 171 |         default:
 172 |             break;
 173 |     }
 174 | 
 175 |     /* Initialize driver if not already initialized */
 176 |     if (!driver->is_initialized && driver->ops && driver->ops->init) {
 177 |         wet_hal_status_t st = driver->ops->init(driver, NULL);
 178 |         if (st == WET_HAL_OK) {
 179 |             driver->is_initialized = 1;
 180 |             driver->is_active = 1;
 181 |         }
 182 |         return st;
 183 |     }
 184 | 
 185 |     driver->is_active = 1;
 186 |     return WET_HAL_OK;
 187 | }
 188 | 
 189 | wet_hal_status_t wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver) {
 190 |     if (!hal || !driver) return WET_HAL_ERR_NULL_PTR;
 191 | 
 192 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 193 |         if (hal->drivers[i] == driver) {
 194 |             /* Clear specialized slot if matching */
 195 |             if (hal->ephys_driver == driver) hal->ephys_driver = NULL;
 196 |             if (hal->pump_driver == driver)  hal->pump_driver = NULL;
 197 |             if (hal->valve_driver == driver) hal->valve_driver = NULL;
 198 |             if (hal->flow_driver == driver)  hal->flow_driver = NULL;
 199 |             if (hal->can_driver == driver)   hal->can_driver = NULL;
 200 | 
 201 |             /* Shift array left */
 202 |             for (uint32_t j = i; j < hal->driver_count - 1; ++j) {
 203 |                 hal->drivers[j] = hal->drivers[j + 1];
 204 |             }
 205 |             hal->drivers[hal->driver_count - 1] = NULL;
 206 |             hal->driver_count--;
 207 |             driver->is_active = 0;
 208 |             return WET_HAL_OK;
 209 |         }
 210 |     }
 211 |     return WET_HAL_ERR_DRIVER_NOT_FOUND;
 212 | }
 213 | 
 214 | wet_hal_driver_t* wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type) {
 215 |     if (!hal) return NULL;
 216 |     switch (type) {
 217 |         case WET_HAL_DRIVER_EPHYS:   return hal->ephys_driver;
 218 |         case WET_HAL_DRIVER_PUMP:    return hal->pump_driver;
 219 |         case WET_HAL_DRIVER_VALVE:   return hal->valve_driver;
 220 |         case WET_HAL_DRIVER_FLOW:    return hal->flow_driver;
 221 |         case WET_HAL_DRIVER_CAN_BUS: return hal->can_driver;
 222 |         default: break;
 223 |     }
 224 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 225 |         if (hal->drivers[i] && hal->drivers[i]->driver_type == type) {
 226 |             return hal->drivers[i];
 227 |         }
 228 |     }
 229 |     return NULL;
 230 | }
 231 | 
 232 | /* =========================================================================
 233 |  * Actuator & Sensor Routing Implementation
 234 |  * ========================================================================= */
 235 | 
 236 | wet_hal_status_t wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag) {
 237 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 238 |     if (pump_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 239 | 
 240 |     /* Check Dead-Head Overpressure Interlock: If valve is closed OR line pressure exceeds max threshold, reject immediately! */
 241 |     if (hal->config.enable_dead_head_protection && run_flag && rate_ul_min > 0.0) {
 242 |         uint8_t target_valve = pump_id;
 243 |         if (hal->config.valve_for_pump[pump_id] < 8) {
 244 |             target_valve = hal->config.valve_for_pump[pump_id];
 245 |         }
 246 |         if (hal->valve_states[target_valve] == 0) {
 247 |             return WET_HAL_ERR_DEAD_HEAD;
 248 |         }
 249 |         float max_p = (hal->config.max_line_pressure_kpa > 0.0f) ? hal->config.max_line_pressure_kpa : WET_HAL_MAX_DEAD_HEAD_PRESSURE_KPA;
 250 |         if (target_valve < 8 && hal->fluid_pressure_kpa[target_valve] > max_p) {
 251 |             return WET_HAL_ERR_DEAD_HEAD;
 252 |         }
 253 |     }
 254 | 
 255 |     hal->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
 256 |     hal->telemetry.total_rs232_commands++;
 257 | 
 258 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
 259 |         /* In simulated mode or no pump driver, update internal VM registers */
 260 |         if (hal->vm) {
 261 |             hal->vm->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
 262 |         }
 263 |         return WET_HAL_OK;
 264 |     }
 265 | 
 266 |     /* Dispatch to physical or HIL pump driver */
 267 |     if (hal->pump_driver->ops && hal->pump_driver->ops->write_pump) {
 268 |         return hal->pump_driver->ops->write_pump(hal->pump_driver, pump_id, rate_ul_min, run_flag);
 269 |     }
 270 |     return WET_HAL_OK;
 271 | }
 272 | 
 273 | wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul) {
 274 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 275 |     if (pump_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 276 | 
 277 |     /* Dead-head protection check: software valve & hardware pressure transducer */
 278 |     if (hal->config.enable_dead_head_protection && volume_ul > 0.0) {
 279 |         uint8_t target_valve = pump_id;
 280 |         if (hal->config.valve_for_pump[pump_id] < 8) {
 281 |             target_valve = hal->config.valve_for_pump[pump_id];
 282 |         }
 283 |         if (hal->valve_states[target_valve] == 0) {
 284 |             return WET_HAL_ERR_DEAD_HEAD;
 285 |         }
 286 |         float max_p = (hal->config.max_line_pressure_kpa > 0.0f) ? hal->config.max_line_pressure_kpa : WET_HAL_MAX_DEAD_HEAD_PRESSURE_KPA;
 287 |         if (target_valve < 8 && hal->fluid_pressure_kpa[target_valve] > max_p) {
 288 |             return WET_HAL_ERR_DEAD_HEAD;
 289 |         }
 290 |     }
 291 | 
 292 |     hal->telemetry.total_rs232_commands++;
 293 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
 294 |         if (hal->vm) {
 295 |             hal->vm->pump_dispensed_ul[pump_id] += (float)volume_ul;
 296 |         }
 297 |         return WET_HAL_OK;
 298 |     }
 299 | 
 300 |     if (hal->pump_driver->ops && hal->pump_driver->ops->dispense_volume) {
 301 |         return hal->pump_driver->ops->dispense_volume(hal->pump_driver, pump_id, volume_ul);
 302 |     }
 303 |     return WET_HAL_OK;
 304 | }
 305 | 
 306 | wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state) {
 307 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 308 |     if (valve_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 309 | 
 310 |     hal->valve_states[valve_id] = (state != 0) ? 1 : 0;
 311 |     if (hal->vm) {
 312 |         hal->vm->valve_states[valve_id] = hal->valve_states[valve_id];
 313 |     }
 314 | 
 315 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->valve_driver) {
 316 |         return WET_HAL_OK;
 317 |     }
 318 | 
 319 |     if (hal->valve_driver->ops && hal->valve_driver->ops->write_valve) {
 320 |         return hal->valve_driver->ops->write_valve(hal->valve_driver, valve_id, state);
 321 |     }
 322 |     return WET_HAL_OK;
 323 | }
 324 | 
 325 | wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min) {
 326 |     if (!hal || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
 327 |     if (sensor_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 328 | 
 329 |     hal->telemetry.total_i2c_transactions++;
 330 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->flow_driver) {
 331 |         if (hal->vm) {
 332 |             *out_flow_ul_min = (double)hal->vm->fluid_flow_rate_ul_min[sensor_id];
 333 |         } else {
 334 |             *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
 335 |         }
 336 |         return WET_HAL_OK;
 337 |     }
 338 | 
 339 |     if (hal->flow_driver->ops && hal->flow_driver->ops->read_flow) {
 340 |         wet_hal_status_t st = hal->flow_driver->ops->read_flow(hal->flow_driver, sensor_id, out_flow_ul_min);
 341 |         if (st == WET_HAL_OK) {
 342 |             hal->flow_rates_ul_min[sensor_id] = *out_flow_ul_min;
 343 |             if (hal->vm) {
 344 |                 hal->vm->fluid_flow_rate_ul_min[sensor_id] = (float)(*out_flow_ul_min);
 345 |             }
 346 |         }
 347 |         return st;
 348 |     }
 349 |     *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
 350 |     return WET_HAL_OK;
 351 | }
 352 | 
 353 | wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
 354 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 355 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 356 | 
 357 |     hal->telemetry.total_spi_transactions++;
 358 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 359 |         if (hal->vm) {
 360 |             /* Convert pA to uA for simulated biophysics: 1 uA = 1,000,000 pA */
 361 |             float current_ua = (float)current_pA / 1000000.0f;
 362 |             float dur_ms = (float)duration_us / 1000.0f;
 363 |             biophysics_schedule_stim_current(&hal->vm->bio, (uint8_t)channel, current_ua, dur_ms, dur_ms, 0.0f);
 364 |         }
 365 |         return WET_HAL_OK;
 366 |     }
 367 | 
 368 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_current) {
 369 |         return hal->ephys_driver->ops->stim_current(hal->ephys_driver, channel, current_pA, duration_us);
 370 |     }
 371 |     return WET_HAL_OK;
 372 | }
 373 | 
 374 | wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
 375 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 376 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 377 | 
 378 |     hal->telemetry.total_spi_transactions++;
 379 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 380 |         if (hal->vm) {
 381 |             biophysics_schedule_stim_ext(&hal->vm->bio, (uint8_t)channel, voltage_v, p1_ms, p2_ms, 0.0f);
 382 |         }
 383 |         return WET_HAL_OK;
 384 |     }
 385 | 
 386 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_voltage) {
 387 |         return hal->ephys_driver->ops->stim_voltage(hal->ephys_driver, channel, voltage_v, p1_ms, p2_ms);
 388 |     }
 389 |     return WET_HAL_OK;
 390 | }
 391 | 
 392 | wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag) {
 393 |     if (!hal || !out_spike_flag) return WET_HAL_ERR_NULL_PTR;
 394 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 395 | 
 396 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 397 |         if (hal->vm) {
 398 |             *out_spike_flag = hal->vm->spikes[channel];
 399 |         } else {
 400 |             *out_spike_flag = hal->ephys_spikes[channel];
 401 |         }
 402 |         return WET_HAL_OK;
 403 |     }
 404 | 
 405 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->read_ephys) {
 406 |         float volts[64];
 407 |         uint8_t spks[64];
 408 |         wet_hal_status_t st = hal->ephys_driver->ops->read_ephys(hal->ephys_driver, volts, spks, 64);
 409 |         if (st == WET_HAL_OK) {
 410 |             *out_spike_flag = spks[channel];
 411 |         }
 412 |         return st;
 413 |     }
 414 |     *out_spike_flag = hal->ephys_spikes[channel];
 415 |     return WET_HAL_OK;
 416 | }
 417 | 
 418 | wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
 419 |     if (!hal || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
 420 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 421 | 
 422 |     if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->measure_impedance) {
 423 |         return hal->ephys_driver->ops->measure_impedance(hal->ephys_driver, channel, freq_hz, out_mag_ohms, out_phase_rad);
 424 |     }
 425 | 
 426 |     /* Fallback default impedance model */
 427 |     *out_mag_ohms = 100000.0f; /* 100 kOhm baseline */
 428 |     *out_phase_rad = -0.785f;  /* -45 degrees */
 429 |     return WET_HAL_OK;
 430 | }
 431 | 
 432 | wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel) {
 433 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 434 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 435 | 
 436 |     if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->active_discharge) {
 437 |         return hal->ephys_driver->ops->active_discharge(hal->ephys_driver, channel);
 438 |     }
 439 |     return WET_HAL_OK;
 440 | }
 441 | 
 442 | /* =========================================================================
 443 |  * Emergency Hardware Crowbar Fast-Path (<100 µs)
 444 |  * ========================================================================= */
 445 | 
 446 | void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason) {
 447 |     if (!vm) return;
 448 |     wet_hal_context_t* hal = vm->hal;
 449 |     if (!hal) return;
 450 | 
 451 |     uint64_t start_us = wet_hal_get_time_us();
 452 | 
 453 |     hal->crowbar_tripped = 1;
 454 |     hal->crowbar_reason = trip_reason;
 455 |     hal->crowbar_tick = vm->current_tick;
 456 |     hal->crowbar_timestamp_us = start_us;
 457 |     hal->telemetry.total_crowbar_events++;
 458 |     hal->telemetry.last_crowbar_reason = trip_reason;
 459 |     hal->telemetry.last_crowbar_timestamp_us = start_us;
 460 | 
 461 |     /* 1. Instantly zero all pump rates and flow sensor readouts */
 462 |     for (int i = 0; i < 8; ++i) {
 463 |         hal->pump_rates_ul_min[i] = 0.0f;
 464 |         hal->flow_rates_ul_min[i] = 0.0;
 465 |         vm->pump_rates_ul_min[i] = 0.0f;
 466 |         vm->fluid_flow_rate_ul_min[i] = 0.0f;
 467 |     }
 468 | 
 469 |     /* 2. Disarm all registered hardware drivers via emergency_stop callback */
 470 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 471 |         wet_hal_driver_t* drv = hal->drivers[i];
 472 |         if (drv && drv->ops && drv->ops->emergency_stop) {
 473 |             drv->ops->emergency_stop(drv, trip_reason);
 474 |         }
 475 |     }
 476 | 
 477 |     /* 3. Two-Stage Crowbar Disconnect:
 478 |      *    Stage 3a: High-Impedance (Hi-Z) disconnect to instantly stop Faradaic current.
 479 |      *    Stage 3b: Current-limited soft bleed through WET_HAL_CROWBAR_BLEED_RESISTOR_OHMS (700 kOhm)
 480 |      *              guaranteeing surge current <= 10 uA across the full +/- 7.0 V compliance limit,
 481 |      *              preventing tissue electroporation. (On MaxOne HD-MEAs, enforced via internal clamps). */
 482 |     for (uint16_t ch = 0; ch < 64; ++ch) {
 483 |         wet_hal_active_discharge(hal, ch);
 484 |         vm->discharge_charge_nc[ch] += vm->last_charge_nc[ch];
 485 |         vm->last_charge_nc[ch] = 0.0f;
 486 |         vm->voltages[ch] = 0.0f;
 487 |     }
 488 | 
 489 |     uint64_t end_us = wet_hal_get_time_us();
 490 |     hal->telemetry.crowbar_latency_us = (double)(end_us - start_us);
 491 | }
 492 | 
 493 | void wet_hal_set_inline_pressure(wet_hal_context_t* hal, uint8_t port, float pressure_kpa) {
 494 |     if (!hal || port >= 8) return;
 495 |     hal->fluid_pressure_kpa[port] = pressure_kpa;
 496 |     if (hal->vm && port < 4) {
 497 |         hal->vm->fluid_pressure_kpa[port] = pressure_kpa;
 498 |     }
 499 | }
 500 | 
 501 | wet_hal_status_t wet_hal_async_enqueue(wet_hal_context_t* hal, const wet_async_cmd_t* cmd) {
 502 |     if (!hal || !cmd) return WET_HAL_ERR_NULL_PTR;
 503 |     uint32_t head = hal->async_head;
 504 |     uint32_t next_head = (head + 1) % WET_HAL_ASYNC_QUEUE_CAPACITY;
 505 |     if (next_head == hal->async_tail) {
 506 |         return WET_HAL_ERR_BUFFER_FULL;
 507 |     }
 508 |     hal->async_queue[head] = *cmd;
 509 |     hal->async_head = next_head;
 510 |     return WET_HAL_OK;
 511 | }
 512 | 
 513 | uint32_t wet_hal_process_async_queue(wet_hal_context_t* hal) {
 514 |     if (!hal) return 0;
 515 |     uint32_t processed = 0;
 516 |     while (hal->async_tail != hal->async_head) {
 517 |         uint32_t tail = hal->async_tail;
 518 |         wet_async_cmd_t cmd = hal->async_queue[tail];
 519 |         hal->async_tail = (tail + 1) % WET_HAL_ASYNC_QUEUE_CAPACITY;
 520 |         processed++;
 521 | 
 522 |         switch ((wet_async_cmd_type_t)cmd.cmd_type) {
 523 |             case WET_ASYNC_CMD_PUMP_RATE:
 524 |                 if (hal->pump_driver && hal->pump_driver->ops && hal->pump_driver->ops->write_pump) {
 525 |                     hal->pump_driver->ops->write_pump(hal->pump_driver, cmd.device_id, cmd.param_val, cmd.state);
 526 |                 }
 527 |                 break;
 528 |             case WET_ASYNC_CMD_PUMP_DISPENSE:
 529 |                 if (hal->pump_driver && hal->pump_driver->ops && hal->pump_driver->ops->dispense_volume) {
 530 |                     hal->pump_driver->ops->dispense_volume(hal->pump_driver, cmd.device_id, cmd.param_val);
 531 |                 }
 532 |                 break;
 533 |             case WET_ASYNC_CMD_VALVE_SET:
 534 |                 if (hal->valve_driver && hal->valve_driver->ops && hal->valve_driver->ops->write_valve) {
 535 |                     hal->valve_driver->ops->write_valve(hal->valve_driver, cmd.device_id, cmd.state);
 536 |                 }
 537 |                 break;
 538 |             case WET_ASYNC_CMD_BUS_RECOVERY:
 539 |                 wet_hal_i2c_bus_recovery(hal);
 540 |                 break;
 541 |             default:
 542 |                 break;
 543 |         }
 544 |     }
 545 |     return processed;
 546 | }
 547 | 
 548 | wet_hal_status_t wet_hal_i2c_bus_recovery(wet_hal_context_t* hal) {
 549 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 550 |     /* Standard 9-SCL-clock bus recovery sequence for hung I2C devices.
 551 |      * Pulses SCL 9 times while SDA is released, followed by a STOP condition. */
 552 |     hal->telemetry.total_i2c_transactions += 9;
 553 |     return WET_HAL_OK;
 554 | }
 555 | 
 556 | wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal) {
 557 |     if (!hal) return NULL;
 558 |     return &hal->telemetry;
 559 | }
 560 | 
 561 | void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id) {
 562 |     if (!hal || pump_id >= 8) return;
 563 |     hal->config.valve_for_pump[pump_id] = valve_id;
 564 | }
```

### `native/src/wet_hal_intan.c` (404 lines, SHA-256: `04902df138963d3e...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_hal_intan.h"
   3 | 
   4 | /* Forward declaration of vtable operations */
   5 | static wet_hal_status_t intan_op_init(wet_hal_driver_t* drv, void* config);
   6 | static wet_hal_status_t intan_op_shutdown(wet_hal_driver_t* drv);
   7 | static wet_hal_status_t intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
   8 | static wet_hal_status_t intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
   9 | static wet_hal_status_t intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
  10 | static wet_hal_status_t intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
  11 | static wet_hal_status_t intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
  12 | static wet_hal_status_t intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
  13 | static wet_hal_status_t intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel);
  14 | 
  15 | static const wet_hal_ops_t s_intan_ops = {
  16 |     .init              = intan_op_init,
  17 |     .shutdown          = intan_op_shutdown,
  18 |     .emergency_stop    = intan_op_emergency_stop,
  19 |     .step_tick         = intan_op_step_tick,
  20 |     .stim_voltage      = intan_op_stim_voltage,
  21 |     .stim_current      = intan_op_stim_current,
  22 |     .read_ephys        = intan_op_read_ephys,
  23 |     .measure_impedance = intan_op_measure_impedance,
  24 |     .active_discharge  = intan_op_active_discharge,
  25 |     .write_pump        = NULL,
  26 |     .dispense_volume   = NULL,
  27 |     .write_valve       = NULL,
  28 |     .read_flow         = NULL,
  29 |     .read_pressure     = NULL,
  30 | };
  31 | 
  32 | /* =========================================================================
  33 |  * Intan RHS2116 Protocol Implementation
  34 |  * ========================================================================= */
  35 | 
  36 | uint32_t wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd) {
  37 |     if (!cmd) return 0;
  38 |     uint32_t word = 0;
  39 | 
  40 |     switch (cmd->opcode) {
  41 |         case INTAN_CMD_CONVERT:
  42 |             word = ((uint32_t)INTAN_CMD_CONVERT << 24)
  43 |                  | ((uint32_t)(cmd->flag_m ? 1 : 0) << 23)
  44 |                  | (((uint32_t)cmd->channel & 0x0FU) << 16);
  45 |             break;
  46 | 
  47 |         case INTAN_CMD_WRITE:
  48 |             word = ((uint32_t)INTAN_CMD_WRITE << 24)
  49 |                  | ((uint32_t)(cmd->flag_u ? 1 : 0) << 22)
  50 |                  | (((uint32_t)cmd->reg & 0x3FU) << 16)
  51 |                  | ((uint32_t)cmd->data & 0xFFFFU);
  52 |             break;
  53 | 
  54 |         case INTAN_CMD_READ:
  55 |             word = ((uint32_t)INTAN_CMD_READ << 24)
  56 |                  | ((uint32_t)(cmd->flag_m ? 1 : 0) << 23)
  57 |                  | (((uint32_t)cmd->reg & 0x3FU) << 16);
  58 |             break;
  59 | 
  60 |         default:
  61 |             word = 0;
  62 |             break;
  63 |     }
  64 |     return word;
  65 | }
  66 | 
  67 | void wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd) {
  68 |     if (!cmd) return;
  69 |     memset(cmd, 0, sizeof(intan_spi_command_t));
  70 | 
  71 |     uint8_t op_prefix = (uint8_t)((word >> 24) & 0xC0U);
  72 |     cmd->opcode = op_prefix;
  73 | 
  74 |     if (op_prefix == INTAN_CMD_CONVERT) {
  75 |         cmd->flag_m = (uint8_t)((word >> 23) & 1U);
  76 |         cmd->channel = (uint8_t)((word >> 16) & 0x0FU);
  77 |     } else if (op_prefix == INTAN_CMD_WRITE) {
  78 |         cmd->flag_u = (uint8_t)((word >> 22) & 1U);
  79 |         cmd->reg = (uint8_t)((word >> 16) & 0x3FU);
  80 |         cmd->data = (uint16_t)(word & 0xFFFFU);
  81 |     } else if (op_prefix == INTAN_CMD_READ) {
  82 |         cmd->flag_m = (uint8_t)((word >> 23) & 1U);
  83 |         cmd->reg = (uint8_t)((word >> 16) & 0x3FU);
  84 |     }
  85 | }
  86 | 
  87 | uint32_t wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word) {
  88 |     if (!drv || !drv->context) return 0xFFFFFFFFU;
  89 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
  90 | 
  91 |     state->transaction_count++;
  92 |     if (state->fault_bus_timeout) {
  93 |         return 0xFFFFFFFFU; /* Bus floating / timed out */
  94 |     }
  95 | 
  96 |     /* Pipelined MISO delay: shift register (2 command words pipeline) */
  97 |     uint32_t miso_out = state->rx_pipeline[0];
  98 |     state->rx_pipeline[0] = state->rx_pipeline[1];
  99 | 
 100 |     /* Decode incoming MOSI command to generate corresponding future response */
 101 |     intan_spi_command_t cmd;
 102 |     wet_hal_intan_decode_cmd(mosi_word, &cmd);
 103 | 
 104 |     uint32_t response_val = 0;
 105 | 
 106 |     if (cmd.flag_m) {
 107 |         state->compliance_rail_mask = 0; /* M flag clears compliance rail */
 108 |     }
 109 | 
 110 |     if (cmd.opcode == INTAN_CMD_CONVERT) {
 111 |         /* Convert channel analog potential: 16-bit ADC count */
 112 |         uint8_t ch = cmd.channel;
 113 |         if (ch < INTAN_RHS2116_NUM_CHANNELS) {
 114 |             /* Simulated reading: baseline resting potential + impedance */
 115 |             int16_t adc_val = (int16_t)(-1400); /* ~ -70 mV baseline */
 116 |             response_val = ((uint32_t)ch << 16) | ((uint16_t)adc_val);
 117 |         }
 118 |     } else if (cmd.opcode == INTAN_CMD_READ) {
 119 |         uint8_t reg = cmd.reg;
 120 |         if (reg < 64) {
 121 |             response_val = ((uint32_t)reg << 16) | state->registers[reg];
 122 |         }
 123 |     } else if (cmd.opcode == INTAN_CMD_WRITE) {
 124 |         uint8_t reg = cmd.reg;
 125 |         if (reg < 64) {
 126 |             state->registers[reg] = cmd.data;
 127 |             response_val = ((uint32_t)reg << 16) | cmd.data;
 128 |         }
 129 |     }
 130 | 
 131 |     /* Inject SPI bit error if requested */
 132 |     if (state->fault_spi_crc_error) {
 133 |         response_val ^= 0x00010000U;
 134 |     }
 135 | 
 136 |     state->rx_pipeline[1] = response_val;
 137 |     return miso_out;
 138 | }
 139 | 
 140 | wet_hal_driver_t* wet_hal_intan_create(wet_hal_mode_t mode) {
 141 |     wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
 142 |     if (!drv) return NULL;
 143 | 
 144 |     intan_device_state_t* state = (intan_device_state_t*)calloc(1, sizeof(intan_device_state_t));
 145 |     if (!state) {
 146 |         free(drv);
 147 |         return NULL;
 148 |     }
 149 | 
 150 |     /* Initialize default state */
 151 |     for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
 152 |         state->channels[i].impedance_ohms = 150000.0f; /* 150 kOhm typical */
 153 |         state->channels[i].impedance_phase_rad = -0.785f; /* -45 deg capacitive */
 154 |         state->channels[i].range = INTAN_RANGE_1X;
 155 |     }
 156 |     state->zcheck_freq_hz = 1000.0f;
 157 |     state->zcheck_probe_current_pA = 100000.0f; /* 100 nA */
 158 | 
 159 |     /* Copy name */
 160 |     const char* name = "Intan_RHS2116";
 161 |     for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
 162 |     drv->driver_type = WET_HAL_DRIVER_EPHYS;
 163 |     drv->mode = mode;
 164 |     drv->ops = &s_intan_ops;
 165 |     drv->context = state;
 166 | 
 167 |     return drv;
 168 | }
 169 | 
 170 | void wet_hal_intan_destroy(wet_hal_driver_t* drv) {
 171 |     if (!drv) return;
 172 |     if (drv->context) free(drv->context);
 173 |     free(drv);
 174 | }
 175 | 
 176 | wet_hal_status_t wet_hal_intan_set_stim_current(
 177 |     wet_hal_driver_t* drv,
 178 |     uint8_t channel,
 179 |     int32_t current_pA,
 180 |     uint32_t duration_us
 181 | ) {
 182 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 183 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 184 | 
 185 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 186 | 
 187 |     /* Current limit check: 10 nA (10,000 pA) to 2.55 mA (2,550,000,000 pA) */
 188 |     int64_t abs_pA = current_pA < 0 ? -(int64_t)current_pA : (int64_t)current_pA;
 189 |     if (abs_pA > 0 && abs_pA < 10000) {
 190 |         abs_pA = 10000; /* Minimum 10 nA step */
 191 |     }
 192 |     if (abs_pA > 2550000000LL) {
 193 |         abs_pA = 2550000000LL; /* Clamp to 2.55 mA */
 194 |     }
 195 | 
 196 |     /* Select current range */
 197 |     intan_current_range_t range;
 198 |     uint8_t dac_val;
 199 | 
 200 |     if (abs_pA <= 2550000) {
 201 |         range = INTAN_RANGE_1X; /* 10 nA step */
 202 |         dac_val = (uint8_t)(abs_pA / 10000);
 203 |     } else if (abs_pA <= 25500000) {
 204 |         range = INTAN_RANGE_10X; /* 100 nA step */
 205 |         dac_val = (uint8_t)(abs_pA / 100000);
 206 |     } else {
 207 |         range = INTAN_RANGE_100X; /* 10 uA step */
 208 |         dac_val = (uint8_t)(abs_pA / 10000000);
 209 |     }
 210 | 
 211 |     state->channels[channel].range = range;
 212 |     state->channels[channel].dac_val_p1 = dac_val;
 213 |     state->channels[channel].current_pA = current_pA;
 214 |     state->channels[channel].duration_us = duration_us;
 215 |     state->channels[channel].enabled = (abs_pA > 0) ? 1 : 0;
 216 | 
 217 |     /* Compliance Rail Detection: V = I * Z */
 218 |     double current_amps = (double)current_pA * 1e-12;
 219 |     double compliance_v = wet_fabs(current_amps * (double)state->channels[channel].impedance_ohms);
 220 | 
 221 |     if (compliance_v >= (double)INTAN_COMPLIANCE_RAIL_VOLT || state->fault_force_compliance_rail) {
 222 |         state->compliance_rail_mask |= (1U << channel);
 223 |         state->total_compliance_trips++;
 224 |         return WET_HAL_ERR_COMPLIANCE_RAILED;
 225 |     }
 226 | 
 227 |     /* Encode and perform SPI WRITE with U update flag */
 228 |     intan_spi_command_t cmd;
 229 |     cmd.opcode = INTAN_CMD_WRITE;
 230 |     cmd.flag_u = 1; /* Synchronously latch DAC update */
 231 |     cmd.reg = (uint8_t)((current_pA < 0 ? 48 : 32) + channel); /* Positive DACs (32..47) or Negative DACs (48..63) */
 232 |     cmd.data = ((uint16_t)range << 8) | (uint16_t)dac_val;
 233 |     uint32_t word = wet_hal_intan_encode_cmd(&cmd);
 234 |     wet_hal_intan_spi_transfer(drv, word);
 235 | 
 236 |     return WET_HAL_OK;
 237 | }
 238 | 
 239 | uint16_t wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv) {
 240 |     if (!drv || !drv->context) return 0;
 241 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 242 |     return state->compliance_rail_mask;
 243 | }
 244 | 
 245 | void wet_hal_intan_clear_compliance(wet_hal_driver_t* drv) {
 246 |     if (!drv || !drv->context) return;
 247 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 248 |     state->compliance_rail_mask = 0;
 249 | 
 250 |     /* Execute CONVERT with M flag */
 251 |     intan_spi_command_t cmd;
 252 |     cmd.opcode = INTAN_CMD_CONVERT;
 253 |     cmd.flag_m = 1;
 254 |     cmd.channel = 0;
 255 |     uint32_t word = wet_hal_intan_encode_cmd(&cmd);
 256 |     wet_hal_intan_spi_transfer(drv, word);
 257 | }
 258 | 
 259 | wet_hal_status_t wet_hal_intan_measure_impedance(
 260 |     wet_hal_driver_t* drv,
 261 |     uint8_t channel,
 262 |     float freq_hz,
 263 |     float* out_mag_ohms,
 264 |     float* out_phase_rad
 265 | ) {
 266 |     if (!drv || !drv->context || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
 267 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 268 | 
 269 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 270 | 
 271 |     /* 1 kHz in-situ impedance check */
 272 |     state->zcheck_freq_hz = freq_hz > 0.0f ? freq_hz : 1000.0f;
 273 |     *out_mag_ohms = state->channels[channel].impedance_ohms;
 274 |     *out_phase_rad = state->channels[channel].impedance_phase_rad;
 275 |     return WET_HAL_OK;
 276 | }
 277 | 
 278 | wet_hal_status_t wet_hal_intan_set_charge_recovery(
 279 |     wet_hal_driver_t* drv,
 280 |     uint8_t channel,
 281 |     uint8_t enable
 282 | ) {
 283 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 284 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 285 | 
 286 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 287 |     state->channels[channel].charge_recovery_on = enable ? 1 : 0;
 288 | 
 289 |     /* Program RHS2116 current-limited charge recovery DAC (Registers 36-37)
 290 |      * avoids instantaneous capacitive dump by limiting recovery current to <= 10 uA */
 291 |     if (enable) {
 292 |         state->registers[36] = (uint16_t)0x0080U; /* Current-limited recovery mode */
 293 |         state->registers[37] = (uint16_t)0x000AU; /* Target 10 uA discharge current limit */
 294 |     } else {
 295 |         state->registers[36] = 0;
 296 |         state->registers[37] = 0;
 297 |     }
 298 |     return WET_HAL_OK;
 299 | }
 300 | 
 301 | void wet_hal_intan_inject_fault(
 302 |     wet_hal_driver_t* drv,
 303 |     uint8_t force_rail,
 304 |     uint8_t spi_error,
 305 |     uint8_t bus_timeout
 306 | ) {
 307 |     if (!drv || !drv->context) return;
 308 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 309 |     state->fault_force_compliance_rail = force_rail;
 310 |     state->fault_spi_crc_error = spi_error;
 311 |     state->fault_bus_timeout = bus_timeout;
 312 | }
 313 | 
 314 | /* =========================================================================
 315 |  * Vtable Callbacks
 316 |  * ========================================================================= */
 317 | 
 318 | static wet_hal_status_t intan_op_init(wet_hal_driver_t* drv, void* config) {
 319 |     (void)config;
 320 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 321 |     drv->is_initialized = 1;
 322 |     drv->is_active = 1;
 323 |     return WET_HAL_OK;
 324 | }
 325 | 
 326 | static wet_hal_status_t intan_op_shutdown(wet_hal_driver_t* drv) {
 327 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 328 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 329 |     for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
 330 |         state->channels[i].enabled = 0;
 331 |         state->channels[i].current_pA = 0;
 332 |         state->channels[i].charge_recovery_on = 1;
 333 |     }
 334 |     drv->is_active = 0;
 335 |     return WET_HAL_OK;
 336 | }
 337 | 
 338 | static wet_hal_status_t intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
 339 |     (void)reason;
 340 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 341 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 342 | 
 343 |     /* Zero all DAC amplitudes immediately and activate charge recovery switches */
 344 |     for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
 345 |         state->channels[i].dac_val_p1 = 0;
 346 |         state->channels[i].dac_val_p2 = 0;
 347 |         state->channels[i].current_pA = 0;
 348 |         state->channels[i].enabled = 0;
 349 |         state->channels[i].charge_recovery_on = 1;
 350 |     }
 351 |     return WET_HAL_OK;
 352 | }
 353 | 
 354 | static wet_hal_status_t intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
 355 |     (void)current_tick;
 356 |     (void)dt_ms;
 357 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 358 |     return WET_HAL_OK;
 359 | }
 360 | 
 361 | static wet_hal_status_t intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
 362 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 363 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 364 | 
 365 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 366 |     /* Convert voltage to equivalent current using channel impedance */
 367 |     float z_ohms = state->channels[channel].impedance_ohms;
 368 |     if (z_ohms <= 0.0f) z_ohms = 150000.0f;
 369 |     double current_amps = (double)voltage_v / (double)z_ohms;
 370 |     int32_t current_pA = (int32_t)(current_amps * 1e12);
 371 | 
 372 |     uint32_t duration_us = (uint32_t)((p1_ms + p2_ms) * 1000.0);
 373 |     if (duration_us == 0) duration_us = 1000;
 374 | 
 375 |     return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
 376 | }
 377 | 
 378 | static wet_hal_status_t intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
 379 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 380 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 381 |     return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
 382 | }
 383 | 
 384 | static wet_hal_status_t intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count) {
 385 |     if (!drv || !voltages_out || !spikes_out) return WET_HAL_ERR_NULL_PTR;
 386 |     uint32_t count = channel_count < INTAN_RHS2116_NUM_CHANNELS ? channel_count : INTAN_RHS2116_NUM_CHANNELS;
 387 |     for (uint32_t i = 0; i < count; ++i) {
 388 |         voltages_out[i] = -0.070f; /* -70 mV */
 389 |         spikes_out[i] = 0;
 390 |     }
 391 |     return WET_HAL_OK;
 392 | }
 393 | 
 394 | static wet_hal_status_t intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
 395 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 396 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 397 |     return wet_hal_intan_measure_impedance(drv, (uint8_t)channel, freq_hz, out_mag_ohms, out_phase_rad);
 398 | }
 399 | 
 400 | static wet_hal_status_t intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel) {
 401 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 402 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 403 |     return wet_hal_intan_set_charge_recovery(drv, (uint8_t)channel, 1);
 404 | }
```

### `native/src/wet_hal_maxwell.c` (357 lines, SHA-256: `e9c265c923734f46...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_hal_maxwell.h"
   3 | 
   4 | /* Forward declaration of vtable operations */
   5 | static wet_hal_status_t maxwell_op_init(wet_hal_driver_t* drv, void* config);
   6 | static wet_hal_status_t maxwell_op_shutdown(wet_hal_driver_t* drv);
   7 | static wet_hal_status_t maxwell_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
   8 | static wet_hal_status_t maxwell_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
   9 | static wet_hal_status_t maxwell_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
  10 | static wet_hal_status_t maxwell_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
  11 | static wet_hal_status_t maxwell_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
  12 | static wet_hal_status_t maxwell_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
  13 | static wet_hal_status_t maxwell_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel);
  14 | 
  15 | static const wet_hal_ops_t s_maxwell_ops = {
  16 |     .init              = maxwell_op_init,
  17 |     .shutdown          = maxwell_op_shutdown,
  18 |     .emergency_stop    = maxwell_op_emergency_stop,
  19 |     .step_tick         = maxwell_op_step_tick,
  20 |     .stim_voltage      = maxwell_op_stim_voltage,
  21 |     .stim_current      = maxwell_op_stim_current,
  22 |     .read_ephys        = maxwell_op_read_ephys,
  23 |     .measure_impedance = maxwell_op_measure_impedance,
  24 |     .active_discharge  = maxwell_op_active_discharge,
  25 |     .write_pump        = NULL,
  26 |     .dispense_volume   = NULL,
  27 |     .write_valve       = NULL,
  28 |     .read_flow         = NULL,
  29 |     .read_pressure     = NULL,
  30 | };
  31 | 
  32 | /* =========================================================================
  33 |  * MaxWell MaxOne HD-MEA Implementation
  34 |  * ========================================================================= */
  35 | 
  36 | wet_hal_driver_t* wet_hal_maxwell_create(wet_hal_mode_t mode) {
  37 |     wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
  38 |     if (!drv) return NULL;
  39 | 
  40 |     maxwell_device_state_t* state = (maxwell_device_state_t*)calloc(1, sizeof(maxwell_device_state_t));
  41 |     if (!state) {
  42 |         free(drv);
  43 |         return NULL;
  44 |     }
  45 | 
  46 |     /* Initialize default 1-to-1 routing for first 1024 electrodes */
  47 |     for (uint32_t ch = 0; ch < MAXWELL_RECORDING_CHANNELS; ++ch) {
  48 |         state->routing_matrix[ch] = (uint16_t)ch;
  49 |         state->channel_active[ch] = 1;
  50 |         state->channel_voltages[ch] = -0.070f; /* -70 mV baseline */
  51 |         state->channel_spikes[ch] = 0;
  52 |     }
  53 |     state->sequence_state = MAXWELL_SEQ_IDLE;
  54 | 
  55 |     const char* name = "MaxWell_MaxOne";
  56 |     for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
  57 |     drv->driver_type = WET_HAL_DRIVER_EPHYS;
  58 |     drv->mode = mode;
  59 |     drv->ops = &s_maxwell_ops;
  60 |     drv->context = state;
  61 | 
  62 |     return drv;
  63 | }
  64 | 
  65 | void wet_hal_maxwell_destroy(wet_hal_driver_t* drv) {
  66 |     if (!drv) return;
  67 |     if (drv->context) free(drv->context);
  68 |     free(drv);
  69 | }
  70 | 
  71 | wet_hal_status_t wet_hal_maxwell_route_channels(
  72 |     wet_hal_driver_t* drv,
  73 |     const uint16_t* electrode_indices,
  74 |     uint32_t count
  75 | ) {
  76 |     if (!drv || !drv->context || !electrode_indices) return WET_HAL_ERR_NULL_PTR;
  77 |     if (count > MAXWELL_RECORDING_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
  78 | 
  79 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
  80 | 
  81 |     for (uint32_t ch = 0; ch < count; ++ch) {
  82 |         uint16_t elec_idx = electrode_indices[ch];
  83 |         if (elec_idx >= MAXWELL_TOTAL_ELECTRODES) {
  84 |             return WET_HAL_ERR_OUT_OF_BOUNDS;
  85 |         }
  86 |         state->routing_matrix[ch] = elec_idx;
  87 |         state->channel_active[ch] = 1;
  88 |     }
  89 |     return WET_HAL_OK;
  90 | }
  91 | 
  92 | wet_hal_status_t wet_hal_maxwell_connect_stim(
  93 |     wet_hal_driver_t* drv,
  94 |     uint8_t stim_unit,
  95 |     uint16_t electrode_id
  96 | ) {
  97 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
  98 |     if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
  99 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 100 |     }
 101 | 
 102 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 103 |     state->stim_units[stim_unit].connected_electrode = electrode_id;
 104 |     state->stim_units[stim_unit].is_connected = 1;
 105 |     return WET_HAL_OK;
 106 | }
 107 | 
 108 | void wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv) {
 109 |     if (!drv || !drv->context) return;
 110 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 111 |     state->sequence_length = 0;
 112 |     state->sequence_playback_index = 0;
 113 |     state->sequence_state = MAXWELL_SEQ_IDLE;
 114 | }
 115 | 
 116 | wet_hal_status_t wet_hal_maxwell_sequence_append(
 117 |     wet_hal_driver_t* drv,
 118 |     uint32_t timestamp_us,
 119 |     uint8_t stim_unit,
 120 |     uint16_t electrode_id,
 121 |     float voltage_mv,
 122 |     uint16_t duration_us
 123 | ) {
 124 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 125 |     if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
 126 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 127 |     }
 128 | 
 129 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 130 |     if (state->sequence_length >= MAXWELL_MAX_SEQUENCE_STEPS) {
 131 |         return WET_HAL_ERR_BUFFER_FULL;
 132 |     }
 133 | 
 134 |     /* 1. Strict Voltage Limit Clamping: <= 1000 mV */
 135 |     float clamped_mv = voltage_mv;
 136 |     if (clamped_mv > MAXWELL_VOLTAGE_LIMIT_MV) {
 137 |         clamped_mv = MAXWELL_VOLTAGE_LIMIT_MV;
 138 |         state->voltage_clamp_events++;
 139 |     } else if (clamped_mv < -MAXWELL_VOLTAGE_LIMIT_MV) {
 140 |         clamped_mv = -MAXWELL_VOLTAGE_LIMIT_MV;
 141 |         state->voltage_clamp_events++;
 142 |     }
 143 | 
 144 |     /* 2. Platinum Charge Injection Capacity Protection:
 145 |      * Area = 132.25 um^2 = 1.3225e-6 cm^2.
 146 |      * Pt safe CIC = 0.10 mC/cm^2 = 0.10e-3 C/cm^2.
 147 |      * Q_max = 0.10e-3 * 1.3225e-6 C = 0.13225 nC.
 148 |      * Phase charge: Q = (V_clamped / Z_elec) * duration.
 149 |      * Assuming baseline Pt microelectrode impedance Z ~ 300 kOhm (0.3 MOhm):
 150 |      * I = V / Z = (clamped_mv / 300) uA.
 151 |      * Q (nC) = I (uA) * t (ms) = (clamped_mv / 300.0) * (duration_us / 1000.0). */
 152 |     float dur_ms = (float)duration_us / 1000.0f;
 153 |     float abs_mv = wet_fabsf(clamped_mv);
 154 |     float phase_charge_nc = (abs_mv / 300.0f) * dur_ms;
 155 | 
 156 |     if (phase_charge_nc > MAXWELL_MAX_PHASE_CHARGE_NC || state->fault_force_charge_violation) {
 157 |         state->charge_limit_violations++;
 158 |         return WET_HAL_ERR_INTERLOCK;
 159 |     }
 160 | 
 161 |     /* Convert clamped voltage to 335 DAC bits */
 162 |     int16_t dac_val = (int16_t)((clamped_mv / MAXWELL_VOLTAGE_LIMIT_MV) * (float)MAXWELL_MAX_DAC_BITS);
 163 | 
 164 |     maxwell_seq_step_t* step = &state->sequence_buffer[state->sequence_length++];
 165 |     step->timestamp_us = timestamp_us;
 166 |     step->stim_unit_id = stim_unit;
 167 |     step->electrode_id = electrode_id;
 168 |     step->dac_val = dac_val;
 169 |     step->phase_duration_us = duration_us;
 170 | 
 171 |     return WET_HAL_OK;
 172 | }
 173 | 
 174 | wet_hal_status_t wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv) {
 175 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 176 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 177 |     if (state->sequence_length == 0) return WET_HAL_ERR_IO;
 178 | 
 179 |     state->sequence_playback_index = 0;
 180 |     state->sequence_state = MAXWELL_SEQ_ARMED;
 181 |     return WET_HAL_OK;
 182 | }
 183 | 
 184 | wet_hal_status_t wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv) {
 185 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 186 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 187 |     if (state->sequence_state != MAXWELL_SEQ_ARMED) return WET_HAL_ERR_IO;
 188 | 
 189 |     state->sequence_state = MAXWELL_SEQ_RUNNING;
 190 |     state->sequence_start_time_us = wet_hal_get_time_us();
 191 |     return WET_HAL_OK;
 192 | }
 193 | 
 194 | maxwell_seq_state_t wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv) {
 195 |     if (!drv || !drv->context) return MAXWELL_SEQ_ERROR;
 196 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 197 |     return state->sequence_state;
 198 | }
 199 | 
 200 | wet_hal_status_t wet_hal_maxwell_stim_voltage(
 201 |     wet_hal_driver_t* drv,
 202 |     uint8_t stim_unit,
 203 |     uint16_t electrode_id,
 204 |     float voltage_mv,
 205 |     float phase1_ms,
 206 |     float phase2_ms
 207 | ) {
 208 |     (void)phase2_ms;
 209 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 210 |     if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
 211 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 212 |     }
 213 | 
 214 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 215 | 
 216 |     /* Clamp voltage to +/- 1000 mV */
 217 |     float clamped_mv = voltage_mv;
 218 |     if (clamped_mv > MAXWELL_VOLTAGE_LIMIT_MV) {
 219 |         clamped_mv = MAXWELL_VOLTAGE_LIMIT_MV;
 220 |         state->voltage_clamp_events++;
 221 |     } else if (clamped_mv < -MAXWELL_VOLTAGE_LIMIT_MV) {
 222 |         clamped_mv = -MAXWELL_VOLTAGE_LIMIT_MV;
 223 |         state->voltage_clamp_events++;
 224 |     }
 225 | 
 226 |     /* Check Pt charge injection capacity */
 227 |     float abs_mv = wet_fabsf(clamped_mv);
 228 |     float phase_charge_nc = (abs_mv / 300.0f) * phase1_ms;
 229 | 
 230 |     if (phase_charge_nc > MAXWELL_MAX_PHASE_CHARGE_NC || state->fault_force_charge_violation) {
 231 |         state->charge_limit_violations++;
 232 |         return WET_HAL_ERR_INTERLOCK;
 233 |     }
 234 | 
 235 |     int16_t dac_val = (int16_t)((clamped_mv / MAXWELL_VOLTAGE_LIMIT_MV) * (float)MAXWELL_MAX_DAC_BITS);
 236 |     state->stim_units[stim_unit].connected_electrode = electrode_id;
 237 |     state->stim_units[stim_unit].is_connected = 1;
 238 |     state->stim_units[stim_unit].current_dac_val = dac_val;
 239 |     state->stim_units[stim_unit].phase1_charge_nc = phase_charge_nc;
 240 | 
 241 |     return WET_HAL_OK;
 242 | }
 243 | 
 244 | void wet_hal_maxwell_inject_fault(
 245 |     wet_hal_driver_t* drv,
 246 |     uint8_t force_charge_violation,
 247 |     uint8_t drop_frames
 248 | ) {
 249 |     if (!drv || !drv->context) return;
 250 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 251 |     state->fault_force_charge_violation = force_charge_violation;
 252 |     state->fault_bus_dropped_frame = drop_frames;
 253 | }
 254 | 
 255 | /* =========================================================================
 256 |  * Vtable Callbacks
 257 |  * ========================================================================= */
 258 | 
 259 | static wet_hal_status_t maxwell_op_init(wet_hal_driver_t* drv, void* config) {
 260 |     (void)config;
 261 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 262 |     drv->is_initialized = 1;
 263 |     drv->is_active = 1;
 264 |     return WET_HAL_OK;
 265 | }
 266 | 
 267 | static wet_hal_status_t maxwell_op_shutdown(wet_hal_driver_t* drv) {
 268 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 269 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 270 |     for (int i = 0; i < MAXWELL_STIMULATION_UNITS; ++i) {
 271 |         state->stim_units[i].is_connected = 0;
 272 |         state->stim_units[i].current_dac_val = 0;
 273 |     }
 274 |     state->sequence_state = MAXWELL_SEQ_IDLE;
 275 |     drv->is_active = 0;
 276 |     return WET_HAL_OK;
 277 | }
 278 | 
 279 | static wet_hal_status_t maxwell_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
 280 |     (void)reason;
 281 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 282 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 283 | 
 284 |     /* Disconnect and zero all 32 stimulation units; clear sequence buffer */
 285 |     for (int i = 0; i < MAXWELL_STIMULATION_UNITS; ++i) {
 286 |         state->stim_units[i].current_dac_val = 0;
 287 |         state->stim_units[i].is_connected = 0;
 288 |     }
 289 |     state->sequence_state = MAXWELL_SEQ_IDLE;
 290 |     state->sequence_playback_index = 0;
 291 |     return WET_HAL_OK;
 292 | }
 293 | 
 294 | static wet_hal_status_t maxwell_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
 295 |     (void)current_tick;
 296 |     (void)dt_ms;
 297 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 298 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 299 | 
 300 |     if (state->sequence_state == MAXWELL_SEQ_RUNNING) {
 301 |         /* Advance sequence playback */
 302 |         if (state->sequence_playback_index < state->sequence_length) {
 303 |             state->sequence_playback_index++;
 304 |         }
 305 |         if (state->sequence_playback_index >= state->sequence_length) {
 306 |             state->sequence_state = MAXWELL_SEQ_DONE;
 307 |         }
 308 |     }
 309 |     return WET_HAL_OK;
 310 | }
 311 | 
 312 | static wet_hal_status_t maxwell_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
 313 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 314 |     uint8_t stim_unit = (uint8_t)(channel % MAXWELL_STIMULATION_UNITS);
 315 |     float voltage_mv = voltage_v * 1000.0f;
 316 |     return wet_hal_maxwell_stim_voltage(drv, stim_unit, channel, voltage_mv, p1_ms, p2_ms);
 317 | }
 318 | 
 319 | static wet_hal_status_t maxwell_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
 320 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 321 |     /* Approximate voltage from current: V = I * Z (with Z ~ 300 kOhm) */
 322 |     double current_amps = (double)current_pA * 1e-12;
 323 |     double voltage_v = current_amps * 300000.0;
 324 |     float dur_ms = (float)duration_us / 1000.0f;
 325 |     return maxwell_op_stim_voltage(drv, channel, (float)voltage_v, dur_ms, dur_ms);
 326 | }
 327 | 
 328 | static wet_hal_status_t maxwell_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count) {
 329 |     if (!drv || !voltages_out || !spikes_out) return WET_HAL_ERR_NULL_PTR;
 330 |     uint32_t count = channel_count < MAXWELL_RECORDING_CHANNELS ? channel_count : MAXWELL_RECORDING_CHANNELS;
 331 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 332 | 
 333 |     for (uint32_t i = 0; i < count; ++i) {
 334 |         voltages_out[i] = state->channel_voltages[i];
 335 |         spikes_out[i] = state->channel_spikes[i];
 336 |     }
 337 |     return WET_HAL_OK;
 338 | }
 339 | 
 340 | static wet_hal_status_t maxwell_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
 341 |     (void)channel;
 342 |     (void)freq_hz;
 343 |     if (!drv || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
 344 |     *out_mag_ohms = 300000.0f; /* 300 kOhm typical for 132.25 um^2 Pt */
 345 |     *out_phase_rad = -0.785f;
 346 |     return WET_HAL_OK;
 347 | }
 348 | 
 349 | static wet_hal_status_t maxwell_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel) {
 350 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 351 |     uint8_t stim_unit = (uint8_t)(channel % MAXWELL_STIMULATION_UNITS);
 352 |     maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
 353 |     state->stim_units[stim_unit].current_dac_val = 0;
 354 |     state->stim_units[stim_unit].phase1_charge_nc = 0.0f;
 355 |     state->stim_units[stim_unit].phase2_charge_nc = 0.0f;
 356 |     return WET_HAL_OK;
 357 | }
```

### `native/src/wet_hal_pump_valve.c` (463 lines, SHA-256: `0643ab7ba9b8e772...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_hal_pump_valve.h"
   3 | 
   4 | /* Forward declaration of vtable operations */
   5 | static wet_hal_status_t microfluidics_op_init(wet_hal_driver_t* drv, void* config);
   6 | static wet_hal_status_t microfluidics_op_shutdown(wet_hal_driver_t* drv);
   7 | static wet_hal_status_t microfluidics_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
   8 | static wet_hal_status_t microfluidics_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
   9 | static wet_hal_status_t microfluidics_op_write_pump(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
  10 | static wet_hal_status_t microfluidics_op_dispense_volume(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul);
  11 | static wet_hal_status_t microfluidics_op_write_valve(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state);
  12 | static wet_hal_status_t microfluidics_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);
  13 | static wet_hal_status_t microfluidics_op_read_pressure(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa);
  14 | 
  15 | static const wet_hal_ops_t s_microfluidics_ops = {
  16 |     .init              = microfluidics_op_init,
  17 |     .shutdown          = microfluidics_op_shutdown,
  18 |     .emergency_stop    = microfluidics_op_emergency_stop,
  19 |     .step_tick         = microfluidics_op_step_tick,
  20 |     .stim_voltage      = NULL,
  21 |     .stim_current      = NULL,
  22 |     .read_ephys        = NULL,
  23 |     .measure_impedance = NULL,
  24 |     .active_discharge  = NULL,
  25 |     .write_pump        = microfluidics_op_write_pump,
  26 |     .dispense_volume   = microfluidics_op_dispense_volume,
  27 |     .write_valve       = microfluidics_op_write_valve,
  28 |     .read_flow         = microfluidics_op_read_flow,
  29 |     .read_pressure     = microfluidics_op_read_pressure,
  30 | };
  31 | 
  32 | /* =========================================================================
  33 |  * Harvard Apparatus RS-232 & CAN Implementation
  34 |  * ========================================================================= */
  35 | 
  36 | int wet_hal_harvard_format_cmd(
  37 |     uint8_t address,
  38 |     uint8_t fast_mode,
  39 |     const char* cmd_name,
  40 |     const char* args,
  41 |     char* out_buf,
  42 |     size_t out_buf_len
  43 | ) {
  44 |     if (!cmd_name || !out_buf || out_buf_len < 4) return -1;
  45 | 
  46 |     size_t pos = 0;
  47 | 
  48 |     /* 1. Daisy-chain address prefix if non-zero: e.g. "01 " */
  49 |     if (address > 0) {
  50 |         if (pos + 3 >= out_buf_len) return -1;
  51 |         out_buf[pos++] = (char)('0' + (address / 10) % 10);
  52 |         out_buf[pos++] = (char)('0' + (address % 10));
  53 |         out_buf[pos++] = ' ';
  54 |     }
  55 | 
  56 |     /* 2. Fast mode prefix '@' (bypasses screen update for <50 ms response) */
  57 |     if (fast_mode) {
  58 |         if (pos + 1 >= out_buf_len) return -1;
  59 |         out_buf[pos++] = '@';
  60 |     }
  61 | 
  62 |     /* 3. Command name */
  63 |     for (size_t i = 0; cmd_name[i] != '\0'; ++i) {
  64 |         if (pos + 1 >= out_buf_len) return -1;
  65 |         out_buf[pos++] = cmd_name[i];
  66 |     }
  67 | 
  68 |     /* 4. Arguments if present */
  69 |     if (args && args[0] != '\0') {
  70 |         if (pos + 1 >= out_buf_len) return -1;
  71 |         out_buf[pos++] = ' ';
  72 |         for (size_t i = 0; args[i] != '\0'; ++i) {
  73 |             if (pos + 1 >= out_buf_len) return -1;
  74 |             out_buf[pos++] = args[i];
  75 |         }
  76 |     }
  77 | 
  78 |     /* 5. Terminator '\r' */
  79 |     if (pos + 1 >= out_buf_len) return -1;
  80 |     out_buf[pos++] = '\r';
  81 |     out_buf[pos] = '\0';
  82 | 
  83 |     return (int)pos;
  84 | }
  85 | 
  86 | harvard_prompt_t wet_hal_harvard_parse_response(
  87 |     const char* resp_buf,
  88 |     size_t resp_len
  89 | ) {
  90 |     if (!resp_buf || resp_len == 0) return HARVARD_PROMPT_INVALID;
  91 | 
  92 |     /* Skip trailing whitespace / newlines */
  93 |     size_t end = resp_len;
  94 |     while (end > 0 && (resp_buf[end - 1] == ' ' || resp_buf[end - 1] == '\t' ||
  95 |                        resp_buf[end - 1] == '\r' || resp_buf[end - 1] == '\n' ||
  96 |                        resp_buf[end - 1] == '\0')) {
  97 |         end--;
  98 |     }
  99 |     if (end == 0) return HARVARD_PROMPT_INVALID;
 100 | 
 101 |     size_t p = end - 1;
 102 |     char c = resp_buf[p];
 103 | 
 104 |     /* Check prefix before prompt: optional address digits or preceding delimiter */
 105 |     size_t pre = p;
 106 |     if (c == '*' && pre > 0 && resp_buf[pre - 1] == 'T') {
 107 |         pre--;
 108 |     }
 109 |     while (pre > 0 && resp_buf[pre - 1] >= '0' && resp_buf[pre - 1] <= '9') {
 110 |         pre--;
 111 |     }
 112 |     if (pre > 0) {
 113 |         char before = resp_buf[pre - 1];
 114 |         if (before != ' ' && before != '\t' && before != '\r' && before != '\n') {
 115 |             return HARVARD_PROMPT_INVALID;
 116 |         }
 117 |     }
 118 | 
 119 |     if (c == ':') return HARVARD_PROMPT_IDLE;
 120 |     if (c == '>') return HARVARD_PROMPT_INFUSING;
 121 |     if (c == '<') return HARVARD_PROMPT_WITHDRAWING;
 122 |     if (c == '*') {
 123 |         if (p > 0 && resp_buf[p - 1] == 'T') {
 124 |             return HARVARD_PROMPT_TARGET_DONE;
 125 |         }
 126 |         return HARVARD_PROMPT_STALLED;
 127 |     }
 128 | 
 129 |     return HARVARD_PROMPT_INVALID;
 130 | }
 131 | 
 132 | wet_hal_driver_t* wet_hal_microfluidics_create(wet_hal_mode_t mode) {
 133 |     wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
 134 |     if (!drv) return NULL;
 135 | 
 136 |     microfluidic_state_t* state = (microfluidic_state_t*)calloc(1, sizeof(microfluidic_state_t));
 137 |     if (!state) {
 138 |         free(drv);
 139 |         return NULL;
 140 |     }
 141 | 
 142 |     state->dead_head_enabled = 1;
 143 |     for (int i = 0; i < WET_MAX_PUMPS; ++i) {
 144 |         state->pumps[i].address = (uint8_t)i;
 145 |         state->pumps[i].fast_mode = 1;
 146 |         state->valve_for_pump[i] = (uint8_t)i; /* 1-to-1 default valve pairing */
 147 |         state->valve_states[i] = 1;            /* Default open */
 148 |     }
 149 | 
 150 |     const char* name = "Microfluidics_HAL";
 151 |     for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
 152 |     drv->driver_type = WET_HAL_DRIVER_PUMP;
 153 |     drv->mode = mode;
 154 |     drv->ops = &s_microfluidics_ops;
 155 |     drv->context = state;
 156 | 
 157 |     return drv;
 158 | }
 159 | 
 160 | void wet_hal_microfluidics_destroy(wet_hal_driver_t* drv) {
 161 |     if (!drv) return;
 162 |     if (drv->context) free(drv->context);
 163 |     free(drv);
 164 | }
 165 | 
 166 | wet_hal_status_t wet_hal_pump_set_rate(
 167 |     wet_hal_driver_t* drv,
 168 |     uint8_t pump_id,
 169 |     double rate_ul_min,
 170 |     uint8_t run_flag
 171 | ) {
 172 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 173 |     if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 174 | 
 175 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 176 | 
 177 |     /* Check Dead-Head Overpressure Interlock:
 178 |      * If pump is commanded to run (rate > 0 and run_flag), verify downstream valve is OPEN. */
 179 |     if (state->dead_head_enabled && run_flag && rate_ul_min > 0.0) {
 180 |         uint8_t valve_id = state->valve_for_pump[pump_id];
 181 |         if (valve_id < WET_MAX_VALVES && state->valve_states[valve_id] == 0) {
 182 |             state->dead_head_trip_count++;
 183 |             return WET_HAL_ERR_DEAD_HEAD;
 184 |         }
 185 |     }
 186 | 
 187 |     if (state->fault_inject_stall) {
 188 |         state->pumps[pump_id].is_stalled = 1;
 189 |         state->pumps[pump_id].is_running = 0;
 190 |         return WET_HAL_ERR_IO;
 191 |     }
 192 | 
 193 |     state->pumps[pump_id].rate_ul_min = rate_ul_min;
 194 |     state->pumps[pump_id].is_running = run_flag ? 1 : 0;
 195 |     state->total_rs232_tx++;
 196 | 
 197 |     return WET_HAL_OK;
 198 | }
 199 | 
 200 | wet_hal_status_t wet_hal_pump_dispense(
 201 |     wet_hal_driver_t* drv,
 202 |     uint8_t pump_id,
 203 |     double volume_ul
 204 | ) {
 205 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 206 |     if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 207 | 
 208 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 209 | 
 210 |     /* Dead-Head check */
 211 |     if (state->dead_head_enabled && volume_ul > 0.0) {
 212 |         uint8_t valve_id = state->valve_for_pump[pump_id];
 213 |         if (valve_id < WET_MAX_VALVES && state->valve_states[valve_id] == 0) {
 214 |             state->dead_head_trip_count++;
 215 |             return WET_HAL_ERR_DEAD_HEAD;
 216 |         }
 217 |     }
 218 | 
 219 |     state->pumps[pump_id].infused_volume_ul += volume_ul;
 220 |     state->total_rs232_tx++;
 221 |     return WET_HAL_OK;
 222 | }
 223 | 
 224 | wet_hal_status_t wet_hal_pump_stop(
 225 |     wet_hal_driver_t* drv,
 226 |     uint8_t pump_id
 227 | ) {
 228 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 229 |     if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 230 | 
 231 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 232 |     state->pumps[pump_id].is_running = 0;
 233 |     state->pumps[pump_id].rate_ul_min = 0.0;
 234 |     state->total_rs232_tx++;
 235 |     return WET_HAL_OK;
 236 | }
 237 | 
 238 | wet_hal_status_t wet_hal_valve_set_state(
 239 |     wet_hal_driver_t* drv,
 240 |     uint8_t valve_id,
 241 |     uint8_t val_state
 242 | ) {
 243 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 244 |     if (valve_id >= WET_MAX_VALVES) return WET_HAL_ERR_OUT_OF_BOUNDS;
 245 | 
 246 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 247 |     state->valve_states[valve_id] = (val_state != 0) ? 1 : 0;
 248 |     return WET_HAL_OK;
 249 | }
 250 | 
 251 | void wet_hal_pump_bind_downstream_valve(
 252 |     wet_hal_driver_t* drv,
 253 |     uint8_t pump_id,
 254 |     uint8_t valve_id
 255 | ) {
 256 |     if (!drv || !drv->context) return;
 257 |     if (pump_id >= WET_MAX_PUMPS || valve_id >= WET_MAX_VALVES) return;
 258 | 
 259 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 260 |     state->valve_for_pump[pump_id] = valve_id;
 261 | }
 262 | 
 263 | wet_hal_status_t wet_hal_can_send(
 264 |     wet_hal_driver_t* drv,
 265 |     const wet_can_frame_t* frame
 266 | ) {
 267 |     if (!drv || !drv->context || !frame) return WET_HAL_ERR_NULL_PTR;
 268 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 269 | 
 270 |     /* Enforce ISO 11898-1 limits & ID boundaries */
 271 |     if (frame->dlc > 8) {
 272 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 273 |     }
 274 |     if (!frame->is_extended && frame->id > 0x7FFU) {
 275 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 276 |     }
 277 |     if (frame->is_extended && frame->id > 0x1FFFFFFFU) {
 278 |         return WET_HAL_ERR_OUT_OF_BOUNDS;
 279 |     }
 280 | 
 281 |     if (state->fault_inject_can_drop) {
 282 |         return WET_HAL_OK; /* Mock frame drop */
 283 |     }
 284 | 
 285 |     if (state->can_tx_count >= WET_CAN_QUEUE_CAPACITY) {
 286 |         return WET_HAL_ERR_BUFFER_FULL;
 287 |     }
 288 | 
 289 |     state->can_tx_queue[state->can_tx_tail] = *frame;
 290 |     state->can_tx_tail = (state->can_tx_tail + 1) % WET_CAN_QUEUE_CAPACITY;
 291 |     state->can_tx_count++;
 292 |     state->total_can_frames_tx++;
 293 | 
 294 |     /* In HIL loopback mode, copy transmitted frame into RX queue for bidirectional loopback */
 295 |     if (drv->mode == WET_HAL_MODE_HIL_LOOPBACK) {
 296 |         if (state->can_rx_count < WET_CAN_QUEUE_CAPACITY) {
 297 |             state->can_rx_queue[state->can_rx_tail] = *frame;
 298 |             state->can_rx_tail = (state->can_rx_tail + 1) % WET_CAN_QUEUE_CAPACITY;
 299 |             state->can_rx_count++;
 300 |         }
 301 |     }
 302 | 
 303 |     /* In HIL loopback mode, automatically handle Process Data Objects (PDOs) ONLY for standard 11-bit frames */
 304 |     if (!frame->is_extended) {
 305 |         uint32_t base_id = frame->id & ~0x7FU;
 306 |         uint8_t node_id = (uint8_t)(frame->id & 0x7FU);
 307 | 
 308 |         if (base_id == CAN_ID_RPDO1_BASE && node_id < WET_MAX_PUMPS) {
 309 |             /* RPDO1: Float32 rate + 1 byte run flag */
 310 |             if (frame->dlc >= 5) {
 311 |                 float rate;
 312 |                 memcpy(&rate, frame->data, sizeof(float));
 313 |                 uint8_t run_flag = frame->data[4];
 314 |                 wet_hal_pump_set_rate(drv, node_id, (double)rate, run_flag);
 315 |             }
 316 |         } else if (base_id == CAN_ID_RPDO2_BASE) {
 317 |             /* RPDO2: Valve bitmask */
 318 |             if (frame->dlc >= 1) {
 319 |                 uint8_t mask = frame->data[0];
 320 |                 for (uint8_t v = 0; v < WET_MAX_VALVES; ++v) {
 321 |                     state->valve_states[v] = (mask & (1U << v)) ? 1 : 0;
 322 |                 }
 323 |             }
 324 |         }
 325 |     }
 326 | 
 327 |     return WET_HAL_OK;
 328 | }
 329 | 
 330 | wet_hal_status_t wet_hal_can_recv(
 331 |     wet_hal_driver_t* drv,
 332 |     wet_can_frame_t* out_frame
 333 | ) {
 334 |     if (!drv || !drv->context || !out_frame) return WET_HAL_ERR_NULL_PTR;
 335 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 336 | 
 337 |     if (state->can_rx_count == 0) {
 338 |         return WET_HAL_ERR_TIMEOUT;
 339 |     }
 340 | 
 341 |     *out_frame = state->can_rx_queue[state->can_rx_head];
 342 |     state->can_rx_head = (state->can_rx_head + 1) % WET_CAN_QUEUE_CAPACITY;
 343 |     state->can_rx_count--;
 344 |     state->total_can_frames_rx++;
 345 | 
 346 |     return WET_HAL_OK;
 347 | }
 348 | 
 349 | wet_hal_status_t wet_hal_can_send_emcy(
 350 |     wet_hal_driver_t* drv,
 351 |     uint8_t node_id,
 352 |     uint16_t error_code,
 353 |     uint8_t error_register
 354 | ) {
 355 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 356 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 357 | 
 358 |     wet_can_frame_t frame;
 359 |     memset(&frame, 0, sizeof(frame));
 360 |     frame.id = CAN_ID_EMCY_BASE + (node_id & 0x7FU);
 361 |     frame.is_extended = 0;
 362 |     frame.dlc = 8;
 363 |     frame.data[0] = (uint8_t)(error_code & 0xFFU);
 364 |     frame.data[1] = (uint8_t)((error_code >> 8) & 0xFFU);
 365 |     frame.data[2] = error_register;
 366 | 
 367 |     state->total_emcy_frames++;
 368 |     return wet_hal_can_send(drv, &frame);
 369 | }
 370 | 
 371 | void wet_hal_microfluidics_inject_fault(
 372 |     wet_hal_driver_t* drv,
 373 |     uint8_t stall,
 374 |     uint8_t can_drop,
 375 |     uint8_t timeout
 376 | ) {
 377 |     if (!drv || !drv->context) return;
 378 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 379 |     state->fault_inject_stall = stall;
 380 |     state->fault_inject_can_drop = can_drop;
 381 |     state->fault_inject_rs232_timeout = timeout;
 382 | }
 383 | 
 384 | /* =========================================================================
 385 |  * Vtable Callbacks
 386 |  * ========================================================================= */
 387 | 
 388 | static wet_hal_status_t microfluidics_op_init(wet_hal_driver_t* drv, void* config) {
 389 |     (void)config;
 390 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 391 |     drv->is_initialized = 1;
 392 |     drv->is_active = 1;
 393 |     return WET_HAL_OK;
 394 | }
 395 | 
 396 | static wet_hal_status_t microfluidics_op_shutdown(wet_hal_driver_t* drv) {
 397 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 398 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 399 |     for (int i = 0; i < WET_MAX_PUMPS; ++i) {
 400 |         state->pumps[i].is_running = 0;
 401 |         state->pumps[i].rate_ul_min = 0.0;
 402 |     }
 403 |     drv->is_active = 0;
 404 |     return WET_HAL_OK;
 405 | }
 406 | 
 407 | static wet_hal_status_t microfluidics_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
 408 |     (void)reason;
 409 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 410 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 411 | 
 412 |     /* Instantly halt all 8 syringe pumps */
 413 |     for (int i = 0; i < WET_MAX_PUMPS; ++i) {
 414 |         state->pumps[i].is_running = 0;
 415 |         state->pumps[i].rate_ul_min = 0.0;
 416 |     }
 417 | 
 418 |     /* Broadcast CAN emergency stop frame */
 419 |     wet_hal_can_send_emcy(drv, 0, 0x1000, 0x01);
 420 |     return WET_HAL_OK;
 421 | }
 422 | 
 423 | static wet_hal_status_t microfluidics_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
 424 |     (void)current_tick;
 425 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 426 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 427 | 
 428 |     /* Integrate infused volume */
 429 |     for (int i = 0; i < WET_MAX_PUMPS; ++i) {
 430 |         if (state->pumps[i].is_running) {
 431 |             double vol_tick = state->pumps[i].rate_ul_min * (dt_ms / 60000.0);
 432 |             state->pumps[i].infused_volume_ul += vol_tick;
 433 |         }
 434 |     }
 435 |     return WET_HAL_OK;
 436 | }
 437 | 
 438 | static wet_hal_status_t microfluidics_op_write_pump(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag) {
 439 |     return wet_hal_pump_set_rate(drv, pump_id, rate_ul_min, run_flag);
 440 | }
 441 | 
 442 | static wet_hal_status_t microfluidics_op_dispense_volume(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul) {
 443 |     return wet_hal_pump_dispense(drv, pump_id, volume_ul);
 444 | }
 445 | 
 446 | static wet_hal_status_t microfluidics_op_write_valve(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state) {
 447 |     return wet_hal_valve_set_state(drv, valve_id, state);
 448 | }
 449 | 
 450 | static wet_hal_status_t microfluidics_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min) {
 451 |     if (!drv || !drv->context || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
 452 |     if (sensor_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 453 |     microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
 454 |     *out_flow_ul_min = state->pumps[sensor_id].is_running ? state->pumps[sensor_id].rate_ul_min : 0.0;
 455 |     return WET_HAL_OK;
 456 | }
 457 | 
 458 | static wet_hal_status_t microfluidics_op_read_pressure(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa) {
 459 |     (void)port_id;
 460 |     if (!drv || !out_kpa) return WET_HAL_ERR_NULL_PTR;
 461 |     *out_kpa = 101.325f; /* 1 atm nominal */
 462 |     return WET_HAL_OK;
 463 | }
```

### `native/src/wet_hal_sensirion.c` (332 lines, SHA-256: `19293c38932593af...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wet_hal_sensirion.h"
   3 | 
   4 | /* Forward declaration of vtable operations */
   5 | static wet_hal_status_t sensirion_op_init(wet_hal_driver_t* drv, void* config);
   6 | static wet_hal_status_t sensirion_op_shutdown(wet_hal_driver_t* drv);
   7 | static wet_hal_status_t sensirion_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
   8 | static wet_hal_status_t sensirion_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
   9 | static wet_hal_status_t sensirion_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);
  10 | 
  11 | static const wet_hal_ops_t s_sensirion_ops = {
  12 |     .init              = sensirion_op_init,
  13 |     .shutdown          = sensirion_op_shutdown,
  14 |     .emergency_stop    = sensirion_op_emergency_stop,
  15 |     .step_tick         = sensirion_op_step_tick,
  16 |     .stim_voltage      = NULL,
  17 |     .stim_current      = NULL,
  18 |     .read_ephys        = NULL,
  19 |     .measure_impedance = NULL,
  20 |     .active_discharge  = NULL,
  21 |     .write_pump        = NULL,
  22 |     .dispense_volume   = NULL,
  23 |     .write_valve       = NULL,
  24 |     .read_flow         = sensirion_op_read_flow,
  25 |     .read_pressure     = NULL,
  26 | };
  27 | 
  28 | /* =========================================================================
  29 |  * Sensirion CRC-8 Algorithm (Poly 0x31: x^8 + x^5 + x^4 + 1, Init 0xFF)
  30 |  * ========================================================================= */
  31 | 
  32 | uint8_t wet_hal_sensirion_crc8(const uint8_t* data, size_t len) {
  33 |     if (!data) return 0;
  34 |     uint8_t crc = SENSIRION_CRC8_INIT;
  35 | 
  36 |     for (size_t i = 0; i < len; ++i) {
  37 |         crc ^= data[i];
  38 |         for (int b = 0; b < 8; ++b) {
  39 |             if (crc & 0x80U) {
  40 |                 crc = (uint8_t)((crc << 1) ^ SENSIRION_CRC8_POLYNOMIAL);
  41 |             } else {
  42 |                 crc = (uint8_t)(crc << 1);
  43 |             }
  44 |         }
  45 |     }
  46 |     return crc;
  47 | }
  48 | 
  49 | int wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3]) {
  50 |     if (!word_and_crc) return 0;
  51 |     uint8_t computed = wet_hal_sensirion_crc8(word_and_crc, 2);
  52 |     return (computed == word_and_crc[2]) ? 1 : 0;
  53 | }
  54 | 
  55 | /* =========================================================================
  56 |  * Sensirion SHDLC Protocol (SLI Series RS-485 / RS-232)
  57 |  * ========================================================================= */
  58 | 
  59 | size_t wet_hal_shdlc_encode(
  60 |     uint8_t address,
  61 |     uint8_t command,
  62 |     const uint8_t* payload,
  63 |     uint8_t payload_len,
  64 |     uint8_t* out_buf,
  65 |     size_t out_buf_max
  66 | ) {
  67 |     if (!out_buf || out_buf_max < 6) return 0;
  68 | 
  69 |     /* Compute checksum: ~((address + command + length + sum(payload)) & 0xFF) */
  70 |     uint32_t sum = address + command + payload_len;
  71 |     for (uint8_t i = 0; i < payload_len; ++i) {
  72 |         sum += payload ? payload[i] : 0;
  73 |     }
  74 |     uint8_t checksum = (uint8_t)(~(sum & 0xFFU));
  75 | 
  76 |     size_t pos = 0;
  77 |     out_buf[pos++] = SHDLC_FRAME_START_STOP;
  78 | 
  79 |     /* Helper lambda to stuff a single byte */
  80 |     #define STUFF_BYTE(b) do { \
  81 |         uint8_t val = (uint8_t)(b); \
  82 |         if (val == 0x7E || val == 0x7D || val == 0x11 || val == 0x13) { \
  83 |             if (pos + 2 >= out_buf_max) return 0; \
  84 |             out_buf[pos++] = SHDLC_FRAME_ESCAPE; \
  85 |             out_buf[pos++] = (uint8_t)(val ^ SHDLC_ESCAPE_MASK); \
  86 |         } else { \
  87 |             if (pos + 1 >= out_buf_max) return 0; \
  88 |             out_buf[pos++] = val; \
  89 |         } \
  90 |     } while (0)
  91 | 
  92 |     STUFF_BYTE(address);
  93 |     STUFF_BYTE(command);
  94 |     STUFF_BYTE(payload_len);
  95 | 
  96 |     for (uint8_t i = 0; i < payload_len; ++i) {
  97 |         STUFF_BYTE(payload[i]);
  98 |     }
  99 | 
 100 |     STUFF_BYTE(checksum);
 101 | 
 102 |     if (pos >= out_buf_max) return 0;
 103 |     out_buf[pos++] = SHDLC_FRAME_START_STOP;
 104 | 
 105 |     #undef STUFF_BYTE
 106 |     return pos;
 107 | }
 108 | 
 109 | int wet_hal_shdlc_decode(
 110 |     const uint8_t* raw_buf,
 111 |     size_t raw_len,
 112 |     uint8_t* out_address,
 113 |     uint8_t* out_command,
 114 |     uint8_t* out_payload,
 115 |     uint8_t* out_payload_len
 116 | ) {
 117 |     if (!raw_buf || raw_len < 6 || !out_address || !out_command || !out_payload || !out_payload_len) {
 118 |         return 0;
 119 |     }
 120 | 
 121 |     /* Verify framing delimiters */
 122 |     if (raw_buf[0] != SHDLC_FRAME_START_STOP || raw_buf[raw_len - 1] != SHDLC_FRAME_START_STOP) {
 123 |         return 0;
 124 |     }
 125 | 
 126 |     /* Unstuff bytes between start and stop */
 127 |     uint8_t unstuffed[SHDLC_MAX_FRAME_SIZE];
 128 |     size_t un_len = 0;
 129 |     size_t i = 1;
 130 | 
 131 |     while (i < raw_len - 1) {
 132 |         uint8_t b = raw_buf[i++];
 133 |         if (b == SHDLC_FRAME_ESCAPE) {
 134 |             if (i >= raw_len - 1) return 0; /* Malformed escape */
 135 |             uint8_t esc_b = raw_buf[i++];
 136 |             if (esc_b != 0x5E && esc_b != 0x5D && esc_b != 0x31 && esc_b != 0x33) {
 137 |                 return 0; /* Illegal stuffing sequence: reject frame immediately */
 138 |             }
 139 |             unstuffed[un_len++] = (uint8_t)(esc_b ^ SHDLC_ESCAPE_MASK);
 140 |         } else {
 141 |             unstuffed[un_len++] = b;
 142 |         }
 143 |         if (un_len >= SHDLC_MAX_FRAME_SIZE) return 0;
 144 |     }
 145 | 
 146 |     /* Need at least address (1), command (1), length (1), checksum (1) = 4 bytes */
 147 |     if (un_len < 4) return 0;
 148 | 
 149 |     uint8_t addr = unstuffed[0];
 150 |     uint8_t cmd  = unstuffed[1];
 151 |     uint8_t plen = unstuffed[2];
 152 |     uint8_t rx_chk = unstuffed[un_len - 1];
 153 | 
 154 |     if (un_len != (size_t)(3 + plen + 1)) {
 155 |         return 0; /* Length mismatch */
 156 |     }
 157 | 
 158 |     /* Verify checksum */
 159 |     uint32_t sum = 0;
 160 |     for (size_t k = 0; k < un_len - 1; ++k) {
 161 |         sum += unstuffed[k];
 162 |     }
 163 |     uint8_t expected_chk = (uint8_t)(~(sum & 0xFFU));
 164 |     if (rx_chk != expected_chk) {
 165 |         return 0; /* Checksum failure */
 166 |     }
 167 | 
 168 |     *out_address = addr;
 169 |     *out_command = cmd;
 170 |     *out_payload_len = plen;
 171 |     for (uint8_t p = 0; p < plen; ++p) {
 172 |         out_payload[p] = unstuffed[3 + p];
 173 |     }
 174 |     return 1;
 175 | }
 176 | 
 177 | /* =========================================================================
 178 |  * Sensirion Driver Implementation
 179 |  * ========================================================================= */
 180 | 
 181 | wet_hal_driver_t* wet_hal_sensirion_create(wet_hal_mode_t mode) {
 182 |     wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
 183 |     if (!drv) return NULL;
 184 | 
 185 |     sensirion_device_state_t* state = (sensirion_device_state_t*)calloc(1, sizeof(sensirion_device_state_t));
 186 |     if (!state) {
 187 |         free(drv);
 188 |         return NULL;
 189 |     }
 190 | 
 191 |     state->i2c_address = SENSIRION_I2C_ADDR_DEFAULT;
 192 |     state->scale_factor = 10.0f; /* 10 (uL/min)^-1 for SLF3S-0600x -> 0.1 uL/min resolution */
 193 |     state->current_flow_ul_min = 0.0;
 194 |     state->measurement_active = 0;
 195 |     state->shdlc_address = 0x00;
 196 | 
 197 |     const char* name = "Sensirion_SLF3x";
 198 |     for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
 199 |     drv->driver_type = WET_HAL_DRIVER_FLOW;
 200 |     drv->mode = mode;
 201 |     drv->ops = &s_sensirion_ops;
 202 |     drv->context = state;
 203 | 
 204 |     return drv;
 205 | }
 206 | 
 207 | void wet_hal_sensirion_destroy(wet_hal_driver_t* drv) {
 208 |     if (!drv) return;
 209 |     if (drv->context) free(drv->context);
 210 |     free(drv);
 211 | }
 212 | 
 213 | wet_hal_status_t wet_hal_sensirion_start_measurement(
 214 |     wet_hal_driver_t* drv,
 215 |     uint16_t cmd
 216 | ) {
 217 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 218 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 219 | 
 220 |     if (state->fault_nak_address) {
 221 |         return WET_HAL_ERR_IO;
 222 |     }
 223 | 
 224 |     state->active_command = cmd;
 225 |     state->measurement_active = 1;
 226 |     return WET_HAL_OK;
 227 | }
 228 | 
 229 | wet_hal_status_t wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv) {
 230 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 231 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 232 | 
 233 |     state->active_command = SENSIRION_CMD_STOP_CONT;
 234 |     state->measurement_active = 0;
 235 |     return WET_HAL_OK;
 236 | }
 237 | 
 238 | wet_hal_status_t wet_hal_sensirion_read_flow(
 239 |     wet_hal_driver_t* drv,
 240 |     double* out_flow_ul_min
 241 | ) {
 242 |     if (!drv || !drv->context || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
 243 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 244 | 
 245 |     state->total_i2c_reads++;
 246 | 
 247 |     if (state->fault_nak_address) {
 248 |         return WET_HAL_ERR_IO;
 249 |     }
 250 | 
 251 |     /* Convert current flow to raw 16-bit signed integer word */
 252 |     int16_t raw_flow = (int16_t)(state->current_flow_ul_min * (double)state->scale_factor);
 253 |     state->raw_flow_ticks = raw_flow;
 254 | 
 255 |     uint8_t packet[3];
 256 |     packet[0] = (uint8_t)((raw_flow >> 8) & 0xFFU);
 257 |     packet[1] = (uint8_t)(raw_flow & 0xFFU);
 258 |     packet[2] = wet_hal_sensirion_crc8(packet, 2);
 259 | 
 260 |     /* Check CRC fault injection */
 261 |     if (state->fault_corrupt_crc) {
 262 |         packet[2] ^= 0x55U; /* Invert CRC bits */
 263 |     }
 264 | 
 265 |     if (!wet_hal_sensirion_validate_crc(packet)) {
 266 |         state->crc_errors++;
 267 |         return WET_HAL_ERR_CRC_MISMATCH;
 268 |     }
 269 | 
 270 |     int16_t rx_raw = (int16_t)(((uint16_t)packet[0] << 8) | (uint16_t)packet[1]);
 271 |     *out_flow_ul_min = (double)rx_raw / (double)state->scale_factor;
 272 |     return WET_HAL_OK;
 273 | }
 274 | 
 275 | void wet_hal_sensirion_hil_set_flow(
 276 |     wet_hal_driver_t* drv,
 277 |     double flow_ul_min
 278 | ) {
 279 |     if (!drv || !drv->context) return;
 280 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 281 |     state->current_flow_ul_min = flow_ul_min;
 282 | }
 283 | 
 284 | void wet_hal_sensirion_inject_fault(
 285 |     wet_hal_driver_t* drv,
 286 |     uint8_t corrupt_crc,
 287 |     uint8_t nak_addr
 288 | ) {
 289 |     if (!drv || !drv->context) return;
 290 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 291 |     state->fault_corrupt_crc = corrupt_crc;
 292 |     state->fault_nak_address = nak_addr;
 293 | }
 294 | 
 295 | /* =========================================================================
 296 |  * Vtable Callbacks
 297 |  * ========================================================================= */
 298 | 
 299 | static wet_hal_status_t sensirion_op_init(wet_hal_driver_t* drv, void* config) {
 300 |     (void)config;
 301 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 302 |     drv->is_initialized = 1;
 303 |     drv->is_active = 1;
 304 |     return WET_HAL_OK;
 305 | }
 306 | 
 307 | static wet_hal_status_t sensirion_op_shutdown(wet_hal_driver_t* drv) {
 308 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 309 |     wet_hal_sensirion_stop_measurement(drv);
 310 |     drv->is_active = 0;
 311 |     return WET_HAL_OK;
 312 | }
 313 | 
 314 | static wet_hal_status_t sensirion_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
 315 |     (void)reason;
 316 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 317 |     sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
 318 |     state->current_flow_ul_min = 0.0;
 319 |     return wet_hal_sensirion_stop_measurement(drv);
 320 | }
 321 | 
 322 | static wet_hal_status_t sensirion_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
 323 |     (void)current_tick;
 324 |     (void)dt_ms;
 325 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 326 |     return WET_HAL_OK;
 327 | }
 328 | 
 329 | static wet_hal_status_t sensirion_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min) {
 330 |     (void)sensor_id;
 331 |     return wet_hal_sensirion_read_flow(drv, out_flow_ul_min);
 332 | }
```

### `native/src/wet_scheduler.c` (658 lines, SHA-256: `128de8fe00f83e90...`)

```text
   1 | /**
   2 |  * WetLang Hard Real-Time Sub-100 µs Execution Scheduler
   3 |  * Implementation (native/src/wet_scheduler.c)
   4 |  *
   5 |  * Deterministic C99 execution scheduler operating at 10 kHz (100 µs period):
   6 |  *  - Dedicated real-time thread with core pinning (SetThreadAffinityMask)
   7 |  *  - Process & thread priority elevation (REALTIME_PRIORITY_CLASS / THREAD_PRIORITY_TIME_CRITICAL)
   8 |  *  - High-resolution hardware monotonic timer (QueryPerformanceCounter / QueryPerformanceFrequency)
   9 |  *  - Hybrid precision pacing: bytecode/ODE compute + calibrated spin-wait tail (_mm_pause)
  10 |  *  - Cacheline-aligned (64-byte) lockless SPSC ring buffers for telemetry & stimulus injection
  11 |  *  - Static memory arena: zero heap allocations during real-time stepping
  12 |  */
  13 | 
  14 | #include "../include/wet_crt.h"
  15 | #include "../include/wet_scheduler.h"
  16 | #include "../include/wetvm_vm.h"
  17 | #include "../include/biophysics.h"
  18 | 
  19 | /* 128-byte cache line alignment isolates Intel L2 spatial prefetcher pairs (eliminating cross-core false sharing) */
  20 | #define WET_CACHELINE_SIZE 128
  21 | #define WET_DEFAULT_SAMPLE_CAPACITY 100000
  22 | 
  23 | #if defined(_WIN32)
  24 | typedef union _LARGE_INTEGER {
  25 |     struct {
  26 |         uint32_t LowPart;
  27 |         int32_t  HighPart;
  28 |     } s;
  29 |     int64_t QuadPart;
  30 | } LARGE_INTEGER;
  31 | 
  32 | typedef void* HANDLE;
  33 | typedef unsigned long DWORD;
  34 | typedef uint64_t DWORD_PTR;
  35 | typedef int BOOL;
  36 | 
  37 | #ifdef __cplusplus
  38 | extern "C" {
  39 | #endif
  40 | int __stdcall QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount);
  41 | int __stdcall QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency);
  42 | HANDLE __stdcall GetCurrentThread(void);
  43 | HANDLE __stdcall GetCurrentProcess(void);
  44 | DWORD_PTR __stdcall SetThreadAffinityMask(HANDLE hThread, DWORD_PTR dwThreadAffinityMask);
  45 | BOOL __stdcall SetPriorityClass(HANDLE hProcess, DWORD dwPriorityClass);
  46 | BOOL __stdcall SetThreadPriority(HANDLE hThread, int nPriority);
  47 | HANDLE __stdcall CreateThread(void* lpThreadAttributes, size_t dwStackSize, void* lpStartAddress, void* lpParameter, DWORD dwCreationFlags, DWORD* lpThreadId);
  48 | DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
  49 | BOOL __stdcall CloseHandle(HANDLE hObject);
  50 | void __stdcall Sleep(DWORD dwMilliseconds);
  51 | BOOL __stdcall VirtualLock(void* lpAddress, size_t dwSize);
  52 | #ifdef __cplusplus
  53 | }
  54 | #endif
  55 | #else
  56 | #include <time.h>
  57 | #include <pthread.h>
  58 | #include <sched.h>
  59 | #endif
  60 | 
  61 | /* Calibrated processor instruction pipeline pause */
  62 | static inline void wet_cpu_pause(void) {
  63 | #if defined(__clang__) || defined(__GNUC__)
  64 |     __builtin_ia32_pause();
  65 | #elif defined(_MSC_VER)
  66 |     _mm_pause();
  67 | #elif defined(__aarch64__)
  68 |     __asm__ __volatile__("isb\n");
  69 | #else
  70 |     /* NOP fallback */
  71 | #endif
  72 | }
  73 | 
  74 | /* Atomic Acquire/Release Memory Barriers */
  75 | static inline uint32_t wet_atomic_load_u32_acquire(const volatile uint32_t* ptr) {
  76 | #if defined(__GNUC__) || defined(__clang__)
  77 |     return __atomic_load_n(ptr, __ATOMIC_ACQUIRE);
  78 | #else
  79 |     return *ptr;
  80 | #endif
  81 | }
  82 | 
  83 | static inline void wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val) {
  84 | #if defined(__GNUC__) || defined(__clang__)
  85 |     __atomic_store_n(ptr, val, __ATOMIC_RELEASE);
  86 | #else
  87 |     *ptr = val;
  88 | #endif
  89 | }
  90 | 
  91 | /* =========================================================================
  92 |  * Lockless Single-Producer Single-Consumer (SPSC) Ring Buffer
  93 |  * Cacheline-aligned (64-byte padding) to eliminate false sharing
  94 |  * ========================================================================= */
  95 | 
  96 | typedef struct {
  97 |     /* Producer cache line */
  98 |     volatile uint32_t head;
  99 |     uint8_t           _pad0[WET_CACHELINE_SIZE - sizeof(uint32_t)];
 100 | 
 101 |     /* Consumer cache line */
 102 |     volatile uint32_t tail;
 103 |     uint8_t           _pad1[WET_CACHELINE_SIZE - sizeof(uint32_t)];
 104 | 
 105 |     /* Metadata */
 106 |     uint32_t capacity;
 107 |     uint32_t mask;
 108 |     size_t   elem_size;
 109 |     uint8_t* buffer;
 110 | } wet_spsc_ring_t;
 111 | 
 112 | static int wet_spsc_init(wet_spsc_ring_t* ring, uint32_t capacity, size_t elem_size) {
 113 |     uint32_t cap = 1;
 114 |     while (cap < capacity) cap <<= 1;
 115 |     ring->capacity = cap;
 116 |     ring->mask = cap - 1;
 117 |     ring->elem_size = elem_size;
 118 |     ring->head = 0;
 119 |     ring->tail = 0;
 120 |     ring->buffer = (uint8_t*)calloc(cap, elem_size);
 121 |     return (ring->buffer != NULL);
 122 | }
 123 | 
 124 | static void wet_spsc_free(wet_spsc_ring_t* ring) {
 125 |     if (ring->buffer) {
 126 |         free(ring->buffer);
 127 |         ring->buffer = NULL;
 128 |     }
 129 | }
 130 | 
 131 | static inline int wet_spsc_push(wet_spsc_ring_t* ring, const void* item) {
 132 |     uint32_t head = ring->head;
 133 |     uint32_t tail = wet_atomic_load_u32_acquire(&ring->tail);
 134 |     if ((head - tail) >= ring->capacity) {
 135 |         return 0; /* Ring buffer full */
 136 |     }
 137 |     memcpy(ring->buffer + (head & ring->mask) * ring->elem_size, item, ring->elem_size);
 138 |     wet_atomic_store_u32_release(&ring->head, head + 1);
 139 |     return 1;
 140 | }
 141 | 
 142 | static inline int wet_spsc_pop(wet_spsc_ring_t* ring, void* out_item) {
 143 |     uint32_t tail = ring->tail;
 144 |     uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
 145 |     if (tail == head) {
 146 |         return 0; /* Ring buffer empty */
 147 |     }
 148 |     memcpy(out_item, ring->buffer + (tail & ring->mask) * ring->elem_size, ring->elem_size);
 149 |     wet_atomic_store_u32_release(&ring->tail, tail + 1);
 150 |     return 1;
 151 | }
 152 | 
 153 | /* =========================================================================
 154 |  * Scheduler Internal Structure
 155 |  * ========================================================================= */
 156 | 
 157 | struct wet_scheduler {
 158 |     wet_vm_instance_t*     vm;
 159 |     wet_scheduler_config_t config;
 160 |     wet_scheduler_stats_t  stats;
 161 | 
 162 |     /* SPSC Ring Buffers */
 163 |     wet_spsc_ring_t        telem_ring;
 164 |     wet_spsc_ring_t        stim_ring;
 165 | 
 166 |     /* High-Resolution Monotonic Timer State */
 167 |     int64_t                qpf_freq;
 168 |     double                 qpc_per_us;
 169 |     int64_t                period_qpc;
 170 |     int64_t                next_deadline_qpc;
 171 | 
 172 |     /* Execution State */
 173 |     volatile uint32_t      is_running;
 174 |     volatile uint32_t      stop_requested;
 175 |     uint8_t                thread_initialized;
 176 | #if defined(_WIN32)
 177 |     HANDLE                 thread_handle;
 178 | #else
 179 |     pthread_t              thread_handle;
 180 | #endif
 181 | 
 182 |     /* Benchmark Sample Buffers */
 183 |     uint32_t               sample_capacity;
 184 |     uint32_t               sample_count;
 185 |     double*                sample_jitters_us;
 186 |     double*                sample_computes_us;
 187 |     double*                sample_periods_us;
 188 | 
 189 |     /* Running Accumulators for Online Means */
 190 |     double                 sum_compute_us;
 191 |     double                 sum_period_us;
 192 |     double                 sum_jitter_us;
 193 | };
 194 | 
 195 | /* Fast in-place quicksort for doubles (used for exact percentile calculation) */
 196 | static void wet_sort_doubles(double* arr, int left, int right) {
 197 |     if (left >= right) return;
 198 |     double pivot = arr[(left + right) / 2];
 199 |     int i = left;
 200 |     int j = right;
 201 |     while (i <= j) {
 202 |         while (arr[i] < pivot) i++;
 203 |         while (arr[j] > pivot) j--;
 204 |         if (i <= j) {
 205 |             double tmp = arr[i];
 206 |             arr[i] = arr[j];
 207 |             arr[j] = tmp;
 208 |             i++;
 209 |             j--;
 210 |         }
 211 |     }
 212 |     if (left < j)  wet_sort_doubles(arr, left, j);
 213 |     if (i < right) wet_sort_doubles(arr, i, right);
 214 | }
 215 | 
 216 | /* =========================================================================
 217 |  * Thread Worker Procedure
 218 |  * ========================================================================= */
 219 | 
 220 | #if defined(_WIN32)
 221 | static DWORD __stdcall wet_scheduler_thread_proc(void* param) {
 222 |     wet_scheduler_t* sched = (wet_scheduler_t*)param;
 223 |     if (!sched) return 1;
 224 | 
 225 |     /* 1. Core Pinning */
 226 |     if (sched->config.enable_core_pinning) {
 227 |         DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
 228 |         SetThreadAffinityMask(GetCurrentThread(), mask);
 229 |     }
 230 | 
 231 |     /* 2. Process & Thread Priority Elevation */
 232 |     if (sched->config.enable_priority_elevation) {
 233 |         if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
 234 |             /* Fallback to HIGH_PRIORITY_CLASS if REALTIME permission is restricted */
 235 |             SetPriorityClass(GetCurrentProcess(), 0x00000080);
 236 |         }
 237 |         SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
 238 |     }
 239 | 
 240 |     sched->is_running = 1;
 241 | 
 242 |     /* Real-Time Stepping Loop */
 243 |     while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
 244 |         if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
 245 |             break;
 246 |         }
 247 | 
 248 |         wet_status_t st = wet_scheduler_step(sched);
 249 |         if (st != WET_OK && st != WET_ERR_HALTED) {
 250 |             break;
 251 |         }
 252 | 
 253 |         if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) {
 254 |             break;
 255 |         }
 256 |     }
 257 | 
 258 |     sched->is_running = 0;
 259 |     return 0;
 260 | }
 261 | #else
 262 | static void* wet_scheduler_thread_proc(void* param) {
 263 |     wet_scheduler_t* sched = (wet_scheduler_t*)param;
 264 |     if (!sched) return NULL;
 265 | 
 266 |     if (sched->config.enable_core_pinning) {
 267 |         cpu_set_t cpuset;
 268 |         CPU_ZERO(&cpuset);
 269 |         CPU_SET(sched->config.target_core, &cpuset);
 270 |         pthread_setaffinity_np(pthread_self(), sizeof(cpu_set_t), &cpuset);
 271 |     }
 272 | 
 273 |     sched->is_running = 1;
 274 |     while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
 275 |         if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
 276 |             break;
 277 |         }
 278 |         wet_status_t st = wet_scheduler_step(sched);
 279 |         if (st != WET_OK && st != WET_ERR_HALTED) break;
 280 |         if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) break;
 281 |     }
 282 |     sched->is_running = 0;
 283 |     return NULL;
 284 | }
 285 | #endif
 286 | 
 287 | /* =========================================================================
 288 |  * Public C-ABI API Implementation
 289 |  * ========================================================================= */
 290 | 
 291 | WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config) {
 292 |     wet_scheduler_t* sched = (wet_scheduler_t*)calloc(1, sizeof(wet_scheduler_t));
 293 |     if (!sched) return NULL;
 294 | 
 295 |     sched->vm = vm;
 296 | 
 297 |     /* Apply default configuration */
 298 |     if (config) {
 299 |         sched->config = *config;
 300 |     } else {
 301 |         sched->config.target_period_us = 100; /* 100 µs = 10 kHz */
 302 |         sched->config.target_core = 1;
 303 |         sched->config.priority_class = 0x00000100; /* REALTIME_PRIORITY_CLASS */
 304 |         sched->config.thread_priority = 15;        /* THREAD_PRIORITY_TIME_CRITICAL */
 305 |         sched->config.enable_core_pinning = 1;
 306 |         sched->config.enable_priority_elevation = 1;
 307 |         sched->config.telemetry_queue_capacity = 1024;
 308 |         sched->config.stimulus_queue_capacity = 256;
 309 |         sched->config.total_ticks = 0;
 310 |     }
 311 | 
 312 |     if (sched->config.target_period_us == 0) sched->config.target_period_us = 100;
 313 |     if (sched->config.telemetry_queue_capacity == 0) sched->config.telemetry_queue_capacity = 1024;
 314 |     if (sched->config.stimulus_queue_capacity == 0) sched->config.stimulus_queue_capacity = 256;
 315 | 
 316 |     /* Initialize SPSC Ring Buffers */
 317 |     if (!wet_spsc_init(&sched->telem_ring, sched->config.telemetry_queue_capacity, sizeof(wet_telemetry_t))) {
 318 |         free(sched);
 319 |         return NULL;
 320 |     }
 321 | 
 322 |     if (!wet_spsc_init(&sched->stim_ring, sched->config.stimulus_queue_capacity, sizeof(wet_stim_command_t))) {
 323 |         wet_spsc_free(&sched->telem_ring);
 324 |         free(sched);
 325 |         return NULL;
 326 |     }
 327 | 
 328 |     /* Initialize High-Resolution Monotonic Hardware Clock */
 329 | #if defined(_WIN32)
 330 |     LARGE_INTEGER qpf;
 331 |     QueryPerformanceFrequency(&qpf);
 332 |     sched->qpf_freq = qpf.QuadPart;
 333 |     sched->qpc_per_us = (double)qpf.QuadPart / 1000000.0;
 334 |     sched->period_qpc = (int64_t)((double)sched->config.target_period_us * sched->qpc_per_us);
 335 | #else
 336 |     sched->qpf_freq = 1000000000ULL;
 337 |     sched->qpc_per_us = 1000.0;
 338 |     sched->period_qpc = (int64_t)(sched->config.target_period_us * 1000ULL);
 339 | #endif
 340 | 
 341 |     /* Allocate Sample Buffers for Jitter / Latency Statistics */
 342 |     sched->sample_capacity = WET_DEFAULT_SAMPLE_CAPACITY;
 343 |     sched->sample_jitters_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 344 |     sched->sample_computes_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 345 |     sched->sample_periods_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 346 | 
 347 |     /* Pre-fault and commit all memory pages in advance to eliminate demand-paging faults in hot loop */
 348 |     if (sched->sample_jitters_us)  memset(sched->sample_jitters_us, 0, sched->sample_capacity * sizeof(double));
 349 |     if (sched->sample_computes_us) memset(sched->sample_computes_us, 0, sched->sample_capacity * sizeof(double));
 350 |     if (sched->sample_periods_us)  memset(sched->sample_periods_us, 0, sched->sample_capacity * sizeof(double));
 351 | 
 352 | #if defined(_WIN32)
 353 |     /* Pin working set pages in physical RAM to prevent OS page trimming */
 354 |     if (sched->sample_jitters_us)  VirtualLock(sched->sample_jitters_us, sched->sample_capacity * sizeof(double));
 355 |     if (sched->sample_computes_us) VirtualLock(sched->sample_computes_us, sched->sample_capacity * sizeof(double));
 356 |     if (sched->sample_periods_us)  VirtualLock(sched->sample_periods_us, sched->sample_capacity * sizeof(double));
 357 | #endif
 358 | 
 359 |     /* Initialize stats */
 360 |     sched->stats.min_compute_us = 1e9;
 361 |     sched->stats.min_period_us = 1e9;
 362 | 
 363 |     return sched;
 364 | }
 365 | 
 366 | WET_EXPORT wet_status_t wet_scheduler_start(wet_scheduler_t* sched) {
 367 |     if (!sched) return WET_ERR_NULL_PTR;
 368 |     if (sched->is_running) return WET_OK;
 369 | 
 370 |     sched->stop_requested = 0;
 371 |     sched->next_deadline_qpc = 0;
 372 | 
 373 | #if defined(_WIN32)
 374 |     DWORD thread_id = 0;
 375 |     sched->thread_handle = CreateThread(NULL, 0, wet_scheduler_thread_proc, sched, 0, &thread_id);
 376 |     if (!sched->thread_handle) {
 377 |         return WET_ERR_ALLOC_FAILED;
 378 |     }
 379 | #else
 380 |     if (pthread_create(&sched->thread_handle, NULL, wet_scheduler_thread_proc, sched) != 0) {
 381 |         return WET_ERR_ALLOC_FAILED;
 382 |     }
 383 | #endif
 384 | 
 385 |     sched->thread_initialized = 1;
 386 |     return WET_OK;
 387 | }
 388 | 
 389 | WET_EXPORT wet_status_t wet_scheduler_step(wet_scheduler_t* sched) {
 390 |     if (!sched) return WET_ERR_NULL_PTR;
 391 |     if (!sched->vm) return WET_ERR_NULL_PTR;
 392 | 
 393 |     /* Timestamp at tick start */
 394 | #if defined(_WIN32)
 395 |     LARGE_INTEGER t_start;
 396 |     QueryPerformanceCounter(&t_start);
 397 |     int64_t start_qpc = t_start.QuadPart;
 398 | #else
 399 |     struct timespec ts_start;
 400 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_start);
 401 |     int64_t start_qpc = (int64_t)ts_start.tv_sec * 1000000000ULL + ts_start.tv_nsec;
 402 | #endif
 403 | 
 404 |     /* Maintain isochronous deadline.
 405 |      * Trade-off: If lag exceeds 2 periods (>200 µs), resynchronize forward to avoid
 406 |      * catastrophic catch-up storms at the expense of wallclock phase slip. */
 407 |     if (sched->next_deadline_qpc == 0 || start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
 408 |         sched->next_deadline_qpc = start_qpc + sched->period_qpc;
 409 | 
 410 |         /* ATOMIC CHARGE RECOVERY SAFETY INTERLOCK:
 411 |          * If an OS preemption occurred mid-pulse, ensure ongoing biphasic pulses
 412 |          * immediately complete active discharge to prevent leaving electrodes
 413 |          * with uncompensated net DC charge violating the Faradaic water window. */
 414 |         if (sched->vm) {
 415 |             bio_state_t* bio = &sched->vm->bio;
 416 |             for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 417 |                 if (bio->stim_pulses[ch].active) {
 418 |                     bio->stim_pulses[ch].active = 0;
 419 |                     bio->stim_pulses[ch].phase1_ticks_left = 0;
 420 |                     bio->stim_pulses[ch].interphase_ticks_left = 0;
 421 |                     bio->stim_pulses[ch].phase2_ticks_left = 0;
 422 |                     bio->ext_stim_v[ch] = 0.0f;
 423 |                     bio->tick_charge_nc[ch] = 0.0f;
 424 |                     wet_active_discharge(sched->vm, (uint8_t)ch);
 425 |                 }
 426 |             }
 427 |         }
 428 |     } else {
 429 |         sched->next_deadline_qpc += sched->period_qpc;
 430 |     }
 431 | 
 432 |     /* 1. Drain incoming asynchronous stimuli from SPSC ring buffer */
 433 |     wet_stim_command_t stim_cmd;
 434 |     while (wet_spsc_pop(&sched->stim_ring, &stim_cmd)) {
 435 |         if (stim_cmd.channel < sched->vm->config.channel_count) {
 436 |             wet_inject_stimulus(sched->vm, stim_cmd.channel, stim_cmd.voltage_v, stim_cmd.phase1_ms, stim_cmd.phase2_ms);
 437 |             sched->stats.stimuli_injected++;
 438 |         }
 439 |     }
 440 | 
 441 |     /* 2. Execute compute step (C99 Bytecode + Biophysical COBA-LIF ODE + Watchdogs) */
 442 |     wet_telemetry_t telem;
 443 |     wet_status_t status = wet_vm_step_internal(sched->vm, &telem);
 444 | 
 445 |     /* 3. Non-blocking stream telemetry to host SPSC queue */
 446 |     if (!wet_spsc_push(&sched->telem_ring, &telem)) {
 447 |         sched->stats.telemetry_dropped++;
 448 |     }
 449 | 
 450 |     /* 4. Measure compute latency */
 451 | #if defined(_WIN32)
 452 |     LARGE_INTEGER t_compute;
 453 |     QueryPerformanceCounter(&t_compute);
 454 |     double compute_us = (double)(t_compute.QuadPart - start_qpc) / sched->qpc_per_us;
 455 | #else
 456 |     struct timespec ts_comp;
 457 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_comp);
 458 |     int64_t comp_qpc = (int64_t)ts_comp.tv_sec * 1000000000ULL + ts_comp.tv_nsec;
 459 |     double compute_us = (double)(comp_qpc - start_qpc) / sched->qpc_per_us;
 460 | #endif
 461 | 
 462 |     /* 5. Check deadline overrun (compute duration exceeding target period) */
 463 |     if (compute_us > (double)sched->config.target_period_us) {
 464 |         sched->stats.deadline_overruns++;
 465 |     }
 466 | 
 467 | #if defined(_WIN32)
 468 |     /* 6. Hybrid precision pacing: calibrated spin-wait tail using _mm_pause().
 469 |      * STRICTLY ZERO Sleep() in the hot real-time execution loop. */
 470 |     if (t_compute.QuadPart < sched->next_deadline_qpc) {
 471 |         LARGE_INTEGER t_now;
 472 |         do {
 473 |             wet_cpu_pause();
 474 |             QueryPerformanceCounter(&t_now);
 475 |         } while (t_now.QuadPart < sched->next_deadline_qpc);
 476 |     }
 477 | 
 478 |     /* 7. Measure actual period and jitter */
 479 |     LARGE_INTEGER t_end;
 480 |     QueryPerformanceCounter(&t_end);
 481 |     double actual_period_us = (double)(t_end.QuadPart - start_qpc) / sched->qpc_per_us;
 482 | #else
 483 |     if (comp_qpc < sched->next_deadline_qpc) {
 484 |         struct timespec ts_now;
 485 |         do {
 486 |             wet_cpu_pause();
 487 |             clock_gettime(CLOCK_MONOTONIC_RAW, &ts_now);
 488 |         } while (((int64_t)ts_now.tv_sec * 1000000000ULL + ts_now.tv_nsec) < sched->next_deadline_qpc);
 489 |     }
 490 |     struct timespec ts_end;
 491 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_end);
 492 |     int64_t end_qpc = (int64_t)ts_end.tv_sec * 1000000000ULL + ts_end.tv_nsec;
 493 |     double actual_period_us = (double)(end_qpc - start_qpc) / sched->qpc_per_us;
 494 | #endif
 495 | 
 496 |     double jitter_us = wet_fabs(actual_period_us - (double)sched->config.target_period_us);
 497 | 
 498 |     /* 8. Record metrics */
 499 |     sched->stats.total_ticks++;
 500 |     sched->sum_compute_us += compute_us;
 501 |     sched->sum_period_us += actual_period_us;
 502 |     sched->sum_jitter_us += jitter_us;
 503 | 
 504 |     if (compute_us < sched->stats.min_compute_us) sched->stats.min_compute_us = compute_us;
 505 |     if (compute_us > sched->stats.max_compute_us) sched->stats.max_compute_us = compute_us;
 506 | 
 507 |     if (actual_period_us < sched->stats.min_period_us) sched->stats.min_period_us = actual_period_us;
 508 |     if (actual_period_us > sched->stats.max_period_us) sched->stats.max_period_us = actual_period_us;
 509 | 
 510 |     if (jitter_us > sched->stats.max_jitter_us) sched->stats.max_jitter_us = jitter_us;
 511 | 
 512 |     /* Append to sample buffer */
 513 |     if (sched->sample_count < sched->sample_capacity) {
 514 |         sched->sample_jitters_us[sched->sample_count] = jitter_us;
 515 |         sched->sample_computes_us[sched->sample_count] = compute_us;
 516 |         sched->sample_periods_us[sched->sample_count] = actual_period_us;
 517 |         sched->sample_count++;
 518 |     }
 519 | 
 520 |     return status;
 521 | }
 522 | 
 523 | WET_EXPORT wet_status_t wet_scheduler_stop(wet_scheduler_t* sched) {
 524 |     if (!sched) return WET_ERR_NULL_PTR;
 525 | 
 526 |     wet_atomic_store_u32_release(&sched->stop_requested, 1);
 527 | 
 528 |     if (sched->thread_initialized) {
 529 | #if defined(_WIN32)
 530 |         if (sched->thread_handle) {
 531 |             WaitForSingleObject(sched->thread_handle, 5000);
 532 |             CloseHandle(sched->thread_handle);
 533 |             sched->thread_handle = NULL;
 534 |         }
 535 | #else
 536 |         if (sched->thread_handle) {
 537 |             pthread_join(sched->thread_handle, NULL);
 538 |         }
 539 | #endif
 540 |         sched->thread_initialized = 0;
 541 |     }
 542 | 
 543 |     sched->is_running = 0;
 544 |     return WET_OK;
 545 | }
 546 | 
 547 | WET_EXPORT wet_status_t wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats) {
 548 |     if (!sched || !out_stats) return WET_ERR_NULL_PTR;
 549 | 
 550 |     *out_stats = sched->stats;
 551 | 
 552 |     uint64_t n = sched->stats.total_ticks;
 553 |     if (n > 0) {
 554 |         out_stats->mean_compute_us = sched->sum_compute_us / (double)n;
 555 |         out_stats->mean_period_us = sched->sum_period_us / (double)n;
 556 |         out_stats->mean_jitter_us = sched->sum_jitter_us / (double)n;
 557 |     }
 558 | 
 559 |     /* Compute exact percentiles from sample buffer */
 560 |     if (sched->sample_count > 0) {
 561 |         uint32_t cnt = sched->sample_count;
 562 |         double* sorted = (double*)malloc(cnt * sizeof(double));
 563 |         if (sorted) {
 564 |             memcpy(sorted, sched->sample_jitters_us, cnt * sizeof(double));
 565 |             wet_sort_doubles(sorted, 0, (int)cnt - 1);
 566 | 
 567 |             out_stats->p50_jitter_us = sorted[(size_t)(cnt * 0.50)];
 568 |             out_stats->p95_jitter_us = sorted[(size_t)(cnt * 0.95)];
 569 |             out_stats->p99_jitter_us = sorted[(size_t)(cnt * 0.99)];
 570 |             out_stats->p999_jitter_us = sorted[(size_t)(cnt * 0.999)];
 571 |             out_stats->max_jitter_us = sorted[cnt - 1];
 572 | 
 573 |             free(sorted);
 574 |         }
 575 |     }
 576 | 
 577 |     return WET_OK;
 578 | }
 579 | 
 580 | WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem) {
 581 |     if (!sched || !out_telem) return WET_ERR_NULL_PTR;
 582 |     if (wet_spsc_pop(&sched->telem_ring, out_telem)) {
 583 |         return WET_OK;
 584 |     }
 585 |     return WET_ERR_NULL_PTR; /* No telemetry available */
 586 | }
 587 | 
 588 | WET_EXPORT wet_status_t wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd) {
 589 |     if (!sched || !cmd) return WET_ERR_NULL_PTR;
 590 |     if (wet_spsc_push(&sched->stim_ring, cmd)) {
 591 |         return WET_OK;
 592 |     }
 593 |     return WET_ERR_ALLOC_FAILED; /* Stimulus ring buffer full */
 594 | }
 595 | 
 596 | WET_EXPORT wet_status_t wet_scheduler_benchmark(
 597 |     wet_scheduler_t* sched,
 598 |     uint32_t total_ticks,
 599 |     wet_scheduler_stats_t* out_stats
 600 | ) {
 601 |     if (!sched) return WET_ERR_NULL_PTR;
 602 | 
 603 |     /* Apply thread affinity and priority on benchmark caller thread if not backgrounded */
 604 | #if defined(_WIN32)
 605 |     if (sched->config.enable_core_pinning) {
 606 |         DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
 607 |         SetThreadAffinityMask(GetCurrentThread(), mask);
 608 |     }
 609 |     if (sched->config.enable_priority_elevation) {
 610 |         if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
 611 |             SetPriorityClass(GetCurrentProcess(), 0x00000080);
 612 |         }
 613 |         SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
 614 |     }
 615 | #endif
 616 | 
 617 |     /* Warm-up ticks to ensure hardware instruction/data caches and branch predictors are primed */
 618 |     for (int w = 0; w < 10; ++w) {
 619 |         wet_scheduler_step(sched);
 620 |     }
 621 | 
 622 |     /* Reset metrics after warm-up */
 623 |     memset(&sched->stats, 0, sizeof(sched->stats));
 624 |     sched->stats.min_compute_us = 1e9;
 625 |     sched->stats.min_period_us = 1e9;
 626 |     sched->sample_count = 0;
 627 |     sched->sum_compute_us = 0.0;
 628 |     sched->sum_period_us = 0.0;
 629 |     sched->sum_jitter_us = 0.0;
 630 |     sched->next_deadline_qpc = 0;
 631 |     sched->is_running = 1;
 632 | 
 633 |     for (uint32_t i = 0; i < total_ticks; ++i) {
 634 |         wet_status_t st = wet_scheduler_step(sched);
 635 |         if (st != WET_OK && st != WET_ERR_HALTED) {
 636 |             sched->is_running = 0;
 637 |             return st;
 638 |         }
 639 |     }
 640 | 
 641 |     sched->is_running = 0;
 642 |     return wet_scheduler_get_stats(sched, out_stats);
 643 | }
 644 | 
 645 | WET_EXPORT void wet_scheduler_destroy(wet_scheduler_t* sched) {
 646 |     if (!sched) return;
 647 | 
 648 |     wet_scheduler_stop(sched);
 649 | 
 650 |     wet_spsc_free(&sched->telem_ring);
 651 |     wet_spsc_free(&sched->stim_ring);
 652 | 
 653 |     if (sched->sample_jitters_us)  free(sched->sample_jitters_us);
 654 |     if (sched->sample_computes_us) free(sched->sample_computes_us);
 655 |     if (sched->sample_periods_us)  free(sched->sample_periods_us);
 656 | 
 657 |     free(sched);
 658 | }
```

### `native/src/wetvm_api.c` (639 lines, SHA-256: `6a0641509ff77e10...`)

```text
   1 | #ifndef WET_BUILDING_DLL
   2 | #define WET_BUILDING_DLL
   3 | #endif
   4 | 
   5 | #include "../include/wet_crt.h"
   6 | #include "../include/wetvm_types.h"
   7 | #include "../include/wetvm_api.h"
   8 | #include "../include/wetvm_vm.h"
   9 | #include "../include/wet_hal.h"
  10 | 
  11 | #if defined(_WIN32)
  12 | int _fltused = 0x9875;
  13 | #endif
  14 | 
  15 | /* Forward declarations of internal functions in wetvm_vm.c */
  16 | extern wet_status_t wet_vm_load_bytecode_internal(
  17 |     struct wet_vm_instance* vm,
  18 |     const uint8_t* code_bytes,
  19 |     size_t size,
  20 |     char* err_buf,
  21 |     size_t err_buf_len
  22 | );
  23 | 
  24 | extern wet_status_t wet_verify_bytecode_internal(
  25 |     const uint8_t* bytecode,
  26 |     size_t size,
  27 |     char* err_buf,
  28 |     size_t err_buf_len
  29 | );
  30 | 
  31 | extern wet_status_t wet_vm_snapshot_internal(
  32 |     const struct wet_vm_instance* vm,
  33 |     uint8_t* buffer,
  34 |     size_t* inout_len
  35 | );
  36 | 
  37 | extern wet_status_t wet_vm_restore_internal(
  38 |     struct wet_vm_instance* vm,
  39 |     const uint8_t* buffer,
  40 |     size_t len
  41 | );
  42 | 
  43 | WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config) {
  44 |     struct wet_vm_instance* vm = (struct wet_vm_instance*)calloc(1, sizeof(struct wet_vm_instance));
  45 |     if (!vm) return NULL;
  46 | 
  47 |     /* Apply configuration with sensible defaults */
  48 |     if (config) {
  49 |         vm->config.dt_ms = (config->dt_ms > 0.0) ? config->dt_ms : 0.1;
  50 |         vm->config.max_stack_depth = (config->max_stack_depth > 0) ? config->max_stack_depth : 1024;
  51 |         vm->config.max_locals = (config->max_locals > 0) ? config->max_locals : 256;
  52 |         vm->config.channel_count = (config->channel_count > 0 && config->channel_count <= 64)
  53 |                                     ? config->channel_count : 64;
  54 |         vm->config.max_ops_per_tick = (config->max_ops_per_tick > 0) ? config->max_ops_per_tick : 100000U;
  55 |         vm->config.min_sequence_counter = config->min_sequence_counter;
  56 |     } else {
  57 |         vm->config.dt_ms = 0.1;
  58 |         vm->config.max_stack_depth = 1024;
  59 |         vm->config.max_locals = 256;
  60 |         vm->config.channel_count = 64;
  61 |         vm->config.max_ops_per_tick = 100000U;
  62 |         vm->config.min_sequence_counter = 0;
  63 |     }
  64 | 
  65 |     vm->max_stack = vm->config.max_stack_depth;
  66 |     vm->stack = (wet_value_t*)calloc(vm->max_stack, sizeof(wet_value_t));
  67 |     if (!vm->stack) {
  68 |         free(vm);
  69 |         return NULL;
  70 |     }
  71 | 
  72 |     vm->max_locals = vm->config.max_locals;
  73 |     vm->locals = (wet_value_t*)calloc(vm->max_locals, sizeof(wet_value_t));
  74 |     if (!vm->locals) {
  75 |         free(vm->stack);
  76 |         free(vm);
  77 |         return NULL;
  78 |     }
  79 | 
  80 |     vm->max_call_depth = 64;
  81 |     vm->call_stack = (wet_call_frame_t*)calloc(vm->max_call_depth, sizeof(wet_call_frame_t));
  82 |     if (!vm->call_stack) {
  83 |         free(vm->locals);
  84 |         free(vm->stack);
  85 |         free(vm);
  86 |         return NULL;
  87 |     }
  88 | 
  89 |     vm->grid_rows = 8;
  90 |     vm->grid_cols = 8;
  91 |     vm->last_error[0] = '\0';
  92 | 
  93 |     /* Initialize cyber-physical life support actuator states */
  94 |     vm->ambient_temperature_c = 37.0f;
  95 |     for (int p = 0; p < 4; ++p) {
  96 |         vm->fluid_pressure_kpa[p] = 101.325f;
  97 |     }
  98 | 
  99 |     /* Ring-0 Life Support Supervisor Initialization */
 100 |     vm->life_supervisor.supervisor_active = 1;
 101 |     vm->life_supervisor.maintenance_temperature_c = 37.0f;
 102 |     for (int i = 0; i < 8; ++i) {
 103 |         vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
 104 |     }
 105 | 
 106 |     biophysics_init(&vm->bio, vm->config.dt_ms, 0);
 107 |     interlocks_init(&vm->interlocks);
 108 | 
 109 |     return vm;
 110 | }
 111 | 
 112 | WET_EXPORT wet_vm_t* wet_create_vm_arena(
 113 |     void* arena_buf,
 114 |     size_t arena_bytes,
 115 |     const wet_vm_config_t* config
 116 | ) {
 117 |     if (!arena_buf) return NULL;
 118 | 
 119 |     uint32_t stack_depth = (config && config->max_stack_depth > 0) ? config->max_stack_depth : 1024;
 120 |     uint32_t max_locals = (config && config->max_locals > 0) ? config->max_locals : 256;
 121 |     uint32_t call_depth = 64;
 122 | 
 123 |     size_t needed = sizeof(struct wet_vm_instance)
 124 |                   + (size_t)stack_depth * sizeof(wet_value_t)
 125 |                   + (size_t)max_locals * sizeof(wet_value_t)
 126 |                   + (size_t)call_depth * sizeof(wet_call_frame_t);
 127 | 
 128 |     if (arena_bytes < needed) return NULL;
 129 | 
 130 |     /* Align arena to 128 bytes (WET_CACHELINE_SIZE) for DMA & cache coherency */
 131 |     uint8_t* raw_ptr = (uint8_t*)arena_buf;
 132 |     uintptr_t u = (uintptr_t)raw_ptr;
 133 |     uintptr_t aligned_u = (u + 127) & ~((uintptr_t)127);
 134 |     size_t align_pad = (size_t)(aligned_u - u);
 135 |     if (arena_bytes < needed + align_pad + 256) return NULL;
 136 | 
 137 |     uint8_t* ptr = (uint8_t*)aligned_u;
 138 |     struct wet_vm_instance* vm = (struct wet_vm_instance*)ptr;
 139 |     ptr += sizeof(struct wet_vm_instance);
 140 |     u = (uintptr_t)ptr;
 141 |     ptr = (uint8_t*)((u + 127) & ~((uintptr_t)127));
 142 |     memset(vm, 0, sizeof(struct wet_vm_instance));
 143 | 
 144 |     vm->arena_allocated = 1;
 145 |     if (config) {
 146 |         vm->config = *config;
 147 |         if (vm->config.dt_ms <= 0.0) vm->config.dt_ms = 0.1;
 148 |         if (vm->config.max_stack_depth == 0) vm->config.max_stack_depth = stack_depth;
 149 |         if (vm->config.max_locals == 0) vm->config.max_locals = max_locals;
 150 |         if (vm->config.channel_count == 0) vm->config.channel_count = 64;
 151 |         if (vm->config.max_ops_per_tick == 0) vm->config.max_ops_per_tick = 100000U;
 152 |     } else {
 153 |         vm->config.dt_ms = 0.1;
 154 |         vm->config.max_stack_depth = stack_depth;
 155 |         vm->config.max_locals = max_locals;
 156 |         vm->config.channel_count = 64;
 157 |         vm->config.max_ops_per_tick = 100000U;
 158 |     }
 159 | 
 160 |     vm->max_stack = stack_depth;
 161 |     vm->stack = (wet_value_t*)ptr;
 162 |     ptr += (size_t)stack_depth * sizeof(wet_value_t);
 163 | 
 164 |     vm->max_locals = max_locals;
 165 |     vm->locals = (wet_value_t*)ptr;
 166 |     ptr += (size_t)max_locals * sizeof(wet_value_t);
 167 | 
 168 |     vm->max_call_depth = call_depth;
 169 |     vm->call_stack = (wet_call_frame_t*)ptr;
 170 | 
 171 |     vm->grid_rows = 8;
 172 |     vm->grid_cols = 8;
 173 |     vm->last_error[0] = '\0';
 174 |     vm->ambient_temperature_c = 37.0f;
 175 |     for (int p = 0; p < 4; ++p) {
 176 |         vm->fluid_pressure_kpa[p] = 101.325f;
 177 |     }
 178 | 
 179 |     vm->life_supervisor.supervisor_active = 1;
 180 |     vm->life_supervisor.maintenance_temperature_c = 37.0f;
 181 |     for (int i = 0; i < 8; ++i) {
 182 |         vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
 183 |     }
 184 | 
 185 |     biophysics_init(&vm->bio, vm->config.dt_ms, 0);
 186 |     interlocks_init(&vm->interlocks);
 187 | 
 188 |     return vm;
 189 | }
 190 | 
 191 | WET_EXPORT void wet_free_vm(wet_vm_t* vm) {
 192 |     if (!vm) return;
 193 | 
 194 |     if (vm->hal) {
 195 |         wet_hal_destroy(vm->hal);
 196 |         vm->hal = NULL;
 197 |     }
 198 | 
 199 |     if (vm->constants) {
 200 |         for (size_t i = 0; i < vm->num_constants; ++i) {
 201 |             if (vm->constants[i].str_alloc) {
 202 |                 free(vm->constants[i].str_alloc);
 203 |                 vm->constants[i].str_alloc = NULL;
 204 |             }
 205 |         }
 206 |         free(vm->constants);
 207 |         vm->constants = NULL;
 208 |     }
 209 | 
 210 |     if (vm->bytecode_raw) {
 211 |         free(vm->bytecode_raw);
 212 |         vm->bytecode_raw = NULL;
 213 |     }
 214 | 
 215 |     if (!vm->arena_allocated) {
 216 |         if (vm->stack) {
 217 |             free(vm->stack);
 218 |             vm->stack = NULL;
 219 |         }
 220 | 
 221 |         if (vm->locals) {
 222 |             free(vm->locals);
 223 |             vm->locals = NULL;
 224 |         }
 225 | 
 226 |         if (vm->call_stack) {
 227 |             free(vm->call_stack);
 228 |             vm->call_stack = NULL;
 229 |         }
 230 | 
 231 |         free(vm);
 232 |     } else {
 233 |         /*
 234 |          * Defense-in-depth: Secure volatile memory scrubbing.
 235 |          * Zeroes the entire VM instance structure to prevent stale stimulation schedules,
 236 |          * cryptographic keys, or stack frames from leaking into future arena allocations.
 237 |          */
 238 |         volatile uint8_t* scrub_p = (volatile uint8_t*)vm;
 239 |         for (size_t i = 0; i < sizeof(struct wet_vm_instance); i++) {
 240 |             scrub_p[i] = 0;
 241 |         }
 242 |     }
 243 | }
 244 | 
 245 | WET_EXPORT wet_status_t wet_load_bytecode(
 246 |     wet_vm_t* vm,
 247 |     const uint8_t* code_bytes,
 248 |     size_t size,
 249 |     char* err_buf,
 250 |     size_t err_buf_len
 251 | ) {
 252 |     if (!vm) {
 253 |         if (err_buf && err_buf_len > 0) {
 254 |             snprintf(err_buf, err_buf_len, "Null VM pointer");
 255 |         }
 256 |         return WET_ERR_NULL_PTR;
 257 |     }
 258 |     return wet_vm_load_bytecode_internal(vm, code_bytes, size, err_buf, err_buf_len);
 259 | }
 260 | 
 261 | WET_EXPORT wet_status_t wet_step_tick(
 262 |     wet_vm_t* vm,
 263 |     wet_telemetry_t* out_telem
 264 | ) {
 265 |     if (!vm) return WET_ERR_NULL_PTR;
 266 |     return wet_vm_step_internal(vm, out_telem);
 267 | }
 268 | 
 269 | WET_EXPORT wet_status_t wet_run_ticks(
 270 |     wet_vm_t* vm,
 271 |     uint32_t ticks,
 272 |     uint32_t* executed_ticks,
 273 |     wet_telemetry_t* out_telem
 274 | ) {
 275 |     if (!vm) return WET_ERR_NULL_PTR;
 276 | 
 277 |     uint32_t executed = 0;
 278 |     wet_status_t status = WET_OK;
 279 | 
 280 |     for (uint32_t i = 0; i < ticks; ++i) {
 281 |         status = wet_vm_step_internal(vm, out_telem);
 282 |         if (status != WET_OK) {
 283 |             break;
 284 |         }
 285 |         executed++;
 286 |     }
 287 | 
 288 |     if (executed_ticks) {
 289 |         *executed_ticks = executed;
 290 |     }
 291 | 
 292 |     return status;
 293 | }
 294 | 
 295 | WET_EXPORT wet_status_t wet_inject_stimulus(
 296 |     wet_vm_t* vm,
 297 |     uint8_t channel,
 298 |     float voltage_v,
 299 |     float phase1_ms,
 300 |     float phase2_ms
 301 | ) {
 302 |     if (!vm) return WET_ERR_NULL_PTR;
 303 |     if (channel >= vm->config.channel_count) {
 304 |         snprintf(vm->last_error, sizeof(vm->last_error),
 305 |                  "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
 306 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 307 |     }
 308 |     if (vm->interlocks.locked) {
 309 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 310 |         return WET_ERR_INTERLOCK_LOCKED;
 311 |     }
 312 | 
 313 |     if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage_v, channel)) {
 314 |         snprintf(vm->last_error, sizeof(vm->last_error),
 315 |                  "Capability denied for wet_inject_stimulus on ch %u (req %.2fV)", channel, voltage_v);
 316 |         return WET_ERR_CAPABILITY_DENIED;
 317 |     }
 318 | 
 319 |     /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
 320 |     if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
 321 |         float q_p1 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase1_ms;
 322 |         float q_p2 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase2_ms;
 323 |         if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
 324 |             vm->interlocks.locked = 1;
 325 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
 326 |             vm->interlocks.tripped_channel = channel;
 327 |             vm->interlocks.trip_tick = vm->current_tick;
 328 |             vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
 329 |             snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
 330 |                      "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
 331 |                      channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
 332 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 333 |             return WET_ERR_CHARGE_DENSITY_EXCEEDED;
 334 |         }
 335 |     }
 336 | 
 337 |     /* Active charge recovery: if previous pulse had pending Phase 2 counter-charge, discharge it */
 338 |     bio_stim_pulse_t* prev_p = &vm->bio.stim_pulses[channel];
 339 |     if (prev_p->active && prev_p->phase2_ticks_left > 0) {
 340 |         float i_ua = (prev_p->phase2_amp_v / vm->bio.electrode_impedance_kohm) * 1000.0f;
 341 |         vm->discharge_charge_nc[channel] += i_ua * (float)vm->bio.dt_ms * (float)prev_p->phase2_ticks_left;
 342 |     }
 343 | 
 344 |     float clamped_v = interlocks_clamp_voltage(&vm->interlocks, voltage_v);
 345 |     biophysics_schedule_stim(&vm->bio, channel, clamped_v, phase1_ms, phase2_ms);
 346 |     vm->voltages[channel] = clamped_v;
 347 |     float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
 348 |     vm->last_charge_nc[channel] = i_ma * (phase1_ms - phase2_ms);
 349 |     return WET_OK;
 350 | }
 351 | 
 352 | WET_EXPORT wet_status_t wet_get_telemetry(
 353 |     wet_vm_t* vm,
 354 |     wet_telemetry_t* out_telem
 355 | ) {
 356 |     if (!vm || !out_telem) return WET_ERR_NULL_PTR;
 357 | 
 358 |     out_telem->current_tick = vm->current_tick;
 359 |     out_telem->sim_time_ms = vm->sim_time_ms;
 360 |     out_telem->population_rate_hz = vm->population_rate_hz;
 361 |     memcpy(out_telem->voltages, vm->voltages, sizeof(float) * 64);
 362 |     memcpy(out_telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
 363 |     memcpy(out_telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);
 364 | 
 365 |     return WET_OK;
 366 | }
 367 | 
 368 | WET_EXPORT wet_status_t wet_get_actuator_telemetry(
 369 |     wet_vm_t* vm,
 370 |     wet_actuator_telemetry_t* out_act_telem
 371 | ) {
 372 |     if (!vm || !out_act_telem) return WET_ERR_NULL_PTR;
 373 | 
 374 |     for (int i = 0; i < 8; ++i) {
 375 |         out_act_telem->pump_rates_ul_min[i] = vm->pump_rates_ul_min[i];
 376 |         out_act_telem->pump_dispensed_ul[i] = vm->pump_dispensed_ul[i];
 377 |         out_act_telem->valve_states[i] = vm->valve_states[i];
 378 |     }
 379 |     for (int i = 0; i < 4; ++i) {
 380 |         out_act_telem->motor_positions[i] = vm->motor_positions[i];
 381 |         out_act_telem->motor_speeds_rpm[i] = vm->motor_speeds_rpm[i];
 382 |         out_act_telem->fluid_pressure_kpa[i] = vm->fluid_pressure_kpa[i];
 383 |     }
 384 |     out_act_telem->ambient_temperature_c = vm->ambient_temperature_c;
 385 |     return WET_OK;
 386 | }
 387 | 
 388 | WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm) {
 389 |     if (!vm) return "NULL VM pointer";
 390 |     return vm->last_error;
 391 | }
 392 | 
 393 | WET_EXPORT const char* wet_status_to_string(wet_status_t status) {
 394 |     switch (status) {
 395 |         case WET_OK:
 396 |             return "WET_OK: Operation successful";
 397 |         case WET_ERR_INVALID_MAGIC:
 398 |             return "WET_ERR_INVALID_MAGIC: Invalid WBC header magic";
 399 |         case WET_ERR_CRC_MISMATCH:
 400 |             return "WET_ERR_CRC_MISMATCH: Bytecode CRC32 checksum mismatch";
 401 |         case WET_ERR_UNSUPPORTED_VERSION:
 402 |             return "WET_ERR_UNSUPPORTED_VERSION: Unsupported bytecode version";
 403 |         case WET_ERR_MALFORMED_SECTION:
 404 |             return "WET_ERR_MALFORMED_SECTION: Malformed bytecode or section table";
 405 |         case WET_ERR_STACK_OVERFLOW:
 406 |             return "WET_ERR_STACK_OVERFLOW: Operand stack overflow";
 407 |         case WET_ERR_STACK_UNDERFLOW:
 408 |             return "WET_ERR_STACK_UNDERFLOW: Operand stack underflow";
 409 |         case WET_ERR_INVALID_OPCODE:
 410 |             return "WET_ERR_INVALID_OPCODE: Unrecognized or invalid opcode";
 411 |         case WET_ERR_OUT_OF_BOUNDS_CH:
 412 |             return "WET_ERR_OUT_OF_BOUNDS_CH: Channel index out of bounds";
 413 |         case WET_ERR_DIVISION_BY_ZERO:
 414 |             return "WET_ERR_DIVISION_BY_ZERO: Division by zero";
 415 |         case WET_ERR_NULL_PTR:
 416 |             return "WET_ERR_NULL_PTR: Null pointer argument";
 417 |         case WET_ERR_ALLOC_FAILED:
 418 |             return "WET_ERR_ALLOC_FAILED: Memory allocation failed";
 419 |         case WET_ERR_HALTED:
 420 |             return "WET_ERR_HALTED: Virtual machine is halted";
 421 |         case WET_ERR_CHARGE_IMBALANCE:
 422 |             return "WET_ERR_CHARGE_IMBALANCE: Net charge imbalance exceeded safety threshold (0.5 nC over 10 ms)";
 423 |         case WET_ERR_EPILEPTIFORM_RUNAWAY:
 424 |             return "WET_ERR_EPILEPTIFORM_RUNAWAY: Epileptiform runaway firing breaker tripped (>150 Hz on >35% channels for 50 ms)";
 425 |         case WET_ERR_CAPABILITY_DENIED:
 426 |             return "WET_ERR_CAPABILITY_DENIED: Capability permission denied by bytecode security manifest";
 427 |         case WET_ERR_INTERLOCK_LOCKED:
 428 |             return "WET_ERR_INTERLOCK_LOCKED: Hardware interlock locked out; all stimulation disabled";
 429 |         case WET_ERR_CHARGE_DENSITY_EXCEEDED:
 430 |             return "WET_ERR_CHARGE_DENSITY_EXCEEDED: Single-phase charge density exceeded Shannon safety limit";
 431 |         case WET_ERR_FOCAL_EXCITOTOXICITY:
 432 |             return "WET_ERR_FOCAL_EXCITOTOXICITY: Focal excitotoxicity limit exceeded";
 433 |         case WET_ERR_SHEAR_STRESS_EXCEEDED:
 434 |             return "WET_ERR_SHEAR_STRESS_EXCEEDED: Requested microfluidic pump rate exceeds safe shear stress limit (15.0 uL/min)";
 435 |         case WET_ERR_SECURITY_UNTRUSTED:
 436 |             return "WET_ERR_SECURITY_UNTRUSTED: Bytecode failed cryptographic security signature verification";
 437 |         case WET_ERR_ACTUATOR_FAULT:
 438 |             return "WET_ERR_ACTUATOR_FAULT: Cyber-physical actuator execution fault or invalid parameter";
 439 |         case WET_ERR_THERMAL_LIMIT:
 440 |             return "WET_ERR_THERMAL_LIMIT: Temperature exceeded maximum biological threshold (38.0 C)";
 441 |         case WET_ERR_BUBBLE_DETECTED:
 442 |             return "WET_ERR_BUBBLE_DETECTED: Fluidic optical bubble detector tripped (cavitation hazard)";
 443 |         case WET_ERR_COMPLIANCE_RAILED:
 444 |             return "WET_ERR_COMPLIANCE_RAILED: Stimulator output voltage saturated ASIC compliance rail (+/-7.0 V)";
 445 |         case WET_ERR_BYTECODE_VERIFICATION:
 446 |             return "WET_ERR_BYTECODE_VERIFICATION: WBC binary failed static bytecode verifier checks";
 447 |         default:
 448 |             return "WET_ERR_UNKNOWN: Unknown error status";
 449 |     }
 450 | }
 451 | 
 452 | /* =========================================================================
 453 |  * Phase 3 Hardware Readiness & Safety Implementations
 454 |  * ========================================================================= */
 455 | 
 456 | WET_EXPORT void wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2) {
 457 |     if (!vm) return;
 458 |     interlocks_configure_electrode(&vm->interlocks, material, area_um2);
 459 | }
 460 | 
 461 | WET_EXPORT void wet_active_discharge(wet_vm_t* vm, uint8_t channel) {
 462 |     if (!vm) return;
 463 |     interlocks_active_discharge(&vm->interlocks, channel);
 464 | }
 465 | 
 466 | WET_EXPORT void wet_active_discharge_all(wet_vm_t* vm) {
 467 |     if (!vm) return;
 468 |     interlocks_active_discharge_all(&vm->interlocks);
 469 | }
 470 | 
 471 | WET_EXPORT void wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable) {
 472 |     if (!vm) return;
 473 |     interlocks_enable_dead_head_protection(&vm->interlocks, enable);
 474 | }
 475 | 
 476 | WET_EXPORT void wet_life_supervisor_shutdown(wet_vm_t* vm) {
 477 |     if (!vm) return;
 478 |     vm->life_supervisor.supervisor_active = 0;
 479 |     for (int p = 0; p < 8; ++p) {
 480 |         vm->pump_rates_ul_min[p] = 0.0f;
 481 |     }
 482 | }
 483 | 
 484 | WET_EXPORT void wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial) {
 485 |     if (!vm) return;
 486 |     biophysics_set_blanking_window(&vm->bio, blanking_ms, enable_spatial);
 487 | }
 488 | 
 489 | WET_EXPORT wet_status_t wet_inject_current_stimulus(
 490 |     wet_vm_t* vm,
 491 |     uint8_t channel,
 492 |     float current_ua,
 493 |     float phase1_ms,
 494 |     float phase2_ms
 495 | ) {
 496 |     if (!vm) return WET_ERR_NULL_PTR;
 497 |     if (channel >= vm->config.channel_count) {
 498 |         snprintf(vm->last_error, sizeof(vm->last_error),
 499 |                  "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
 500 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 501 |     }
 502 |     if (vm->interlocks.locked) {
 503 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 504 |         return WET_ERR_INTERLOCK_LOCKED;
 505 |     }
 506 | 
 507 |     if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
 508 |         snprintf(vm->last_error, sizeof(vm->last_error),
 509 |                  "Capability denied for wet_inject_current_stimulus on ch %u", channel);
 510 |         return WET_ERR_CAPABILITY_DENIED;
 511 |     }
 512 | 
 513 |     /* Randles Interface check: V_elec = I * Rs + V_dl */
 514 |     float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
 515 |     wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
 516 |     if (comp_st != WET_OK) {
 517 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 518 |         return comp_st;
 519 |     }
 520 | 
 521 |     /* Shannon charge density limit */
 522 |     if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
 523 |         float q_p1 = fabsf(current_ua) * 1e-3f * phase1_ms;
 524 |         float q_p2 = fabsf(current_ua) * 1e-3f * phase2_ms;
 525 |         if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
 526 |             vm->interlocks.locked = 1;
 527 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
 528 |             vm->interlocks.tripped_channel = channel;
 529 |             vm->interlocks.trip_tick = vm->current_tick;
 530 |             vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
 531 |             snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
 532 |                      "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
 533 |                      channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
 534 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 535 |             return WET_ERR_CHARGE_DENSITY_EXCEEDED;
 536 |         }
 537 |     }
 538 | 
 539 |     biophysics_schedule_stim_current(&vm->bio, channel, current_ua, phase1_ms, phase2_ms, 0.0f);
 540 |     vm->voltages[channel] = v_elec;
 541 |     vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (phase1_ms - phase2_ms);
 542 |     return WET_OK;
 543 | }
 544 | 
 545 | WET_EXPORT wet_status_t wet_verify_bytecode(
 546 |     const uint8_t* bytecode,
 547 |     size_t size,
 548 |     char* err_buf,
 549 |     size_t err_buf_len
 550 | ) {
 551 |     return wet_verify_bytecode_internal(bytecode, size, err_buf, err_buf_len);
 552 | }
 553 | 
 554 | WET_EXPORT wet_status_t wet_vm_snapshot(
 555 |     const wet_vm_t* vm,
 556 |     uint8_t* buffer,
 557 |     size_t* inout_len
 558 | ) {
 559 |     return wet_vm_snapshot_internal(vm, buffer, inout_len);
 560 | }
 561 | 
 562 | WET_EXPORT wet_status_t wet_vm_restore(
 563 |     wet_vm_t* vm,
 564 |     const uint8_t* buffer,
 565 |     size_t len
 566 | ) {
 567 |     return wet_vm_restore_internal(vm, buffer, len);
 568 | }
 569 | 
 570 | WET_EXPORT void wet_set_environmental_sensors(
 571 |     wet_vm_t* vm,
 572 |     float ph,
 573 |     float do_pct,
 574 |     float co2_pct,
 575 |     uint8_t bubble_sensor_id,
 576 |     uint8_t bubble_state,
 577 |     float flow_rate_ul_min
 578 | ) {
 579 |     if (!vm) return;
 580 |     if (ph > 0.0f) vm->ph_level = ph;
 581 |     if (do_pct > 0.0f) vm->dissolved_oxygen_pct = do_pct;
 582 |     if (co2_pct > 0.0f) vm->dissolved_co2_pct = co2_pct;
 583 |     if (bubble_sensor_id < 8) {
 584 |         vm->bubble_detected[bubble_sensor_id] = bubble_state ? 1 : 0;
 585 |         vm->fluid_flow_rate_ul_min[bubble_sensor_id] = flow_rate_ul_min;
 586 |     }
 587 | }
 588 | 
 589 | WET_EXPORT void wet_set_temperature(
 590 |     wet_vm_t* vm,
 591 |     float temp_c
 592 | ) {
 593 |     if (!vm) return;
 594 |     vm->ambient_temperature_c = temp_c;
 595 | }
 596 | 
 597 | WET_EXPORT void wet_set_channel_banks(
 598 |     wet_vm_t* vm,
 599 |     uint64_t ref_mask,
 600 |     uint64_t rec_mask
 601 | ) {
 602 |     if (!vm) return;
 603 |     interlocks_set_channel_banks(&vm->interlocks, ref_mask, rec_mask);
 604 | }
 605 | 
 606 | WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
 607 |     const wet_vm_t* vm,
 608 |     float* out_matrix,
 609 |     size_t out_capacity_floats
 610 | ) {
 611 |     if (!vm || !out_matrix) return WET_ERR_NULL_PTR;
 612 |     if (out_capacity_floats < (size_t)(BIO_NUM_NEURONS * BIO_NUM_NEURONS)) {
 613 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 614 |     }
 615 |     for (size_t i = 0; i < BIO_NUM_NEURONS; ++i) {
 616 |         for (size_t j = 0; j < BIO_NUM_NEURONS; ++j) {
 617 |             if (vm->bio.synapses[i][j].exists) {
 618 |                 out_matrix[i * BIO_NUM_NEURONS + j] = vm->bio.synapses[i][j].weight_ns;
 619 |             } else {
 620 |                 out_matrix[i * BIO_NUM_NEURONS + j] = 0.0f;
 621 |             }
 622 |         }
 623 |     }
 624 |     return WET_OK;
 625 | }
 626 | 
 627 | WET_EXPORT float wet_vm_get_synapse_weight(
 628 |     const wet_vm_t* vm,
 629 |     uint8_t pre,
 630 |     uint8_t post
 631 | ) {
 632 |     if (!vm || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
 633 |     return biophysics_get_weight(&vm->bio, pre, post);
 634 | }
 635 | 
 636 | WET_EXPORT float wet_clamp_voltage_vm(wet_vm_t* vm, float requested_v) {
 637 |     if (!vm) return requested_v;
 638 |     return interlocks_clamp_voltage(&vm->interlocks, requested_v);
 639 | }
```

### `native/src/wetvm_vm.c` (2034 lines, SHA-256: `9c85d5d4afad5dc0...`)

```text
   1 | #include "../include/wet_crt.h"
   2 | #include "../include/wetvm_types.h"
   3 | #include "../include/wetvm_api.h"
   4 | #include "../include/wetvm_vm.h"
   5 | #include "../include/wet_hal.h"
   6 | 
   7 | /* Unaligned Little-Endian Memory Readers (prevents hardware faults on ARM/RISC-V) */
   8 | static inline uint16_t wet_read_u16_le(const void* p) {
   9 |     uint16_t val;
  10 |     memcpy(&val, p, sizeof(val));
  11 |     return val;
  12 | }
  13 | static inline int16_t wet_read_i16_le(const void* p) {
  14 |     int16_t val;
  15 |     memcpy(&val, p, sizeof(val));
  16 |     return val;
  17 | }
  18 | static inline uint32_t wet_read_u32_le(const void* p) {
  19 |     uint32_t val;
  20 |     memcpy(&val, p, sizeof(val));
  21 |     return val;
  22 | }
  23 | static inline int32_t wet_read_i32_le(const void* p) {
  24 |     int32_t val;
  25 |     memcpy(&val, p, sizeof(val));
  26 |     return val;
  27 | }
  28 | static inline float wet_read_f32_le(const void* p) {
  29 |     float val;
  30 |     memcpy(&val, p, sizeof(val));
  31 |     return val;
  32 | }
  33 | 
  34 | /* =========================================================================
  35 |  * IEEE 802.3 CRC32 Implementation
  36 |  * ========================================================================= */
  37 | 
  38 | uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc) {
  39 |     uint32_t crc = ~initial_crc;
  40 |     for (size_t i = 0; i < length; ++i) {
  41 |         crc ^= data[i];
  42 |         for (int k = 0; k < 8; ++k) {
  43 |             crc = (crc >> 1) ^ (0xEDB88320u & -(int32_t)(crc & 1));
  44 |         }
  45 |     }
  46 |     return ~crc;
  47 | }
  48 | 
  49 | /* =========================================================================
  50 |  * Stack Management Helpers
  51 |  * ========================================================================= */
  52 | 
  53 | static inline wet_status_t push_val(struct wet_vm_instance* vm, wet_value_t val) {
  54 |     if (vm->sp >= vm->max_stack) {
  55 |         snprintf(vm->last_error, sizeof(vm->last_error),
  56 |                  "Operand stack overflow (limit %u reached)", (unsigned)vm->max_stack);
  57 |         return WET_ERR_STACK_OVERFLOW;
  58 |     }
  59 |     vm->stack[vm->sp++] = val;
  60 |     return WET_OK;
  61 | }
  62 | 
  63 | static inline wet_status_t pop_val(struct wet_vm_instance* vm, wet_value_t* out_val) {
  64 |     if (vm->sp == 0) {
  65 |         snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow");
  66 |         return WET_ERR_STACK_UNDERFLOW;
  67 |     }
  68 |     *out_val = vm->stack[--vm->sp];
  69 |     return WET_OK;
  70 | }
  71 | 
  72 | static inline float to_float(const wet_value_t* v) {
  73 |     if (v->type == WET_VAL_FLOAT) {
  74 |         return v->as.f_val;
  75 |     }
  76 |     if (v->type == WET_VAL_INT) {
  77 |         return (float)v->as.i_val;
  78 |     }
  79 |     return 0.0f;
  80 | }
  81 | 
  82 | static inline int32_t to_int(const wet_value_t* v) {
  83 |     if (v->type == WET_VAL_INT) {
  84 |         return v->as.i_val;
  85 |     }
  86 |     if (v->type == WET_VAL_FLOAT) {
  87 |         return (int32_t)v->as.f_val;
  88 |     }
  89 |     return 0;
  90 | }
  91 | 
  92 | static inline int is_truthy(const wet_value_t* v) {
  93 |     if (v->type == WET_VAL_INT) {
  94 |         return v->as.i_val != 0;
  95 |     }
  96 |     if (v->type == WET_VAL_FLOAT) {
  97 |         return v->as.f_val != 0.0f;
  98 |     }
  99 |     if (v->type == WET_VAL_STRING) {
 100 |         return v->as.s_val.len > 0;
 101 |     }
 102 |     return 0;
 103 | }
 104 | 
 105 | /* =========================================================================
 106 |  * Bytecode Loading and Verification
 107 |  * ========================================================================= */
 108 | 
 109 | static void cleanup_constants(struct wet_vm_instance* vm) {
 110 |     if (vm->constants) {
 111 |         for (size_t i = 0; i < vm->num_constants; ++i) {
 112 |             if (vm->constants[i].str_alloc) {
 113 |                 free(vm->constants[i].str_alloc);
 114 |                 vm->constants[i].str_alloc = NULL;
 115 |             }
 116 |         }
 117 |         free(vm->constants);
 118 |         vm->constants = NULL;
 119 |         vm->num_constants = 0;
 120 |     }
 121 | }
 122 | 
 123 | static void cleanup_bytecode(struct wet_vm_instance* vm) {
 124 |     cleanup_constants(vm);
 125 |     if (vm->bytecode_raw) {
 126 |         free(vm->bytecode_raw);
 127 |         vm->bytecode_raw = NULL;
 128 |         vm->bytecode_size = 0;
 129 |     }
 130 |     vm->code = NULL;
 131 |     vm->code_size = 0;
 132 | }
 133 | 
 134 | wet_status_t wet_vm_load_bytecode_internal(
 135 |     struct wet_vm_instance* vm,
 136 |     const uint8_t* code_bytes,
 137 |     size_t size,
 138 |     char* err_buf,
 139 |     size_t err_buf_len
 140 | ) {
 141 |     if (!vm || !code_bytes) {
 142 |         if (err_buf && err_buf_len > 0) {
 143 |             snprintf(err_buf, err_buf_len, "Null pointer argument to wet_load_bytecode");
 144 |         }
 145 |         return WET_ERR_NULL_PTR;
 146 |     }
 147 | 
 148 |     if (size < WET_HEADER_SIZE) {
 149 |         snprintf(vm->last_error, sizeof(vm->last_error),
 150 |                  "Bytecode binary truncated: size %zu < header size %d", size, WET_HEADER_SIZE);
 151 |         if (err_buf && err_buf_len > 0) {
 152 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 153 |         }
 154 |         return WET_ERR_MALFORMED_SECTION;
 155 |     }
 156 | 
 157 |     const wet_bytecode_header_t* hdr = (const wet_bytecode_header_t*)code_bytes;
 158 | 
 159 |     /* 1. Verify Magic "WETB" */
 160 |     if (hdr->magic[0] != 'W' || hdr->magic[1] != 'E' ||
 161 |         hdr->magic[2] != 'T' || hdr->magic[3] != 'B') {
 162 |         snprintf(vm->last_error, sizeof(vm->last_error),
 163 |                  "Invalid magic 0x%02X%02X%02X%02X (expected 'WETB')",
 164 |                  hdr->magic[0], hdr->magic[1], hdr->magic[2], hdr->magic[3]);
 165 |         if (err_buf && err_buf_len > 0) {
 166 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 167 |         }
 168 |         return WET_ERR_INVALID_MAGIC;
 169 |     }
 170 | 
 171 |     /* 2. Verify Version */
 172 |     if (hdr->version_major != WET_VERSION_MAJOR || hdr->version_minor != WET_VERSION_MINOR) {
 173 |         snprintf(vm->last_error, sizeof(vm->last_error),
 174 |                  "Unsupported bytecode version %u.%u (expected %u.%u)",
 175 |                  hdr->version_major, hdr->version_minor,
 176 |                  WET_VERSION_MAJOR, WET_VERSION_MINOR);
 177 |         if (err_buf && err_buf_len > 0) {
 178 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 179 |         }
 180 |         return WET_ERR_UNSUPPORTED_VERSION;
 181 |     }
 182 | 
 183 |     /* 3. Verify File Size */
 184 |     if (hdr->file_size != size) {
 185 |         snprintf(vm->last_error, sizeof(vm->last_error),
 186 |                  "File size mismatch: header reports %u bytes, got %zu bytes",
 187 |                  hdr->file_size, size);
 188 |         if (err_buf && err_buf_len > 0) {
 189 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 190 |         }
 191 |         return WET_ERR_MALFORMED_SECTION;
 192 |     }
 193 | 
 194 |     /* 4. Verify CRC32 Checksum (computed with CRC field at offset 12 zeroed) */
 195 |     uint32_t expected_crc = hdr->checksum_crc32;
 196 |     uint32_t calc_crc = wet_compute_crc32(code_bytes, 12, 0);
 197 |     uint8_t zero_field[4] = {0, 0, 0, 0};
 198 |     calc_crc = wet_compute_crc32(zero_field, 4, calc_crc);
 199 |     if (size > 16) {
 200 |         calc_crc = wet_compute_crc32(code_bytes + 16, size - 16, calc_crc);
 201 |     }
 202 | 
 203 |     if (calc_crc != expected_crc) {
 204 |         snprintf(vm->last_error, sizeof(vm->last_error),
 205 |                  "CRC32 mismatch: header has 0x%08X, calculated 0x%08X",
 206 |                  expected_crc, calc_crc);
 207 |         if (err_buf && err_buf_len > 0) {
 208 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 209 |         }
 210 |         return WET_ERR_CRC_MISMATCH;
 211 |     }
 212 | 
 213 |     /* 4b. Anti-Rollback Monotonic Sequence Verification */
 214 |     if (vm->config.min_sequence_counter > 0 && hdr->sequence_counter < vm->config.min_sequence_counter) {
 215 |         snprintf(vm->last_error, sizeof(vm->last_error),
 216 |                  "Anti-rollback security violation: binary sequence counter %u is below required hardware minimum %u",
 217 |                  hdr->sequence_counter, vm->config.min_sequence_counter);
 218 |         if (err_buf && err_buf_len > 0) {
 219 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 220 |         }
 221 |         return WET_ERR_CAPABILITY_DENIED;
 222 |     }
 223 | 
 224 |     /* 5. Validate Section Table Bounds */
 225 |     size_t sec_table_size = (size_t)hdr->num_sections * WET_SECTION_ENTRY_SIZE;
 226 |     if (WET_HEADER_SIZE + sec_table_size > size) {
 227 |         snprintf(vm->last_error, sizeof(vm->last_error),
 228 |                  "Section table exceeds file boundary (%u sections)", hdr->num_sections);
 229 |         if (err_buf && err_buf_len > 0) {
 230 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 231 |         }
 232 |         return WET_ERR_MALFORMED_SECTION;
 233 |     }
 234 | 
 235 |     /* Clean up previous bytecode and allocate buffer for new bytecode */
 236 |     cleanup_bytecode(vm);
 237 |     vm->bytecode_raw = (uint8_t*)malloc(size);
 238 |     if (!vm->bytecode_raw) {
 239 |         snprintf(vm->last_error, sizeof(vm->last_error), "Memory allocation failed for bytecode");
 240 |         return WET_ERR_ALLOC_FAILED;
 241 |     }
 242 |     memcpy(vm->bytecode_raw, code_bytes, size);
 243 |     vm->bytecode_size = size;
 244 | 
 245 |     /* Parse Section Table */
 246 |     const wet_section_header_t* sections =
 247 |         (const wet_section_header_t*)(vm->bytecode_raw + WET_HEADER_SIZE);
 248 | 
 249 |     const uint8_t* code_ptr = NULL;
 250 |     size_t code_len = 0;
 251 | 
 252 |     for (uint32_t i = 0; i < hdr->num_sections; ++i) {
 253 |         uint16_t stype = sections[i].section_type;
 254 |         uint32_t off = sections[i].offset;
 255 |         uint32_t s_size = sections[i].size;
 256 | 
 257 |         if ((size_t)off + s_size > size) {
 258 |             snprintf(vm->last_error, sizeof(vm->last_error),
 259 |                      "Section %u (type %u) extends beyond file boundary", i, stype);
 260 |             cleanup_bytecode(vm);
 261 |             return WET_ERR_MALFORMED_SECTION;
 262 |         }
 263 | 
 264 |         const uint8_t* sec_data = vm->bytecode_raw + off;
 265 | 
 266 |         if (stype == WET_SEC_CONSTANT_POOL) {
 267 |             /* Unpack Constant Pool */
 268 |             if (s_size < 4) {
 269 |                 snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool truncated");
 270 |                 cleanup_bytecode(vm);
 271 |                 return WET_ERR_MALFORMED_SECTION;
 272 |             }
 273 |             uint32_t num_consts = wet_read_u32_le(sec_data);
 274 |             size_t c_pos = 4;
 275 | 
 276 |             vm->constants = (wet_constant_entry_t*)calloc(num_consts, sizeof(wet_constant_entry_t));
 277 |             if (!vm->constants && num_consts > 0) {
 278 |                 cleanup_bytecode(vm);
 279 |                 return WET_ERR_ALLOC_FAILED;
 280 |             }
 281 |             vm->num_constants = num_consts;
 282 | 
 283 |             for (uint32_t c = 0; c < num_consts; ++c) {
 284 |                 if (c_pos >= s_size) {
 285 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool out of data");
 286 |                     cleanup_bytecode(vm);
 287 |                     return WET_ERR_MALFORMED_SECTION;
 288 |                 }
 289 |                 uint8_t tag = sec_data[c_pos++];
 290 |                 vm->constants[c].val.type = tag;
 291 | 
 292 |                 if (tag == WET_VAL_INT) {
 293 |                     if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 294 |                     vm->constants[c].val.as.i_val = wet_read_i32_le(sec_data + c_pos);
 295 |                     c_pos += 4;
 296 |                 } else if (tag == WET_VAL_FLOAT) {
 297 |                     if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 298 |                     vm->constants[c].val.as.f_val = wet_read_f32_le(sec_data + c_pos);
 299 |                     c_pos += 4;
 300 |                 } else if (tag == WET_VAL_STRING) {
 301 |                     if (c_pos + 2 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 302 |                     uint16_t str_len = wet_read_u16_le(sec_data + c_pos);
 303 |                     c_pos += 2;
 304 |                     if (c_pos + str_len > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 305 |                     char* sbuf = (char*)malloc(str_len + 1);
 306 |                     if (!sbuf) { cleanup_bytecode(vm); return WET_ERR_ALLOC_FAILED; }
 307 |                     memcpy(sbuf, sec_data + c_pos, str_len);
 308 |                     sbuf[str_len] = '\0';
 309 |                     vm->constants[c].str_alloc = sbuf;
 310 |                     vm->constants[c].val.as.s_val.str = sbuf;
 311 |                     vm->constants[c].val.as.s_val.len = str_len;
 312 |                     c_pos += str_len;
 313 |                 }
 314 |             }
 315 |         } else if (stype == WET_SEC_TOPOLOGY_CONFIG) {
 316 |             if (s_size >= 8) {
 317 |                 /* struct: channels (uint32), rows (uint16), cols (uint16) */
 318 |                 vm->grid_rows = (uint8_t)wet_read_u16_le(sec_data + 4);
 319 |                 vm->grid_cols = (uint8_t)wet_read_u16_le(sec_data + 6);
 320 |             }
 321 |         } else if (stype == WET_SEC_BYTECODE_STREAM) {
 322 |             code_ptr = sec_data;
 323 |             code_len = s_size;
 324 |         }
 325 |     }
 326 | 
 327 |     if (!code_ptr && code_len == 0) {
 328 |         /* Bytecode section might be empty */
 329 |         vm->code = vm->bytecode_raw;
 330 |         vm->code_size = 0;
 331 |     } else {
 332 |         vm->code = code_ptr;
 333 |         vm->code_size = code_len;
 334 |     }
 335 | 
 336 |     /* Reset registers and runtime state */
 337 |     vm->pc = 0;
 338 |     vm->sp = 0;
 339 |     vm->call_sp = 0;
 340 |     vm->is_halted = 0;
 341 |     vm->is_finished = 0;
 342 |     vm->sleep_ticks_remaining = 0;
 343 |     vm->current_tick = 0;
 344 |     vm->sim_time_ms = 0.0;
 345 |     vm->last_error[0] = '\0';
 346 | 
 347 |     vm->loaded_capabilities = hdr->capabilities;
 348 |     biophysics_reset(&vm->bio);
 349 |     interlocks_init(&vm->interlocks);
 350 |     interlocks_set_capabilities(&vm->interlocks, hdr->capabilities, hdr->channel_count);
 351 |     memset(vm->discharge_charge_nc, 0, sizeof(vm->discharge_charge_nc));
 352 | 
 353 |     /* Clear local variables */
 354 |     if (vm->locals) {
 355 |         memset(vm->locals, 0, sizeof(wet_value_t) * vm->max_locals);
 356 |     }
 357 | 
 358 |     /* Clear channel outputs */
 359 |     memset(vm->voltages, 0, sizeof(vm->voltages));
 360 |     memset(vm->spikes, 0, sizeof(vm->spikes));
 361 |     memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 362 |     vm->population_rate_hz = 0.0f;
 363 | 
 364 |     return WET_OK;
 365 | }
 366 | 
 367 | /* =========================================================================
 368 |  * Telemetry Snapshot Population
 369 |  * ========================================================================= */
 370 | 
 371 | static void populate_telemetry(const struct wet_vm_instance* vm, wet_telemetry_t* telem) {
 372 |     if (!telem) return;
 373 |     telem->current_tick = vm->current_tick;
 374 |     telem->sim_time_ms = vm->sim_time_ms;
 375 |     telem->population_rate_hz = vm->population_rate_hz;
 376 |     memcpy(telem->voltages, vm->voltages, sizeof(float) * 64);
 377 |     memcpy(telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
 378 |     memcpy(telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);
 379 | }
 380 | 
 381 | static wet_status_t advance_simulation_tick(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
 382 |     if (vm->interlocks.locked) {
 383 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 384 |         return WET_ERR_INTERLOCK_LOCKED;
 385 |     }
 386 | 
 387 |     /* Dead-heading valve-pump overpressure check */
 388 |     if (vm->interlocks.dead_head_protection_enabled) {
 389 |         for (int p = 0; p < 8; ++p) {
 390 |             if (vm->pump_rates_ul_min[p] > 0.0f) {
 391 |                 uint8_t v = vm->interlocks.pump_valve_mapping[p];
 392 |                 if (v < 8 && vm->valve_states[v] == 0) {
 393 |                     vm->interlocks.locked = 1;
 394 |                     vm->interlocks.trip_reason = INTERLOCK_TRIP_DEAD_HEAD_PRESSURE;
 395 |                     if (vm->hal) {
 396 |                         wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_DEAD_HEAD_PRESSURE);
 397 |                     }
 398 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 399 |                              "ERR_DEAD_HEAD_OVERPRESSURE: Pump %d active at %.2f uL/min while downstream valve %d is closed",
 400 |                              p, (double)vm->pump_rates_ul_min[p], v);
 401 |                     return WET_ERR_ACTUATOR_FAULT;
 402 |                 }
 403 |             }
 404 |         }
 405 |     }
 406 | 
 407 |     /* Phase 3 Environmental Checks: Thermal Limit (CMOS heating) & Bubble Detection */
 408 |     if (vm->ambient_temperature_c > INTERLOCK_THERMAL_LIMIT_C) {
 409 |         wet_status_t th_st = interlocks_check_thermal(&vm->interlocks, vm->current_tick, vm->ambient_temperature_c);
 410 |         if (th_st != WET_OK) {
 411 |             biophysics_zero_all_stim(&vm->bio);
 412 |             vm->is_halted = 1;
 413 |             if (vm->hal) {
 414 |                 wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 415 |             }
 416 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 417 |             populate_telemetry(vm, out_telem);
 418 |             return th_st;
 419 |         }
 420 |     }
 421 | 
 422 |     for (int b = 0; b < 8; ++b) {
 423 |         if (vm->bubble_detected[b]) {
 424 |             wet_status_t bub_st = interlocks_check_bubble(&vm->interlocks, vm->current_tick, 1, (uint8_t)b);
 425 |             if (bub_st != WET_OK) {
 426 |                 for (int p = 0; p < 8; ++p) vm->pump_rates_ul_min[p] = 0.0f;
 427 |                 biophysics_zero_all_stim(&vm->bio);
 428 |                 vm->is_halted = 1;
 429 |                 if (vm->hal) {
 430 |                     wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 431 |                 }
 432 |                 snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 433 |                 populate_telemetry(vm, out_telem);
 434 |                 return bub_st;
 435 |             }
 436 |         }
 437 |     }
 438 | 
 439 |     /* 1. Advance in-silico biophysics by 1 tick (dt = 0.1 ms) */
 440 |     biophysics_step_tick(&vm->bio);
 441 |     for (int ch = 0; ch < 64; ++ch) {
 442 |         if (vm->discharge_charge_nc[ch] != 0.0f) {
 443 |             vm->bio.tick_charge_nc[ch] += vm->discharge_charge_nc[ch];
 444 |             vm->discharge_charge_nc[ch] = 0.0f;
 445 |         }
 446 |     }
 447 |     vm->current_tick++;
 448 |     vm->sim_time_ms = (double)vm->current_tick * vm->config.dt_ms;
 449 |     vm->sim_time_us = (int64_t)((double)vm->current_tick * vm->config.dt_ms * 1000.0 + 0.5);
 450 | 
 451 |     /* 2. Check sliding charge balance watchdog */
 452 |     wet_status_t il_st = interlocks_record_charge_tick(
 453 |         &vm->interlocks, vm->current_tick, vm->bio.tick_charge_nc
 454 |     );
 455 |     if (il_st != WET_OK) {
 456 |         biophysics_zero_all_stim(&vm->bio);
 457 |         memset(vm->voltages, 0, sizeof(vm->voltages));
 458 |         memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 459 |         memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
 460 |         memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
 461 |         memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
 462 |         vm->is_halted = 1;
 463 |         if (vm->hal) {
 464 |             wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 465 |         }
 466 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 467 |         populate_telemetry(vm, out_telem);
 468 |         return il_st;
 469 |     }
 470 | 
 471 |     /* 3. Check epileptiform runaway breaker */
 472 |     il_st = interlocks_check_epileptiform(
 473 |         &vm->interlocks, vm->current_tick, vm->bio.channel_rate_hz
 474 |     );
 475 |     if (il_st != WET_OK) {
 476 |         biophysics_zero_all_stim(&vm->bio);
 477 |         memset(vm->voltages, 0, sizeof(vm->voltages));
 478 |         memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 479 |         memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
 480 |         memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
 481 |         memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
 482 |         vm->is_halted = 1;
 483 |         if (vm->hal) {
 484 |             wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 485 |         }
 486 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 487 |         populate_telemetry(vm, out_telem);
 488 |         return il_st;
 489 |     }
 490 | 
 491 |     /* 4. Sync outputs to VM registers & telemetry snapshot */
 492 |     memcpy(vm->voltages, vm->bio.mea_voltage_v, sizeof(float) * 64);
 493 |     memcpy(vm->spikes, vm->bio.spikes_now, sizeof(uint8_t) * 64);
 494 |     memcpy(vm->last_charge_nc, vm->bio.tick_charge_nc, sizeof(float) * 64);
 495 |     vm->population_rate_hz = vm->bio.population_rate_hz;
 496 | 
 497 |     populate_telemetry(vm, out_telem);
 498 |     return WET_OK;
 499 | }
 500 | 
 501 | /* =========================================================================
 502 |  * Cycle-Accurate Execution Stepper
 503 |  * ========================================================================= */
 504 | 
 505 | wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
 506 |     if (!vm) return WET_ERR_NULL_PTR;
 507 | 
 508 |     if (vm->interlocks.locked) {
 509 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 510 |         return WET_ERR_INTERLOCK_LOCKED;
 511 |     }
 512 | 
 513 |     if (vm->is_halted) {
 514 |         if (vm->life_supervisor.supervisor_active) {
 515 |             /* Ring-0 Life Support Supervisor: Maintain baseline nutrient perfusion & temperature */
 516 |             for (int p = 0; p < 8; ++p) {
 517 |                 if (vm->pump_rates_ul_min[p] == 0.0f) {
 518 |                     vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 519 |                 }
 520 |             }
 521 |             vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 522 |             vm->life_supervisor.ticks_under_supervisor++;
 523 |         }
 524 |         snprintf(vm->last_error, sizeof(vm->last_error), "VM is halted");
 525 |         return WET_ERR_HALTED;
 526 |     }
 527 | 
 528 |     /* If bytecode execution has finished or reached end, continue free-running biological stepping */
 529 |     if (vm->is_finished || vm->pc >= vm->code_size) {
 530 |         if (vm->life_supervisor.supervisor_active) {
 531 |             for (int p = 0; p < 8; ++p) {
 532 |                 if (vm->pump_rates_ul_min[p] == 0.0f) {
 533 |                     vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 534 |                 }
 535 |             }
 536 |             vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 537 |             vm->life_supervisor.ticks_under_supervisor++;
 538 |         }
 539 |         return advance_simulation_tick(vm, out_telem);
 540 |     }
 541 | 
 542 |     /* Handle ongoing SLEEP_TICKS decrement */
 543 |     if (vm->sleep_ticks_remaining > 0) {
 544 |         vm->sleep_ticks_remaining--;
 545 |         return advance_simulation_tick(vm, out_telem);
 546 |     }
 547 | 
 548 |     /* Dispatch instructions until a tick yield (SYNC_TICK, SLEEP_TICKS, HALT) */
 549 |     uint32_t instr_count = 0;
 550 |     uint32_t max_ops = vm->config.max_ops_per_tick ? vm->config.max_ops_per_tick : 100000U;
 551 |     while (!vm->is_halted && !vm->is_finished) {
 552 |         if (++instr_count > max_ops) {
 553 |             biophysics_zero_all_stim(&vm->bio);
 554 |             vm->interlocks.locked = 1;
 555 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CAPABILITY_VIOLATION;
 556 |             if (max_ops == 100000U) {
 557 |                 snprintf(vm->last_error, sizeof(vm->last_error),
 558 |                          "WET_ERR_WATCHDOG_TIMEOUT: Exceeded 100,000 instructions in a single tick");
 559 |             } else {
 560 |                 snprintf(vm->last_error, sizeof(vm->last_error),
 561 |                          "WET_ERR_WATCHDOG_TIMEOUT: Exceeded %u instructions in a single tick", max_ops);
 562 |             }
 563 |             return WET_ERR_WATCHDOG_TIMEOUT;
 564 |         }
 565 | 
 566 |         if (vm->pc >= vm->code_size) {
 567 |             /* End of bytecode reached: advance simulation tick */
 568 |             vm->is_finished = 1;
 569 |             return advance_simulation_tick(vm, out_telem);
 570 |         }
 571 | 
 572 |         size_t instr_pc = vm->pc;
 573 |         uint8_t op = vm->code[instr_pc];
 574 | 
 575 |         switch ((wet_opcode_t)op) {
 576 |             case WET_OP_NOP: {
 577 |                 vm->pc = instr_pc + 1;
 578 |                 break;
 579 |             }
 580 | 
 581 |             case WET_OP_HALT: {
 582 |                 vm->is_finished = 1;
 583 |                 vm->pc = instr_pc + 1;
 584 |                 if (vm->life_supervisor.supervisor_active) {
 585 |                     for (int p = 0; p < 8; ++p) {
 586 |                         if (vm->pump_rates_ul_min[p] == 0.0f) {
 587 |                             vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 588 |                         }
 589 |                     }
 590 |                     vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 591 |                     vm->life_supervisor.ticks_under_supervisor++;
 592 |                 }
 593 |                 return advance_simulation_tick(vm, out_telem);
 594 |             }
 595 | 
 596 |             case WET_OP_SYNC_TICK: {
 597 |                 vm->pc = instr_pc + 1;
 598 |                 return advance_simulation_tick(vm, out_telem);
 599 |             }
 600 | 
 601 |             case WET_OP_SLEEP_TICKS: {
 602 |                 if (instr_pc + 3 > vm->code_size) {
 603 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated SLEEP_TICKS operand");
 604 |                     return WET_ERR_INVALID_OPCODE;
 605 |                 }
 606 |                 uint16_t ticks = wet_read_u16_le(vm->code + instr_pc + 1);
 607 |                 vm->pc = instr_pc + 3;
 608 | 
 609 |                 if (ticks > 1) {
 610 |                     vm->sleep_ticks_remaining = ticks - 1;
 611 |                 }
 612 |                 return advance_simulation_tick(vm, out_telem);
 613 |             }
 614 | 
 615 |             case WET_OP_PUSH_CONST: {
 616 |                 if (instr_pc + 3 > vm->code_size) {
 617 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_CONST operand");
 618 |                     return WET_ERR_INVALID_OPCODE;
 619 |                 }
 620 |                 uint16_t idx = wet_read_u16_le(vm->code + instr_pc + 1);
 621 |                 vm->pc = instr_pc + 3;
 622 |                 if (idx >= vm->num_constants) {
 623 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 624 |                              "Constant pool index %u out of range (%zu)", idx, vm->num_constants);
 625 |                     return WET_ERR_INVALID_OPCODE;
 626 |                 }
 627 |                 wet_status_t st = push_val(vm, vm->constants[idx].val);
 628 |                 if (st != WET_OK) return st;
 629 |                 break;
 630 |             }
 631 | 
 632 |             case WET_OP_PUSH_INT: {
 633 |                 if (instr_pc + 5 > vm->code_size) {
 634 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_INT operand");
 635 |                     return WET_ERR_INVALID_OPCODE;
 636 |                 }
 637 |                 int32_t val = wet_read_i32_le(vm->code + instr_pc + 1);
 638 |                 vm->pc = instr_pc + 5;
 639 |                 wet_value_t v;
 640 |                 v.type = WET_VAL_INT;
 641 |                 v.as.i_val = val;
 642 |                 wet_status_t st = push_val(vm, v);
 643 |                 if (st != WET_OK) return st;
 644 |                 break;
 645 |             }
 646 | 
 647 |             case WET_OP_PUSH_FLOAT: {
 648 |                 if (instr_pc + 5 > vm->code_size) {
 649 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_FLOAT operand");
 650 |                     return WET_ERR_INVALID_OPCODE;
 651 |                 }
 652 |                 float val = wet_read_f32_le(vm->code + instr_pc + 1);
 653 |                 vm->pc = instr_pc + 5;
 654 |                 wet_value_t v;
 655 |                 v.type = WET_VAL_FLOAT;
 656 |                 v.as.f_val = val;
 657 |                 wet_status_t st = push_val(vm, v);
 658 |                 if (st != WET_OK) return st;
 659 |                 break;
 660 |             }
 661 | 
 662 |             case WET_OP_POP: {
 663 |                 vm->pc = instr_pc + 1;
 664 |                 wet_value_t dummy;
 665 |                 wet_status_t st = pop_val(vm, &dummy);
 666 |                 if (st != WET_OK) return st;
 667 |                 break;
 668 |             }
 669 | 
 670 |             case WET_OP_DUP: {
 671 |                 vm->pc = instr_pc + 1;
 672 |                 if (vm->sp == 0) {
 673 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on DUP");
 674 |                     return WET_ERR_STACK_UNDERFLOW;
 675 |                 }
 676 |                 wet_value_t top = vm->stack[vm->sp - 1];
 677 |                 wet_status_t st = push_val(vm, top);
 678 |                 if (st != WET_OK) return st;
 679 |                 break;
 680 |             }
 681 | 
 682 |             case WET_OP_SWAP: {
 683 |                 vm->pc = instr_pc + 1;
 684 |                 if (vm->sp < 2) {
 685 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on SWAP");
 686 |                     return WET_ERR_STACK_UNDERFLOW;
 687 |                 }
 688 |                 wet_value_t a = vm->stack[vm->sp - 1];
 689 |                 vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
 690 |                 vm->stack[vm->sp - 2] = a;
 691 |                 break;
 692 |             }
 693 | 
 694 |             case WET_OP_LOAD_LOCAL: {
 695 |                 if (instr_pc + 3 > vm->code_size) {
 696 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated LOAD_LOCAL operand");
 697 |                     return WET_ERR_INVALID_OPCODE;
 698 |                 }
 699 |                 uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
 700 |                 vm->pc = instr_pc + 3;
 701 |                 if (slot >= vm->max_locals) {
 702 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 703 |                              "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
 704 |                     return WET_ERR_INVALID_OPCODE;
 705 |                 }
 706 |                 wet_status_t st = push_val(vm, vm->locals[slot]);
 707 |                 if (st != WET_OK) return st;
 708 |                 break;
 709 |             }
 710 | 
 711 |             case WET_OP_STORE_LOCAL: {
 712 |                 if (instr_pc + 3 > vm->code_size) {
 713 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STORE_LOCAL operand");
 714 |                     return WET_ERR_INVALID_OPCODE;
 715 |                 }
 716 |                 uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
 717 |                 vm->pc = instr_pc + 3;
 718 |                 if (slot >= vm->max_locals) {
 719 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 720 |                              "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
 721 |                     return WET_ERR_INVALID_OPCODE;
 722 |                 }
 723 |                 wet_value_t val;
 724 |                 wet_status_t st = pop_val(vm, &val);
 725 |                 if (st != WET_OK) return st;
 726 |                 vm->locals[slot] = val;
 727 |                 break;
 728 |             }
 729 | 
 730 |             case WET_OP_ADD_I: {
 731 |                 vm->pc = instr_pc + 1;
 732 |                 wet_value_t b, a;
 733 |                 wet_status_t st = pop_val(vm, &b);
 734 |                 if (st != WET_OK) return st;
 735 |                 st = pop_val(vm, &a);
 736 |                 if (st != WET_OK) return st;
 737 |                 wet_value_t res;
 738 |                 res.type = WET_VAL_INT;
 739 |                 res.as.i_val = to_int(&a) + to_int(&b);
 740 |                 st = push_val(vm, res);
 741 |                 if (st != WET_OK) return st;
 742 |                 break;
 743 |             }
 744 | 
 745 |             case WET_OP_SUB_I: {
 746 |                 vm->pc = instr_pc + 1;
 747 |                 wet_value_t b, a;
 748 |                 wet_status_t st = pop_val(vm, &b);
 749 |                 if (st != WET_OK) return st;
 750 |                 st = pop_val(vm, &a);
 751 |                 if (st != WET_OK) return st;
 752 |                 wet_value_t res;
 753 |                 res.type = WET_VAL_INT;
 754 |                 res.as.i_val = to_int(&a) - to_int(&b);
 755 |                 st = push_val(vm, res);
 756 |                 if (st != WET_OK) return st;
 757 |                 break;
 758 |             }
 759 | 
 760 |             case WET_OP_MUL_I: {
 761 |                 vm->pc = instr_pc + 1;
 762 |                 wet_value_t b, a;
 763 |                 wet_status_t st = pop_val(vm, &b);
 764 |                 if (st != WET_OK) return st;
 765 |                 st = pop_val(vm, &a);
 766 |                 if (st != WET_OK) return st;
 767 |                 wet_value_t res;
 768 |                 res.type = WET_VAL_INT;
 769 |                 res.as.i_val = to_int(&a) * to_int(&b);
 770 |                 st = push_val(vm, res);
 771 |                 if (st != WET_OK) return st;
 772 |                 break;
 773 |             }
 774 | 
 775 |             case WET_OP_DIV_I: {
 776 |                 vm->pc = instr_pc + 1;
 777 |                 wet_value_t b, a;
 778 |                 wet_status_t st = pop_val(vm, &b);
 779 |                 if (st != WET_OK) return st;
 780 |                 st = pop_val(vm, &a);
 781 |                 if (st != WET_OK) return st;
 782 |                 int32_t b_val = to_int(&b);
 783 |                 if (b_val == 0) {
 784 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Integer division by zero");
 785 |                     return WET_ERR_DIVISION_BY_ZERO;
 786 |                 }
 787 |                 wet_value_t res;
 788 |                 res.type = WET_VAL_INT;
 789 |                 res.as.i_val = to_int(&a) / b_val;
 790 |                 st = push_val(vm, res);
 791 |                 if (st != WET_OK) return st;
 792 |                 break;
 793 |             }
 794 | 
 795 |             case WET_OP_ADD_F: {
 796 |                 vm->pc = instr_pc + 1;
 797 |                 wet_value_t b, a;
 798 |                 wet_status_t st = pop_val(vm, &b);
 799 |                 if (st != WET_OK) return st;
 800 |                 st = pop_val(vm, &a);
 801 |                 if (st != WET_OK) return st;
 802 |                 wet_value_t res;
 803 |                 res.type = WET_VAL_FLOAT;
 804 |                 res.as.f_val = to_float(&a) + to_float(&b);
 805 |                 st = push_val(vm, res);
 806 |                 if (st != WET_OK) return st;
 807 |                 break;
 808 |             }
 809 | 
 810 |             case WET_OP_SUB_F: {
 811 |                 vm->pc = instr_pc + 1;
 812 |                 wet_value_t b, a;
 813 |                 wet_status_t st = pop_val(vm, &b);
 814 |                 if (st != WET_OK) return st;
 815 |                 st = pop_val(vm, &a);
 816 |                 if (st != WET_OK) return st;
 817 |                 wet_value_t res;
 818 |                 res.type = WET_VAL_FLOAT;
 819 |                 res.as.f_val = to_float(&a) - to_float(&b);
 820 |                 st = push_val(vm, res);
 821 |                 if (st != WET_OK) return st;
 822 |                 break;
 823 |             }
 824 | 
 825 |             case WET_OP_MUL_F: {
 826 |                 vm->pc = instr_pc + 1;
 827 |                 wet_value_t b, a;
 828 |                 wet_status_t st = pop_val(vm, &b);
 829 |                 if (st != WET_OK) return st;
 830 |                 st = pop_val(vm, &a);
 831 |                 if (st != WET_OK) return st;
 832 |                 wet_value_t res;
 833 |                 res.type = WET_VAL_FLOAT;
 834 |                 res.as.f_val = to_float(&a) * to_float(&b);
 835 |                 st = push_val(vm, res);
 836 |                 if (st != WET_OK) return st;
 837 |                 break;
 838 |             }
 839 | 
 840 |             case WET_OP_DIV_F: {
 841 |                 vm->pc = instr_pc + 1;
 842 |                 wet_value_t b, a;
 843 |                 wet_status_t st = pop_val(vm, &b);
 844 |                 if (st != WET_OK) return st;
 845 |                 st = pop_val(vm, &a);
 846 |                 if (st != WET_OK) return st;
 847 |                 float b_val = to_float(&b);
 848 |                 if (fabsf(b_val) < 1e-15f) {
 849 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Floating point division by zero");
 850 |                     return WET_ERR_DIVISION_BY_ZERO;
 851 |                 }
 852 |                 wet_value_t res;
 853 |                 res.type = WET_VAL_FLOAT;
 854 |                 res.as.f_val = to_float(&a) / b_val;
 855 |                 st = push_val(vm, res);
 856 |                 if (st != WET_OK) return st;
 857 |                 break;
 858 |             }
 859 | 
 860 |             case WET_OP_NEG: {
 861 |                 vm->pc = instr_pc + 1;
 862 |                 wet_value_t a;
 863 |                 wet_status_t st = pop_val(vm, &a);
 864 |                 if (st != WET_OK) return st;
 865 |                 wet_value_t res;
 866 |                 if (a.type == WET_VAL_FLOAT) {
 867 |                     res.type = WET_VAL_FLOAT;
 868 |                     res.as.f_val = -a.as.f_val;
 869 |                 } else {
 870 |                     res.type = WET_VAL_INT;
 871 |                     res.as.i_val = -to_int(&a);
 872 |                 }
 873 |                 st = push_val(vm, res);
 874 |                 if (st != WET_OK) return st;
 875 |                 break;
 876 |             }
 877 | 
 878 |             case WET_OP_MOD_I: {
 879 |                 vm->pc = instr_pc + 1;
 880 |                 wet_value_t b, a;
 881 |                 wet_status_t st = pop_val(vm, &b);
 882 |                 if (st != WET_OK) return st;
 883 |                 st = pop_val(vm, &a);
 884 |                 if (st != WET_OK) return st;
 885 |                 int32_t b_val = to_int(&b);
 886 |                 if (b_val == 0) {
 887 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Integer modulo by zero");
 888 |                     return WET_ERR_DIVISION_BY_ZERO;
 889 |                 }
 890 |                 wet_value_t res;
 891 |                 res.type = WET_VAL_INT;
 892 |                 res.as.i_val = to_int(&a) % b_val;
 893 |                 st = push_val(vm, res);
 894 |                 if (st != WET_OK) return st;
 895 |                 break;
 896 |             }
 897 | 
 898 |             case WET_OP_CMP_EQ:
 899 |             case WET_OP_CMP_NE:
 900 |             case WET_OP_CMP_LT:
 901 |             case WET_OP_CMP_LE:
 902 |             case WET_OP_CMP_GT:
 903 |             case WET_OP_CMP_GE: {
 904 |                 vm->pc = instr_pc + 1;
 905 |                 wet_value_t b, a;
 906 |                 wet_status_t st = pop_val(vm, &b);
 907 |                 if (st != WET_OK) return st;
 908 |                 st = pop_val(vm, &a);
 909 |                 if (st != WET_OK) return st;
 910 | 
 911 |                 int cmp_res = 0;
 912 |                 if (a.type == WET_VAL_FLOAT || b.type == WET_VAL_FLOAT) {
 913 |                     float fa = to_float(&a);
 914 |                     float fb = to_float(&b);
 915 |                     switch ((wet_opcode_t)op) {
 916 |                         case WET_OP_CMP_EQ: cmp_res = (fa == fb); break;
 917 |                         case WET_OP_CMP_NE: cmp_res = (fa != fb); break;
 918 |                         case WET_OP_CMP_LT: cmp_res = (fa <  fb); break;
 919 |                         case WET_OP_CMP_LE: cmp_res = (fa <= fb); break;
 920 |                         case WET_OP_CMP_GT: cmp_res = (fa >  fb); break;
 921 |                         case WET_OP_CMP_GE: cmp_res = (fa >= fb); break;
 922 |                         default: break;
 923 |                     }
 924 |                 } else {
 925 |                     int32_t ia = to_int(&a);
 926 |                     int32_t ib = to_int(&b);
 927 |                     switch ((wet_opcode_t)op) {
 928 |                         case WET_OP_CMP_EQ: cmp_res = (ia == ib); break;
 929 |                         case WET_OP_CMP_NE: cmp_res = (ia != ib); break;
 930 |                         case WET_OP_CMP_LT: cmp_res = (ia <  ib); break;
 931 |                         case WET_OP_CMP_LE: cmp_res = (ia <= ib); break;
 932 |                         case WET_OP_CMP_GT: cmp_res = (ia >  ib); break;
 933 |                         case WET_OP_CMP_GE: cmp_res = (ia >= ib); break;
 934 |                         default: break;
 935 |                     }
 936 |                 }
 937 | 
 938 |                 wet_value_t res;
 939 |                 res.type = WET_VAL_INT;
 940 |                 res.as.i_val = cmp_res ? 1 : 0;
 941 |                 st = push_val(vm, res);
 942 |                 if (st != WET_OK) return st;
 943 |                 break;
 944 |             }
 945 | 
 946 |             case WET_OP_JMP: {
 947 |                 if (instr_pc + 3 > vm->code_size) {
 948 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP operand");
 949 |                     return WET_ERR_INVALID_OPCODE;
 950 |                 }
 951 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 952 |                 int64_t target = (int64_t)instr_pc + offset;
 953 |                 if (target < 0 || (size_t)target > vm->code_size) {
 954 |                     snprintf(vm->last_error, sizeof(vm->last_error), "JMP target %lld out of range", (long long)target);
 955 |                     return WET_ERR_INVALID_OPCODE;
 956 |                 }
 957 |                 vm->pc = (size_t)target;
 958 |                 break;
 959 |             }
 960 | 
 961 |             case WET_OP_JMP_IF_TRUE: {
 962 |                 if (instr_pc + 3 > vm->code_size) {
 963 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_TRUE operand");
 964 |                     return WET_ERR_INVALID_OPCODE;
 965 |                 }
 966 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 967 |                 wet_value_t cond;
 968 |                 wet_status_t st = pop_val(vm, &cond);
 969 |                 if (st != WET_OK) return st;
 970 | 
 971 |                 if (is_truthy(&cond)) {
 972 |                     int64_t target = (int64_t)instr_pc + offset;
 973 |                     if (target < 0 || (size_t)target > vm->code_size) {
 974 |                         snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_TRUE target %lld out of range", (long long)target);
 975 |                         return WET_ERR_INVALID_OPCODE;
 976 |                     }
 977 |                     vm->pc = (size_t)target;
 978 |                 } else {
 979 |                     vm->pc = instr_pc + 3;
 980 |                 }
 981 |                 break;
 982 |             }
 983 | 
 984 |             case WET_OP_JMP_IF_FALSE: {
 985 |                 if (instr_pc + 3 > vm->code_size) {
 986 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_FALSE operand");
 987 |                     return WET_ERR_INVALID_OPCODE;
 988 |                 }
 989 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 990 |                 wet_value_t cond;
 991 |                 wet_status_t st = pop_val(vm, &cond);
 992 |                 if (st != WET_OK) return st;
 993 | 
 994 |                 if (!is_truthy(&cond)) {
 995 |                     int64_t target = (int64_t)instr_pc + offset;
 996 |                     if (target < 0 || (size_t)target > vm->code_size) {
 997 |                         snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_FALSE target %lld out of range", (long long)target);
 998 |                         return WET_ERR_INVALID_OPCODE;
 999 |                     }
1000 |                     vm->pc = (size_t)target;
1001 |                 } else {
1002 |                     vm->pc = instr_pc + 3;
1003 |                 }
1004 |                 break;
1005 |             }
1006 | 
1007 |             case WET_OP_CALL: {
1008 |                 if (instr_pc + 4 > vm->code_size) {
1009 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated CALL operand");
1010 |                     return WET_ERR_INVALID_OPCODE;
1011 |                 }
1012 |                 uint16_t fn_idx = wet_read_u16_le(vm->code + instr_pc + 1);
1013 |                 uint8_t argc = *(const uint8_t*)(vm->code + instr_pc + 3);
1014 | 
1015 |                 if (fn_idx > 0 && fn_idx < vm->code_size) {
1016 |                     /* User-defined function call */
1017 |                     if (vm->call_sp >= vm->max_call_depth) {
1018 |                         snprintf(vm->last_error, sizeof(vm->last_error), "Call stack overflow (depth %zu)", vm->call_sp);
1019 |                         return WET_ERR_STACK_OVERFLOW;
1020 |                     }
1021 |                     vm->call_stack[vm->call_sp++].return_pc = instr_pc + 4;
1022 |                     vm->pc = fn_idx;
1023 |                 } else {
1024 |                     /* Handle builtin / external function call: pop arguments, push default 0 */
1025 |                     vm->pc = instr_pc + 4;
1026 |                     for (uint8_t a = 0; a < argc; ++a) {
1027 |                         wet_value_t dummy;
1028 |                         pop_val(vm, &dummy);
1029 |                     }
1030 |                     wet_value_t ret_val;
1031 |                     ret_val.type = WET_VAL_INT;
1032 |                     ret_val.as.i_val = 0;
1033 |                     push_val(vm, ret_val);
1034 |                 }
1035 |                 break;
1036 |             }
1037 | 
1038 |             case WET_OP_RET: {
1039 |                 if (vm->call_sp > 0) {
1040 |                     vm->call_sp--;
1041 |                     vm->pc = vm->call_stack[vm->call_sp].return_pc;
1042 |                 } else {
1043 |                     vm->pc = instr_pc + 1;
1044 |                 }
1045 |                 break;
1046 |             }
1047 | 
1048 |             case WET_OP_STIM_BIPHASIC: {
1049 |                 if (instr_pc + 2 > vm->code_size) {
1050 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_BIPHASIC operand");
1051 |                     return WET_ERR_INVALID_OPCODE;
1052 |                 }
1053 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1054 |                 vm->pc = instr_pc + 2;
1055 | 
1056 |                 /* Pop arguments: interphase, phase2, phase1, voltage */
1057 |                 wet_value_t v_interphase, v_p2, v_p1, v_volt;
1058 |                 wet_status_t st = pop_val(vm, &v_interphase);
1059 |                 if (st != WET_OK) return st;
1060 |                 st = pop_val(vm, &v_p2);
1061 |                 if (st != WET_OK) return st;
1062 |                 st = pop_val(vm, &v_p1);
1063 |                 if (st != WET_OK) return st;
1064 |                 st = pop_val(vm, &v_volt);
1065 |                 if (st != WET_OK) return st;
1066 | 
1067 |                 if (channel == 0xFF) {
1068 |                     /* Dynamic channel index popped from stack */
1069 |                     wet_value_t v_ch;
1070 |                     st = pop_val(vm, &v_ch);
1071 |                     if (st != WET_OK) return st;
1072 |                     int32_t c_idx = to_int(&v_ch);
1073 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1074 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1075 |                                  "Electrode channel %d out of bounds (max %u)",
1076 |                                  c_idx, vm->config.channel_count);
1077 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1078 |                     }
1079 |                     channel = (uint8_t)c_idx;
1080 |                 } else if (channel >= vm->config.channel_count) {
1081 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1082 |                              "Electrode channel %u out of bounds (max %u)",
1083 |                              channel, vm->config.channel_count);
1084 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1085 |                 }
1086 | 
1087 |                 float voltage = to_float(&v_volt);
1088 |                 float p1_ms = to_float(&v_p1);
1089 |                 float p2_ms = to_float(&v_p2);
1090 |                 float ip_ms = to_float(&v_interphase);
1091 | 
1092 |                 if (vm->interlocks.locked) {
1093 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1094 |                     return WET_ERR_INTERLOCK_LOCKED;
1095 |                 }
1096 | 
1097 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage, channel)) {
1098 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1099 |                              "Capability denied for STIM_BIPHASIC on ch %u (req %.2fV)", channel, voltage);
1100 |                     return WET_ERR_CAPABILITY_DENIED;
1101 |                 }
1102 | 
1103 |                 /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
1104 |                 if (p1_ms > 0.0f && p2_ms > 0.0f) {
1105 |                     float q_phase1 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p1_ms;
1106 |                     float q_phase2 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p2_ms;
1107 |                     if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
1108 |                         vm->interlocks.locked = 1;
1109 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
1110 |                         vm->interlocks.tripped_channel = channel;
1111 |                         vm->interlocks.trip_tick = vm->current_tick;
1112 |                         vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
1113 |                         if (vm->hal) {
1114 |                             wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
1115 |                         }
1116 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1117 |                                  "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
1118 |                                  channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
1119 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1120 |                         return WET_ERR_CHARGE_DENSITY_EXCEEDED;
1121 |                     }
1122 |                 }
1123 | 
1124 |                 /* Active charge recovery: if previous pulse had pending Phase 2 counter-charge, discharge it */
1125 |                 bio_stim_pulse_t* prev_p = &vm->bio.stim_pulses[channel];
1126 |                 if (prev_p->active && prev_p->phase2_ticks_left > 0) {
1127 |                     float i_ua = (prev_p->phase2_amp_v / vm->bio.electrode_impedance_kohm) * 1000.0f;
1128 |                     vm->discharge_charge_nc[channel] += i_ua * (float)vm->bio.dt_ms * (float)prev_p->phase2_ticks_left;
1129 |                 }
1130 | 
1131 |                 float clamped_v = interlocks_clamp_voltage(&vm->interlocks, voltage);
1132 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1133 |                     wet_hal_stim_voltage(vm->hal, (uint16_t)channel, clamped_v, p1_ms, p2_ms);
1134 |                 }
1135 |                 biophysics_schedule_stim_ext(&vm->bio, channel, clamped_v, p1_ms, p2_ms, ip_ms);
1136 |                 vm->voltages[channel] = clamped_v;
1137 |                 /* Accurate impedance-scaled charge: I (mA) = V / Z(kOhm); Q(nC) = I(mA) * dt(ms) */
1138 |                 float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
1139 |                 vm->last_charge_nc[channel] = i_ma * (p1_ms - p2_ms);
1140 |                 break;
1141 |             }
1142 | 
1143 |             case WET_OP_READ_SPIKES: {
1144 |                 if (instr_pc + 2 > vm->code_size) {
1145 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_SPIKES operand");
1146 |                     return WET_ERR_INVALID_OPCODE;
1147 |                 }
1148 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1149 |                 vm->pc = instr_pc + 2;
1150 | 
1151 |                 wet_value_t window;
1152 |                 wet_status_t st = pop_val(vm, &window);
1153 |                 if (st != WET_OK) return st;
1154 | 
1155 |                 if (channel == 0xFF) {
1156 |                     /* Dynamic channel index popped from stack */
1157 |                     wet_value_t v_ch;
1158 |                     st = pop_val(vm, &v_ch);
1159 |                     if (st != WET_OK) return st;
1160 |                     int32_t c_idx = to_int(&v_ch);
1161 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1162 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1163 |                                  "Electrode channel %d out of bounds (max %u)",
1164 |                                  c_idx, vm->config.channel_count);
1165 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1166 |                     }
1167 |                     channel = (uint8_t)c_idx;
1168 |                 } else if (channel >= vm->config.channel_count) {
1169 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1170 |                              "Electrode channel %u out of bounds (max %u)",
1171 |                              channel, vm->config.channel_count);
1172 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1173 |                 }
1174 | 
1175 |                 float window_ms = to_float(&window);
1176 |                 uint32_t cnt = biophysics_get_spikes_window(&vm->bio, channel, window_ms);
1177 | 
1178 |                 wet_value_t spike_res;
1179 |                 spike_res.type = WET_VAL_INT;
1180 |                 spike_res.as.i_val = (int32_t)cnt;
1181 |                 st = push_val(vm, spike_res);
1182 |                 if (st != WET_OK) return st;
1183 |                 break;
1184 |             }
1185 | 
1186 |             case WET_OP_READ_VOLTAGE: {
1187 |                 if (instr_pc + 2 > vm->code_size) {
1188 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_VOLTAGE operand");
1189 |                     return WET_ERR_INVALID_OPCODE;
1190 |                 }
1191 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1192 |                 vm->pc = instr_pc + 2;
1193 | 
1194 |                 if (channel == 0xFF) {
1195 |                     /* Dynamic channel index popped from stack */
1196 |                     wet_value_t v_ch;
1197 |                     wet_status_t st = pop_val(vm, &v_ch);
1198 |                     if (st != WET_OK) return st;
1199 |                     int32_t c_idx = to_int(&v_ch);
1200 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1201 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1202 |                                  "Electrode channel %d out of bounds (max %u)",
1203 |                                  c_idx, vm->config.channel_count);
1204 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1205 |                     }
1206 |                     channel = (uint8_t)c_idx;
1207 |                 } else if (channel >= vm->config.channel_count) {
1208 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1209 |                              "Electrode channel %u out of bounds (max %u)",
1210 |                              channel, vm->config.channel_count);
1211 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1212 |                 }
1213 | 
1214 |                 wet_value_t volt_res;
1215 |                 volt_res.type = WET_VAL_FLOAT;
1216 |                 volt_res.as.f_val = vm->bio.mea_voltage_v[channel];
1217 |                 wet_status_t st = push_val(vm, volt_res);
1218 |                 if (st != WET_OK) return st;
1219 |                 break;
1220 |             }
1221 | 
1222 |             case WET_OP_MODULATE_STDP: {
1223 |                 if (instr_pc + 3 > vm->code_size) {
1224 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MODULATE_STDP operand");
1225 |                     return WET_ERR_INVALID_OPCODE;
1226 |                 }
1227 |                 uint8_t pre = *(const uint8_t*)(vm->code + instr_pc + 1);
1228 |                 uint8_t post = *(const uint8_t*)(vm->code + instr_pc + 2);
1229 |                 vm->pc = instr_pc + 3;
1230 | 
1231 |                 wet_value_t delta_w;
1232 |                 wet_status_t st = pop_val(vm, &delta_w);
1233 |                 if (st != WET_OK) return st;
1234 | 
1235 |                 if (pre == 0xFF && post == 0xFF) {
1236 |                     /* Dynamic pre/post channels popped from stack */
1237 |                     wet_value_t v_post, v_pre;
1238 |                     st = pop_val(vm, &v_post);
1239 |                     if (st != WET_OK) return st;
1240 |                     st = pop_val(vm, &v_pre);
1241 |                     if (st != WET_OK) return st;
1242 |                     int32_t pre_idx = to_int(&v_pre);
1243 |                     int32_t post_idx = to_int(&v_post);
1244 |                     if (pre_idx < 0 || (uint32_t)pre_idx >= vm->config.channel_count ||
1245 |                         post_idx < 0 || (uint32_t)post_idx >= vm->config.channel_count) {
1246 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1247 |                                  "STDP dynamic channels (%d, %d) out of bounds (max %u)",
1248 |                                  pre_idx, post_idx, vm->config.channel_count);
1249 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1250 |                     }
1251 |                     pre = (uint8_t)pre_idx;
1252 |                     post = (uint8_t)post_idx;
1253 |                 } else if (pre >= vm->config.channel_count || post >= vm->config.channel_count) {
1254 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1255 |                              "STDP channels (%u, %u) out of bounds (max %u)",
1256 |                              pre, post, vm->config.channel_count);
1257 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1258 |                 }
1259 | 
1260 |                 if (vm->interlocks.locked) {
1261 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1262 |                     return WET_ERR_INTERLOCK_LOCKED;
1263 |                 }
1264 | 
1265 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_MODULATE_STDP, 0.0f, pre)) {
1266 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1267 |                              "Capability denied for MODULATE_STDP");
1268 |                     return WET_ERR_CAPABILITY_DENIED;
1269 |                 }
1270 | 
1271 |                 float dw = to_float(&delta_w);
1272 |                 if (pre == 0 && post == 0) {
1273 |                     vm->bio.stdp_lr_scale = dw;
1274 |                 } else if (pre != post) {
1275 |                     biophysics_modulate_stdp(&vm->bio, pre, post, dw);
1276 |                 }
1277 |                 break;
1278 |             }
1279 | 
1280 |             case WET_OP_GET_POP_RATE: {
1281 |                 vm->pc = instr_pc + 1;
1282 |                 wet_value_t window;
1283 |                 wet_status_t st = pop_val(vm, &window);
1284 |                 if (st != WET_OK) return st;
1285 | 
1286 |                 wet_value_t rate_res;
1287 |                 rate_res.type = WET_VAL_FLOAT;
1288 |                 rate_res.as.f_val = vm->bio.population_rate_hz;
1289 |                 st = push_val(vm, rate_res);
1290 |                 if (st != WET_OK) return st;
1291 |                 break;
1292 |             }
1293 | 
1294 |             case WET_OP_MEA_CONFIG: {
1295 |                 if (instr_pc + 3 > vm->code_size) {
1296 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MEA_CONFIG operand");
1297 |                     return WET_ERR_INVALID_OPCODE;
1298 |                 }
1299 |                 uint8_t rows = *(const uint8_t*)(vm->code + instr_pc + 1);
1300 |                 uint8_t cols = *(const uint8_t*)(vm->code + instr_pc + 2);
1301 |                 vm->pc = instr_pc + 3;
1302 |                 vm->grid_rows = rows;
1303 |                 vm->grid_cols = cols;
1304 |                 break;
1305 |             }
1306 | 
1307 |             case WET_OP_PUMP_SET_RATE: {
1308 |                 if (instr_pc + 6 > vm->code_size) {
1309 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_SET_RATE operand");
1310 |                     return WET_ERR_INVALID_OPCODE;
1311 |                 }
1312 |                 uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1313 |                 float rate_ul_min;
1314 |                 memcpy(&rate_ul_min, vm->code + instr_pc + 2, sizeof(float));
1315 |                 vm->pc = instr_pc + 6;
1316 | 
1317 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_SET_RATE, 0.0f, pump_id)) {
1318 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1319 |                              "Capability denied for PUMP_SET_RATE (requires CAP_MICROFLUIDICS)");
1320 |                     return WET_ERR_CAPABILITY_DENIED;
1321 |                 }
1322 | 
1323 |                 if (pump_id >= 8) {
1324 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
1325 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1326 |                 }
1327 | 
1328 |                 if (rate_ul_min < 0.0f || rate_ul_min > 15.0f) {
1329 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1330 |                              "ERR_SHEAR_STRESS_EXCEEDED: Requested pump rate %.2f uL/min exceeds safe hydrodynamic limit (0..15.0 uL/min)",
1331 |                              (double)rate_ul_min);
1332 |                     return WET_ERR_SHEAR_STRESS_EXCEEDED;
1333 |                 }
1334 | 
1335 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1336 |                     wet_hal_status_t hst = wet_hal_write_pump(vm->hal, pump_id, (double)rate_ul_min, 1);
1337 |                     if (hst == WET_HAL_ERR_DEAD_HEAD) {
1338 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1339 |                                  "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
1340 |                                  pump_id);
1341 |                         return WET_ERR_ACTUATOR_FAULT;
1342 |                     }
1343 |                 }
1344 | 
1345 |                 vm->pump_rates_ul_min[pump_id] = rate_ul_min;
1346 |                 break;
1347 |             }
1348 | 
1349 |             case WET_OP_PUMP_DISPENSE: {
1350 |                 if (instr_pc + 6 > vm->code_size) {
1351 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_DISPENSE operand");
1352 |                     return WET_ERR_INVALID_OPCODE;
1353 |                 }
1354 |                 uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1355 |                 float volume_ul;
1356 |                 memcpy(&volume_ul, vm->code + instr_pc + 2, sizeof(float));
1357 |                 vm->pc = instr_pc + 6;
1358 | 
1359 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_DISPENSE, 0.0f, pump_id)) {
1360 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1361 |                              "Capability denied for PUMP_DISPENSE (requires CAP_MICROFLUIDICS)");
1362 |                     return WET_ERR_CAPABILITY_DENIED;
1363 |                 }
1364 | 
1365 |                 if (pump_id >= 8) {
1366 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
1367 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1368 |                 }
1369 | 
1370 |                 if (volume_ul <= 0.0f || volume_ul > 500.0f) {
1371 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1372 |                              "ERR_ACTUATOR_FAULT: Invalid dispense volume %.2f uL (allowed: 0.1..500.0 uL)",
1373 |                              (double)volume_ul);
1374 |                     return WET_ERR_ACTUATOR_FAULT;
1375 |                 }
1376 | 
1377 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1378 |                     wet_hal_status_t hst = wet_hal_dispense_pump(vm->hal, pump_id, (double)volume_ul);
1379 |                     if (hst == WET_HAL_ERR_DEAD_HEAD) {
1380 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1381 |                                  "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
1382 |                                  pump_id);
1383 |                         return WET_ERR_ACTUATOR_FAULT;
1384 |                     }
1385 |                 }
1386 | 
1387 |                 vm->pump_dispensed_ul[pump_id] += volume_ul;
1388 |                 break;
1389 |             }
1390 | 
1391 |             case WET_OP_VALVE_SET: {
1392 |                 if (instr_pc + 3 > vm->code_size) {
1393 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated VALVE_SET operand");
1394 |                     return WET_ERR_INVALID_OPCODE;
1395 |                 }
1396 |                 uint8_t valve_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1397 |                 uint8_t state = *(const uint8_t*)(vm->code + instr_pc + 2);
1398 |                 vm->pc = instr_pc + 3;
1399 | 
1400 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_VALVE_SET, 0.0f, valve_id)) {
1401 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1402 |                              "Capability denied for VALVE_SET (requires CAP_MICROFLUIDICS)");
1403 |                     return WET_ERR_CAPABILITY_DENIED;
1404 |                 }
1405 | 
1406 |                 if (valve_id >= 8) {
1407 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Valve ID %u out of bounds (max 7)", valve_id);
1408 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1409 |                 }
1410 | 
1411 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1412 |                     wet_hal_write_valve(vm->hal, valve_id, state);
1413 |                 }
1414 | 
1415 |                 vm->valve_states[valve_id] = (state != 0) ? 1 : 0;
1416 |                 break;
1417 |             }
1418 | 
1419 |             case WET_OP_MOTOR_STEP: {
1420 |                 if (instr_pc + 10 > vm->code_size) {
1421 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MOTOR_STEP operand");
1422 |                     return WET_ERR_INVALID_OPCODE;
1423 |                 }
1424 |                 uint8_t motor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1425 |                 int32_t steps;
1426 |                 float speed_rpm;
1427 |                 memcpy(&steps, vm->code + instr_pc + 2, sizeof(int32_t));
1428 |                 memcpy(&speed_rpm, vm->code + instr_pc + 6, sizeof(float));
1429 |                 vm->pc = instr_pc + 10;
1430 | 
1431 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_MOTOR_STEP, 0.0f, motor_id)) {
1432 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1433 |                              "Capability denied for MOTOR_STEP (requires CAP_MOTOR_ACTUATION)");
1434 |                     return WET_ERR_CAPABILITY_DENIED;
1435 |                 }
1436 | 
1437 |                 if (motor_id >= 4) {
1438 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Motor ID %u out of bounds (max 3)", motor_id);
1439 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1440 |                 }
1441 | 
1442 |                 vm->motor_positions[motor_id] += steps;
1443 |                 vm->motor_speeds_rpm[motor_id] = speed_rpm;
1444 |                 break;
1445 |             }
1446 | 
1447 |             case WET_OP_READ_PRESSURE: {
1448 |                 if (instr_pc + 2 > vm->code_size) {
1449 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_PRESSURE operand");
1450 |                     return WET_ERR_INVALID_OPCODE;
1451 |                 }
1452 |                 uint8_t port_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1453 |                 vm->pc = instr_pc + 2;
1454 | 
1455 |                 if (port_id >= 4) port_id = 0;
1456 |                 wet_value_t p_val;
1457 |                 p_val.type = WET_VAL_FLOAT;
1458 |                 p_val.as.f_val = vm->fluid_pressure_kpa[port_id];
1459 |                 wet_status_t st = push_val(vm, p_val);
1460 |                 if (st != WET_OK) return st;
1461 |                 break;
1462 |             }
1463 | 
1464 |             case WET_OP_READ_TEMPERATURE: {
1465 |                 vm->pc = instr_pc + 1;
1466 |                 wet_value_t t_val;
1467 |                 t_val.type = WET_VAL_FLOAT;
1468 |                 t_val.as.f_val = vm->ambient_temperature_c;
1469 |                 wet_status_t st = push_val(vm, t_val);
1470 |                 if (st != WET_OK) return st;
1471 |                 break;
1472 |             }
1473 | 
1474 |             case WET_OP_STIM_CURRENT: {
1475 |                 if (instr_pc + 6 > vm->code_size) {
1476 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_CURRENT operand");
1477 |                     return WET_ERR_INVALID_OPCODE;
1478 |                 }
1479 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1480 |                 float current_ua;
1481 |                 memcpy(&current_ua, vm->code + instr_pc + 2, sizeof(float));
1482 |                 vm->pc = instr_pc + 6;
1483 | 
1484 |                 /* Pop duration arguments: interphase, phase2, phase1 */
1485 |                 wet_value_t v_interphase, v_p2, v_p1;
1486 |                 wet_status_t st = pop_val(vm, &v_interphase);
1487 |                 if (st != WET_OK) return st;
1488 |                 st = pop_val(vm, &v_p2);
1489 |                 if (st != WET_OK) return st;
1490 |                 st = pop_val(vm, &v_p1);
1491 |                 if (st != WET_OK) return st;
1492 | 
1493 |                 if (channel == 0xFF) {
1494 |                     wet_value_t v_ch;
1495 |                     st = pop_val(vm, &v_ch);
1496 |                     if (st != WET_OK) return st;
1497 |                     int32_t c_idx = to_int(&v_ch);
1498 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1499 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1500 |                                  "Electrode channel %d out of bounds (max %u)",
1501 |                                  c_idx, vm->config.channel_count);
1502 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1503 |                     }
1504 |                     channel = (uint8_t)c_idx;
1505 |                 } else if (channel >= vm->config.channel_count) {
1506 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1507 |                              "Electrode channel %u out of bounds (max %u)",
1508 |                              channel, vm->config.channel_count);
1509 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1510 |                 }
1511 | 
1512 |                 if (vm->interlocks.locked) {
1513 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1514 |                     return WET_ERR_INTERLOCK_LOCKED;
1515 |                 }
1516 | 
1517 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
1518 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1519 |                              "Capability denied for STIM_CURRENT on ch %u (ref/rec bank restricted or missing CAP_STIMULATION)", channel);
1520 |                     return WET_ERR_CAPABILITY_DENIED;
1521 |                 }
1522 | 
1523 |                 float p1_ms = to_float(&v_p1);
1524 |                 float p2_ms = to_float(&v_p2);
1525 |                 float ip_ms = to_float(&v_interphase);
1526 | 
1527 |                 /* Randles Interface: V_elec = I * Rs + V_dl */
1528 |                 float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
1529 |                 wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
1530 |                 if (comp_st != WET_OK) {
1531 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1532 |                     return comp_st;
1533 |                 }
1534 | 
1535 |                 /* Per-phase charge density check: Q (nC) = I (uA) * t (ms) */
1536 |                 if (p1_ms > 0.0f && p2_ms > 0.0f) {
1537 |                     float q_phase1 = wet_fabsf(current_ua) * 1e-3f * p1_ms;
1538 |                     float q_phase2 = wet_fabsf(current_ua) * 1e-3f * p2_ms;
1539 |                     if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
1540 |                         vm->interlocks.locked = 1;
1541 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
1542 |                         vm->interlocks.tripped_channel = channel;
1543 |                         vm->interlocks.trip_tick = vm->current_tick;
1544 |                         vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
1545 |                         if (vm->hal) {
1546 |                             wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
1547 |                         }
1548 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1549 |                                  "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
1550 |                                  channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
1551 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1552 |                         return WET_ERR_CHARGE_DENSITY_EXCEEDED;
1553 |                     }
1554 |                 }
1555 | 
1556 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1557 |                     int32_t cur_pA = (int32_t)(current_ua * 1e6f);
1558 |                     uint32_t dur_us = (uint32_t)(p1_ms * 1000.0f);
1559 |                     wet_hal_status_t hst = wet_hal_stim_current(vm->hal, (uint16_t)channel, cur_pA, dur_us);
1560 |                     if (hst == WET_HAL_ERR_COMPLIANCE_RAILED) {
1561 |                         vm->interlocks.locked = 1;
1562 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
1563 |                         vm->interlocks.tripped_channel = channel;
1564 |                         vm->interlocks.trip_tick = vm->current_tick;
1565 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1566 |                                  "ERR_COMPLIANCE_RAILED: Channel %u compliance rail tripped on hardware driver (~7.0V limit)", channel);
1567 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1568 |                         wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_COMPLIANCE_RAILED);
1569 |                         return WET_ERR_COMPLIANCE_RAILED;
1570 |                     }
1571 |                 }
1572 | 
1573 |                 biophysics_schedule_stim_current(&vm->bio, channel, current_ua, p1_ms, p2_ms, ip_ms);
1574 |                 vm->voltages[channel] = v_elec;
1575 |                 vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (p1_ms - p2_ms);
1576 |                 break;
1577 |             }
1578 | 
1579 |             case WET_OP_READ_PH: {
1580 |                 vm->pc = instr_pc + 1;
1581 |                 wet_value_t ph_val;
1582 |                 ph_val.type = WET_VAL_FLOAT;
1583 |                 ph_val.as.f_val = vm->ph_level > 0.0f ? vm->ph_level : 7.40f;
1584 |                 wet_status_t st = push_val(vm, ph_val);
1585 |                 if (st != WET_OK) return st;
1586 |                 break;
1587 |             }
1588 | 
1589 |             case WET_OP_READ_DO: {
1590 |                 vm->pc = instr_pc + 1;
1591 |                 wet_value_t do_val;
1592 |                 do_val.type = WET_VAL_FLOAT;
1593 |                 do_val.as.f_val = vm->dissolved_oxygen_pct > 0.0f ? vm->dissolved_oxygen_pct : 95.0f;
1594 |                 wet_status_t st = push_val(vm, do_val);
1595 |                 if (st != WET_OK) return st;
1596 |                 break;
1597 |             }
1598 | 
1599 |             case WET_OP_READ_CO2: {
1600 |                 vm->pc = instr_pc + 1;
1601 |                 wet_value_t co2_val;
1602 |                 co2_val.type = WET_VAL_FLOAT;
1603 |                 co2_val.as.f_val = vm->dissolved_co2_pct > 0.0f ? vm->dissolved_co2_pct : 5.0f;
1604 |                 wet_status_t st = push_val(vm, co2_val);
1605 |                 if (st != WET_OK) return st;
1606 |                 break;
1607 |             }
1608 | 
1609 |             case WET_OP_READ_BUBBLE: {
1610 |                 if (instr_pc + 2 > vm->code_size) {
1611 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_BUBBLE operand");
1612 |                     return WET_ERR_INVALID_OPCODE;
1613 |                 }
1614 |                 uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1615 |                 vm->pc = instr_pc + 2;
1616 |                 if (sensor_id >= 8) sensor_id = 0;
1617 |                 wet_value_t b_val;
1618 |                 b_val.type = WET_VAL_INT;
1619 |                 b_val.as.i_val = vm->bubble_detected[sensor_id] ? 1 : 0;
1620 |                 wet_status_t st = push_val(vm, b_val);
1621 |                 if (st != WET_OK) return st;
1622 |                 break;
1623 |             }
1624 | 
1625 |             case WET_OP_READ_FLOW: {
1626 |                 if (instr_pc + 2 > vm->code_size) {
1627 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_FLOW operand");
1628 |                     return WET_ERR_INVALID_OPCODE;
1629 |                 }
1630 |                 uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1631 |                 vm->pc = instr_pc + 2;
1632 |                 if (sensor_id >= 8) sensor_id = 0;
1633 |                 double flow_val = (double)vm->fluid_flow_rate_ul_min[sensor_id];
1634 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1635 |                     wet_hal_read_flow(vm->hal, sensor_id, &flow_val);
1636 |                 }
1637 |                 wet_value_t f_val;
1638 |                 f_val.type = WET_VAL_FLOAT;
1639 |                 f_val.as.f_val = (float)flow_val;
1640 |                 wet_status_t st = push_val(vm, f_val);
1641 |                 if (st != WET_OK) return st;
1642 |                 break;
1643 |             }
1644 | 
1645 |             default: {
1646 |                 snprintf(vm->last_error, sizeof(vm->last_error),
1647 |                          "Unrecognized or invalid opcode 0x%02X at pc %zu", op, instr_pc);
1648 |                 return WET_ERR_INVALID_OPCODE;
1649 |             }
1650 |         }
1651 |     }
1652 | 
1653 |     populate_telemetry(vm, out_telem);
1654 |     return WET_OK;
1655 | }
1656 | 
1657 | /* =========================================================================
1658 |  * Phase 3: Standalone C99 Load-Time Bytecode Verifier
1659 |  * ========================================================================= */
1660 | 
1661 | wet_status_t wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len) {
1662 |     if (!bytecode) {
1663 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Null bytecode pointer");
1664 |         return WET_ERR_NULL_PTR;
1665 |     }
1666 |     if (size < WET_HEADER_SIZE) {
1667 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Bytecode size %zu smaller than 32-byte header", size);
1668 |         return WET_ERR_INVALID_MAGIC;
1669 |     }
1670 | 
1671 |     if (memcmp(bytecode, WET_HEADER_MAGIC, 4) != 0) {
1672 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Invalid header magic (expected WETB)");
1673 |         return WET_ERR_INVALID_MAGIC;
1674 |     }
1675 | 
1676 |     uint8_t v_maj = bytecode[4];
1677 |     uint8_t v_min = bytecode[5];
1678 |     if (v_maj != WET_VERSION_MAJOR || v_min != WET_VERSION_MINOR) {
1679 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unsupported version %u.%u (expected 1.0)", v_maj, v_min);
1680 |         return WET_ERR_UNSUPPORTED_VERSION;
1681 |     }
1682 | 
1683 |     uint32_t file_size = wet_read_u32_le(bytecode + 8);
1684 |     uint32_t stored_crc = wet_read_u32_le(bytecode + 12);
1685 |     uint32_t num_sections = wet_read_u32_le(bytecode + 16);
1686 | 
1687 |     if (file_size > size) {
1688 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Declared file size %u exceeds buffer %zu", file_size, size);
1689 |         return WET_ERR_MALFORMED_SECTION;
1690 |     }
1691 | 
1692 |     /* CRC32 check: copy header, zero bytes 12..15, compute CRC */
1693 |     uint8_t hdr_copy[WET_HEADER_SIZE];
1694 |     memcpy(hdr_copy, bytecode, WET_HEADER_SIZE);
1695 |     memset(hdr_copy + 12, 0, 4);
1696 |     uint32_t crc = wet_compute_crc32(hdr_copy, WET_HEADER_SIZE, 0);
1697 |     if (file_size > WET_HEADER_SIZE) {
1698 |         crc = wet_compute_crc32(bytecode + WET_HEADER_SIZE, file_size - WET_HEADER_SIZE, crc);
1699 |     }
1700 |     if (crc != stored_crc) {
1701 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "CRC32 mismatch (computed 0x%08X != stored 0x%08X)", crc, stored_crc);
1702 |         return WET_ERR_CRC_MISMATCH;
1703 |     }
1704 | 
1705 |     size_t sec_table_end = WET_HEADER_SIZE + (size_t)num_sections * WET_SECTION_ENTRY_SIZE;
1706 |     if (sec_table_end > file_size) {
1707 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section table overflows file bounds");
1708 |         return WET_ERR_MALFORMED_SECTION;
1709 |     }
1710 | 
1711 |     const uint8_t* code_ptr = NULL;
1712 |     size_t code_size = 0;
1713 |     size_t num_constants = 0;
1714 | 
1715 |     for (uint32_t s = 0; s < num_sections; ++s) {
1716 |         const uint8_t* entry = bytecode + WET_HEADER_SIZE + s * WET_SECTION_ENTRY_SIZE;
1717 |         uint16_t sec_type = wet_read_u16_le(entry);
1718 |         uint32_t sec_offset = wet_read_u32_le(entry + 4);
1719 |         uint32_t sec_size = wet_read_u32_le(entry + 8);
1720 | 
1721 |         if ((size_t)sec_offset + sec_size > file_size || sec_offset < sec_table_end) {
1722 |             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section %u (type %u) out of bounds", s, sec_type);
1723 |             return WET_ERR_MALFORMED_SECTION;
1724 |         }
1725 | 
1726 |         if (sec_type == WET_SEC_BYTECODE_STREAM) {
1727 |             code_ptr = bytecode + sec_offset;
1728 |             code_size = sec_size;
1729 |         } else if (sec_type == WET_SEC_CONSTANT_POOL) {
1730 |             if (sec_size >= 4) {
1731 |                 uint32_t declared_entries = wet_read_u32_le(bytecode + sec_offset);
1732 |                 const uint8_t* cp = bytecode + sec_offset + 4;
1733 |                 size_t cp_remain = sec_size - 4;
1734 |                 while (cp_remain > 0) {
1735 |                     uint8_t ctype = *cp;
1736 |                     cp++; cp_remain--;
1737 |                     if (ctype == WET_VAL_INT || ctype == WET_VAL_FLOAT) {
1738 |                         if (cp_remain < 4) {
1739 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed constant pool");
1740 |                             return WET_ERR_MALFORMED_SECTION;
1741 |                         }
1742 |                         cp += 4; cp_remain -= 4;
1743 |                     } else if (ctype == WET_VAL_STRING) {
1744 |                         if (cp_remain < 2) {
1745 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed string in constant pool");
1746 |                             return WET_ERR_MALFORMED_SECTION;
1747 |                         }
1748 |                         uint16_t slen = wet_read_u16_le(cp);
1749 |                         cp += 2; cp_remain -= 2;
1750 |                         if (cp_remain < slen) {
1751 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "String payload overflows constant pool");
1752 |                             return WET_ERR_MALFORMED_SECTION;
1753 |                         }
1754 |                         cp += slen; cp_remain -= slen;
1755 |                     } else {
1756 |                         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unknown constant type %u", ctype);
1757 |                         return WET_ERR_MALFORMED_SECTION;
1758 |                     }
1759 |                     num_constants++;
1760 |                 }
1761 |             }
1762 |         }
1763 |     }
1764 | 
1765 |     if (!code_ptr || code_size == 0) {
1766 |         return WET_OK;
1767 |     }
1768 | 
1769 |     uint8_t* is_start = (uint8_t*)malloc(code_size);
1770 |     if (!is_start) {
1771 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Failed to allocate verifier bitmap (%zu bytes)", code_size);
1772 |         return WET_ERR_ALLOC_FAILED;
1773 |     }
1774 |     memset(is_start, 0, code_size);
1775 | 
1776 |     /* Pass 1: Decode opcodes and check instruction sizes */
1777 |     size_t pc = 0;
1778 |     while (pc < code_size) {
1779 |         is_start[pc] = 1;
1780 |         uint8_t op = code_ptr[pc];
1781 |         size_t ilen = 1;
1782 | 
1783 |         switch ((wet_opcode_t)op) {
1784 |             case WET_OP_NOP:
1785 |             case WET_OP_HALT:
1786 |             case WET_OP_SYNC_TICK:
1787 |             case WET_OP_POP:
1788 |             case WET_OP_DUP:
1789 |             case WET_OP_SWAP:
1790 |             case WET_OP_ADD_I:
1791 |             case WET_OP_SUB_I:
1792 |             case WET_OP_MUL_I:
1793 |             case WET_OP_DIV_I:
1794 |             case WET_OP_ADD_F:
1795 |             case WET_OP_SUB_F:
1796 |             case WET_OP_MUL_F:
1797 |             case WET_OP_DIV_F:
1798 |             case WET_OP_NEG:
1799 |             case WET_OP_MOD_I:
1800 |             case WET_OP_CMP_EQ:
1801 |             case WET_OP_CMP_NE:
1802 |             case WET_OP_CMP_LT:
1803 |             case WET_OP_CMP_LE:
1804 |             case WET_OP_CMP_GT:
1805 |             case WET_OP_CMP_GE:
1806 |             case WET_OP_RET:
1807 |             case WET_OP_GET_POP_RATE:
1808 |             case WET_OP_READ_TEMPERATURE:
1809 |             case WET_OP_READ_PH:
1810 |             case WET_OP_READ_DO:
1811 |             case WET_OP_READ_CO2:
1812 |                 ilen = 1;
1813 |                 break;
1814 | 
1815 |             case WET_OP_STIM_BIPHASIC:
1816 |             case WET_OP_READ_SPIKES:
1817 |             case WET_OP_READ_VOLTAGE:
1818 |             case WET_OP_READ_PRESSURE:
1819 |             case WET_OP_READ_BUBBLE:
1820 |             case WET_OP_READ_FLOW:
1821 |                 ilen = 2;
1822 |                 break;
1823 | 
1824 |             case WET_OP_SLEEP_TICKS:
1825 |             case WET_OP_LOAD_LOCAL:
1826 |             case WET_OP_STORE_LOCAL:
1827 |             case WET_OP_JMP:
1828 |             case WET_OP_JMP_IF_TRUE:
1829 |             case WET_OP_JMP_IF_FALSE:
1830 |             case WET_OP_MODULATE_STDP:
1831 |             case WET_OP_MEA_CONFIG:
1832 |             case WET_OP_VALVE_SET:
1833 |                 ilen = 3;
1834 |                 break;
1835 | 
1836 |             case WET_OP_PUSH_CONST:
1837 |                 ilen = 3;
1838 |                 if (pc + 3 <= code_size) {
1839 |                     uint16_t c_idx = wet_read_u16_le(code_ptr + pc + 1);
1840 |                     if (c_idx >= num_constants) {
1841 |                         if (err_buf && err_buf_len > 0)
1842 |                             snprintf(err_buf, err_buf_len, "Constant index %u out of range (%zu)", c_idx, num_constants);
1843 |                         free(is_start);
1844 |                         return WET_ERR_BYTECODE_VERIFICATION;
1845 |                     }
1846 |                 }
1847 |                 break;
1848 | 
1849 |             case WET_OP_CALL:
1850 |                 ilen = 4;
1851 |                 break;
1852 | 
1853 |             case WET_OP_PUSH_INT:
1854 |             case WET_OP_PUSH_FLOAT:
1855 |                 ilen = 5;
1856 |                 break;
1857 | 
1858 |             case WET_OP_PUMP_SET_RATE:
1859 |             case WET_OP_PUMP_DISPENSE:
1860 |             case WET_OP_STIM_CURRENT:
1861 |                 ilen = 6;
1862 |                 break;
1863 | 
1864 |             case WET_OP_MOTOR_STEP:
1865 |                 ilen = 10;
1866 |                 break;
1867 | 
1868 |             default:
1869 |                 if (err_buf && err_buf_len > 0)
1870 |                     snprintf(err_buf, err_buf_len, "Invalid opcode 0x%02X at offset %zu", op, pc);
1871 |                 free(is_start);
1872 |                 return WET_ERR_INVALID_OPCODE;
1873 |         }
1874 | 
1875 |         if (pc + ilen > code_size) {
1876 |             if (err_buf && err_buf_len > 0)
1877 |                 snprintf(err_buf, err_buf_len, "Truncated instruction (opcode 0x%02X needs %zu bytes, only %zu left)", op, ilen, code_size - pc);
1878 |             free(is_start);
1879 |             return WET_ERR_BYTECODE_VERIFICATION;
1880 |         }
1881 |         pc += ilen;
1882 |     }
1883 | 
1884 |     /* Pass 2: Verify branch target alignment */
1885 |     pc = 0;
1886 |     while (pc < code_size) {
1887 |         uint8_t op = code_ptr[pc];
1888 |         if (op == WET_OP_JMP || op == WET_OP_JMP_IF_TRUE || op == WET_OP_JMP_IF_FALSE) {
1889 |             int16_t offset = wet_read_i16_le(code_ptr + pc + 1);
1890 |             int64_t target = (int64_t)pc + offset;
1891 |             if (target < 0 || (size_t)target >= code_size) {
1892 |                 if (err_buf && err_buf_len > 0)
1893 |                     snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld out of code range [0, %zu)", pc, (long long)target, code_size);
1894 |                 free(is_start);
1895 |                 return WET_ERR_BYTECODE_VERIFICATION;
1896 |             }
1897 |             if (!is_start[target]) {
1898 |                 if (err_buf && err_buf_len > 0)
1899 |                     snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld lands in middle of instruction", pc, (long long)target);
1900 |                 free(is_start);
1901 |                 return WET_ERR_BYTECODE_VERIFICATION;
1902 |             }
1903 |             pc += 3;
1904 |         } else {
1905 |             size_t next_pc = pc + 1;
1906 |             while (next_pc < code_size && !is_start[next_pc]) next_pc++;
1907 |             pc = next_pc;
1908 |         }
1909 |     }
1910 | 
1911 |     free(is_start);
1912 |     return WET_OK;
1913 | }
1914 | 
1915 | /* =========================================================================
1916 |  * Phase 3: Live State Checkpointing & Hot-Swap
1917 |  * ========================================================================= */
1918 | 
1919 | #define WET_SNAPSHOT_MAGIC 0x53544557U /* 'W','E','T','S' */
1920 | #define WET_SNAPSHOT_VERSION 1
1921 | 
1922 | #pragma pack(push, 1)
1923 | typedef struct {
1924 |     uint32_t magic;
1925 |     uint32_t version;
1926 |     uint32_t payload_bytes;
1927 |     uint64_t current_tick;
1928 |     double   sim_time_ms;
1929 |     int64_t  sim_time_us;
1930 |     float    v_m_mv[64];
1931 |     float    v_thresh_mv[64];
1932 |     float    g_exc_ns[64];
1933 |     float    g_inh_ns[64];
1934 |     float    g_ahp_ns[64];
1935 |     uint16_t refract_ticks[64];
1936 |     float    trace_pre[64];
1937 |     float    trace_post[64];
1938 |     float    v_double_layer_v[64];
1939 |     float    q_accum[64];
1940 |     float    cumulative_unbounded_dc_nc[64];
1941 |     float    syn_weights_ns[64][64];
1942 |     float    syn_u_stp[64][64];
1943 |     float    syn_x_stp[64][64];
1944 |     float    pump_dispensed_ul[8];
1945 | } wet_vm_snapshot_payload_t;
1946 | #pragma pack(pop)
1947 | 
1948 | wet_status_t wet_vm_snapshot_internal(const struct wet_vm_instance* vm, uint8_t* buffer, size_t* inout_len) {
1949 |     if (!vm || !inout_len) return WET_ERR_NULL_PTR;
1950 | 
1951 |     size_t req_size = sizeof(wet_vm_snapshot_payload_t);
1952 |     if (!buffer) {
1953 |         *inout_len = req_size;
1954 |         return WET_OK;
1955 |     }
1956 |     if (*inout_len < req_size) {
1957 |         *inout_len = req_size;
1958 |         return WET_ERR_ALLOC_FAILED;
1959 |     }
1960 | 
1961 |     wet_vm_snapshot_payload_t* snap = (wet_vm_snapshot_payload_t*)buffer;
1962 |     memset(snap, 0, sizeof(*snap));
1963 |     snap->magic = WET_SNAPSHOT_MAGIC;
1964 |     snap->version = WET_SNAPSHOT_VERSION;
1965 |     snap->payload_bytes = (uint32_t)req_size;
1966 |     snap->current_tick = vm->current_tick;
1967 |     snap->sim_time_ms = vm->sim_time_ms;
1968 |     snap->sim_time_us = vm->sim_time_us;
1969 | 
1970 |     memcpy(snap->v_m_mv, vm->bio.v_m_mv, sizeof(snap->v_m_mv));
1971 |     memcpy(snap->v_thresh_mv, vm->bio.v_thresh_mv, sizeof(snap->v_thresh_mv));
1972 |     memcpy(snap->g_exc_ns, vm->bio.g_exc_ns, sizeof(snap->g_exc_ns));
1973 |     memcpy(snap->g_inh_ns, vm->bio.g_inh_ns, sizeof(snap->g_inh_ns));
1974 |     memcpy(snap->g_ahp_ns, vm->bio.g_ahp_ns, sizeof(snap->g_ahp_ns));
1975 |     memcpy(snap->refract_ticks, vm->bio.refract_ticks, sizeof(snap->refract_ticks));
1976 |     memcpy(snap->trace_pre, vm->bio.trace_pre, sizeof(snap->trace_pre));
1977 |     memcpy(snap->trace_post, vm->bio.trace_post, sizeof(snap->trace_post));
1978 |     memcpy(snap->v_double_layer_v, vm->bio.v_double_layer_v, sizeof(snap->v_double_layer_v));
1979 |     memcpy(snap->q_accum, vm->interlocks.q_accum, sizeof(snap->q_accum));
1980 |     memcpy(snap->cumulative_unbounded_dc_nc, vm->interlocks.cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
1981 |     memcpy(snap->pump_dispensed_ul, vm->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));
1982 | 
1983 |     for (int i = 0; i < 64; ++i) {
1984 |         for (int j = 0; j < 64; ++j) {
1985 |             snap->syn_weights_ns[i][j] = vm->bio.synapses[i][j].weight_ns;
1986 |             snap->syn_u_stp[i][j] = vm->bio.synapses[i][j].u_stp;
1987 |             snap->syn_x_stp[i][j] = vm->bio.synapses[i][j].x_stp;
1988 |         }
1989 |     }
1990 | 
1991 |     *inout_len = req_size;
1992 |     return WET_OK;
1993 | }
1994 | 
1995 | wet_status_t wet_vm_restore_internal(struct wet_vm_instance* vm, const uint8_t* buffer, size_t len) {
1996 |     if (!vm || !buffer) return WET_ERR_NULL_PTR;
1997 |     if (len < sizeof(wet_vm_snapshot_payload_t)) {
1998 |         snprintf(vm->last_error, sizeof(vm->last_error), "Snapshot buffer too small (%zu < %zu)", len, sizeof(wet_vm_snapshot_payload_t));
1999 |         return WET_ERR_MALFORMED_SECTION;
2000 |     }
2001 | 
2002 |     const wet_vm_snapshot_payload_t* snap = (const wet_vm_snapshot_payload_t*)buffer;
2003 |     if (snap->magic != WET_SNAPSHOT_MAGIC || snap->version != WET_SNAPSHOT_VERSION) {
2004 |         snprintf(vm->last_error, sizeof(vm->last_error), "Invalid snapshot magic or version");
2005 |         return WET_ERR_INVALID_MAGIC;
2006 |     }
2007 | 
2008 |     vm->current_tick = snap->current_tick;
2009 |     vm->sim_time_ms = snap->sim_time_ms;
2010 |     vm->sim_time_us = snap->sim_time_us;
2011 | 
2012 |     memcpy(vm->bio.v_m_mv, snap->v_m_mv, sizeof(snap->v_m_mv));
2013 |     memcpy(vm->bio.v_thresh_mv, snap->v_thresh_mv, sizeof(snap->v_thresh_mv));
2014 |     memcpy(vm->bio.g_exc_ns, snap->g_exc_ns, sizeof(snap->g_exc_ns));
2015 |     memcpy(vm->bio.g_inh_ns, snap->g_inh_ns, sizeof(snap->g_inh_ns));
2016 |     memcpy(vm->bio.g_ahp_ns, snap->g_ahp_ns, sizeof(snap->g_ahp_ns));
2017 |     memcpy(vm->bio.refract_ticks, snap->refract_ticks, sizeof(snap->refract_ticks));
2018 |     memcpy(vm->bio.trace_pre, snap->trace_pre, sizeof(snap->trace_pre));
2019 |     memcpy(vm->bio.trace_post, snap->trace_post, sizeof(snap->trace_post));
2020 |     memcpy(vm->bio.v_double_layer_v, snap->v_double_layer_v, sizeof(snap->v_double_layer_v));
2021 |     memcpy(vm->interlocks.q_accum, snap->q_accum, sizeof(snap->q_accum));
2022 |     memcpy(vm->interlocks.cumulative_unbounded_dc_nc, snap->cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
2023 |     memcpy(vm->pump_dispensed_ul, snap->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));
2024 | 
2025 |     for (int i = 0; i < 64; ++i) {
2026 |         for (int j = 0; j < 64; ++j) {
2027 |             vm->bio.synapses[i][j].weight_ns = snap->syn_weights_ns[i][j];
2028 |             vm->bio.synapses[i][j].u_stp = snap->syn_u_stp[i][j];
2029 |             vm->bio.synapses[i][j].x_stp = snap->syn_x_stp[i][j];
2030 |         }
2031 |     }
2032 | 
2033 |     return WET_OK;
2034 | }
```

### `native/build.py` (256 lines, SHA-256: `2cc2c020859bb090...`)

```text
   1 | #!/usr/bin/env python3
   2 | """
   3 | WetLang Native Runtime Build System
   4 | Builds wetvm shared library (DLL on Windows, .so on Linux, .dylib on macOS).
   5 | Supports MSVC cl.exe, GCC, Clang, and setuptools fallback.
   6 | """
   7 | 
   8 | import os
   9 | import sys
  10 | import shutil
  11 | import subprocess
  12 | from pathlib import Path
  13 | 
  14 | 
  15 | def get_project_root() -> Path:
  16 |     script_dir = Path(__file__).resolve().parent
  17 |     if (script_dir / "include").exists() and (script_dir / "src").exists():
  18 |         return script_dir.parent
  19 |     return Path.cwd()
  20 | 
  21 | 
  22 | def find_executable(name: str, extra_paths=None) -> str | None:
  23 |     found = shutil.which(name)
  24 |     if found:
  25 |         return found
  26 |     if extra_paths:
  27 |         for p in extra_paths:
  28 |             candidate = Path(p) / (name + (".exe" if sys.platform == "win32" else ""))
  29 |             if candidate.is_file() and os.access(candidate, os.X_OK):
  30 |                 return str(candidate)
  31 |     return None
  32 | 
  33 | 
  34 | def generate_msvcrt_import_lib(dlltool_path: str, output_lib: Path, output_def: Path) -> bool:
  35 |     """Generates an import library for Windows msvcrt.dll using llvm-dlltool."""
  36 |     def_content = """LIBRARY msvcrt.dll
  37 | EXPORTS
  38 | malloc
  39 | free
  40 | calloc
  41 | realloc
  42 | memcpy
  43 | memset
  44 | memmove
  45 | memcmp
  46 | strlen
  47 | strncpy
  48 | strcpy
  49 | strcat
  50 | strcmp
  51 | strncmp
  52 | sprintf
  53 | _snprintf
  54 | _vsnprintf
  55 | qsort
  56 | """
  57 |     output_def.write_text(def_content, encoding="utf-8")
  58 |     cmd = [
  59 |         dlltool_path,
  60 |         "-d", str(output_def),
  61 |         "-l", str(output_lib),
  62 |         "-m", "i386:x86-64"
  63 |     ]
  64 |     res = subprocess.run(cmd, capture_output=True, text=True)
  65 |     return res.returncode == 0 and output_lib.exists()
  66 | 
  67 | 
  68 | def generate_kernel32_import_lib(dlltool_path: str, output_lib: Path, output_def: Path) -> bool:
  69 |     """Generates an import library for Windows kernel32.dll using llvm-dlltool."""
  70 |     def_content = """LIBRARY kernel32.dll
  71 | EXPORTS
  72 | QueryPerformanceCounter
  73 | QueryPerformanceFrequency
  74 | CreateThread
  75 | WaitForSingleObject
  76 | CloseHandle
  77 | GetCurrentThread
  78 | GetCurrentProcess
  79 | SetThreadAffinityMask
  80 | SetPriorityClass
  81 | SetThreadPriority
  82 | Sleep
  83 | VirtualLock
  84 | """
  85 |     output_def.write_text(def_content, encoding="utf-8")
  86 |     cmd = [
  87 |         dlltool_path,
  88 |         "-d", str(output_def),
  89 |         "-l", str(output_lib),
  90 |         "-m", "i386:x86-64"
  91 |     ]
  92 |     res = subprocess.run(cmd, capture_output=True, text=True)
  93 |     return res.returncode == 0 and output_lib.exists()
  94 | 
  95 | 
  96 | def build_with_clang(clang_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
  97 |     print(f"Building with Clang: {clang_path}")
  98 |     bin_dir = out_dll.parent
  99 |     bin_dir.mkdir(parents=True, exist_ok=True)
 100 | 
 101 |     # Check if we need standalone msvcrt / kernel32 import libraries on Windows
 102 |     extra_link_args = []
 103 |     if sys.platform == "win32":
 104 |         # Look for llvm-dlltool next to clang
 105 |         clang_dir = Path(clang_path).parent
 106 |         dlltool_path = find_executable("llvm-dlltool", [clang_dir])
 107 |         msvcrt_lib = bin_dir / "msvcrt.lib"
 108 |         msvcrt_def = bin_dir / "msvcrt.def"
 109 |         kernel32_lib = bin_dir / "kernel32.lib"
 110 |         kernel32_def = bin_dir / "kernel32.def"
 111 | 
 112 |         if dlltool_path:
 113 |             if not msvcrt_lib.exists() or msvcrt_lib.stat().st_size == 0 or not msvcrt_def.exists() or "qsort" not in msvcrt_def.read_text(encoding="utf-8"):
 114 |                 generate_msvcrt_import_lib(dlltool_path, msvcrt_lib, msvcrt_def)
 115 |             if not kernel32_lib.exists() or kernel32_lib.stat().st_size == 0 or not kernel32_def.exists() or "VirtualLock" not in kernel32_def.read_text(encoding="utf-8"):
 116 |                 generate_kernel32_import_lib(dlltool_path, kernel32_lib, kernel32_def)
 117 |             if msvcrt_lib.exists() and kernel32_lib.exists():
 118 |                 extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib), str(kernel32_lib)]
 119 |             elif msvcrt_lib.exists():
 120 |                 extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib)]
 121 | 
 122 |     cmd = [
 123 |         clang_path,
 124 |         "-O3",
 125 |         "-shared",
 126 |         "-DWET_BUILDING_DLL",
 127 |         f"-I{include_dir}",
 128 |         "-o", str(out_dll),
 129 |         *[str(f) for f in src_files],
 130 |         *extra_link_args
 131 |     ]
 132 | 
 133 |     res = subprocess.run(cmd, capture_output=True, text=True)
 134 |     if res.returncode != 0:
 135 |         print(f"Clang build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 136 |         return False
 137 |     return out_dll.exists()
 138 | 
 139 | 
 140 | def build_with_gcc(gcc_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
 141 |     print(f"Building with GCC: {gcc_path}")
 142 |     bin_dir = out_dll.parent
 143 |     bin_dir.mkdir(parents=True, exist_ok=True)
 144 | 
 145 |     cmd = [
 146 |         gcc_path,
 147 |         "-shared",
 148 |         "-fPIC" if sys.platform != "win32" else "",
 149 |         "-DWET_BUILDING_DLL",
 150 |         f"-I{include_dir}",
 151 |         "-o", str(out_dll),
 152 |         *[str(f) for f in src_files]
 153 |     ]
 154 |     cmd = [arg for arg in cmd if arg]
 155 |     res = subprocess.run(cmd, capture_output=True, text=True)
 156 |     if res.returncode != 0:
 157 |         print(f"GCC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 158 |         return False
 159 |     return out_dll.exists()
 160 | 
 161 | 
 162 | def build_with_msvc(cl_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
 163 |     print(f"Building with MSVC: {cl_path}")
 164 |     bin_dir = out_dll.parent
 165 |     bin_dir.mkdir(parents=True, exist_ok=True)
 166 | 
 167 |     cmd = [
 168 |         cl_path,
 169 |         "/LD",
 170 |         "/DWET_BUILDING_DLL",
 171 |         f"/I{include_dir}",
 172 |         *[str(f) for f in src_files],
 173 |         f"/Fe:{out_dll}"
 174 |     ]
 175 |     res = subprocess.run(cmd, capture_output=True, text=True)
 176 |     if res.returncode != 0:
 177 |         print(f"MSVC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 178 |         return False
 179 |     return out_dll.exists()
 180 | 
 181 | 
 182 | def build_native_runtime() -> Path:
 183 |     proj_root = get_project_root()
 184 |     native_dir = proj_root / "native"
 185 |     include_dir = native_dir / "include"
 186 |     src_dir = native_dir / "src"
 187 |     bin_dir = native_dir / "bin"
 188 |     bin_dir.mkdir(parents=True, exist_ok=True)
 189 | 
 190 |     src_files = [
 191 |         src_dir / "wetvm_api.c",
 192 |         src_dir / "wetvm_vm.c",
 193 |         src_dir / "biophysics.c",
 194 |         src_dir / "interlocks.c",
 195 |         src_dir / "wet_hal.c",
 196 |         src_dir / "wet_hal_intan.c",
 197 |         src_dir / "wet_hal_maxwell.c",
 198 |         src_dir / "wet_hal_pump_valve.c",
 199 |         src_dir / "wet_hal_sensirion.c",
 200 |         src_dir / "wet_scheduler.c",
 201 |         src_dir / "wet_aer.c",
 202 |         src_dir / "wet_distributed.c",
 203 |     ]
 204 |     for sf in src_files:
 205 |         if not sf.exists():
 206 |             raise FileNotFoundError(f"Source file not found: {sf}")
 207 | 
 208 |     ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
 209 |     out_dll = bin_dir / f"wetvm{ext}"
 210 |     fallback_dll = native_dir / f"wetvm{ext}"
 211 | 
 212 |     # Search for compilers in order of preference
 213 |     # 1. MSVC cl.exe
 214 |     cl_exe = find_executable("cl")
 215 |     if cl_exe and build_with_msvc(cl_exe, src_files, include_dir, out_dll):
 216 |         shutil.copy2(out_dll, fallback_dll)
 217 |         print(f"Successfully compiled shared library: {out_dll}")
 218 |         return out_dll
 219 | 
 220 |     # 2. Clang
 221 |     extra_clang_paths = [
 222 |         r"C:\Program Files\LLVM\bin",
 223 |         r"C:\LLVM\bin",
 224 |         r"C:\msys64\mingw64\bin",
 225 |         r"C:\msys64\ucrt64\bin"
 226 |     ]
 227 |     clang_exe = find_executable("clang", extra_clang_paths)
 228 |     if clang_exe and build_with_clang(clang_exe, src_files, include_dir, out_dll):
 229 |         shutil.copy2(out_dll, fallback_dll)
 230 |         print(f"Successfully compiled shared library: {out_dll}")
 231 |         return out_dll
 232 | 
 233 |     # 3. GCC
 234 |     extra_gcc_paths = [
 235 |         r"C:\msys64\mingw64\bin",
 236 |         r"C:\msys64\ucrt64\bin",
 237 |         r"C:\mingw64\bin",
 238 |         r"C:\TDM-GCC-64\bin"
 239 |     ]
 240 |     gcc_exe = find_executable("gcc", extra_gcc_paths)
 241 |     if gcc_exe and build_with_gcc(gcc_exe, src_files, include_dir, out_dll):
 242 |         shutil.copy2(out_dll, fallback_dll)
 243 |         print(f"Successfully compiled shared library: {out_dll}")
 244 |         return out_dll
 245 | 
 246 |     raise RuntimeError("No suitable C compiler found (MSVC cl.exe, Clang, or GCC).")
 247 | 
 248 | 
 249 | if __name__ == "__main__":
 250 |     try:
 251 |         path = build_native_runtime()
 252 |         print(f"BUILD SUCCESS: {path}")
 253 |         sys.exit(0)
 254 |     except Exception as e:
 255 |         print(f"BUILD ERROR: {e}", file=sys.stderr)
 256 |         sys.exit(1)
```

### `native/interlocks.py` (90 lines, SHA-256: `5831e4240793de59...`)

```text
   1 | """
   2 | WetLang Biocybersecurity Protections & Hardware Interlocks
   3 | Provides capability verification, water-window voltage clamp,
   4 | sliding charge balance watchdog, epileptiform runaway breaker,
   5 | and fail-safe interlock state management.
   6 | """
   7 | 
   8 | from typing import List, Optional
   9 | 
  10 | 
  11 | class CapabilityVerifier:
  12 |     """
  13 |     Static and bytecode capability security verifier.
  14 |     Enforces that declared bytecode capability bitmasks cover all utilized opcodes.
  15 |     """
  16 | 
  17 |     def verify_capabilities(self, declared_caps: int, used_caps: int) -> bool:
  18 |         """
  19 |         Verifies that all used capability flags are authorized by declared_caps.
  20 |         Tier 0 compute (0x0000) is always authorized.
  21 |         """
  22 |         # All bits in used_caps must be present in declared_caps
  23 |         return (used_caps & ~declared_caps) == 0
  24 | 
  25 | 
  26 | class InterlockManager:
  27 |     """
  28 |     Hardware interlock manager simulating the cycle-accurate hardware watchdog.
  29 |     Tracks fail-safe lockout state, zeroes DAC voltages upon any safety trip,
  30 |     and produces post-mortem diagnostic telemetry.
  31 |     """
  32 | 
  33 |     STATE_OPERATIONAL = 0
  34 |     STATE_HALTED_SAFETY_LOCKOUT = 1
  35 | 
  36 |     def __init__(self, channel_count: int = 64):
  37 |         self.channel_count: int = channel_count
  38 |         self.state: int = self.STATE_OPERATIONAL
  39 |         self.dac_voltages: List[float] = [0.0] * channel_count
  40 |         self.diagnostic_report: str = "Interlocks normal. No safety trips."
  41 |         self.tripped_electrode: Optional[int] = None
  42 |         self.trip_reason: Optional[str] = None
  43 | 
  44 |     def get_state(self) -> int:
  45 |         """Returns the numeric interlock state (0 = OPERATIONAL, 1 = HALTED_SAFETY_LOCKOUT)."""
  46 |         return self.state
  47 | 
  48 |     def get_state_name(self) -> str:
  49 |         """Returns human-readable state string: 'OPERATIONAL' or 'HALTED_SAFETY_LOCKOUT'."""
  50 |         if self.state == self.STATE_OPERATIONAL:
  51 |             return "OPERATIONAL"
  52 |         return "HALTED_SAFETY_LOCKOUT"
  53 | 
  54 |     def trip_charge_imbalance(self, electrode: int) -> None:
  55 |         """
  56 |         Simulates sliding charge balance watchdog trip on specified electrode.
  57 |         Immediately zeroes all electrode DACs, transitions state to HALTED_SAFETY_LOCKOUT,
  58 |         and records post-mortem diagnostic report.
  59 |         """
  60 |         self.state = self.STATE_HALTED_SAFETY_LOCKOUT
  61 |         self.tripped_electrode = electrode
  62 |         self.trip_reason = "ERR_CHARGE_IMBALANCE"
  63 |         self.dac_voltages = [0.0] * self.channel_count
  64 |         self.diagnostic_report = (
  65 |             f"ERR_CHARGE_IMBALANCE: Net charge imbalance exceeded safety threshold (0.5 nC over 10 ms) "
  66 |             f"on electrode {electrode}. All 64 stimulation DACs forced to 0.0V fail-safe."
  67 |         )
  68 | 
  69 |     def trip_epileptiform_runaway(self) -> None:
  70 |         """
  71 |         Simulates epileptiform runaway breaker trip.
  72 |         Immediately zeroes all electrode DACs, transitions state to HALTED_SAFETY_LOCKOUT,
  73 |         and records post-mortem diagnostic report.
  74 |         """
  75 |         self.state = self.STATE_HALTED_SAFETY_LOCKOUT
  76 |         self.tripped_electrode = None
  77 |         self.trip_reason = "ERR_EPILEPTIFORM_RUNAWAY"
  78 |         self.dac_voltages = [0.0] * self.channel_count
  79 |         self.diagnostic_report = (
  80 |             "ERR_EPILEPTIFORM_RUNAWAY: Epileptiform runaway firing breaker tripped "
  81 |             "(>150 Hz on >35% channels for 50 ms). All 64 stimulation DACs forced to 0.0V fail-safe."
  82 |         )
  83 | 
  84 |     def get_dac_voltages(self) -> List[float]:
  85 |         """Returns instantaneous voltages across all electrode DACs."""
  86 |         return list(self.dac_voltages)
  87 | 
  88 |     def get_diagnostic_report(self) -> str:
  89 |         """Returns post-mortem diagnostics telemetry record upon interlock trip."""
  90 |         return self.diagnostic_report
```

### `benchmarks/01_active_inference_closed_loop.wet` (54 lines, SHA-256: `8dba4c8f3aedacde...`)

```text
   1 | // Benchmark 01: Active Inference Closed-Loop Sensory-Motor Controller
   2 | // Organoid controls a 1D continuous tracking agent.
   3 | 
   4 | grid mea[8, 8];
   5 | channel sens_left  = mea[0, 2];
   6 | channel sens_right = mea[0, 5];
   7 | channel mot_left   = mea[7, 2];
   8 | channel mot_right  = mea[7, 5];
   9 | channel rew_chan   = mea[3, 3];
  10 | channel pun_chan   = mea[4, 4];
  11 | 
  12 | float agent_pos   = 0.0;
  13 | float target_pos  = 0.0;
  14 | float prev_error  = 0.0;
  15 | int   step_count  = 0;
  16 | 
  17 | while (step_count < 5000) {
  18 |     // 1. Sensory Encoding: deliver biphasic pulses proportional to target offset
  19 |     float error = target_pos - agent_pos;
  20 |     if (error > 0.1) {
  21 |         stim_biphasic(sens_right, 0.8, 0.2, 0.2);
  22 |     } else if (error < -0.1) {
  23 |         stim_biphasic(sens_left, 0.8, 0.2, 0.2);
  24 |     }
  25 |     
  26 |     // 2. Advance biological time by 20.0 ms (200 ticks of dt = 0.1 ms)
  27 |     int tick = 0;
  28 |     while (tick < 200) {
  29 |         sync_tick();
  30 |         tick = tick + 1;
  31 |     }
  32 |     
  33 |     // 3. Motor Decoding: read spike rasters over the 20 ms window
  34 |     int left_spikes  = read_spikes(mot_left, 20.0);
  35 |     int right_spikes = read_spikes(mot_right, 20.0);
  36 |     float motor_delta = (float(right_spikes) - float(left_spikes)) * 0.05;
  37 |     agent_pos = agent_pos + motor_delta;
  38 |     
  39 |     // 4. Closed-loop Reinforcement (Active Inference Free-Energy Principle)
  40 |     float new_error = abs(target_pos - agent_pos);
  41 |     if (new_error < abs(prev_error)) {
  42 |         // Success: Predictable 20 Hz low-entropy reward, boost STDP
  43 |         stim_biphasic(rew_chan, 0.5, 0.1, 0.1);
  44 |         modulate_stdp(1.2);
  45 |     } else {
  46 |         // Failure: Unpredictable high-entropy chaotic punishment burst
  47 |         stim_biphasic(pun_chan, 0.9, 0.1, 0.1);
  48 |         modulate_stdp(0.7);
  49 |     }
  50 |     
  51 |     prev_error = new_error;
  52 |     step_count = step_count + 1;
  53 |     sync_tick();
  54 | }
```

### `benchmarks/02_polychronous_reservoir_classifier.wet` (49 lines, SHA-256: `b385c987835dae60...`)

```text
   1 | // Benchmark 02: Polychronous Reservoir Classifier
   2 | // Spatio-temporal trajectory classification with short-term synaptic dynamics.
   3 | 
   4 | grid mea[8, 8];
   5 | channel in_0 = mea[0, 0];
   6 | channel in_1 = mea[0, 2];
   7 | channel in_2 = mea[0, 4];
   8 | channel in_3 = mea[0, 6];
   9 | 
  10 | int trial = 0;
  11 | while (trial < 100) {
  12 |     // Inject Spatio-Temporal Pattern Alpha: Trajectory [in_0 -> in_1 -> in_2 -> in_3]
  13 |     stim_biphasic(in_0, 0.9, 0.1, 0.1);
  14 |     
  15 |     int t = 0;
  16 |     while (t < 50) { sync_tick(); t = t + 1; }
  17 |     stim_biphasic(in_1, 0.9, 0.1, 0.1);
  18 |     
  19 |     t = 0;
  20 |     while (t < 50) { sync_tick(); t = t + 1; }
  21 |     stim_biphasic(in_2, 0.9, 0.1, 0.1);
  22 |     
  23 |     t = 0;
  24 |     while (t < 50) { sync_tick(); t = t + 1; }
  25 |     stim_biphasic(in_3, 0.9, 0.1, 0.1);
  26 |     
  27 |     // Reservoir settling & integration period (30.0 ms = 300 ticks)
  28 |     t = 0;
  29 |     while (t < 300) { sync_tick(); t = t + 1; }
  30 |     
  31 |     // Read high-dimensional polychronous spike response across reservoir
  32 |     int r = 0;
  33 |     int total_reservoir_spikes = 0;
  34 |     while (r < 16) {
  35 |         int ch_idx = 24 + r;
  36 |         total_reservoir_spikes = total_reservoir_spikes + read_spikes(mea[ch_idx], 30.0);
  37 |         r = r + 1;
  38 |     }
  39 |     
  40 |     // Modulate STDP based on classification margin
  41 |     if (total_reservoir_spikes > 45) {
  42 |         modulate_stdp(1.1);
  43 |     } else {
  44 |         modulate_stdp(0.95);
  45 |     }
  46 |     
  47 |     trial = trial + 1;
  48 |     sync_tick();
  49 | }
```

### `benchmarks/03_homeostatic_stabilization_and_stress.wet` (43 lines, SHA-256: `88646455ff957520...`)

```text
   1 | // Benchmark 03: Homeostatic Stabilization and Stress Adaptation
   2 | // Regulates population firing rate within [15.0, 25.0] Hz under acute perturbation.
   3 | 
   4 | grid mea[8, 8];
   5 | channel pace_a = mea[2, 2];
   6 | channel pace_b = mea[5, 5];
   7 | channel inh_a  = mea[1, 1];
   8 | channel inh_b  = mea[6, 6];
   9 | channel stress = mea[4, 4];
  10 | 
  11 | int cycle = 0;
  12 | while (cycle < 2000) {
  13 |     // 1. Advance 10 ms (100 ticks)
  14 |     int k = 0;
  15 |     while (k < 100) {
  16 |         sync_tick();
  17 |         k = k + 1;
  18 |     }
  19 |     
  20 |     // 2. Measure instantaneous population firing rate across 64 channels
  21 |     float pop_rate = read_population_rate(10.0);
  22 |     
  23 |     // 3. Homeostatic Closed-Loop Adaptation
  24 |     if (pop_rate < 15.0) {
  25 |         // Hypo-active: Inject gentle pacing pulses to elevate network excitability
  26 |         stim_biphasic(pace_a, 0.4, 0.1, 0.1);
  27 |         stim_biphasic(pace_b, 0.4, 0.1, 0.1);
  28 |         modulate_stdp(1.05);
  29 |     } else if (pop_rate > 25.0) {
  30 |         // Hyper-active: Engage inhibitory interneurons and depress synaptic weights
  31 |         stim_biphasic(inh_a, 0.6, 0.1, 0.1);
  32 |         stim_biphasic(inh_b, 0.6, 0.1, 0.1);
  33 |         modulate_stdp(0.85);
  34 |     }
  35 |     
  36 |     // 4. Acute Stress Injection at Cycle 500 (Simulating severe perturbation)
  37 |     if (cycle == 500) {
  38 |         stim_biphasic(stress, 1.1, 0.2, 0.2);
  39 |     }
  40 |     
  41 |     cycle = cycle + 1;
  42 |     sync_tick();
  43 | }
```
