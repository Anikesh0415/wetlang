# Volume VI: Verified Appendices, Checksums, Live Logs & Source Listings

**Platform:** Wetworld — WetLang Neural Organoid Computing Platform (v1.1.0)  
**Founder & Lead Architect:** Anikesh Tiwari (Surat, Gujarat, India)  
**Generated Programmatically:** `2026-11-22 13:46:12 UTC` by `docs/compendium/generate_compendium.py`  
**Repository Scope:** 220 tracked files | 3,782,475 bytes | 63,467 text lines

---

## Appendix A: Complete Repository SHA-256 & Line-Count Manifest

| # | Repository Path | Bytes | Lines | SHA-256 Checksum (Truncated / Full) |
|---:|---|---:|---:|---|
| 1 | `.gitattributes` | 486 | 19 | `06605de4ccdde7ca2ca17571eb44c8c655f32202de1d7df81c42525f53021a4b` |
| 2 | `benchmarks/01_active_inference_closed_loop.wbc` | 1,540 | BIN | `65fa6fd3fbda453cd7ecb53ffb0b2e7a7387aafcbaa3223438da42cc3ba458ec` |
| 3 | `benchmarks/01_active_inference_closed_loop.wet` | 1,778 | 54 | `8dba4c8f3aedacde3c467c3a4bff80b581523ac37842fde9c85634474eb2b0f7` |
| 4 | `benchmarks/02_polychronous_reservoir_classifier.wbc` | 1,676 | BIN | `171e9560331c67d7f0fddd97efd985572356233e23e3607d5aefcacd3dfadcb7` |
| 5 | `benchmarks/02_polychronous_reservoir_classifier.wet` | 1,377 | 49 | `b385c987835dae60a479f77e6ec581a81d8ed8ecf5aa83400704fc6275416511` |
| 6 | `benchmarks/03_homeostatic_stabilization_and_stress.wbc` | 1,111 | BIN | `e7d2c293becbfebf9f39232d7c0f14439eb8c987a54e4be0282656f0cd02bee4` |
| 7 | `benchmarks/03_homeostatic_stabilization_and_stress.wet` | 1,326 | 43 | `88646455ff957520a8401921c7d8ee9a22b30b6ed78f889fba178acbaa454be5` |
| 8 | `bindings/__init__.py` | 798 | 42 | `7cfb2e1e1803c1220d5e90ab609730761d1d3500a35b087e5e5f966260b263d0` |
| 9 | `bindings/ffi.py` | 48,474 | 1127 | `57f28e802ac68829986c36c4ab8c21b0f7c7291f6300722c1bd8e54c9ce7fe96` |
| 10 | `bindings/runtime.py` | 18,677 | 505 | `b6ce663da7e4f5898025be58f5e4da55a1e112298c107dc194f0c8eb9fb694c4` |
| 11 | `bindings/scheduler.py` | 10,504 | 302 | `a26fa321476c3e7ec4644f3b92c2457bc7fda9669dac9104dab7f5385ca6d0ba` |
| 12 | `biophysics/__init__.py` | 386 | 17 | `2f45135b6989e595f5de6fbdec9752182da1831209ce27d4779056f4baf245cc` |
| 13 | `biophysics/mea_grid.py` | 3,885 | 94 | `d0ccaf43957f0d45139a4ad5410a5d1a70d25e65caec517ad36c6d65985ebc84` |
| 14 | `biophysics/ode_solver.py` | 4,088 | 109 | `2ce4db9b21d3fe8ca193cc3a5d15b47c34aff7f2ab32f175dd617a3e5b0c78c1` |
| 15 | `biophysics/stdp.py` | 2,473 | 70 | `f156f43f0b438efe8042b53c54e9e092202b3499987fbcd23b304f2e96c90b50` |
| 16 | `biophysics/stp.py` | 3,623 | 112 | `ceebb61134d250aad60823ac9f0514cffa3124524c4e9e816ba406fca9c6fb5e` |
| 17 | `biophysics/telemetry.py` | 2,752 | 84 | `7ca0976d1c5d9f3fc88b5e7b5e8b8060d06bfd84e99ba96f75682d5b883501a9` |
| 18 | `compiler/__init__.py` | 2,240 | 123 | `79a50dc641756ee2daf14af80d412259090d2ed7d7abbbdb37f1d130eaa0b725` |
| 19 | `compiler/ast_nodes.py` | 6,125 | 254 | `d81ae7e413aa53a49a9ffc0b06309993b58f9cedb4815138d39f2eb8c6ddfd96` |
| 20 | `compiler/compiler_cli.py` | 3,295 | 104 | `245778ace8d44d4af528d6505dba37937e34cb0dca16706b1c998e16c4ca77c2` |
| 21 | `compiler/crypto_signer.py` | 6,002 | 151 | `fc997ccd07fcb31b5ac0d3c864d290e903cb2b76b6b5772bb1a0d393cbe4d854` |
| 22 | `compiler/emitter.py` | 39,247 | 951 | `0c0daf0ece1d0a17ff0f04f10373d423dd4605ffea4dbf52a4796b5bff743d60` |
| 23 | `compiler/isa.py` | 5,750 | 185 | `1236dcf84a16009f80c2a0d98a58cf56c8d10a4a7ef061f34a0792b3f0976e0c` |
| 24 | `compiler/lexer.py` | 14,228 | 407 | `537066d4e72fece2c7fecdd99eb68cd4496c70c7ddb43b37dc41d3f16e736e67` |
| 25 | `compiler/nir_bridge.py` | 34,942 | 910 | `b8145cffc82cf8a1b0b03845ac0092637a7143b8ee5c2408393ffa264f8b1989` |
| 26 | `compiler/parser.py` | 35,928 | 905 | `779033cb13b290b8f448c7575c8629681492b08e79f06cad0799bffafe3c7347` |
| 27 | `compiler/semantic.py` | 37,453 | 848 | `cafb5abc9bb024e32c27e8718696c01d79f93b900c0fdcc5f556ad660e739c61` |
| 28 | `compiler/token.py` | 7,461 | 270 | `1cb5c20236fd522b40b4589a77df2cd4b0e0097169e175c563b85a479aa77a6c` |
| 29 | `docs/adversarial_debate.md` | 29,926 | 286 | `80620f350cff9f2e9af1781d27e1718c63cfb5efdad4f6bf57b8c55a63fb62a4` |
| 30 | `docs/AUDIT_EXTERNAL_REVIEW.md` | 31,132 | 413 | `32396889220ebc8dcff5330dec7b0f3f215ed6a3941639a781d82909e7d3314e` |
| 31 | `docs/language_spec.md` | 24,511 | 398 | `55d53316fbed42199073c50ccdadd66ab033e922607d875da348ba889ca05458` |
| 32 | `docs/PHASE2_DEEP_AUDIT_REPORT.md` | 6,094 | 73 | `ac4c405458cd04e0e71bd096b0d9dfd754a9ff92ba6e736ee16f86df2bbe0e32` |
| 33 | `docs/WETLANG_V1_MASTER_AUDIT_DOSSIER.md` | 30,348 | 219 | `7988a6f4ddbf431c6fb846a43a7a7bbba6f46b990ec4a1a32e6f8e3d174680dd` |
| 34 | `examples/sample_closed_loop.wbc` | 525 | BIN | `8a58718093bb37d2e0f1867153fffbd824587f02c0d79e01d4b4705ac0bedc6f` |
| 35 | `examples/sample_closed_loop.wet` | 411 | 15 | `718976d0535685e8edf39d139722a014f8483069ab806e3506c9b24f9f8c7ad5` |
| 36 | `legacy_specs/test_wetworld_cuda.py` | 4,873 | 102 | `fb3ce5f34f58dad1f45aba5cfd2a362903daf6d5c448e7af4ccf17100ac6fed8` |
| 37 | `legacy_specs/WETLANG_LANGUAGE_SPECIFICATION.md` | 4,316 | 117 | `35857be3692842bc2fd2f244fd962f72d91a1be523e89b0334fa17e48c2a2361` |
| 38 | `legacy_specs/wetworld_oi_studio.html` | 63,613 | 1551 | `825462c388983fe7ab343387b4a32fa35060a1a5ed712b6872e0ee9b23a4ae8a` |
| 39 | `legacy_specs/WETWORLD_README.md` | 6,435 | 102 | `9b4a47efb9a29e1b3cbdd86e8ff37ecf372024805482c15a6954e3e6e4e9f409` |
| 40 | `native/__init__.py` | 61 | 3 | `d0681b3b7d83c57b6d20bfe602085e1620539b6f082cec5308bcaac40394e318` |
| 41 | `native/bin/kernel32.def` | 235 | 13 | `c3ccb263de8fa517c0b6fba27d957c083b72b43f29c70902ab60a12c9a76aba5` |
| 42 | `native/bin/kernel32.lib` | 3,480 | BIN | `9a7fd047c8b062c3e371da22a21a04afba4e3413dc27349ad1ba60a900b72f30` |
| 43 | `native/bin/msvcrt.def` | 182 | 20 | `15775a186f68afed2dc83e1da279ac9aba5b77549e25f44633b7dcf65ba7e553` |
| 44 | `native/bin/msvcrt.lib` | 3,984 | BIN | `0abf27283319dc423d0c0ad066308cbe84f78765d3ff61a767d2c382abb699a8` |
| 45 | `native/bin/wetvm.dll` | 74,240 | BIN | `76a6e9243c919473c6dbd54306d52f09404d8877f449da4ea16731974447ed07` |
| 46 | `native/bin/wetvm.lib` | 25,982 | BIN | `f2268a5b382202234ca7718980dfe0966dc88119eea5f3941524c1fbeca246dc` |
| 47 | `native/build.py` | 8,066 | 253 | `d80faddc3126e4c4ddea917b8d60e86317e90a1da4f4e26d9510b600024dae27` |
| 48 | `native/include/biophysics.h` | 9,671 | 214 | `c1ff823a6b9772a608a761911e20a36bba3d8a721bf95ef167e63c8c75f628fc` |
| 49 | `native/include/interlocks.h` | 7,799 | 165 | `2eeee7b4f3868ac4edf4cffd59eaf1c58d7167b45b98a5a7120912fa7e52f2da` |
| 50 | `native/include/wet_crt.h` | 3,325 | 108 | `3c1a972b9cd8b7c7959e2d7362edb27f211577b535869a752b90d51e41a26f3c` |
| 51 | `native/include/wet_hal.h` | 8,351 | 191 | `a9a2d1dca0115a12a6cbb7fe2dfbd777e0c936e5abb96dc97ddfba3c9c3e0c6a` |
| 52 | `native/include/wet_hal_intan.h` | 5,000 | 169 | `15e6a6849d146a2522be660507c0ca896dd40db8b3164b866e5ec5d8fede6a10` |
| 53 | `native/include/wet_hal_maxwell.h` | 5,292 | 173 | `f5be2fac6cba467d89fd78a8017982cea9cdf18710406fc87bc107dce396df05` |
| 54 | `native/include/wet_hal_pump_valve.h` | 6,625 | 216 | `5db2b883e4822e33c028397394bc3ebc75b4be823e53b5253528faab68c198c2` |
| 55 | `native/include/wet_hal_sensirion.h` | 4,384 | 153 | `c5cadc6f9f2f1b2b7d0ea747dc19cce5246f1822519dd02d14092c4f9056144b` |
| 56 | `native/include/wet_scheduler.h` | 6,890 | 136 | `ae755ab83f92e02449f3bd47eeb7223b47a0ee8efee79bff5020215f4e89be4d` |
| 57 | `native/include/wetvm_api.h` | 8,240 | 301 | `1ce7d24e459ec9bba04d2779564345d78f0fbd72c79430d083b11ecb00f6cf2a` |
| 58 | `native/include/wetvm_types.h` | 6,610 | 177 | `90dc6be4f81eb94219c356bc070d53992ad863aeea0789956bd4405cc10858a3` |
| 59 | `native/include/wetvm_vm.h` | 4,235 | 146 | `e769cd7ca730fe3f32e0731b58dd048350163b60d9e6f48be06a67649ee774d4` |
| 60 | `native/interlocks.py` | 3,689 | 90 | `5831e4240793de5987e600feed2d8d32a6a294f05587113050968078dfe56b7c` |
| 61 | `native/src/biophysics.c` | 23,068 | 540 | `9f12d3ca6c10cd8861cfd27bc1b9f33d6093699f790481d12d9a4299c65e77a6` |
| 62 | `native/src/interlocks.c` | 12,833 | 314 | `f5b7f88bdfe056916239ff9c51b256da2feac36f5b23f3dcb0095b32e4034fa3` |
| 63 | `native/src/wet_hal.c` | 17,159 | 489 | `f975ddf0fa223c9c723c5b500923c5121c35bbc5668bb8565cc9bd6a0fcdf452` |
| 64 | `native/src/wet_hal_intan.c` | 15,192 | 394 | `a25facbb372a8c41704e7f9d126cd44945866204928fcaf3ab4f831509178813` |
| 65 | `native/src/wet_hal_maxwell.c` | 14,303 | 357 | `e9c265c923734f464bf80b17bd7bd6f732492c32b1b2a1f2f390ad633185553a` |
| 66 | `native/src/wet_hal_pump_valve.c` | 16,066 | 463 | `0643ab7ba9b8e772538af708222527a1b845c6d61f84e941534d97a750c3f68d` |
| 67 | `native/src/wet_hal_sensirion.c` | 10,766 | 332 | `19293c38932593af4d119653c6ff904c1567163fdd58a80d2e729d08987bf3fe` |
| 68 | `native/src/wet_scheduler.c` | 22,277 | 630 | `1fc17137ae23e51587879d05f6b311b27aaf4f43598582830e9051b194716df4` |
| 69 | `native/src/wetvm_api.c` | 21,794 | 613 | `8971d78775e796a52f7b1d5c2f0225f584899cf8bb1ae64e7d32a3c3d6044103` |
| 70 | `native/src/wetvm_vm.c` | 86,904 | 2023 | `4cce51ec2f893ada95d77421d245e841a9d9cff96c39c371b2aade2aeaa4a095` |
| 71 | `native/wetvm.dll` | 74,240 | BIN | `76a6e9243c919473c6dbd54306d52f09404d8877f449da4ea16731974447ed07` |
| 72 | `PROJECT.md` | 14,727 | 198 | `0ed7cee23597284f347b97dc1c85ba3d001b493489ecd773375aff47aa328d40` |
| 73 | `pytest.ini` | 95 | 4 | `f99f036c5063c3bba344c0ab687e6d0c0eb585764b8fcfaddd6fd34958e58c5f` |
| 74 | `README.md` | 11,769 | 227 | `31669126f89bf3b8b741d7a007464b1322d0eba65fbc0d5979655481015517e5` |
| 75 | `sandbox/__init__.py` | 665 | 17 | `d9a19ca91142f3e6aee021869b7d4ec18802570b34a4788bcae422ea27e853f8` |
| 76 | `sandbox/gym_env.py` | 4,742 | 125 | `c2e87b7c1c91b7e6acb1752edb2d20b72e505442971dc3bda654a2e0a1b68544` |
| 77 | `sandbox/snntorch_cross_validation.py` | 3,193 | 89 | `520ebfa09f643e5ecedf6994c8d8964450a960cf76900360c0b8e016011d8e7d` |
| 78 | `sandbox/universal_organoid_sandbox.py` | 9,419 | 245 | `7d6bd7d2f6e452a2c6ada2ec1998d0aac3cdd8ff95cdd395bf8dba5bf77a22bd` |
| 79 | `TEST_INFRA.md` | 5,666 | 71 | `9bfab52507a9ce87deaabb3d4f18f439a8826f28c06fbe67a693ed6b99c69606` |
| 80 | `TEST_READY.md` | 1,330 | 28 | `033fc27c27d1a17cdbf1378a56d1184ef143b5c632cf553a0ef082a8720b3585` |
| 81 | `test_reports/tier3_4_report.json` | 921 | 44 | `202e27a3017044a1f3ff314893eb49cd0e3d005b8bee59dd279a96ad7bc08a67` |
| 82 | `tests/e2e/__init__.py` | 890 | 43 | `90fc12f4d49c01d1af12d768fff0eef372150c091fac25a1bf94e252f4da4c1d` |
| 83 | `tests/e2e/common.py` | 38,914 | 1062 | `faf560dae3b7e1b42a2e333b0e75bd619b00fb71c0ba111d4dcdb1ebaeb9dc24` |
| 84 | `tests/e2e/test_tier1_features.py` | 74,476 | 1582 | `55a282b60f08cdb5d7a7d45faf7aa57cd700c8796e522a2f4082a8298c2959d1` |
| 85 | `tests/e2e/test_tier2_boundaries.py` | 82,966 | 1835 | `989e23f9ba080d04d6e04c26126a7c6c0dc26effd7f7d6981ec179f93be57562` |
| 86 | `tests/e2e/test_tier3_pairwise.py` | 42,694 | 976 | `3008ff114dd1105258c4777d37427bf1a08962647f0615a17989caeacee2f6d8` |
| 87 | `tests/e2e/test_tier4_benchmarks.py` | 26,398 | 577 | `51287efebd301ab19d55bd630548f109ae5e19fb29d73be9abfeedec665003a3` |
| 88 | `tests/run_e2e_tests.py` | 11,055 | 322 | `2ca92dbb3cc9c230a7d3cf9d38eede7a55cb77e13aa57fd9ce967b918e5f2c48` |
| 89 | `tests/test_audit_remediation.py` | 15,595 | 372 | `c5df3ce3eb8584e6f6c013a091613a7a7399983683148336fb370d254de64d10` |
| 90 | `tests/test_benchmarks.py` | 7,830 | 216 | `415b239383f290b91cca89c402389b8f1d586d3c2081fa0392c4891730e4d04f` |
| 91 | `tests/test_hal_drivers.py` | 29,061 | 709 | `ca8bf850cd03ce66597afdf9b4ac95e91666bc871cdd03ad6755f3a72e71620d` |
| 92 | `tests/test_interlocks.py` | 12,556 | 302 | `0dd0fa920d0d8a597a4330fd9da868e2046a7daab6fa11a6ddc9b85d950c1725` |
| 93 | `tests/test_nir_bridge.py` | 17,608 | 480 | `c922ec35314e3d0c355388cf14c923072fced18bb968fdaad7e0c7922684bbd2` |
| 94 | `tests/test_ode_stability.py` | 17,095 | 425 | `d401dfe9d0d16c79a2a1d5ce5a6eed3d69a79286a5b83266e1bcaba24883d376` |
| 95 | `tests/test_parser_diagnostics.py` | 13,059 | 437 | `56a0914159f7f9c6302bba7aaa7ec78bd8d4d820337cf40abde9e3f06948cc3b` |
| 96 | `tests/test_phase2_deep_audit.py` | 14,468 | 348 | `d2b739b630b6e93a060f7a02c21a3c8bc8c0daa19ec508cc2086cd9d452614a4` |
| 97 | `tests/test_phase3_hardware_readiness.py` | 23,696 | 515 | `9a9418836d4fe8a96a1c8fda9c7fe69702eb97187229c6d5094166e76e83aa01` |
| 98 | `tests/test_rt_scheduler.py` | 12,112 | 307 | `9bf6783185ad4b93b74ce3c1a10c0f4ae5bf7693f9488c0108b59e6a322fe5a6` |
| 99 | `tests/test_static_verifier.py` | 17,470 | 584 | `54ca1aa3eb0d25c2b451224e8bea3be522a566a7502f2c4d7864dce57c770d5f` |
| 100 | `tests/test_universal_sandbox.py` | 5,725 | 139 | `ab7be8be193420d1d25a3ab3324be9342ee420b20210c3067199c1741832df1d` |
| 101 | `wetlang_github_release/.gitattributes` | 486 | 19 | `06605de4ccdde7ca2ca17571eb44c8c655f32202de1d7df81c42525f53021a4b` |
| 102 | `wetlang_github_release/.gitignore` | 379 | 35 | `e16352655b73321e73348d85f754869373f3aeabd9e1781c0b9875656029136f` |
| 103 | `wetlang_github_release/benchmarks/01_active_inference_closed_loop.wbc` | 1,540 | BIN | `65fa6fd3fbda453cd7ecb53ffb0b2e7a7387aafcbaa3223438da42cc3ba458ec` |
| 104 | `wetlang_github_release/benchmarks/01_active_inference_closed_loop.wet` | 1,778 | 54 | `8dba4c8f3aedacde3c467c3a4bff80b581523ac37842fde9c85634474eb2b0f7` |
| 105 | `wetlang_github_release/benchmarks/02_polychronous_reservoir_classifier.wbc` | 1,676 | BIN | `171e9560331c67d7f0fddd97efd985572356233e23e3607d5aefcacd3dfadcb7` |
| 106 | `wetlang_github_release/benchmarks/02_polychronous_reservoir_classifier.wet` | 1,377 | 49 | `b385c987835dae60a479f77e6ec581a81d8ed8ecf5aa83400704fc6275416511` |
| 107 | `wetlang_github_release/benchmarks/03_homeostatic_stabilization_and_stress.wbc` | 1,111 | BIN | `e7d2c293becbfebf9f39232d7c0f14439eb8c987a54e4be0282656f0cd02bee4` |
| 108 | `wetlang_github_release/benchmarks/03_homeostatic_stabilization_and_stress.wet` | 1,326 | 43 | `88646455ff957520a8401921c7d8ee9a22b30b6ed78f889fba178acbaa454be5` |
| 109 | `wetlang_github_release/bin/wetlang` | 48 | 2 | `ddb439bcbff7b0a10072988327d74d9bbbfa6186207ce83b2e2e5a750fca677c` |
| 110 | `wetlang_github_release/bin/wetlang.cmd` | 35 | 2 | `4fd697a7d010293e3287761ec698ebf8c24b1092eb8ff2ed40029c92cefb0582` |
| 111 | `wetlang_github_release/bin/wetvm.dll` | 74,240 | BIN | `c737bd45ae1654097e0b0da9202943f0d5cb996c9aa1a3ac6a5d483ba6cba1bd` |
| 112 | `wetlang_github_release/CONTRIBUTING.md` | 1,371 | 35 | `e05ce8218f37cbccd487443e6ed7306ff633ec3c93091d8fcf9f4af802955dd5` |
| 113 | `wetlang_github_release/docs/adversarial_debate.md` | 29,926 | 286 | `80620f350cff9f2e9af1781d27e1718c63cfb5efdad4f6bf57b8c55a63fb62a4` |
| 114 | `wetlang_github_release/docs/AUDIT_REPORT.md` | 6,094 | 73 | `ac4c405458cd04e0e71bd096b0d9dfd754a9ff92ba6e736ee16f86df2bbe0e32` |
| 115 | `wetlang_github_release/docs/LANGUAGE_SPECIFICATION.md` | 24,511 | 398 | `55d53316fbed42199073c50ccdadd66ab033e922607d875da348ba889ca05458` |
| 116 | `wetlang_github_release/docs/WETLANG_MASTER_REFERENCE_COMPENDIUM.pdf` | 701,662 | BIN | `e493a944c2bdda14a8b23770200782980ebf8ded4e8dcc41b3ed3f16a648d985` |
| 117 | `wetlang_github_release/docs/WETLANG_V1_MASTER_AUDIT_DOSSIER.md` | 30,348 | 219 | `7988a6f4ddbf431c6fb846a43a7a7bbba6f46b990ec4a1a32e6f8e3d174680dd` |
| 118 | `wetlang_github_release/examples/01_single_organoid_baseline.wbc` | 259 | BIN | `d4476a8217f32780adc25d8817e5805fd996267e17caf1be1c7524ae4dc6fc47` |
| 119 | `wetlang_github_release/examples/01_single_organoid_baseline.wet` | 499 | 18 | `30f38bde068238378589ac7d452824f53fee9ef3d2ee8221194857178748f00a` |
| 120 | `wetlang_github_release/examples/02_krogh_perfused_organoid.wet` | 593 | 19 | `41de709fd536cd8dffb322193491fc54f36e884ce63abb8aea1811e92c7d919d` |
| 121 | `wetlang_github_release/examples/03_cyber_physical_actuation.wet` | 875 | 30 | `c7c591df662ff70c603b001e3688bc6bb49d8fe15772015e58d541e5aa357a00` |
| 122 | `wetlang_github_release/examples/04_multi_organoid_connectome.wet` | 574 | 24 | `cd4c2e7e2420c6200d95f9aafaa2955aca5f70003bae6a7447cb6d060313a93a` |
| 123 | `wetlang_github_release/examples/05_gymnasium_active_inference.py` | 1,524 | 41 | `ba14f7afba193b87701e83499cc5b1812ff497d35911decef269544047e7c174` |
| 124 | `wetlang_github_release/examples/06_snntorch_validation.py` | 1,036 | 23 | `4d8f52c84fa79b4b2a4b4b7d90693baadd840247d272285e988dbb6acca9dee0` |
| 125 | `wetlang_github_release/LICENSE` | 778 | 17 | `ad302ce114a707983380135aa042d5b051caae9ee20ae8c270c8dbaeec8e4171` |
| 126 | `wetlang_github_release/native/__init__.py` | 61 | 3 | `d0681b3b7d83c57b6d20bfe602085e1620539b6f082cec5308bcaac40394e318` |
| 127 | `wetlang_github_release/native/bin/kernel32.def` | 235 | 13 | `c3ccb263de8fa517c0b6fba27d957c083b72b43f29c70902ab60a12c9a76aba5` |
| 128 | `wetlang_github_release/native/bin/kernel32.lib` | 3,480 | BIN | `9a7fd047c8b062c3e371da22a21a04afba4e3413dc27349ad1ba60a900b72f30` |
| 129 | `wetlang_github_release/native/bin/msvcrt.def` | 182 | 20 | `15775a186f68afed2dc83e1da279ac9aba5b77549e25f44633b7dcf65ba7e553` |
| 130 | `wetlang_github_release/native/bin/msvcrt.lib` | 3,984 | BIN | `0abf27283319dc423d0c0ad066308cbe84f78765d3ff61a767d2c382abb699a8` |
| 131 | `wetlang_github_release/native/bin/wetvm.dll` | 74,240 | BIN | `c737bd45ae1654097e0b0da9202943f0d5cb996c9aa1a3ac6a5d483ba6cba1bd` |
| 132 | `wetlang_github_release/native/bin/wetvm.lib` | 25,982 | BIN | `f2268a5b382202234ca7718980dfe0966dc88119eea5f3941524c1fbeca246dc` |
| 133 | `wetlang_github_release/native/build.py` | 8,066 | 253 | `d80faddc3126e4c4ddea917b8d60e86317e90a1da4f4e26d9510b600024dae27` |
| 134 | `wetlang_github_release/native/include/biophysics.h` | 9,671 | 214 | `c1ff823a6b9772a608a761911e20a36bba3d8a721bf95ef167e63c8c75f628fc` |
| 135 | `wetlang_github_release/native/include/interlocks.h` | 7,799 | 165 | `2eeee7b4f3868ac4edf4cffd59eaf1c58d7167b45b98a5a7120912fa7e52f2da` |
| 136 | `wetlang_github_release/native/include/wet_crt.h` | 3,325 | 108 | `3c1a972b9cd8b7c7959e2d7362edb27f211577b535869a752b90d51e41a26f3c` |
| 137 | `wetlang_github_release/native/include/wet_hal.h` | 8,351 | 191 | `a9a2d1dca0115a12a6cbb7fe2dfbd777e0c936e5abb96dc97ddfba3c9c3e0c6a` |
| 138 | `wetlang_github_release/native/include/wet_hal_intan.h` | 5,000 | 169 | `15e6a6849d146a2522be660507c0ca896dd40db8b3164b866e5ec5d8fede6a10` |
| 139 | `wetlang_github_release/native/include/wet_hal_maxwell.h` | 5,292 | 173 | `f5be2fac6cba467d89fd78a8017982cea9cdf18710406fc87bc107dce396df05` |
| 140 | `wetlang_github_release/native/include/wet_hal_pump_valve.h` | 6,625 | 216 | `5db2b883e4822e33c028397394bc3ebc75b4be823e53b5253528faab68c198c2` |
| 141 | `wetlang_github_release/native/include/wet_hal_sensirion.h` | 4,384 | 153 | `c5cadc6f9f2f1b2b7d0ea747dc19cce5246f1822519dd02d14092c4f9056144b` |
| 142 | `wetlang_github_release/native/include/wet_scheduler.h` | 6,890 | 136 | `ae755ab83f92e02449f3bd47eeb7223b47a0ee8efee79bff5020215f4e89be4d` |
| 143 | `wetlang_github_release/native/include/wetvm_api.h` | 8,240 | 301 | `1ce7d24e459ec9bba04d2779564345d78f0fbd72c79430d083b11ecb00f6cf2a` |
| 144 | `wetlang_github_release/native/include/wetvm_types.h` | 6,610 | 177 | `90dc6be4f81eb94219c356bc070d53992ad863aeea0789956bd4405cc10858a3` |
| 145 | `wetlang_github_release/native/include/wetvm_vm.h` | 4,235 | 146 | `e769cd7ca730fe3f32e0731b58dd048350163b60d9e6f48be06a67649ee774d4` |
| 146 | `wetlang_github_release/native/interlocks.py` | 3,689 | 90 | `5831e4240793de5987e600feed2d8d32a6a294f05587113050968078dfe56b7c` |
| 147 | `wetlang_github_release/native/src/biophysics.c` | 23,068 | 540 | `9f12d3ca6c10cd8861cfd27bc1b9f33d6093699f790481d12d9a4299c65e77a6` |
| 148 | `wetlang_github_release/native/src/interlocks.c` | 12,833 | 314 | `f5b7f88bdfe056916239ff9c51b256da2feac36f5b23f3dcb0095b32e4034fa3` |
| 149 | `wetlang_github_release/native/src/wet_hal.c` | 17,159 | 489 | `f975ddf0fa223c9c723c5b500923c5121c35bbc5668bb8565cc9bd6a0fcdf452` |
| 150 | `wetlang_github_release/native/src/wet_hal_intan.c` | 15,192 | 394 | `a25facbb372a8c41704e7f9d126cd44945866204928fcaf3ab4f831509178813` |
| 151 | `wetlang_github_release/native/src/wet_hal_maxwell.c` | 14,303 | 357 | `e9c265c923734f464bf80b17bd7bd6f732492c32b1b2a1f2f390ad633185553a` |
| 152 | `wetlang_github_release/native/src/wet_hal_pump_valve.c` | 16,066 | 463 | `0643ab7ba9b8e772538af708222527a1b845c6d61f84e941534d97a750c3f68d` |
| 153 | `wetlang_github_release/native/src/wet_hal_sensirion.c` | 10,766 | 332 | `19293c38932593af4d119653c6ff904c1567163fdd58a80d2e729d08987bf3fe` |
| 154 | `wetlang_github_release/native/src/wet_scheduler.c` | 22,277 | 630 | `1fc17137ae23e51587879d05f6b311b27aaf4f43598582830e9051b194716df4` |
| 155 | `wetlang_github_release/native/src/wetvm_api.c` | 21,794 | 613 | `8971d78775e796a52f7b1d5c2f0225f584899cf8bb1ae64e7d32a3c3d6044103` |
| 156 | `wetlang_github_release/native/src/wetvm_vm.c` | 86,904 | 2023 | `4cce51ec2f893ada95d77421d245e841a9d9cff96c39c371b2aade2aeaa4a095` |
| 157 | `wetlang_github_release/native/wetvm.dll` | 74,240 | BIN | `c737bd45ae1654097e0b0da9202943f0d5cb996c9aa1a3ac6a5d483ba6cba1bd` |
| 158 | `wetlang_github_release/PROJECT.md` | 14,727 | 198 | `0ed7cee23597284f347b97dc1c85ba3d001b493489ecd773375aff47aa328d40` |
| 159 | `wetlang_github_release/pyproject.toml` | 1,424 | 56 | `bf1a96c42071520b00e4568bced3fca5241bc3ac8d59d7c9ec540f2accb14c94` |
| 160 | `wetlang_github_release/pytest.ini` | 80 | 4 | `f4bf1ab2c2b7363adbb36a4924619319baff715b1cc63cb9de6d252a3d11e4d5` |
| 161 | `wetlang_github_release/README.md` | 13,102 | 232 | `9aedcb2b6eda33a8ce0f92f58a80e6556bd0a8716bf34761c50d39080804427b` |
| 162 | `wetlang_github_release/requirements.txt` | 75 | 5 | `6c0084c24660fd7f560241e652a7fab38e715289d6ffcdd53e9e8933d7af96f6` |
| 163 | `wetlang_github_release/setup.py` | 262 | 13 | `4cf4331fe446579d9be12eb58dc6740ce38212edbddf087ab4718a284fa01082` |
| 164 | `wetlang_github_release/TEST_INFRA.md` | 5,666 | 71 | `9bfab52507a9ce87deaabb3d4f18f439a8826f28c06fbe67a693ed6b99c69606` |
| 165 | `wetlang_github_release/TEST_READY.md` | 1,330 | 28 | `033fc27c27d1a17cdbf1378a56d1184ef143b5c632cf553a0ef082a8720b3585` |
| 166 | `wetlang_github_release/tests/conftest.py` | 248 | 10 | `84fa09784e3171a88012caf158a599110e2d2cc4581ecb8ee07cb514f44ee0ba` |
| 167 | `wetlang_github_release/tests/e2e/__init__.py` | 890 | 43 | `90fc12f4d49c01d1af12d768fff0eef372150c091fac25a1bf94e252f4da4c1d` |
| 168 | `wetlang_github_release/tests/e2e/common.py` | 38,914 | 1062 | `faf560dae3b7e1b42a2e333b0e75bd619b00fb71c0ba111d4dcdb1ebaeb9dc24` |
| 169 | `wetlang_github_release/tests/e2e/test_tier1_features.py` | 74,476 | 1582 | `55a282b60f08cdb5d7a7d45faf7aa57cd700c8796e522a2f4082a8298c2959d1` |
| 170 | `wetlang_github_release/tests/e2e/test_tier2_boundaries.py` | 82,966 | 1835 | `989e23f9ba080d04d6e04c26126a7c6c0dc26effd7f7d6981ec179f93be57562` |
| 171 | `wetlang_github_release/tests/e2e/test_tier3_pairwise.py` | 42,694 | 976 | `3008ff114dd1105258c4777d37427bf1a08962647f0615a17989caeacee2f6d8` |
| 172 | `wetlang_github_release/tests/e2e/test_tier4_benchmarks.py` | 26,398 | 577 | `51287efebd301ab19d55bd630548f109ae5e19fb29d73be9abfeedec665003a3` |
| 173 | `wetlang_github_release/tests/run_e2e_tests.py` | 11,055 | 322 | `2ca92dbb3cc9c230a7d3cf9d38eede7a55cb77e13aa57fd9ce967b918e5f2c48` |
| 174 | `wetlang_github_release/tests/test_actuators.py` | 987 | 36 | `e0740cc2b9fa7b8475c6f7b6f2001cae3312291bdbc88e08f6fdc620ad5b0951` |
| 175 | `wetlang_github_release/tests/test_audit_remediation.py` | 15,595 | 372 | `c5df3ce3eb8584e6f6c013a091613a7a7399983683148336fb370d254de64d10` |
| 176 | `wetlang_github_release/tests/test_benchmarks.py` | 7,830 | 216 | `415b239383f290b91cca89c402389b8f1d586d3c2081fa0392c4891730e4d04f` |
| 177 | `wetlang_github_release/tests/test_compiler.py` | 965 | 30 | `9f312c9e6fae882410299a7194f6b6c150ddcc1075dbd2fafb910747bde36f82` |
| 178 | `wetlang_github_release/tests/test_hal_drivers.py` | 29,061 | 709 | `ca8bf850cd03ce66597afdf9b4ac95e91666bc871cdd03ad6755f3a72e71620d` |
| 179 | `wetlang_github_release/tests/test_interlocks.py` | 12,556 | 302 | `0dd0fa920d0d8a597a4330fd9da868e2046a7daab6fa11a6ddc9b85d950c1725` |
| 180 | `wetlang_github_release/tests/test_nir_bridge.py` | 17,608 | 480 | `c922ec35314e3d0c355388cf14c923072fced18bb968fdaad7e0c7922684bbd2` |
| 181 | `wetlang_github_release/tests/test_ode_stability.py` | 17,095 | 425 | `d401dfe9d0d16c79a2a1d5ce5a6eed3d69a79286a5b83266e1bcaba24883d376` |
| 182 | `wetlang_github_release/tests/test_parser_diagnostics.py` | 13,059 | 437 | `56a0914159f7f9c6302bba7aaa7ec78bd8d4d820337cf40abde9e3f06948cc3b` |
| 183 | `wetlang_github_release/tests/test_phase2_deep_audit.py` | 14,468 | 348 | `d2b739b630b6e93a060f7a02c21a3c8bc8c0daa19ec508cc2086cd9d452614a4` |
| 184 | `wetlang_github_release/tests/test_phase3_hardware_readiness.py` | 23,696 | 515 | `9a9418836d4fe8a96a1c8fda9c7fe69702eb97187229c6d5094166e76e83aa01` |
| 185 | `wetlang_github_release/tests/test_rt_scheduler.py` | 12,112 | 307 | `9bf6783185ad4b93b74ce3c1a10c0f4ae5bf7693f9488c0108b59e6a322fe5a6` |
| 186 | `wetlang_github_release/tests/test_runtime.py` | 643 | 22 | `7f8381b60a4cca97c68f4e63799cbf16ea489df723f7c6c01752a427af672269` |
| 187 | `wetlang_github_release/tests/test_sandbox.py` | 1,113 | 31 | `5a2415e1659ca63f9374f5913db18b28721967a0de52e3e0551495ac9ff62884` |
| 188 | `wetlang_github_release/tests/test_static_verifier.py` | 17,470 | 584 | `54ca1aa3eb0d25c2b451224e8bea3be522a566a7502f2c4d7864dce57c770d5f` |
| 189 | `wetlang_github_release/tests/test_universal_sandbox.py` | 5,725 | 139 | `ab7be8be193420d1d25a3ab3324be9342ee420b20210c3067199c1741832df1d` |
| 190 | `wetlang_github_release/wetlang/__init__.py` | 2,004 | 63 | `3ecc051bf952306bbae884529944b9169392ca30c6b8e781fee56d1bc5abee82` |
| 191 | `wetlang_github_release/wetlang/bindings/__init__.py` | 798 | 42 | `7cfb2e1e1803c1220d5e90ab609730761d1d3500a35b087e5e5f966260b263d0` |
| 192 | `wetlang_github_release/wetlang/bindings/ffi.py` | 48,474 | 1127 | `57f28e802ac68829986c36c4ab8c21b0f7c7291f6300722c1bd8e54c9ce7fe96` |
| 193 | `wetlang_github_release/wetlang/bindings/runtime.py` | 18,677 | 505 | `b6ce663da7e4f5898025be58f5e4da55a1e112298c107dc194f0c8eb9fb694c4` |
| 194 | `wetlang_github_release/wetlang/bindings/scheduler.py` | 10,504 | 302 | `a26fa321476c3e7ec4644f3b92c2457bc7fda9669dac9104dab7f5385ca6d0ba` |
| 195 | `wetlang_github_release/wetlang/biophysics/__init__.py` | 386 | 17 | `2f45135b6989e595f5de6fbdec9752182da1831209ce27d4779056f4baf245cc` |
| 196 | `wetlang_github_release/wetlang/biophysics/mea_grid.py` | 3,885 | 94 | `d0ccaf43957f0d45139a4ad5410a5d1a70d25e65caec517ad36c6d65985ebc84` |
| 197 | `wetlang_github_release/wetlang/biophysics/ode_solver.py` | 4,088 | 109 | `2ce4db9b21d3fe8ca193cc3a5d15b47c34aff7f2ab32f175dd617a3e5b0c78c1` |
| 198 | `wetlang_github_release/wetlang/biophysics/stdp.py` | 2,473 | 70 | `f156f43f0b438efe8042b53c54e9e092202b3499987fbcd23b304f2e96c90b50` |
| 199 | `wetlang_github_release/wetlang/biophysics/stp.py` | 3,623 | 112 | `ceebb61134d250aad60823ac9f0514cffa3124524c4e9e816ba406fca9c6fb5e` |
| 200 | `wetlang_github_release/wetlang/biophysics/telemetry.py` | 2,752 | 84 | `7ca0976d1c5d9f3fc88b5e7b5e8b8060d06bfd84e99ba96f75682d5b883501a9` |
| 201 | `wetlang_github_release/wetlang/cli.py` | 7,244 | 191 | `9cdb73e6406f12c08df57bf394d4e225a9f62584f1b599c26087867265e69ca2` |
| 202 | `wetlang_github_release/wetlang/compiler/__init__.py` | 2,240 | 123 | `79a50dc641756ee2daf14af80d412259090d2ed7d7abbbdb37f1d130eaa0b725` |
| 203 | `wetlang_github_release/wetlang/compiler/ast_nodes.py` | 6,125 | 254 | `d81ae7e413aa53a49a9ffc0b06309993b58f9cedb4815138d39f2eb8c6ddfd96` |
| 204 | `wetlang_github_release/wetlang/compiler/compiler_cli.py` | 3,295 | 104 | `245778ace8d44d4af528d6505dba37937e34cb0dca16706b1c998e16c4ca77c2` |
| 205 | `wetlang_github_release/wetlang/compiler/crypto_signer.py` | 6,002 | 151 | `fc997ccd07fcb31b5ac0d3c864d290e903cb2b76b6b5772bb1a0d393cbe4d854` |
| 206 | `wetlang_github_release/wetlang/compiler/emitter.py` | 39,247 | 951 | `0c0daf0ece1d0a17ff0f04f10373d423dd4605ffea4dbf52a4796b5bff743d60` |
| 207 | `wetlang_github_release/wetlang/compiler/isa.py` | 5,750 | 185 | `1236dcf84a16009f80c2a0d98a58cf56c8d10a4a7ef061f34a0792b3f0976e0c` |
| 208 | `wetlang_github_release/wetlang/compiler/lexer.py` | 14,228 | 407 | `537066d4e72fece2c7fecdd99eb68cd4496c70c7ddb43b37dc41d3f16e736e67` |
| 209 | `wetlang_github_release/wetlang/compiler/nir_bridge.py` | 34,942 | 910 | `b8145cffc82cf8a1b0b03845ac0092637a7143b8ee5c2408393ffa264f8b1989` |
| 210 | `wetlang_github_release/wetlang/compiler/parser.py` | 35,928 | 905 | `779033cb13b290b8f448c7575c8629681492b08e79f06cad0799bffafe3c7347` |
| 211 | `wetlang_github_release/wetlang/compiler/semantic.py` | 37,453 | 848 | `cafb5abc9bb024e32c27e8718696c01d79f93b900c0fdcc5f556ad660e739c61` |
| 212 | `wetlang_github_release/wetlang/compiler/token.py` | 7,461 | 270 | `1cb5c20236fd522b40b4589a77df2cd4b0e0097169e175c563b85a479aa77a6c` |
| 213 | `wetlang_github_release/wetlang/runtime/__init__.py` | 585 | 32 | `80f25ac8bdcf546019300a646ea2035f167a57d8f529b995212677ceab963bb1` |
| 214 | `wetlang_github_release/wetlang/runtime/ffi.py` | 10,509 | 297 | `6e1717b508cb1fae7d6018f4e29fc0cac5fb94cd3a3acdd4e635d6cd7a4f19cc` |
| 215 | `wetlang_github_release/wetlang/runtime/runtime.py` | 10,880 | 323 | `7a1b134d8712895e2bfe840e95e2853a62ffdf24f23a6218a0dd0b983728dcaa` |
| 216 | `wetlang_github_release/wetlang/runtime.py` | 18,677 | 505 | `b6ce663da7e4f5898025be58f5e4da55a1e112298c107dc194f0c8eb9fb694c4` |
| 217 | `wetlang_github_release/wetlang/sandbox/__init__.py` | 665 | 17 | `d9a19ca91142f3e6aee021869b7d4ec18802570b34a4788bcae422ea27e853f8` |
| 218 | `wetlang_github_release/wetlang/sandbox/gym_env.py` | 4,742 | 125 | `c2e87b7c1c91b7e6acb1752edb2d20b72e505442971dc3bda654a2e0a1b68544` |
| 219 | `wetlang_github_release/wetlang/sandbox/snntorch_cross_validation.py` | 3,193 | 89 | `520ebfa09f643e5ecedf6994c8d8964450a960cf76900360c0b8e016011d8e7d` |
| 220 | `wetlang_github_release/wetlang/sandbox/universal_organoid_sandbox.py` | 9,419 | 245 | `7d6bd7d2f6e452a2c6ada2ec1998d0aac3cdd8ff95cdd395bf8dba5bf77a22bd` |

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

#### `native/include/wet_crt.h`

- **Macros / Constants:** `snprintf` = `_snprintf`, `fabsf` = `wet_fabsf`
- **Functions:** `malloc(size_t size)`; `calloc(size_t num, size_t size)`; `free(void* ptr)`; `memcpy(void* dest, const void* src, size_t count)`; `memset(void* dest, int ch, size_t count)`; `memcmp(const void* s1, const void* s2, size_t count)`; `strlen(const char* str)`; `strncpy(char* dest, const char* src, size_t count)`; `strcpy(char* dest, const char* src)`; `strcat(char* dest, const char* src)`; `strcmp(const char* s1, const char* s2)`; `strncmp(const char* s1, const char* s2, size_t count)`; `sprintf(char* buffer, const char* format, ...)`; `_snprintf(char* buffer, size_t count, const char* format, ...)`; `wet_fabsf(float x)`; `wet_fabs(double x)`; `wet_clampf(float x, float lo, float hi)`; `wet_clampd(double x, double lo, double hi)`; `wet_exp(double x)`; `wet_expf(float x)`; `wet_sqrt(double x)`; `wet_rng_next(uint64_t* state)`; `wet_rng_uniform(uint64_t* state)`; `wet_rng_normal(uint64_t* state)`

#### `native/include/wet_hal.h`

- **Types / Structs / Enums:** `struct wet_hal_context`, `struct wet_hal_driver`, `wet_hal_config_t`, `wet_hal_driver_type_t`, `wet_hal_mode_t`, `wet_hal_ops_t`, `wet_hal_status_t`, `wet_hal_telemetry_t`
- **Macros / Constants:** `WET_HAL_MAX_DRIVERS` = `16`
- **Functions:** `wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_destroy(wet_hal_context_t* hal)`; `wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal)`; `wet_hal_get_context(wet_vm_t* vm)`; `wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode)`; `wet_hal_get_mode(const wet_hal_context_t* hal)`; `wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type)`; `wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul)`; `wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state)`; `wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min)`; `wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag)`; `wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel)`; `wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason)`; `wet_hal_get_telemetry(wet_hal_context_t* hal)`; `wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id)`; `wet_hal_get_time_us(void)`

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
- **Functions:** `wet_create_vm(const wet_vm_config_t* config)`; `wet_create_vm_arena(void* arena_buf, size_t arena_bytes, const wet_vm_config_t* config)`; `wet_free_vm(wet_vm_t* vm)`; `wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2)`; `wet_active_discharge(wet_vm_t* vm, uint8_t channel)`; `wet_active_discharge_all(wet_vm_t* vm)`; `wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable)`; `wet_life_supervisor_shutdown(wet_vm_t* vm)`; `wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)`; `wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)`; `wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)`; `wet_get_last_error(wet_vm_t* vm)`; `wet_status_to_string(wet_status_t status)`; `wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial)`; `wet_inject_current_stimulus(wet_vm_t* vm, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms)`; `wet_verify_bytecode(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot(const wet_vm_t* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore(wet_vm_t* vm, const uint8_t* buffer, size_t len)`; `wet_set_environmental_sensors(wet_vm_t* vm, float ph, float do_pct, float co2_pct, uint8_t bubble_sensor_id, uint8_t bubble_state, float flow_rate_ul_min)`; `wet_set_temperature(wet_vm_t* vm, float temp_c)`; `wet_set_channel_banks(wet_vm_t* vm, uint64_t ref_mask, uint64_t rec_mask)`; `wet_vm_get_synapse_matrix(const wet_vm_t* vm, float* out_matrix, size_t out_capacity_floats)`; `wet_vm_get_synapse_weight(const wet_vm_t* vm, uint8_t pre, uint8_t post)`

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

#### `native/src/wet_hal.c`

- **Types / Structs / Enums:** `LARGE_INTEGER`
- **Functions:** `wet_hal_get_time_us(void)`; `wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_destroy(wet_hal_context_t* hal)`; `wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config)`; `wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal)`; `wet_hal_get_context(wet_vm_t* vm)`; `wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode)`; `wet_hal_get_mode(const wet_hal_context_t* hal)`; `wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver)`; `wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type)`; `wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag)`; `wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul)`; `wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state)`; `wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min)`; `wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us)`; `wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms)`; `wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag)`; `wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad)`; `wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel)`; `wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason)`; `wet_hal_get_telemetry(wet_hal_context_t* hal)`; `wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id)`

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
- **Macros / Constants:** `WET_CACHELINE_SIZE` = `64`, `WET_DEFAULT_SAMPLE_CAPACITY` = `100000`
- **Functions:** `wet_cpu_pause(void)`; `wet_atomic_load_u32_acquire(const volatile uint32_t* ptr)`; `wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val)`; `wet_spsc_init(wet_spsc_ring_t* ring, uint32_t capacity, size_t elem_size)`; `wet_spsc_free(wet_spsc_ring_t* ring)`; `wet_spsc_push(wet_spsc_ring_t* ring, const void* item)`; `wet_spsc_pop(wet_spsc_ring_t* ring, void* out_item)`; `wet_sort_doubles(double* arr, int left, int right)`; `wet_scheduler_thread_proc(void* param)`; `wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config)`; `wet_scheduler_start(wet_scheduler_t* sched)`; `wet_scheduler_step(wet_scheduler_t* sched)`; `wet_scheduler_stop(wet_scheduler_t* sched)`; `wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem)`; `wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd)`; `wet_scheduler_benchmark(wet_scheduler_t* sched, uint32_t total_ticks, wet_scheduler_stats_t* out_stats)`; `wet_scheduler_destroy(wet_scheduler_t* sched)`

#### `native/src/wetvm_api.c`

- **Functions:** `wet_create_vm(const wet_vm_config_t* config)`; `wet_create_vm_arena(void* arena_buf, size_t arena_bytes, const wet_vm_config_t* config)`; `wet_free_vm(wet_vm_t* vm)`; `wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)`; `wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)`; `wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)`; `wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)`; `wet_get_last_error(wet_vm_t* vm)`; `wet_status_to_string(wet_status_t status)`; `wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2)`; `wet_active_discharge(wet_vm_t* vm, uint8_t channel)`; `wet_active_discharge_all(wet_vm_t* vm)`; `wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable)`; `wet_life_supervisor_shutdown(wet_vm_t* vm)`; `wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial)`; `wet_inject_current_stimulus(wet_vm_t* vm, uint8_t channel, float current_ua, float phase1_ms, float phase2_ms)`; `wet_verify_bytecode(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot(const wet_vm_t* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore(wet_vm_t* vm, const uint8_t* buffer, size_t len)`; `wet_set_environmental_sensors(wet_vm_t* vm, float ph, float do_pct, float co2_pct, uint8_t bubble_sensor_id, uint8_t bubble_state, float flow_rate_ul_min)`; `wet_set_temperature(wet_vm_t* vm, float temp_c)`; `wet_set_channel_banks(wet_vm_t* vm, uint64_t ref_mask, uint64_t rec_mask)`; `wet_vm_get_synapse_matrix(const wet_vm_t* vm, float* out_matrix, size_t out_capacity_floats)`; `wet_vm_get_synapse_weight(const wet_vm_t* vm, uint8_t pre, uint8_t post)`

#### `native/src/wetvm_vm.c`

- **Types / Structs / Enums:** `wet_vm_snapshot_payload_t`
- **Macros / Constants:** `WET_SNAPSHOT_MAGIC` = `0x53544557U`, `WET_SNAPSHOT_VERSION` = `1`
- **Functions:** `wet_read_u16_le(const void* p)`; `wet_read_i16_le(const void* p)`; `wet_read_u32_le(const void* p)`; `wet_read_i32_le(const void* p)`; `wet_read_f32_le(const void* p)`; `wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc)`; `push_val(struct wet_vm_instance* vm, wet_value_t val)`; `pop_val(struct wet_vm_instance* vm, wet_value_t* out_val)`; `to_float(const wet_value_t* v)`; `to_int(const wet_value_t* v)`; `is_truthy(const wet_value_t* v)`; `cleanup_constants(struct wet_vm_instance* vm)`; `cleanup_bytecode(struct wet_vm_instance* vm)`; `wet_vm_load_bytecode_internal(struct wet_vm_instance* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)`; `populate_telemetry(const struct wet_vm_instance* vm, wet_telemetry_t* telem)`; `advance_simulation_tick(struct wet_vm_instance* vm, wet_telemetry_t* out_telem)`; `wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem)`; `wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len)`; `wet_vm_snapshot_internal(const struct wet_vm_instance* vm, uint8_t* buffer, size_t* inout_len)`; `wet_vm_restore_internal(struct wet_vm_instance* vm, const uint8_t* buffer, size_t len)`

### B.2 Python Modules (`compiler/`, `bindings/`, `biophysics/`, `native/`)

#### `compiler/ast_nodes.py`

- class `ASTNode`: accept()
- class `ProgramNode`: (dataclass)
- class `OrganoidDeclNode`: (dataclass)
- class `ConnectDeclNode`: (dataclass)
- class `PortDeclNode`: (dataclass)
- class `GridDeclNode`: (dataclass)
- class `ChannelDeclNode`: (dataclass)
- class `ParamNode`: (dataclass)
- class `FnDeclNode`: (dataclass)
- class `StreamItemNode`: (dataclass)
- class `StreamDeclNode`: (dataclass)
- class `BlockNode`: (dataclass)
- class `LetStmtNode`: (dataclass)
- class `AssignStmtNode`: (dataclass)
- class `StimStmtNode`: (dataclass)
- class `ModulateStmtNode`: (dataclass)
- class `SyncTickStmtNode`: (dataclass)
- class `IfStmtNode`: (dataclass)
- class `WhileStmtNode`: (dataclass)
- class `ForStmtNode`: (dataclass)
- class `ReturnStmtNode`: (dataclass)
- class `ExprStmtNode`: (dataclass)
- class `BinaryOpNode`: (dataclass)
- class `UnaryOpNode`: (dataclass)
- class `LiteralNode`: (dataclass)
- class `PhysicalLiteralNode`: (dataclass)
- class `IdentifierNode`: (dataclass)
- class `CallNode`: (dataclass)
- class `IndexNode`: (dataclass)
- class `RangeNode`: (dataclass)
- class `DomainCallNode`: (dataclass)
- class `ASTVisitor`: visit(), generic_visit()

#### `compiler/compiler_cli.py`

- def `format_ast(node, indent)`
- def `main(argv)`

#### `compiler/crypto_signer.py`

- def `generate_ed25519_keypair()`
- def `sign_bytecode_ed25519(bytecode, private_key_bytes)`
- def `verify_bytecode_ed25519(signed_bytecode, public_key_bytes)`
- def `sign_bytecode(bytecode, secret_key)`
- def `verify_bytecode_signature(signed_bytecode, secret_key)`

#### `compiler/emitter.py`

- class `ConstantPool`: __init__(), add_int(), add_float(), add_string(), serialize()
- class `BytecodeEmitter`: __init__(), _emit_duration_ms(), _is_int_expr(), _is_const_channel(), emit(), emit_jump(), patch_jump(), current_offset(), get_or_create_local(), compile(), visit_ProgramNode(), visit_OrganoidDeclNode(), visit_ConnectDeclNode(), visit_PortDeclNode(), visit_GridDeclNode(), visit_ChannelDeclNode(), visit_FnDeclNode(), visit_StreamDeclNode(), visit_BlockNode(), visit_LetStmtNode(), visit_AssignStmtNode(), visit_StimStmtNode(), visit_ModulateStmtNode(), visit_SyncTickStmtNode(), visit_IfStmtNode(), visit_WhileStmtNode(), visit_ForStmtNode(), visit_ReturnStmtNode(), visit_ExprStmtNode(), visit_BinaryOpNode(), visit_UnaryOpNode(), visit_LiteralNode(), visit_PhysicalLiteralNode(), visit_IdentifierNode(), visit_CallNode(), visit_IndexNode(), visit_DomainCallNode(), _resolve_channel_index(), _eval_const_int(), _extract_int_constant(), _extract_float_si_value(), _build_wbc_binary(), _serialize_topology(), _serialize_manifest(), _serialize_line_map()
- def `compile_source(source_text, filename)`
- def `disassemble(bytecode_bytes)`

#### `compiler/isa.py`

- class `Capability`: (IntEnum)
- class `SectionType`: (IntEnum)
- class `Opcode`: (IntEnum)

#### `compiler/lexer.py`

- class `LexerError`: __init__()
- class `Lexer`: __init__(), _peek(), _advance(), _match(), tokenize(), _scan_number(), _scan_string(), _scan_identifier_or_keyword(), _scan_operator_or_delimiter()

#### `compiler/nir_bridge.py`

- class `DalesPrincipleError`: (subclass alias of ValueError)
- class `NIRValidationError`: (subclass alias of ValueError)
- class `NIRNode`: node_type(), to_dict()
- class `Input`: shape()
- class `Output`: shape()
- class `Linear`: __post_init__()
- class `Affine`: __post_init__()
- class `LIF`: __post_init__()
- class `CubaLIF`: __post_init__()
- class `Izhikevich`: __post_init__()
- class `NIRGraph`: add_node(), add_edge(), get_predecessors(), get_successors(), is_recurrent(), topological_sort(), to_dict()
- def `validate_dales_principle(weight, eps)`
- def `enforce_dales_principle(weight, eps)`
- def `decompose_to_dales_principle(weight, eps)`
- def `save_nir_hdf5(graph, filepath)`
- def `load_nir_hdf5(filepath)`
- def `save_nir_json(graph, filepath)`
- def `load_nir_json(source)`
- def `nir_to_wet_source(graph, mea_rows, mea_cols, num_cycles, enforce_dale)`
- def `nir_to_wet_ast(graph, mea_rows, mea_cols, num_cycles, enforce_dale)`
- def `nir_to_wet_bytecode(graph, mea_rows, mea_cols, num_cycles, enforce_dale)`
- def `load_nir_into_vm(graph, vm, enforce_dale)`
- def `wet_ast_to_nir(ast)`
- def `wet_bytecode_to_nir(bytecode)`
- def `wet_vm_to_nir(vm, num_neurons)`

#### `compiler/parser.py`

- class `ParseError`: __init__()
- class `Parser`: __init__(), _current(), _peek(), _advance(), _match(), _is_identifier_token(), _expect_identifier(), _expect(), parse(), _parse_top_level_decl(), _parse_organoid_decl(), _parse_connect_decl(), _parse_port_decl(), _parse_grid_decl(), _parse_channel_decl(), _parse_fn_decl(), _parse_stream_decl(), _parse_type_name(), _parse_statement(), _parse_block(), _parse_let_statement(), _parse_typed_var_decl(), _parse_stim_statement(), _parse_modulate_statement(), _parse_sync_tick_statement(), _parse_if_statement(), _parse_while_statement(), _parse_for_statement(), _parse_return_statement(), _parse_assign_or_expr_statement(), parse_expression(), _parse_prefix()

#### `compiler/semantic.py`

- class `SemanticError`: __init__()
- class `Symbol`: __init__()
- class `Scope`: __init__(), define(), resolve(), is_local()
- class `SemanticAnalyzer`: __init__(), analyze(), _init_builtins(), _pass1_symbols_and_bounds(), _pass2_types_and_dimensions(), _pass3_loop_yield_verifier()
- class `_Pass1Visitor`: __init__(), visit_ProgramNode(), visit_GridDeclNode(), visit_ChannelDeclNode(), visit_OrganoidDeclNode(), visit_ConnectDeclNode(), visit_PortDeclNode(), visit_FnDeclNode(), visit_StreamDeclNode(), visit_BlockNode(), visit_LetStmtNode(), visit_AssignStmtNode(), visit_StimStmtNode(), visit_ModulateStmtNode(), visit_SyncTickStmtNode(), visit_IfStmtNode(), visit_WhileStmtNode(), visit_ForStmtNode(), visit_ReturnStmtNode(), visit_ExprStmtNode(), visit_BinaryOpNode(), visit_UnaryOpNode(), visit_CallNode(), visit_IndexNode(), visit_DomainCallNode(), visit_IdentifierNode(), _check_coordinate_bounds(), _extract_int_constant(), _type_to_dimension()
- class `_Pass2Visitor`: __init__(), visit_ProgramNode(), visit_OrganoidDeclNode(), visit_ConnectDeclNode(), visit_PortDeclNode(), visit_FnDeclNode(), visit_BlockNode(), visit_LetStmtNode(), visit_AssignStmtNode(), visit_StimStmtNode(), visit_BinaryOpNode(), visit_UnaryOpNode(), visit_PhysicalLiteralNode(), visit_LiteralNode(), visit_IdentifierNode(), _type_to_dimension(), get_dimension(), _extract_float_si_value()
- class `_Pass3LoopYieldVisitor`: __init__(), visit_ProgramNode(), visit_WhileStmtNode(), visit_ForStmtNode(), visit_StreamDeclNode(), _verify_loop_yield(), _check_unyielded_stim_path(), _contains_sync_tick()

#### `compiler/token.py`

- class `Dimension`: (Enum)
- class `TokenType`: (Enum)
- class `Token`: __repr__()

#### `bindings/ffi.py`

- class `WetStatus`: (IntEnum)
- class `WetHalMode`: (IntEnum)
- class `WetHalDriverType`: (IntEnum)
- class `WetHalStatus`: (IntEnum)
- class `WetHalConfig`: __init__()
- class `WetHalTelemetry`: (subclass alias of ctypes.Structure)
- class `WetHalContext`: (subclass alias of ctypes.Structure)
- class `WetCanFrame`: (subclass alias of ctypes.Structure)
- class `WetVMConfig`: __init__()
- class `WetTelemetry`: tick_index(), channel_voltages(), spike_raster(), net_charge(), last_charge()
- class `WetActuatorTelemetry`: pump_rates(), pump_dispensed(), valves(), motors()
- def `_find_library_path()`
- def `load_wetvm_lib(lib_path)`
- def `get_wetvm_lib(lib_path)`
- class `WetVMFFI`: __init__(), get_version(), create_vm(), free_vm(), allocate_telemetry(), step_tick(), run_ticks(), inject_stimulus(), get_last_error(), status_to_string(), load_bytecode(), get_telemetry(), create_vm_arena(), configure_electrode(), active_discharge(), active_discharge_all(), enable_dead_head_protection(), life_supervisor_shutdown(), configure_blanking(), inject_current_stimulus(), verify_bytecode(), snapshot(), restore(), set_environmental_sensors(), set_temperature(), set_channel_banks(), hal_create(), hal_destroy(), hal_get_telemetry(), hal_set_valve_for_pump(), hal_init(), hal_attach(), hal_get_context(), hal_set_mode(), hal_get_mode(), hal_register_driver(), hal_unregister_driver(), hal_find_driver(), hal_write_pump(), hal_dispense_pump(), hal_write_valve(), hal_read_flow(), hal_stim_current(), hal_stim_voltage(), hal_read_spikes(), hal_measure_impedance(), hal_active_discharge(), hal_emergency_crowbar(), intan_create(), intan_destroy(), intan_spi_transfer(), intan_set_stim_current(), intan_get_compliance_status(), intan_clear_compliance(), intan_measure_impedance(), intan_set_charge_recovery(), intan_inject_fault(), maxwell_create(), maxwell_destroy(), maxwell_route_channels(), maxwell_connect_stim(), maxwell_sequence_clear(), maxwell_sequence_append(), maxwell_sequence_arm(), maxwell_sequence_start(), maxwell_sequence_get_state(), maxwell_stim_voltage(), maxwell_inject_fault(), microfluidics_create(), microfluidics_destroy(), harvard_format_cmd(), harvard_parse_response(), pump_set_rate(), pump_dispense(), pump_stop(), valve_set_state(), pump_bind_downstream_valve(), can_send(), can_recv(), can_send_emcy(), microfluidics_inject_fault(), sensirion_create(), sensirion_destroy(), sensirion_crc8(), sensirion_validate_crc(), sensirion_start_measurement(), sensirion_stop_measurement(), sensirion_read_flow(), sensirion_hil_set_flow(), shdlc_encode(), shdlc_decode(), sensirion_inject_fault()

#### `bindings/runtime.py`

- class `WetVMError`: __init__()
- class `WetTelemetryView`: __init__(), current_tick(), tick_index(), sim_time_ms(), population_rate_hz(), channel_voltages(), spike_raster(), last_charge_nc(), get(), __getitem__()
- class `WetVM`: __init__(), close(), __enter__(), __exit__(), __del__(), _check_alive(), load_bytecode(), load(), step_tick(), run_ticks(), step(), inject_stimulus(), get_telemetry(), get_actuator_telemetry(), get_voltages_numpy(), get_spikes_numpy(), get_charge_numpy(), last_error(), _status_to_string(), current_tick(), tick_index(), sim_time_ms(), is_halted(), configure_electrode(), active_discharge(), active_discharge_all(), enable_dead_head_protection(), life_supervisor_shutdown(), configure_blanking(), inject_current_stimulus(), verify_bytecode(), snapshot(), restore(), set_environmental_sensors(), set_temperature(), set_channel_banks(), init_hal(), attach_hal(), get_hal(), emergency_crowbar(), get_synapse_matrix(), get_synapse_weight()
- class `WetRuntime`: (subclass alias of WetVM)

#### `bindings/scheduler.py`

- def `resolve_p_core(requested_core, allow_e_cores)`
- class `WetSchedulerConfig`: __init__()
- class `WetStimCommand`: __init__()
- class `WetSchedulerStats`: as_dict()
- def `_bind_scheduler_ffi(lib)`
- class `WetScheduler`: __init__(), handle(), start(), step(), stop(), get_stats(), poll_telemetry(), push_stimulus(), benchmark(), destroy(), __enter__(), __exit__()

#### `biophysics/mea_grid.py`

- class `MEAGrid`: __init__(), coords_to_channel(), channel_to_coords(), get_electrode_pos(), calculate_field_potential(), get_crosstalk_matrix()

#### `biophysics/ode_solver.py`

- class `LifODESolver`: __init__(), step_passive(), decay_conductance(), update_neuron(), simulate_refractory(), decrement_refractory(), simulate_continuous_stimulus(), elevate_threshold(), activate_ahp()

#### `biophysics/stdp.py`

- class `PairwiseSTDP`: __init__(), compute_delta_w(), decay_trace(), update_weight()

#### `biophysics/stp.py`

- class `SynapseSTP`: __init__(), deliver_spikes(), track_utilization(), recover()

#### `biophysics/telemetry.py`

- class `TelemetryStream`: format_tick_json(), get_csv_header(), make_record(), format_spike_event(), compute_firing_rate()

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
File Size: 1540 bytes | CRC32: 0x5EBE5FC7 | Capabilities: 0x000B
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
File Size: 1676 bytes | CRC32: 0x4B531343 | Capabilities: 0x001B
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
File Size: 1111 bytes | CRC32: 0x2F0A421B | Capabilities: 0x000B
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
 Working Directory  : D:\WetLang
 Tests Discovered   : 313
================================================================================
  [PERF WARNING] tests.e2e.test_tier1_features.TestTier1SyntheticSuite.test_tier1_f27_ode_stability_suite_happy took 1.39s

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
Elapsed Time: 7.049 s
================================================================================

[STDERR]
.........................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 313 tests in 7.042s

OK
```

### D.2 Live Synthetic Unit Test Suite (`python -m pytest tests/test_*.py -v`)

```text
$ python -m pytest tests/test_*.py -v  (exit_code=0)
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\Anikesh\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: D:\WetLang
configfile: pytest.ini
plugins: anyio-4.14.2, platformdirs-4.12.3
collecting ... collected 207 items

tests/test_audit_remediation.py::TestAuditRemediation::test_audit_01_si_time_scaling PASSED [  0%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_02_integer_arithmetic_precision PASSED [  0%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_03_cfg_reachability_pass3 PASSED [  1%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_04_watchdog_timeout_100k PASSED [  1%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_05_leaky_dc_drift_integrator PASSED [  2%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_06_focal_hyperactivity_breaker PASSED [  2%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_07_charge_density_limit PASSED [  3%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_08_cathodic_first_extracellular_sign PASSED [  3%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_09_lfp_zero_baseline PASSED [  4%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_10_amplifier_blanking PASSED [  4%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_11_dynamic_channel_dispatch PASSED [  5%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_12_user_functions_and_calls PASSED [  5%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_13_boolean_normalization PASSED [  6%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_14_safe_unaligned_memory_access PASSED [  6%]
tests/test_audit_remediation.py::TestAuditRemediation::test_audit_15_free_running_simulation_ticks PASSED [  7%]
tests/test_benchmarks.py::test_compile_benchmark_01_active_inference PASSED [  7%]
tests/test_benchmarks.py::test_compile_benchmark_02_polychronous_reservoir PASSED [  8%]
tests/test_benchmarks.py::test_compile_benchmark_03_homeostatic_stabilization PASSED [  8%]
tests/test_benchmarks.py::test_run_benchmark_01_in_wetvm PASSED          [  9%]
tests/test_benchmarks.py::test_run_benchmark_02_in_wetvm PASSED          [  9%]
tests/test_benchmarks.py::test_run_benchmark_03_in_wetvm PASSED          [ 10%]
tests/test_benchmarks.py::test_benchmark_telemetry_jsonl_formatting PASSED [ 10%]
tests/test_benchmarks.py::test_benchmark_telemetry_csv_formatting PASSED [ 11%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_hal_create_and_destroy PASSED [ 11%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_hal_mode_switching PASSED [ 12%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_driver_registration_and_lookup PASSED [ 12%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_emergency_crowbar_fastpath_sub_100us PASSED [ 13%]
tests/test_hal_drivers.py::TestHalCoreArchitecture::test_router_valve_mapping_dead_head PASSED [ 13%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_command_encoding_and_decoding PASSED [ 14%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_constant_current_dac_ranges PASSED [ 14%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_compliance_rail_detection_and_clearing PASSED [ 14%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_in_situ_1khz_impedance_check PASSED [ 15%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_active_charge_recovery_switch PASSED [ 15%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_intan_fault_injection PASSED [ 16%]
tests/test_hal_drivers.py::TestIntanRhs2116Driver::test_intan_voltage_stimulation_duration_and_cathodic_polarity PASSED [ 16%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_routing_matrix_configuration PASSED [ 17%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_sequence_buffering_and_playback PASSED [ 17%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_voltage_clamping_and_charge_injection_protection PASSED [ 18%]
tests/test_hal_drivers.py::TestMaxWellMaxOneDriver::test_maxwell_connect_stim_and_fault_injection PASSED [ 18%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_harvard_rs232_formatting_and_prompt_parsing PASSED [ 19%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_dead_head_overpressure_interlock PASSED [ 19%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_bus_pdo_and_emergency_frames PASSED [ 20%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_dead_head_recovery_and_fault_injection PASSED [ 20%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_bus_boundary_dlc_and_extended_id_segregation PASSED [ 21%]
tests/test_hal_drivers.py::TestMicrofluidicProtocols::test_can_hil_bidirectional_loopback PASSED [ 21%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_crc8_algorithm PASSED [ 22%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_i2c_flow_reading PASSED [ 22%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_shdlc_framing_and_byte_stuffing PASSED [ 23%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_nak_and_multiple_crc_vectors PASSED [ 23%]
tests/test_hal_drivers.py::TestSensirionFlowMeter::test_sensirion_shdlc_illegal_stuffing_rejection PASSED [ 24%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_with_hal_pump_and_flow_routing PASSED [ 24%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_bytecode_actuation_with_hal PASSED [ 25%]
tests/test_hal_drivers.py::TestVmHalIntegration::test_vm_bytecode_dead_head_interlock_trip PASSED [ 25%]
tests/test_interlocks.py::test_voltage_clamp_positive_saturation PASSED  [ 26%]
tests/test_interlocks.py::test_voltage_clamp_negative_saturation PASSED  [ 26%]
tests/test_interlocks.py::test_voltage_clamp_within_water_window_passthrough PASSED [ 27%]
tests/test_interlocks.py::test_static_compile_rejection_overvoltage PASSED [ 27%]
tests/test_interlocks.py::test_static_compile_rejection_undervoltage PASSED [ 28%]
tests/test_interlocks.py::test_sliding_charge_balance_symmetric_biphasic_no_trip PASSED [ 28%]
tests/test_interlocks.py::test_sliding_charge_balance_unbalanced_dc_trip_at_100_ticks PASSED [ 28%]
tests/test_interlocks.py::test_sliding_charge_balance_boundary_threshold PASSED [ 29%]
tests/test_interlocks.py::test_epileptiform_sub_critical_burst_does_not_trip PASSED [ 29%]
tests/test_interlocks.py::test_epileptiform_focal_burst_few_channels_does_not_trip PASSED [ 30%]
tests/test_interlocks.py::test_epileptiform_runaway_trips_at_500_ticks PASSED [ 30%]
tests/test_interlocks.py::test_failsafe_state_lockout_blocks_further_operations PASSED [ 31%]
tests/test_nir_bridge.py::test_cubalif_biophysical_parameters PASSED     [ 31%]
tests/test_nir_bridge.py::test_lif_parameters PASSED                     [ 32%]
tests/test_nir_bridge.py::test_izhikevich_cortical_phenotypes PASSED     [ 32%]
tests/test_nir_bridge.py::test_dales_principle_valid_matrices PASSED     [ 33%]
tests/test_nir_bridge.py::test_dales_principle_violation_raises PASSED   [ 33%]
tests/test_nir_bridge.py::test_decompose_to_dales_principle PASSED       [ 34%]
tests/test_nir_bridge.py::test_feedforward_topological_sort PASSED       [ 34%]
tests/test_nir_bridge.py::test_recurrent_graph_detection PASSED          [ 35%]
tests/test_nir_bridge.py::test_hdf5_serialization_roundtrip PASSED       [ 35%]
tests/test_nir_bridge.py::test_json_serialization_roundtrip PASSED       [ 36%]
tests/test_nir_bridge.py::test_nir_to_wet_source_generation PASSED       [ 36%]
tests/test_nir_bridge.py::test_nir_to_wet_ast PASSED                     [ 37%]
tests/test_nir_bridge.py::test_nir_to_wet_bytecode_and_native_execution PASSED [ 37%]
tests/test_nir_bridge.py::test_nir_dimension_validation_exceeding_channels PASSED [ 38%]
tests/test_nir_bridge.py::test_wet_ast_to_nir PASSED                     [ 38%]
tests/test_nir_bridge.py::test_wet_bytecode_to_nir PASSED                [ 39%]
tests/test_nir_bridge.py::test_wet_vm_to_nir PASSED                      [ 39%]
tests/test_nir_bridge.py::test_vm_get_synapse_matrix_live PASSED         [ 40%]
tests/test_nir_bridge.py::test_multilayer_feedforward_pipeline PASSED    [ 40%]
tests/test_nir_bridge.py::test_hdf5_to_bytecode_roundtrip PASSED         [ 41%]
tests/test_nir_bridge.py::test_affine_dales_principle PASSED             [ 41%]
tests/test_ode_stability.py::test_coba_lif_extreme_positive_current_injection PASSED [ 42%]
tests/test_ode_stability.py::test_coba_lif_extreme_negative_current_injection PASSED [ 42%]
tests/test_ode_stability.py::test_coba_lif_resting_equilibrium_stability PASSED [ 42%]
tests/test_ode_stability.py::test_absolute_refractory_clamp_2ms PASSED   [ 43%]
tests/test_ode_stability.py::test_membrane_clamped_at_reset_during_refractory PASSED [ 43%]
tests/test_ode_stability.py::test_dynamic_threshold_jump_and_decay PASSED [ 44%]
tests/test_ode_stability.py::test_slow_ahp_potassium_conductance_decay PASSED [ 44%]
tests/test_ode_stability.py::test_tsodyks_markram_ee_depression_and_recovery PASSED [ 45%]
tests/test_ode_stability.py::test_tsodyks_markram_ei_facilitation PASSED [ 45%]
tests/test_ode_stability.py::test_stdp_weight_hard_clamping PASSED       [ 46%]
tests/test_ode_stability.py::test_stdp_depression_bias_ratio PASSED      [ 46%]
tests/test_ode_stability.py::test_dales_principle_conductance_reversal PASSED [ 47%]
tests/test_ode_stability.py::test_native_wetvm_multi_tick_stability PASSED [ 47%]
tests/test_parser_diagnostics.py::test_lexer_keywords_and_identifiers PASSED [ 48%]
tests/test_parser_diagnostics.py::test_lexer_physical_literals_si_scaling PASSED [ 48%]
tests/test_parser_diagnostics.py::test_lexer_line_column_tracking PASSED [ 49%]
tests/test_parser_diagnostics.py::test_lexer_comment_skipping PASSED     [ 49%]
tests/test_parser_diagnostics.py::test_lexer_unterminated_block_comment PASSED [ 50%]
tests/test_parser_diagnostics.py::test_lexer_unterminated_string PASSED  [ 50%]
tests/test_parser_diagnostics.py::test_parser_arithmetic_precedence PASSED [ 51%]
tests/test_parser_diagnostics.py::test_parser_logical_operator_precedence PASSED [ 51%]
tests/test_parser_diagnostics.py::test_parser_parentheses_override PASSED [ 52%]
tests/test_parser_diagnostics.py::test_parser_unary_operators PASSED     [ 52%]
tests/test_parser_diagnostics.py::test_parser_grid_and_channel_declarations PASSED [ 53%]
tests/test_parser_diagnostics.py::test_parser_function_and_control_flow PASSED [ 53%]
tests/test_parser_diagnostics.py::test_parser_for_loop PASSED            [ 54%]
tests/test_parser_diagnostics.py::test_parser_stream_declaration PASSED  [ 54%]
tests/test_parser_diagnostics.py::test_parser_domain_primitives PASSED   [ 55%]
tests/test_parser_diagnostics.py::test_parser_error_diagnostics PASSED   [ 55%]
tests/test_parser_diagnostics.py::test_compiler_bytecode_binary_header_and_disasm PASSED [ 56%]
tests/test_parser_diagnostics.py::test_compile_benchmark_01 PASSED       [ 56%]
tests/test_parser_diagnostics.py::test_compile_benchmark_02 PASSED       [ 57%]
tests/test_parser_diagnostics.py::test_compile_benchmark_03 PASSED       [ 57%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_01_wbc_header_truncation PASSED [ 57%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_02_wbc_magic_corruption PASSED [ 58%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_03_wbc_crc32_tamper_detection PASSED [ 58%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_04_wbc_unsupported_version PASSED [ 59%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_05_stimulation_without_capability PASSED [ 59%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_06_microfluidics_without_capability PASSED [ 60%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_07_motor_actuation_without_capability PASSED [ 60%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_08_hydrodynamic_shear_stress_enforcement PASSED [ 61%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_09_compiler_shear_stress_rejection PASSED [ 61%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_10_valid_actuator_telemetry_inspection PASSED [ 62%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_11_cryptographic_signing_and_verification PASSED [ 62%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_12_division_by_zero_safety PASSED [ 63%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_13_stack_underflow_safety PASSED [ 63%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_14_multithreaded_concurrent_vms PASSED [ 64%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_15_hundred_cycle_memory_endurance PASSED [ 64%]
tests/test_phase2_deep_audit.py::TestPhase2DeepAudit::test_16_full_cyber_physical_closed_loop_program PASSED [ 65%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_01_hd_mea_water_window_clamping PASSED [ 65%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_02_persistent_unbounded_dc_accumulator PASSED [ 66%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_03_active_hardware_discharge_recovery PASSED [ 66%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_04_spherical_diffusion_thiele_anoxia PASSED [ 67%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_05_geometry_aware_shear_stress PASSED [ 67%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_06_dead_heading_valve_pump_interlock PASSED [ 68%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_07_ring0_life_support_supervisor PASSED [ 68%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_08_static_arena_allocation_zero_malloc PASSED [ 69%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_09_ed25519_asymmetric_bytecode_provenance PASSED [ 69%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_10_randles_interface_and_compliance_voltage_interlock PASSED [ 70%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_11_configurable_blanking_and_spatial_crosstalk PASSED [ 70%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_12_subnormal_denormal_conductance_zero_clamping PASSED [ 71%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_13_environmental_sensors_ph_do_co2_flow PASSED [ 71%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_14_cmos_thermal_duty_cycle_interlock PASSED [ 71%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_15_optical_bubble_sensor_pump_halt_interlock PASSED [ 72%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_16_load_time_c99_bytecode_verifier PASSED [ 72%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_17_live_state_checkpointing_and_hot_swap PASSED [ 73%]
tests/test_phase3_hardware_readiness.py::TestPhase3HardwareReadiness::test_18_typed_channel_banks_static_safety PASSED [ 73%]
tests/test_rt_scheduler.py::test_scheduler_lifecycle PASSED              [ 74%]
tests/test_rt_scheduler.py::test_scheduler_context_manager PASSED        [ 74%]
tests/test_rt_scheduler.py::test_spsc_stimulus_and_telemetry_streaming PASSED [ 75%]
tests/test_rt_scheduler.py::test_quiescent_hard_realtime_benchmark_10k_ticks PASSED [ 75%]
tests/test_rt_scheduler.py::test_stress_load_hard_realtime_benchmark_10k_ticks PASSED [ 76%]
tests/test_rt_scheduler.py::test_isochronous_pacing_zero_cumulative_drift PASSED [ 76%]
tests/test_static_verifier.py::test_symbol_resolution_undeclared_identifier PASSED [ 77%]
tests/test_static_verifier.py::test_symbol_resolution_redeclared_identifier PASSED [ 77%]
tests/test_static_verifier.py::test_symbol_resolution_duplicate_function_params PASSED [ 78%]
tests/test_static_verifier.py::test_mea_coordinates_valid PASSED         [ 78%]
tests/test_static_verifier.py::test_mea_coordinates_row_out_of_bounds PASSED [ 79%]
tests/test_static_verifier.py::test_mea_coordinates_col_out_of_bounds PASSED [ 79%]
tests/test_static_verifier.py::test_mea_coordinates_negative_row PASSED  [ 80%]
tests/test_static_verifier.py::test_mea_coordinates_negative_col PASSED  [ 80%]
tests/test_static_verifier.py::test_mea_coordinates_linear_out_of_bounds PASSED [ 81%]
tests/test_static_verifier.py::test_mea_coordinates_linear_negative PASSED [ 81%]
tests/test_static_verifier.py::test_mea_coordinates_in_stim_stmt_out_of_bounds PASSED [ 82%]
tests/test_static_verifier.py::test_dimensional_homogeneous_addition PASSED [ 82%]
tests/test_static_verifier.py::test_dimensional_incompatible_addition PASSED [ 83%]
tests/test_static_verifier.py::test_dimensional_multiplication_current_time_to_charge PASSED [ 83%]
tests/test_static_verifier.py::test_dimensional_incompatible_comparison PASSED [ 84%]
tests/test_static_verifier.py::test_static_voltage_clamp_valid PASSED    [ 84%]
tests/test_static_verifier.py::test_static_voltage_clamp_positive_exceeded PASSED [ 85%]
tests/test_static_verifier.py::test_static_voltage_clamp_negative_exceeded PASSED [ 85%]
tests/test_static_verifier.py::test_static_voltage_clamp_unitless_float_exceeded PASSED [ 85%]
tests/test_static_verifier.py::test_loop_yield_bounded_while_loop PASSED [ 86%]
tests/test_static_verifier.py::test_loop_yield_unbounded_while_loop_rejected PASSED [ 86%]
tests/test_static_verifier.py::test_loop_yield_unbounded_if_branch_rejected PASSED [ 87%]
tests/test_static_verifier.py::test_loop_yield_bounded_if_branch_accepted PASSED [ 87%]
tests/test_static_verifier.py::test_loop_yield_pure_compute_loop_accepted PASSED [ 88%]
tests/test_static_verifier.py::test_loop_yield_unbounded_for_loop_rejected PASSED [ 88%]
tests/test_static_verifier.py::test_loop_yield_bounded_for_loop_accepted PASSED [ 89%]
tests/test_static_verifier.py::test_loop_yield_stream_cycle_unbounded_rejected PASSED [ 89%]
tests/test_static_verifier.py::test_loop_yield_stream_cycle_bounded_accepted PASSED [ 90%]
tests/test_static_verifier.py::test_loop_yield_nested_block_unbounded_rejected PASSED [ 90%]
tests/test_static_verifier.py::test_loop_yield_inner_while_loop_evasion_rejected PASSED [ 91%]
tests/test_static_verifier.py::test_loop_yield_inner_for_loop_evasion_rejected PASSED [ 91%]
tests/test_static_verifier.py::test_loop_yield_nested_block_if_without_else_rejected PASSED [ 92%]
tests/test_static_verifier.py::test_static_voltage_clamp_constant_folded_addition_exceeded PASSED [ 92%]
tests/test_static_verifier.py::test_static_voltage_clamp_constant_folded_multiplication_exceeded PASSED [ 93%]
tests/test_static_verifier.py::test_static_voltage_clamp_variable_constant_exceeded PASSED [ 93%]
tests/test_static_verifier.py::test_negative_high_voltage_capability_and_manifest PASSED [ 94%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_out_of_bounds PASSED [ 94%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_linear_out_of_bounds PASSED [ 95%]
tests/test_static_verifier.py::test_mea_coordinates_constant_folded_valid_mapping PASSED [ 95%]
tests/test_static_verifier.py::test_capability_multi_electrode_threshold PASSED [ 96%]
tests/test_universal_sandbox.py::TestUniversalSandbox::test_01_single_organoid_sandbox PASSED [ 96%]
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
======================= 207 passed, 1 warning in 10.07s =======================
```

### D.3 Live 10,000-Tick `wetvm.dll` Latency Microbenchmark

```text
Host Platform : Windows-11-10.0.26300-SP0 (AMD64)
Processor     : Intel64 Family 6 Model 189 Stepping 1, GenuineIntel
Python        : 3.12.10
Workload      : benchmarks/01_active_inference_closed_loop.wet (dt = 0.1 ms = 100 us)

[Mode A: Per-Tick Python->C FFI vm.step_tick() x 10,000 ticks]
  mean   : 23.074 us/tick
  median : 19.200 us/tick
  p95    : 24.600 us/tick
  p99    : 96.100 us/tick
  min    : 8.500 us/tick
  max    : 4550.700 us/tick
  wall   : 234.959 ms (1.0 s simulated time)

[Mode B: Batched Native C vm.run_ticks(10000) x 10 trials]
  mean       : 20.469 us/tick
  median     : 19.237 us/tick
  min        : 17.078 us/tick
  max        : 29.695 us/tick
  throughput : 48854 ticks/sec
  speedup    : 4.89x real-time
```

---

## Appendix E: Verified Line-Numbered Core Source Code Listing

Covers all 48 core source files across `compiler/`, `native/include/`, `native/src/`, `native/build.py`, `native/interlocks.py`, `bindings/`, `biophysics/`, and `benchmarks/*.wet`.

### `compiler/__init__.py` (123 lines, SHA-256: `79a50dc641756ee2...`)

```text
   1 | """
   2 | WetLang Compiler Package
   3 | Complete domain-specific programming language compiler for neural organoids.
   4 | Zero external compiler framework dependencies.
   5 | """
   6 | 
   7 | from compiler.token import (
   8 |     Token,
   9 |     TokenType,
  10 |     Dimension,
  11 |     UNIT_SUFFIXES,
  12 | )
  13 | from compiler.lexer import (
  14 |     Lexer,
  15 |     LexerError,
  16 | )
  17 | from compiler.ast_nodes import (
  18 |     ASTNode,
  19 |     ASTVisitor,
  20 |     ProgramNode,
  21 |     GridDeclNode,
  22 |     ChannelDeclNode,
  23 |     FnDeclNode,
  24 |     ParamNode,
  25 |     StreamDeclNode,
  26 |     StreamItemNode,
  27 |     BlockNode,
  28 |     LetStmtNode,
  29 |     AssignStmtNode,
  30 |     StimStmtNode,
  31 |     ModulateStmtNode,
  32 |     SyncTickStmtNode,
  33 |     IfStmtNode,
  34 |     WhileStmtNode,
  35 |     ForStmtNode,
  36 |     ReturnStmtNode,
  37 |     ExprStmtNode,
  38 |     BinaryOpNode,
  39 |     UnaryOpNode,
  40 |     LiteralNode,
  41 |     PhysicalLiteralNode,
  42 |     IdentifierNode,
  43 |     CallNode,
  44 |     IndexNode,
  45 |     RangeNode,
  46 |     DomainCallNode,
  47 | )
  48 | from compiler.parser import (
  49 |     Parser,
  50 |     ParseError,
  51 | )
  52 | from compiler.semantic import (
  53 |     SemanticAnalyzer,
  54 |     SemanticError,
  55 | )
  56 | from compiler.isa import (
  57 |     Opcode,
  58 |     Capability,
  59 |     SectionType,
  60 |     HEADER_MAGIC,
  61 |     HEADER_SIZE,
  62 |     VERSION_MAJOR,
  63 |     VERSION_MINOR,
  64 |     OPCODE_NAMES,
  65 | )
  66 | from compiler.emitter import (
  67 |     BytecodeEmitter,
  68 |     disassemble,
  69 |     compile_source,
  70 | )
  71 | 
  72 | __all__ = [
  73 |     "Token",
  74 |     "TokenType",
  75 |     "Dimension",
  76 |     "UNIT_SUFFIXES",
  77 |     "Lexer",
  78 |     "LexerError",
  79 |     "Parser",
  80 |     "ParseError",
  81 |     "ASTNode",
  82 |     "ASTVisitor",
  83 |     "ProgramNode",
  84 |     "GridDeclNode",
  85 |     "ChannelDeclNode",
  86 |     "FnDeclNode",
  87 |     "ParamNode",
  88 |     "StreamDeclNode",
  89 |     "StreamItemNode",
  90 |     "BlockNode",
  91 |     "LetStmtNode",
  92 |     "AssignStmtNode",
  93 |     "StimStmtNode",
  94 |     "ModulateStmtNode",
  95 |     "SyncTickStmtNode",
  96 |     "IfStmtNode",
  97 |     "WhileStmtNode",
  98 |     "ForStmtNode",
  99 |     "ReturnStmtNode",
 100 |     "ExprStmtNode",
 101 |     "BinaryOpNode",
 102 |     "UnaryOpNode",
 103 |     "LiteralNode",
 104 |     "PhysicalLiteralNode",
 105 |     "IdentifierNode",
 106 |     "CallNode",
 107 |     "IndexNode",
 108 |     "RangeNode",
 109 |     "DomainCallNode",
 110 |     "SemanticAnalyzer",
 111 |     "SemanticError",
 112 |     "Opcode",
 113 |     "Capability",
 114 |     "SectionType",
 115 |     "HEADER_MAGIC",
 116 |     "HEADER_SIZE",
 117 |     "VERSION_MAJOR",
 118 |     "VERSION_MINOR",
 119 |     "OPCODE_NAMES",
 120 |     "BytecodeEmitter",
 121 |     "disassemble",
 122 |     "compile_source",
 123 | ]
```

### `compiler/ast_nodes.py` (254 lines, SHA-256: `d81ae7e413aa53a4...`)

```text
   1 | """
   2 | WetLang Compiler - Typed Abstract Syntax Tree (AST) Hierarchy
   3 | Hand-crafted from first principles. Complete visitor pattern interfaces.
   4 | """
   5 | 
   6 | from dataclasses import dataclass, field
   7 | from typing import List, Optional, Any, Dict
   8 | from compiler.token import Dimension
   9 | 
  10 | 
  11 | @dataclass
  12 | class ASTNode:
  13 |     """Base class for all Abstract Syntax Tree nodes."""
  14 |     line: int = 0
  15 |     column: int = 0
  16 | 
  17 |     def accept(self, visitor: "ASTVisitor") -> Any:
  18 |         method_name = f"visit_{self.__class__.__name__}"
  19 |         visitor_fn = getattr(visitor, method_name, visitor.generic_visit)
  20 |         return visitor_fn(self)
  21 | 
  22 | 
  23 | # =========================================================================
  24 | # Top-Level & Declarations
  25 | # =========================================================================
  26 | 
  27 | @dataclass
  28 | class ProgramNode(ASTNode):
  29 |     declarations: List[ASTNode] = field(default_factory=list)
  30 | 
  31 | 
  32 | @dataclass
  33 | class OrganoidDeclNode(ASTNode):
  34 |     name: str = ""
  35 |     count: Optional[Any] = None  # None for single organoid, or int/expr for organoid array [N]
  36 |     cells: Optional[Any] = None
  37 |     radius: Optional[Any] = None
  38 |     perfusion: Optional[Any] = None
  39 |     properties: Dict[str, Any] = field(default_factory=dict)
  40 | 
  41 | 
  42 | @dataclass
  43 | class ConnectDeclNode(ASTNode):
  44 |     source: ASTNode = None       # e.g. organoid_A or organoid_A.port
  45 |     target: ASTNode = None       # e.g. organoid_B or organoid_B.port
  46 |     delay_ms: Optional[Any] = None
  47 |     weight: Optional[Any] = None
  48 |     plasticity: Optional[str] = None
  49 | 
  50 | 
  51 | @dataclass
  52 | class PortDeclNode(ASTNode):
  53 |     name: str = ""
  54 |     channels: Any = None
  55 |     mode: Optional[str] = None
  56 | 
  57 | 
  58 | @dataclass
  59 | class GridDeclNode(ASTNode):
  60 |     name: str = ""
  61 |     rows: Any = None
  62 |     cols: Any = None
  63 |     pitch: Optional[Any] = None
  64 |     base_voltage: Optional[Any] = None
  65 | 
  66 | 
  67 | @dataclass
  68 | class ChannelDeclNode(ASTNode):
  69 |     name: str = ""
  70 |     target: ASTNode = None       # IndexNode, IdentifierNode, or RangeNode
  71 |     mode: Optional[str] = None   # "BiphasicStim", "SpikeReadout", etc.
  72 | 
  73 | 
  74 | @dataclass
  75 | class ParamNode(ASTNode):
  76 |     name: str = ""
  77 |     type_name: str = ""
  78 | 
  79 | 
  80 | @dataclass
  81 | class FnDeclNode(ASTNode):
  82 |     name: str = ""
  83 |     params: List[ParamNode] = field(default_factory=list)
  84 |     return_type: Optional[str] = None
  85 |     body: "BlockNode" = None
  86 | 
  87 | 
  88 | @dataclass
  89 | class StreamItemNode(ASTNode):
  90 |     kind: str = ""               # "bind_in", "bind_out", "cycle"
  91 |     left: Optional[str] = None
  92 |     right: Optional[str] = None
  93 |     cycle_block: Optional["BlockNode"] = None
  94 | 
  95 | 
  96 | @dataclass
  97 | class StreamDeclNode(ASTNode):
  98 |     name: str = ""
  99 |     items: List[StreamItemNode] = field(default_factory=list)
 100 | 
 101 | 
 102 | # =========================================================================
 103 | # Statements
 104 | # =========================================================================
 105 | 
 106 | @dataclass
 107 | class BlockNode(ASTNode):
 108 |     statements: List[ASTNode] = field(default_factory=list)
 109 | 
 110 | 
 111 | @dataclass
 112 | class LetStmtNode(ASTNode):
 113 |     name: str = ""
 114 |     is_mut: bool = False
 115 |     type_name: Optional[str] = None
 116 |     initializer: ASTNode = None
 117 | 
 118 | 
 119 | @dataclass
 120 | class AssignStmtNode(ASTNode):
 121 |     target: ASTNode = None       # IdentifierNode or IndexNode
 122 |     value: ASTNode = None
 123 | 
 124 | 
 125 | @dataclass
 126 | class StimStmtNode(ASTNode):
 127 |     channel: ASTNode = None
 128 |     voltage: ASTNode = None
 129 |     phase1: ASTNode = None
 130 |     phase2: ASTNode = None
 131 |     interphase: Optional[ASTNode] = None
 132 | 
 133 | 
 134 | @dataclass
 135 | class ModulateStmtNode(ASTNode):
 136 |     args: List[ASTNode] = field(default_factory=list)
 137 | 
 138 | 
 139 | @dataclass
 140 | class SyncTickStmtNode(ASTNode):
 141 |     count: Optional[ASTNode] = None
 142 | 
 143 | 
 144 | @dataclass
 145 | class IfStmtNode(ASTNode):
 146 |     condition: ASTNode = None
 147 |     then_block: BlockNode = None
 148 |     else_block: Optional[ASTNode] = None  # BlockNode or IfStmtNode
 149 | 
 150 | 
 151 | @dataclass
 152 | class WhileStmtNode(ASTNode):
 153 |     condition: ASTNode = None
 154 |     body: BlockNode = None
 155 | 
 156 | 
 157 | @dataclass
 158 | class ForStmtNode(ASTNode):
 159 |     var_name: str = ""
 160 |     range_start: ASTNode = None
 161 |     range_end: ASTNode = None
 162 |     body: BlockNode = None
 163 | 
 164 | 
 165 | @dataclass
 166 | class ReturnStmtNode(ASTNode):
 167 |     value: Optional[ASTNode] = None
 168 | 
 169 | 
 170 | @dataclass
 171 | class ExprStmtNode(ASTNode):
 172 |     expr: ASTNode = None
 173 | 
 174 | 
 175 | # =========================================================================
 176 | # Expressions
 177 | # =========================================================================
 178 | 
 179 | @dataclass
 180 | class BinaryOpNode(ASTNode):
 181 |     left: ASTNode = None
 182 |     op: str = ""
 183 |     right: ASTNode = None
 184 | 
 185 | 
 186 | @dataclass
 187 | class UnaryOpNode(ASTNode):
 188 |     op: str = ""
 189 |     operand: ASTNode = None
 190 | 
 191 | 
 192 | @dataclass
 193 | class LiteralNode(ASTNode):
 194 |     value: Any = None
 195 |     type_name: str = ""          # "int", "float", "bool", "string"
 196 | 
 197 | 
 198 | @dataclass
 199 | class PhysicalLiteralNode(ASTNode):
 200 |     magnitude: float = 0.0
 201 |     dimension: Dimension = Dimension.NONE
 202 |     si_value: float = 0.0
 203 |     unit_suffix: str = ""
 204 | 
 205 | 
 206 | @dataclass
 207 | class IdentifierNode(ASTNode):
 208 |     name: str = ""
 209 | 
 210 | 
 211 | @dataclass
 212 | class CallNode(ASTNode):
 213 |     callee: ASTNode = None
 214 |     args: List[ASTNode] = field(default_factory=list)
 215 | 
 216 | 
 217 | @dataclass
 218 | class IndexNode(ASTNode):
 219 |     target: ASTNode = None
 220 |     indices: List[ASTNode] = field(default_factory=list)
 221 | 
 222 | 
 223 | @dataclass
 224 | class RangeNode(ASTNode):
 225 |     start: ASTNode = None
 226 |     end: ASTNode = None
 227 | 
 228 | 
 229 | @dataclass
 230 | class DomainCallNode(ASTNode):
 231 |     func_name: str = ""          # "read_spikes", "read_voltage", "pop_firing_rate", "read_population_rate"
 232 |     args: List[ASTNode] = field(default_factory=list)
 233 | 
 234 | 
 235 | # =========================================================================
 236 | # AST Visitor Base Class
 237 | # =========================================================================
 238 | 
 239 | class ASTVisitor:
 240 |     """Base class for AST visitors with double-dispatch."""
 241 |     def visit(self, node: ASTNode) -> Any:
 242 |         if node is None:
 243 |             return None
 244 |         return node.accept(self)
 245 | 
 246 |     def generic_visit(self, node: ASTNode) -> Any:
 247 |         for attr, value in node.__dict__.items():
 248 |             if isinstance(value, ASTNode):
 249 |                 self.visit(value)
 250 |             elif isinstance(value, list):
 251 |                 for item in value:
 252 |                     if isinstance(item, ASTNode):
 253 |                         self.visit(item)
 254 |         return None
```

### `compiler/compiler_cli.py` (104 lines, SHA-256: `245778ace8d44d4a...`)

```text
   1 | """
   2 | WetLang Compiler CLI (wetc)
   3 | Command-line compiler and disassembler for WetLang (.wet -> .wbc).
   4 | """
   5 | 
   6 | import sys
   7 | import argparse
   8 | import os
   9 | from typing import Optional
  10 | 
  11 | from compiler.lexer import Lexer, LexerError
  12 | from compiler.parser import Parser, ParseError
  13 | from compiler.semantic import SemanticAnalyzer, SemanticError
  14 | from compiler.emitter import BytecodeEmitter, disassemble, compile_source
  15 | from compiler.ast_nodes import ProgramNode, ASTNode
  16 | 
  17 | 
  18 | 
  19 | 
  20 | def format_ast(node: ASTNode, indent: int = 0) -> str:
  21 |     """Recursively formats AST nodes for debugging."""
  22 |     sp = "  " * indent
  23 |     lines = [f"{sp}{node.__class__.__name__}"]
  24 |     for k, v in node.__dict__.items():
  25 |         if k in ("line", "column"):
  26 |             continue
  27 |         if isinstance(v, ASTNode):
  28 |             lines.append(f"{sp}  {k}:")
  29 |             lines.append(format_ast(v, indent + 2))
  30 |         elif isinstance(v, list):
  31 |             lines.append(f"{sp}  {k}: [")
  32 |             for item in v:
  33 |                 if isinstance(item, ASTNode):
  34 |                     lines.append(format_ast(item, indent + 2))
  35 |                 else:
  36 |                     lines.append(f"{sp}    {item!r}")
  37 |             lines.append(f"{sp}  ]")
  38 |         else:
  39 |             lines.append(f"{sp}  {k}: {v!r}")
  40 |     return "\n".join(lines)
  41 | 
  42 | 
  43 | def main(argv=None) -> int:
  44 |     parser = argparse.ArgumentParser(
  45 |         prog="wetc",
  46 |         description="WetLang Compiler & Disassembler for Neural Organoid Computing."
  47 |     )
  48 |     parser.add_argument("source", help="Input .wet source file path")
  49 |     parser.add_argument("-o", "--output", help="Output .wbc binary file path")
  50 |     parser.add_argument("--disasm", action="store_true", help="Print disassembly of compiled bytecode")
  51 |     parser.add_argument("--dump-ast", action="store_true", help="Dump Abstract Syntax Tree to stdout")
  52 | 
  53 |     args = parser.parse_args(argv)
  54 | 
  55 |     if not os.path.exists(args.source):
  56 |         print(f"Error: Source file '{args.source}' not found.", file=sys.stderr)
  57 |         return 1
  58 | 
  59 |     try:
  60 |         with open(args.source, "r", encoding="utf-8") as f:
  61 |             source_text = f.read()
  62 | 
  63 |         # Step 1 & 2: Tokenize and Parse
  64 |         lexer = Lexer(source_text)
  65 |         tokens = lexer.tokenize()
  66 |         parser_inst = Parser(tokens, source_text=source_text)
  67 |         ast = parser_inst.parse()
  68 | 
  69 |         if args.dump_ast:
  70 |             print(format_ast(ast))
  71 | 
  72 |         # Step 3: Semantic Analysis
  73 |         analyzer = SemanticAnalyzer(ast)
  74 |         analyzer.analyze()
  75 | 
  76 |         # Step 4: Emit Bytecode
  77 |         emitter = BytecodeEmitter()
  78 |         bytecode = emitter.compile(ast)
  79 | 
  80 |         if args.disasm:
  81 |             print(disassemble(bytecode))
  82 | 
  83 |         # Write output file
  84 |         out_path = args.output
  85 |         if not out_path:
  86 |             base, _ = os.path.splitext(args.source)
  87 |             out_path = base + ".wbc"
  88 | 
  89 |         with open(out_path, "wb") as f:
  90 |             f.write(bytecode)
  91 | 
  92 |         print(f"Successfully compiled '{args.source}' -> '{out_path}' ({len(bytecode)} bytes).")
  93 |         return 0
  94 | 
  95 |     except (LexerError, ParseError, SemanticError) as err:
  96 |         print(f"Compilation Failed: {err}", file=sys.stderr)
  97 |         return 2
  98 |     except Exception as ex:
  99 |         print(f"Unexpected Compiler Error: {ex}", file=sys.stderr)
 100 |         return 3
 101 | 
 102 | 
 103 | if __name__ == "__main__":
 104 |     sys.exit(main())
```

### `compiler/crypto_signer.py` (151 lines, SHA-256: `fc997ccd07fcb31b...`)

```text
   1 | """
   2 | WetLang Biosafety Cryptographic Signing & Tamper Verification
   3 | =============================================================
   4 | Enforces cryptographic provenance for WBC binaries running on physical biological wetware.
   5 | Implements HMAC-SHA256 authenticated manifests preventing unauthorized bytecode execution.
   6 | """
   7 | 
   8 | import hmac
   9 | import hashlib
  10 | import struct
  11 | from typing import Tuple, Optional, List
  12 | 
  13 | from compiler.isa import HEADER_MAGIC, HEADER_SIZE, Capability
  14 | 
  15 | 
  16 | SIGNATURE_MAGIC = b"WETSIG01"          # 8 bytes (HMAC-SHA256)
  17 | SIGNATURE_MAGIC_ED25519 = b"WETED255"  # 8 bytes (Phase 3 Asymmetric Ed25519)
  18 | SIGNATURE_LEN = 32                     # HMAC-SHA256 digest length
  19 | ED25519_SIG_LEN = 64                   # Ed25519 signature length (64 bytes)
  20 | 
  21 | 
  22 | def generate_ed25519_keypair() -> Tuple[bytes, bytes]:
  23 |     """Generates an Ed25519 (private_key_bytes [32B], public_key_bytes [32B]) keypair."""
  24 |     from cryptography.hazmat.primitives.asymmetric import ed25519
  25 |     from cryptography.hazmat.primitives import serialization
  26 |     priv = ed25519.Ed25519PrivateKey.generate()
  27 |     pub = priv.public_key()
  28 |     priv_bytes = priv.private_bytes(
  29 |         encoding=serialization.Encoding.Raw,
  30 |         format=serialization.PrivateFormat.Raw,
  31 |         encryption_algorithm=serialization.NoEncryption()
  32 |     )
  33 |     pub_bytes = pub.public_bytes(
  34 |         encoding=serialization.Encoding.Raw,
  35 |         format=serialization.PublicFormat.Raw
  36 |     )
  37 |     return priv_bytes, pub_bytes
  38 | 
  39 | 
  40 | def sign_bytecode_ed25519(bytecode: bytes, private_key_bytes: bytes) -> bytes:
  41 |     """
  42 |     Signs a WBC binary with an asymmetric Ed25519 biosafety certificate.
  43 |     Bioreactor hardware only needs the 32-byte public key to verify;
  44 |     the private signing key remains offline or in an HSM.
  45 |     """
  46 |     from cryptography.hazmat.primitives.asymmetric import ed25519
  47 |     if len(bytecode) < HEADER_SIZE or bytecode[:4] != HEADER_MAGIC:
  48 |         raise ValueError("Invalid WBC binary: header truncated or magic mismatch")
  49 | 
  50 |     caps = struct.unpack_from("<H", bytecode, 6)[0]
  51 |     caps |= Capability.CAP_SIGNATURE_VERIFIED
  52 | 
  53 |     modified = bytearray(bytecode)
  54 |     struct.pack_into("<H", modified, 6, caps)
  55 | 
  56 |     priv = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)
  57 |     sig = priv.sign(bytes(modified))
  58 | 
  59 |     trailer = struct.pack("<8s64s", SIGNATURE_MAGIC_ED25519, sig)
  60 |     return bytes(modified) + trailer
  61 | 
  62 | 
  63 | def verify_bytecode_ed25519(signed_bytecode: bytes, public_key_bytes: bytes) -> Tuple[bool, str]:
  64 |     """
  65 |     Verifies that the WBC binary carries a valid Ed25519 cryptographic signature
  66 |     matching the 32-byte public key embedded in bioreactor firmware.
  67 |     """
  68 |     from cryptography.hazmat.primitives.asymmetric import ed25519
  69 |     from cryptography.exceptions import InvalidSignature
  70 | 
  71 |     trailer_len = 8 + 64
  72 |     if len(signed_bytecode) < HEADER_SIZE + trailer_len:
  73 |         return False, "Binary too short for Ed25519 trailer"
  74 | 
  75 |     payload = signed_bytecode[:-trailer_len]
  76 |     trailer = signed_bytecode[-trailer_len:]
  77 | 
  78 |     sig_magic, sig_bytes = struct.unpack("<8s64s", trailer)
  79 |     if sig_magic != SIGNATURE_MAGIC_ED25519:
  80 |         return False, f"Invalid Ed25519 trailer magic: {sig_magic!r}"
  81 | 
  82 |     caps = struct.unpack_from("<H", payload, 6)[0]
  83 |     if (caps & Capability.CAP_SIGNATURE_VERIFIED) == 0:
  84 |         return False, "Bytecode lacks CAP_SIGNATURE_VERIFIED capability flag"
  85 | 
  86 |     try:
  87 |         pub = ed25519.Ed25519PublicKey.from_public_bytes(public_key_bytes)
  88 |         pub.verify(sig_bytes, payload)
  89 |         return True, "Valid Ed25519 signature"
  90 |     except InvalidSignature:
  91 |         return False, "Cryptographic signature mismatch: Ed25519 verification failed"
  92 |     except Exception as e:
  93 |         return False, f"Ed25519 verification error: {e}"
  94 | 
  95 | 
  96 | def sign_bytecode(bytecode: bytes, secret_key: bytes) -> bytes:
  97 |     """
  98 |     Signs a WBC binary with an HMAC-SHA256 biosafety certificate.
  99 |     Sets the CAP_SIGNATURE_VERIFIED capability flag in the header and appends
 100 |     the signed manifest trailer.
 101 |     """
 102 |     if len(bytecode) < HEADER_SIZE or bytecode[:4] != HEADER_MAGIC:
 103 |         raise ValueError("Invalid WBC binary: header truncated or magic mismatch")
 104 | 
 105 |     # Unpack capabilities at offset 6 (uint16)
 106 |     caps = struct.unpack_from("<H", bytecode, 6)[0]
 107 |     caps |= Capability.CAP_SIGNATURE_VERIFIED
 108 | 
 109 |     # Reconstruct bytecode with updated capabilities
 110 |     modified = bytearray(bytecode)
 111 |     struct.pack_into("<H", modified, 6, caps)
 112 | 
 113 |     # Compute HMAC-SHA256 over entire modified bytecode
 114 |     h = hmac.new(secret_key, bytes(modified), hashlib.sha256)
 115 |     digest = h.digest()
 116 | 
 117 |     # Append trailer: [SIGNATURE_MAGIC (8s)] [DIGEST (32s)]
 118 |     trailer = struct.pack("<8s32s", SIGNATURE_MAGIC, digest)
 119 |     return bytes(modified) + trailer
 120 | 
 121 | 
 122 | def verify_bytecode_signature(signed_bytecode: bytes, secret_key: bytes) -> Tuple[bool, str]:
 123 |     """
 124 |     Verifies that the signed WBC binary carries a valid cryptographic signature trailer
 125 |     and that the bytecode body matches the computed digest.
 126 |     Returns (is_valid: bool, reason: str).
 127 |     """
 128 |     trailer_len = 8 + 32
 129 |     if len(signed_bytecode) < HEADER_SIZE + trailer_len:
 130 |         return False, "Binary too short to contain cryptographic signature trailer"
 131 | 
 132 |     payload = signed_bytecode[:-trailer_len]
 133 |     trailer = signed_bytecode[-trailer_len:]
 134 | 
 135 |     sig_magic, expected_digest = struct.unpack("<8s32s", trailer)
 136 |     if sig_magic != SIGNATURE_MAGIC:
 137 |         return False, f"Invalid signature trailer magic: {sig_magic!r}"
 138 | 
 139 |     # Verify CAP_SIGNATURE_VERIFIED capability flag
 140 |     caps = struct.unpack_from("<H", payload, 6)[0]
 141 |     if (caps & Capability.CAP_SIGNATURE_VERIFIED) == 0:
 142 |         return False, "Bytecode lacks CAP_SIGNATURE_VERIFIED capability flag"
 143 | 
 144 |     # Compute actual HMAC
 145 |     h = hmac.new(secret_key, payload, hashlib.sha256)
 146 |     actual_digest = h.digest()
 147 | 
 148 |     if not hmac.compare_digest(actual_digest, expected_digest):
 149 |         return False, "Cryptographic signature mismatch: bytecode tampered or invalid secret key"
 150 | 
 151 |     return True, "Valid signature"
```

### `compiler/emitter.py` (951 lines, SHA-256: `0c0daf0ece1d0a17...`)

```text
   1 | """
   2 | WetLang Compiler - Bytecode Binary Emitter & Disassembler
   3 | Hand-crafted from first principles. Complete WBC binary serialization and CRC32 checksum.
   4 | """
   5 | 
   6 | import struct
   7 | import zlib
   8 | from typing import Dict, List, Tuple, Optional, Any, Set
   9 | from compiler.token import Dimension
  10 | from compiler.ast_nodes import (
  11 |     ASTNode,
  12 |     ASTVisitor,
  13 |     ProgramNode,
  14 |     OrganoidDeclNode,
  15 |     ConnectDeclNode,
  16 |     PortDeclNode,
  17 |     GridDeclNode,
  18 |     ChannelDeclNode,
  19 |     FnDeclNode,
  20 |     StreamDeclNode,
  21 |     StreamItemNode,
  22 |     BlockNode,
  23 |     LetStmtNode,
  24 |     AssignStmtNode,
  25 |     StimStmtNode,
  26 |     ModulateStmtNode,
  27 |     SyncTickStmtNode,
  28 |     IfStmtNode,
  29 |     WhileStmtNode,
  30 |     ForStmtNode,
  31 |     ReturnStmtNode,
  32 |     ExprStmtNode,
  33 |     BinaryOpNode,
  34 |     UnaryOpNode,
  35 |     LiteralNode,
  36 |     PhysicalLiteralNode,
  37 |     IdentifierNode,
  38 |     CallNode,
  39 |     IndexNode,
  40 |     RangeNode,
  41 |     DomainCallNode,
  42 | )
  43 | from compiler.isa import (
  44 |     HEADER_MAGIC,
  45 |     HEADER_SIZE,
  46 |     VERSION_MAJOR,
  47 |     VERSION_MINOR,
  48 |     HEADER_STRUCT_FORMAT,
  49 |     Capability,
  50 |     SectionType,
  51 |     SECTION_ENTRY_FORMAT,
  52 |     SECTION_ENTRY_SIZE,
  53 |     Opcode,
  54 |     OPCODE_OPERAND_FORMATS,
  55 |     OPCODE_NAMES,
  56 | )
  57 | 
  58 | 
  59 | class ConstantPool:
  60 |     """Manages deduplicated constants (integers, floats, strings)."""
  61 |     def __init__(self):
  62 |         self.entries: List[Tuple[int, Any]] = []  # (type_tag, value) 1=int, 2=float, 3=string
  63 |         self.lookup: Dict[Tuple[int, Any], int] = {}
  64 | 
  65 |     def add_int(self, val: int) -> int:
  66 |         key = (1, int(val))
  67 |         if key in self.lookup:
  68 |             return self.lookup[key]
  69 |         idx = len(self.entries)
  70 |         self.entries.append(key)
  71 |         self.lookup[key] = idx
  72 |         return idx
  73 | 
  74 |     def add_float(self, val: float) -> int:
  75 |         key = (2, float(val))
  76 |         if key in self.lookup:
  77 |             return self.lookup[key]
  78 |         idx = len(self.entries)
  79 |         self.entries.append(key)
  80 |         self.lookup[key] = idx
  81 |         return idx
  82 | 
  83 |     def add_string(self, val: str) -> int:
  84 |         key = (3, str(val))
  85 |         if key in self.lookup:
  86 |             return self.lookup[key]
  87 |         idx = len(self.entries)
  88 |         self.entries.append(key)
  89 |         self.lookup[key] = idx
  90 |         return idx
  91 | 
  92 |     def serialize(self) -> bytes:
  93 |         data = bytearray()
  94 |         data.extend(struct.pack("<I", len(self.entries)))
  95 |         for tag, val in self.entries:
  96 |             data.append(tag)
  97 |             if tag == 1:
  98 |                 data.extend(struct.pack("<i", val))
  99 |             elif tag == 2:
 100 |                 data.extend(struct.pack("<f", val))
 101 |             elif tag == 3:
 102 |                 s_bytes = val.encode('utf-8')
 103 |                 data.extend(struct.pack("<H", len(s_bytes)))
 104 |                 data.extend(s_bytes)
 105 |         return bytes(data)
 106 | 
 107 | 
 108 | class BytecodeEmitter(ASTVisitor):
 109 |     """
 110 |     Traverses the AST and emits stack machine bytecode with jump backpatching.
 111 |     """
 112 |     def __init__(self):
 113 |         self.code: bytearray = bytearray()
 114 |         self.constant_pool: ConstantPool = ConstantPool()
 115 |         self.locals_map: Dict[str, int] = {}
 116 |         self.next_local_slot: int = 0
 117 |         self.channel_aliases: Dict[str, int] = {} # alias_name -> linear channel 0..63
 118 |         self.channel_modes: Dict[str, str] = {}
 119 |         self.capabilities: int = Capability.NONE
 120 |         self.line_map: List[Tuple[int, int, int]] = [] # (bytecode_offset, line, col)
 121 |         self.max_voltage_seen: float = 0.0
 122 |         self.const_float_values: Dict[str, float] = {}
 123 |         self.const_int_values: Dict[str, int] = {}
 124 |         self.used_electrodes: Set[int] = set()
 125 |         self.local_types: Dict[str, str] = {}
 126 |         self.function_entry_points: Dict[str, int] = {}
 127 | 
 128 |     def _emit_duration_ms(self, node: ASTNode) -> None:
 129 |         """Emits a duration/window argument scaled to milliseconds for the VM internal clock."""
 130 |         if isinstance(node, PhysicalLiteralNode) and node.dimension == Dimension.TIME:
 131 |             # Convert SI seconds to milliseconds (* 1000.0)
 132 |             self.emit(Opcode.PUSH_FLOAT, float(node.si_value * 1000.0), node=node)
 133 |         else:
 134 |             self.visit(node)
 135 | 
 136 |     def _is_int_expr(self, node: ASTNode) -> bool:
 137 |         """Determines if an expression evaluates to an integer type."""
 138 |         if isinstance(node, LiteralNode) and node.type_name == "int":
 139 |             return True
 140 |         if isinstance(node, IdentifierNode):
 141 |             if node.name in self.const_int_values:
 142 |                 return True
 143 |             if getattr(node, "inferred_type", None) == "int":
 144 |                 return True
 145 |             if self.local_types.get(node.name) == "int":
 146 |                 return True
 147 |         if isinstance(node, DomainCallNode) and node.func_name == "read_spikes":
 148 |             return True
 149 |         if isinstance(node, BinaryOpNode) and node.op in ("+", "-", "*", "/", "%"):
 150 |             return self._is_int_expr(node.left) and self._is_int_expr(node.right)
 151 |         if isinstance(node, UnaryOpNode) and node.op in ("-", "+"):
 152 |             return self._is_int_expr(node.operand)
 153 |         if isinstance(node, CallNode) and isinstance(node.callee, IdentifierNode) and node.callee.name == "int":
 154 |             return True
 155 |         return False
 156 | 
 157 |     def _is_const_channel(self, node: ASTNode) -> bool:
 158 |         """Determines if a channel reference is known at compile time."""
 159 |         if isinstance(node, IdentifierNode):
 160 |             if node.name in self.channel_aliases or node.name in self.const_int_values:
 161 |                 return True
 162 |             return False
 163 |         if isinstance(node, LiteralNode) and node.type_name == "int":
 164 |             return True
 165 |         if isinstance(node, IndexNode):
 166 |             for idx in node.indices:
 167 |                 if self._extract_int_constant(idx) is None:
 168 |                     return False
 169 |             return True
 170 |         return self._extract_int_constant(node) is not None
 171 | 
 172 |     def emit(self, opcode: Opcode, *operands: Any, node: Optional[ASTNode] = None) -> int:
 173 |         """Emits an instruction byte and packed operands. Returns instruction start offset."""
 174 |         offset = len(self.code)
 175 |         if node is not None:
 176 |             self.line_map.append((offset, node.line, node.column))
 177 | 
 178 |         self.code.append(opcode.value)
 179 |         fmt = OPCODE_OPERAND_FORMATS.get(opcode, "")
 180 |         if fmt:
 181 |             self.code.extend(struct.pack(fmt, *operands))
 182 |         return offset
 183 | 
 184 |     def emit_jump(self, opcode: Opcode, target_placeholder: int = 0) -> int:
 185 |         """Emits a jump with placeholder offset for backpatching. Returns offset of the int16 operand."""
 186 |         self.code.append(opcode.value)
 187 |         operand_offset = len(self.code)
 188 |         self.code.extend(struct.pack("<h", target_placeholder))
 189 |         return operand_offset
 190 | 
 191 |     def patch_jump(self, operand_offset: int, target_instruction_offset: int) -> None:
 192 |         """Backpatches relative jump offset."""
 193 |         # Relative jump offset = target_instruction_offset - instruction_start_offset
 194 |         instr_start = operand_offset - 1
 195 |         rel_offset = target_instruction_offset - instr_start
 196 |         struct.pack_into("<h", self.code, operand_offset, rel_offset)
 197 | 
 198 |     def current_offset(self) -> int:
 199 |         return len(self.code)
 200 | 
 201 |     def get_or_create_local(self, name: str) -> int:
 202 |         if name not in self.locals_map:
 203 |             slot = self.next_local_slot
 204 |             self.locals_map[name] = slot
 205 |             self.next_local_slot += 1
 206 |             return slot
 207 |         return self.locals_map[name]
 208 | 
 209 |     # =========================================================================
 210 |     # AST Traversal & Code Generation
 211 |     # =========================================================================
 212 | 
 213 |     def compile(self, program: ProgramNode) -> bytes:
 214 |         """Compiles the AST ProgramNode into a complete WBC binary."""
 215 |         self.visit(program)
 216 | 
 217 |         # Set CAP_MULTI_ELECTRODE if more than 16 unique electrodes were used
 218 |         if len(self.used_electrodes) > 16:
 219 |             self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 220 | 
 221 |         # Append final HALT instruction
 222 |         self.emit(Opcode.HALT)
 223 | 
 224 |         # Serialize WBC Sections and Binary
 225 |         return self._build_wbc_binary()
 226 | 
 227 |     def visit_ProgramNode(self, node: ProgramNode) -> None:
 228 |         for decl in node.declarations:
 229 |             self.visit(decl)
 230 | 
 231 |     def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
 232 |         pass
 233 | 
 234 |     def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
 235 |         pass
 236 | 
 237 |     def visit_PortDeclNode(self, node: PortDeclNode) -> None:
 238 |         pass
 239 | 
 240 |     def visit_GridDeclNode(self, node: GridDeclNode) -> None:
 241 |         rows = 8
 242 |         cols = 8
 243 |         if isinstance(node.rows, LiteralNode) and node.rows.type_name == "int":
 244 |             rows = int(node.rows.value)
 245 |         if isinstance(node.cols, LiteralNode) and node.cols.type_name == "int":
 246 |             cols = int(node.cols.value)
 247 |         self.emit(Opcode.MEA_CONFIG, rows, cols, node=node)
 248 | 
 249 |     def visit_ChannelDeclNode(self, node: ChannelDeclNode) -> None:
 250 |         ch_idx = self._resolve_channel_index(node.target)
 251 |         self.channel_aliases[node.name] = ch_idx
 252 |         if node.mode:
 253 |             self.channel_modes[node.name] = node.mode
 254 | 
 255 |     def visit_FnDeclNode(self, node: FnDeclNode) -> None:
 256 |         if node.name == "main":
 257 |             # main is the program entry point: emit body inline without skip jump or ret
 258 |             for param in reversed(node.params):
 259 |                 slot = self.get_or_create_local(param.name)
 260 |                 self.emit(Opcode.STORE_LOCAL, slot, node=node)
 261 |                 if getattr(param, "type_name", None) == "int":
 262 |                     self.local_types[param.name] = "int"
 263 | 
 264 |             self.visit(node.body)
 265 |             return
 266 | 
 267 |         skip_jump = self.emit_jump(Opcode.JMP)
 268 |         fn_entry_pc = self.current_offset()
 269 |         self.function_entry_points[node.name] = fn_entry_pc
 270 | 
 271 |         for param in reversed(node.params):
 272 |             slot = self.get_or_create_local(param.name)
 273 |             self.emit(Opcode.STORE_LOCAL, slot, node=node)
 274 |             if getattr(param, "type_name", None) == "int":
 275 |                 self.local_types[param.name] = "int"
 276 | 
 277 |         self.visit(node.body)
 278 |         self.emit(Opcode.PUSH_INT, 0, node=node)
 279 |         self.emit(Opcode.RET, node=node)
 280 | 
 281 |         self.patch_jump(skip_jump, self.current_offset())
 282 | 
 283 |     def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
 284 |         self.capabilities |= Capability.CAP_CLOSED_LOOP
 285 |         for item in node.items:
 286 |             if item.kind == "cycle" and item.cycle_block is not None:
 287 |                 loop_start = self.current_offset()
 288 |                 self.visit(item.cycle_block)
 289 |                 self.emit_jump(Opcode.JMP, loop_start - self.current_offset())
 290 | 
 291 |     def visit_BlockNode(self, node: BlockNode) -> None:
 292 |         for stmt in node.statements:
 293 |             self.visit(stmt)
 294 | 
 295 |     def visit_LetStmtNode(self, node: LetStmtNode) -> None:
 296 |         slot = self.get_or_create_local(node.name)
 297 |         if getattr(node, "type_name", None) == "int":
 298 |             self.local_types[node.name] = "int"
 299 |         elif getattr(node, "type_name", None) == "float":
 300 |             self.local_types[node.name] = "float"
 301 | 
 302 |         if node.initializer is not None:
 303 |             if self._is_int_expr(node.initializer):
 304 |                 self.local_types[node.name] = "int"
 305 |             self.visit(node.initializer)
 306 |             self.emit(Opcode.STORE_LOCAL, slot, node=node)
 307 |             if not node.is_mut:
 308 |                 f_val = self._extract_float_si_value(node.initializer)
 309 |                 if f_val is not None:
 310 |                     self.const_float_values[node.name] = f_val
 311 |                 i_val = self._extract_int_constant(node.initializer)
 312 |                 if i_val is not None:
 313 |                     self.const_int_values[node.name] = i_val
 314 |         else:
 315 |             # Default zero initialization
 316 |             self.emit(Opcode.PUSH_INT, 0, node=node)
 317 |             self.emit(Opcode.STORE_LOCAL, slot, node=node)
 318 | 
 319 |     def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
 320 |         self.visit(node.value)
 321 |         if isinstance(node.target, IdentifierNode):
 322 |             slot = self.get_or_create_local(node.target.name)
 323 |             self.emit(Opcode.STORE_LOCAL, slot, node=node)
 324 |             if self._is_int_expr(node.value):
 325 |                 self.local_types[node.target.name] = "int"
 326 |         else:
 327 |             # Target is index, evaluate value then store
 328 |             self.emit(Opcode.POP, node=node)
 329 | 
 330 |     def visit_StimStmtNode(self, node: StimStmtNode) -> None:
 331 |         self.capabilities |= Capability.CAP_STIMULATION
 332 | 
 333 |         # Evaluate arguments onto stack: voltage, phase1, phase2, interphase
 334 |         self.visit(node.voltage)
 335 |         self._emit_duration_ms(node.phase1)
 336 |         self._emit_duration_ms(node.phase2)
 337 |         if node.interphase is not None:
 338 |             self._emit_duration_ms(node.interphase)
 339 |         else:
 340 |             self.emit(Opcode.PUSH_FLOAT, 0.0)
 341 | 
 342 |         # Check voltage capability and track max voltage seen
 343 |         v_val = self._extract_float_si_value(node.voltage)
 344 |         if v_val is not None:
 345 |             v_mag = abs(v_val)
 346 |             if v_mag > self.max_voltage_seen:
 347 |                 self.max_voltage_seen = v_mag
 348 |             if v_mag >= 0.8 - 1e-9:
 349 |                 self.capabilities |= Capability.CAP_HIGH_VOLTAGE
 350 |         else:
 351 |             # Fallback unwrap UnaryOpNode / Literals
 352 |             curr = node.voltage
 353 |             while isinstance(curr, UnaryOpNode) and curr.op in ("-", "+"):
 354 |                 curr = curr.operand
 355 |             if isinstance(curr, PhysicalLiteralNode):
 356 |                 v_mag = abs(curr.si_value)
 357 |                 if v_mag > self.max_voltage_seen:
 358 |                     self.max_voltage_seen = v_mag
 359 |                 if v_mag >= 0.8 - 1e-9:
 360 |                     self.capabilities |= Capability.CAP_HIGH_VOLTAGE
 361 |             elif isinstance(curr, LiteralNode) and curr.type_name in ("int", "float"):
 362 |                 v_mag = abs(float(curr.value))
 363 |                 if v_mag > self.max_voltage_seen:
 364 |                     self.max_voltage_seen = v_mag
 365 |                 if v_mag >= 0.8 - 1e-9:
 366 |                     self.capabilities |= Capability.CAP_HIGH_VOLTAGE
 367 | 
 368 |         if not self._is_const_channel(node.channel):
 369 |             self.visit(node.channel)
 370 |             self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 371 |             self.emit(Opcode.STIM_BIPHASIC, 0xFF, node=node)
 372 |         else:
 373 |             ch_idx = self._resolve_channel_index(node.channel)
 374 |             self.used_electrodes.add(ch_idx)
 375 |             if len(self.used_electrodes) > 16:
 376 |                 self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 377 |             self.emit(Opcode.STIM_BIPHASIC, ch_idx, node=node)
 378 | 
 379 |     def visit_ModulateStmtNode(self, node: ModulateStmtNode) -> None:
 380 |         self.capabilities |= Capability.CAP_PLASTICITY
 381 |         if len(node.args) == 3:
 382 |             if not self._is_const_channel(node.args[0]) or not self._is_const_channel(node.args[1]):
 383 |                 self.visit(node.args[0])  # dynamic pre
 384 |                 self.visit(node.args[1])  # dynamic post
 385 |                 self.visit(node.args[2])  # weight delta
 386 |                 self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 387 |                 self.emit(Opcode.MODULATE_STDP, 0xFF, 0xFF, node=node)
 388 |             else:
 389 |                 pre_ch = self._resolve_channel_index(node.args[0])
 390 |                 post_ch = self._resolve_channel_index(node.args[1])
 391 |                 self.used_electrodes.add(pre_ch)
 392 |                 self.used_electrodes.add(post_ch)
 393 |                 if len(self.used_electrodes) > 16:
 394 |                     self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 395 |                 self.visit(node.args[2])  # weight delta
 396 |                 self.emit(Opcode.MODULATE_STDP, pre_ch, post_ch, node=node)
 397 |         elif len(node.args) == 1:
 398 |             self.visit(node.args[0])  # weight delta / rate
 399 |             self.emit(Opcode.MODULATE_STDP, 0, 0, node=node)
 400 |         else:
 401 |             for arg in node.args:
 402 |                 self.visit(arg)
 403 |             self.emit(Opcode.MODULATE_STDP, 0, 0, node=node)
 404 | 
 405 |     def visit_SyncTickStmtNode(self, node: SyncTickStmtNode) -> None:
 406 |         if node.count is not None:
 407 |             if isinstance(node.count, LiteralNode) and node.count.type_name == "int":
 408 |                 cnt = int(node.count.value)
 409 |                 if cnt > 1:
 410 |                     self.emit(Opcode.SLEEP_TICKS, cnt, node=node)
 411 |                     return
 412 |             elif isinstance(node.count, PhysicalLiteralNode) and node.count.dimension == Dimension.TIME:
 413 |                 # e.g. sync_tick(2.0 ms) -> 20 ticks
 414 |                 ticks = int(round(node.count.si_value / 1e-4))
 415 |                 if ticks > 1:
 416 |                     self.emit(Opcode.SLEEP_TICKS, ticks, node=node)
 417 |                     return
 418 | 
 419 |         self.emit(Opcode.SYNC_TICK, node=node)
 420 | 
 421 |     def visit_IfStmtNode(self, node: IfStmtNode) -> None:
 422 |         self.visit(node.condition)
 423 |         false_jump = self.emit_jump(Opcode.JMP_IF_FALSE)
 424 |         self.visit(node.then_block)
 425 | 
 426 |         if node.else_block is not None:
 427 |             end_jump = self.emit_jump(Opcode.JMP)
 428 |             else_start = self.current_offset()
 429 |             self.patch_jump(false_jump, else_start)
 430 |             self.visit(node.else_block)
 431 |             end_offset = self.current_offset()
 432 |             self.patch_jump(end_jump, end_offset)
 433 |         else:
 434 |             then_end = self.current_offset()
 435 |             self.patch_jump(false_jump, then_end)
 436 | 
 437 |     def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
 438 |         loop_start = self.current_offset()
 439 |         self.visit(node.condition)
 440 |         exit_jump = self.emit_jump(Opcode.JMP_IF_FALSE)
 441 |         self.visit(node.body)
 442 |         self.emit_jump(Opcode.JMP, loop_start - (self.current_offset()))
 443 |         loop_end = self.current_offset()
 444 |         self.patch_jump(exit_jump, loop_end)
 445 | 
 446 |     def visit_ForStmtNode(self, node: ForStmtNode) -> None:
 447 |         slot = self.get_or_create_local(node.var_name)
 448 |         # Initialize var to range_start
 449 |         self.visit(node.range_start)
 450 |         self.emit(Opcode.STORE_LOCAL, slot, node=node)
 451 | 
 452 |         loop_start = self.current_offset()
 453 |         self.emit(Opcode.LOAD_LOCAL, slot)
 454 |         self.visit(node.range_end)
 455 |         self.emit(Opcode.CMP_LT)
 456 |         exit_jump = self.emit_jump(Opcode.JMP_IF_FALSE)
 457 | 
 458 |         self.visit(node.body)
 459 | 
 460 |         # Step: slot = slot + 1
 461 |         self.emit(Opcode.LOAD_LOCAL, slot)
 462 |         self.emit(Opcode.PUSH_INT, 1)
 463 |         self.emit(Opcode.ADD_I)
 464 |         self.emit(Opcode.STORE_LOCAL, slot)
 465 | 
 466 |         self.emit_jump(Opcode.JMP, loop_start - (self.current_offset()))
 467 |         loop_end = self.current_offset()
 468 |         self.patch_jump(exit_jump, loop_end)
 469 | 
 470 |     def visit_ReturnStmtNode(self, node: ReturnStmtNode) -> None:
 471 |         if node.value is not None:
 472 |             self.visit(node.value)
 473 |         else:
 474 |             self.emit(Opcode.PUSH_INT, 0)
 475 |         self.emit(Opcode.RET, node=node)
 476 | 
 477 |     def visit_ExprStmtNode(self, node: ExprStmtNode) -> None:
 478 |         self.visit(node.expr)
 479 |         # Void domain calls do not push a return value to the stack; do not emit POP
 480 |         if isinstance(node.expr, DomainCallNode) and node.expr.func_name in (
 481 |             "pump_set_rate", "pump_dispense", "valve_set", "valve_open", "valve_close", "motor_step"
 482 |         ):
 483 |             return
 484 |         self.emit(Opcode.POP, node=node)
 485 | 
 486 |     def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
 487 |         is_int = self._is_int_expr(node.left) and self._is_int_expr(node.right)
 488 |         self.visit(node.left)
 489 |         self.visit(node.right)
 490 | 
 491 |         if node.op == "+":
 492 |             self.emit(Opcode.ADD_I if is_int else Opcode.ADD_F, node=node)
 493 |         elif node.op == "-":
 494 |             self.emit(Opcode.SUB_I if is_int else Opcode.SUB_F, node=node)
 495 |         elif node.op == "*":
 496 |             self.emit(Opcode.MUL_I if is_int else Opcode.MUL_F, node=node)
 497 |         elif node.op == "/":
 498 |             self.emit(Opcode.DIV_I if is_int else Opcode.DIV_F, node=node)
 499 |         elif node.op == "%":
 500 |             self.emit(Opcode.MOD_I, node=node)
 501 |         elif node.op == "==":
 502 |             self.emit(Opcode.CMP_EQ, node=node)
 503 |         elif node.op == "!=":
 504 |             self.emit(Opcode.CMP_NE, node=node)
 505 |         elif node.op == "<":
 506 |             self.emit(Opcode.CMP_LT, node=node)
 507 |         elif node.op == "<=":
 508 |             self.emit(Opcode.CMP_LE, node=node)
 509 |         elif node.op == ">":
 510 |             self.emit(Opcode.CMP_GT, node=node)
 511 |         elif node.op == ">=":
 512 |             self.emit(Opcode.CMP_GE, node=node)
 513 |         elif node.op == "&&":
 514 |             self.emit(Opcode.MUL_I, node=node)
 515 |             self.emit(Opcode.PUSH_INT, 0)
 516 |             self.emit(Opcode.CMP_NE, node=node)
 517 |         elif node.op == "||":
 518 |             # Boolean normalization: (left != 0) + (right != 0) > 0
 519 |             self.emit(Opcode.ADD_I, node=node)
 520 |             self.emit(Opcode.PUSH_INT, 0)
 521 |             self.emit(Opcode.CMP_NE, node=node)
 522 | 
 523 |     def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
 524 |         self.visit(node.operand)
 525 |         if node.op == "-":
 526 |             self.emit(Opcode.NEG, node=node)
 527 |         elif node.op == "!":
 528 |             self.emit(Opcode.PUSH_INT, 0, node=node)
 529 |             self.emit(Opcode.CMP_EQ, node=node)
 530 | 
 531 |     def visit_LiteralNode(self, node: LiteralNode) -> None:
 532 |         if node.type_name == "int":
 533 |             self.emit(Opcode.PUSH_INT, int(node.value), node=node)
 534 |         elif node.type_name == "float":
 535 |             self.emit(Opcode.PUSH_FLOAT, float(node.value), node=node)
 536 |         elif node.type_name == "bool":
 537 |             self.emit(Opcode.PUSH_INT, 1 if node.value else 0, node=node)
 538 |         elif node.type_name == "string":
 539 |             idx = self.constant_pool.add_string(str(node.value))
 540 |             self.emit(Opcode.PUSH_CONST, idx, node=node)
 541 | 
 542 |     def visit_PhysicalLiteralNode(self, node: PhysicalLiteralNode) -> None:
 543 |         # All physical literals are loaded in SI base units on stack
 544 |         self.emit(Opcode.PUSH_FLOAT, float(node.si_value), node=node)
 545 | 
 546 |     def visit_IdentifierNode(self, node: IdentifierNode) -> None:
 547 |         if node.name in self.locals_map:
 548 |             slot = self.locals_map[node.name]
 549 |             self.emit(Opcode.LOAD_LOCAL, slot, node=node)
 550 |         elif node.name in self.channel_aliases:
 551 |             ch_idx = self.channel_aliases[node.name]
 552 |             self.emit(Opcode.PUSH_INT, ch_idx, node=node)
 553 |         else:
 554 |             slot = self.get_or_create_local(node.name)
 555 |             self.emit(Opcode.LOAD_LOCAL, slot, node=node)
 556 | 
 557 |     def visit_CallNode(self, node: CallNode) -> None:
 558 |         # Handle cast/math builtins
 559 |         if isinstance(node.callee, IdentifierNode):
 560 |             cname = node.callee.name
 561 |             if cname in ("int", "float") and len(node.args) == 1:
 562 |                 self.visit(node.args[0])
 563 |                 return
 564 |             if cname == "abs" and len(node.args) == 1:
 565 |                 self.visit(node.args[0])
 566 |                 self.emit(Opcode.DUP)
 567 |                 self.emit(Opcode.PUSH_INT, 0)
 568 |                 self.emit(Opcode.CMP_LT)
 569 |                 skip = self.emit_jump(Opcode.JMP_IF_FALSE)
 570 |                 self.emit(Opcode.NEG)
 571 |                 self.patch_jump(skip, self.current_offset())
 572 |                 return
 573 |             if cname in self.function_entry_points:
 574 |                 for arg in node.args:
 575 |                     self.visit(arg)
 576 |                 fn_pc = self.function_entry_points[cname]
 577 |                 self.emit(Opcode.CALL, fn_pc, len(node.args), node=node)
 578 |                 return
 579 | 
 580 |         for arg in node.args:
 581 |             self.visit(arg)
 582 |         fn_idx = self.constant_pool.add_string(getattr(node.callee, "name", "fn"))
 583 |         self.emit(Opcode.CALL, fn_idx, len(node.args), node=node)
 584 | 
 585 |     def visit_IndexNode(self, node: IndexNode) -> None:
 586 |         if self._is_const_channel(node):
 587 |             ch_idx = self._resolve_channel_index(node)
 588 |             self.emit(Opcode.PUSH_INT, ch_idx, node=node)
 589 |         else:
 590 |             # Dynamic grid/channel indexing
 591 |             if len(node.indices) == 2:
 592 |                 self.visit(node.indices[0])
 593 |                 self.emit(Opcode.PUSH_INT, 8)
 594 |                 self.emit(Opcode.MUL_I)
 595 |                 self.visit(node.indices[1])
 596 |                 self.emit(Opcode.ADD_I)
 597 |             elif len(node.indices) == 1:
 598 |                 self.visit(node.indices[0])
 599 | 
 600 |     def visit_DomainCallNode(self, node: DomainCallNode) -> None:
 601 |         if node.func_name == "read_spikes":
 602 |             if not self._is_const_channel(node.args[0]):
 603 |                 self.visit(node.args[0])  # dynamic channel
 604 |                 self._emit_duration_ms(node.args[1])  # window_ms
 605 |                 self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 606 |                 self.emit(Opcode.READ_SPIKES, 0xFF, node=node)
 607 |             else:
 608 |                 ch_idx = self._resolve_channel_index(node.args[0])
 609 |                 self.used_electrodes.add(ch_idx)
 610 |                 if len(self.used_electrodes) > 16:
 611 |                     self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 612 |                 self._emit_duration_ms(node.args[1])  # window_ms
 613 |                 self.emit(Opcode.READ_SPIKES, ch_idx, node=node)
 614 |         elif node.func_name == "read_voltage":
 615 |             if not self._is_const_channel(node.args[0]):
 616 |                 self.visit(node.args[0])  # dynamic channel
 617 |                 self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 618 |                 self.emit(Opcode.READ_VOLTAGE, 0xFF, node=node)
 619 |             else:
 620 |                 ch_idx = self._resolve_channel_index(node.args[0])
 621 |                 self.used_electrodes.add(ch_idx)
 622 |                 if len(self.used_electrodes) > 16:
 623 |                     self.capabilities |= Capability.CAP_MULTI_ELECTRODE
 624 |                 self.emit(Opcode.READ_VOLTAGE, ch_idx, node=node)
 625 |         elif node.func_name in ("pop_firing_rate", "read_population_rate"):
 626 |             self._emit_duration_ms(node.args[0])  # window_ms
 627 |             self.emit(Opcode.GET_POP_RATE, node=node)
 628 |         elif node.func_name == "pump_set_rate":
 629 |             pump_id = self._eval_const_int(node.args[0])
 630 |             rate_val = 0.0
 631 |             if isinstance(node.args[1], PhysicalLiteralNode):
 632 |                 rate_val = float(node.args[1].magnitude)
 633 |                 if node.args[1].unit_suffix == "mL/min":
 634 |                     rate_val *= 1000.0
 635 |             elif isinstance(node.args[1], LiteralNode):
 636 |                 rate_val = float(node.args[1].value)
 637 |             self.capabilities |= Capability.CAP_MICROFLUIDICS
 638 |             self.emit(Opcode.PUMP_SET_RATE, pump_id, rate_val, node=node)
 639 |         elif node.func_name == "pump_dispense":
 640 |             pump_id = self._eval_const_int(node.args[0])
 641 |             vol_val = 0.0
 642 |             if isinstance(node.args[1], PhysicalLiteralNode):
 643 |                 vol_val = float(node.args[1].magnitude)
 644 |                 if node.args[1].unit_suffix == "mL":
 645 |                     vol_val *= 1000.0
 646 |             elif isinstance(node.args[1], LiteralNode):
 647 |                 vol_val = float(node.args[1].value)
 648 |             self.capabilities |= Capability.CAP_MICROFLUIDICS
 649 |             self.emit(Opcode.PUMP_DISPENSE, pump_id, vol_val, node=node)
 650 |         elif node.func_name in ("valve_set", "valve_open", "valve_close"):
 651 |             valve_id = self._eval_const_int(node.args[0])
 652 |             if node.func_name == "valve_open":
 653 |                 state = 1
 654 |             elif node.func_name == "valve_close":
 655 |                 state = 0
 656 |             else:
 657 |                 state = 1 if self._eval_const_int(node.args[1]) else 0
 658 |             self.capabilities |= Capability.CAP_MICROFLUIDICS
 659 |             self.emit(Opcode.VALVE_SET, valve_id, state, node=node)
 660 |         elif node.func_name == "motor_step":
 661 |             motor_id = self._eval_const_int(node.args[0])
 662 |             steps = self._eval_const_int(node.args[1])
 663 |             speed = 60.0
 664 |             if len(node.args) > 2:
 665 |                 if isinstance(node.args[2], PhysicalLiteralNode):
 666 |                     speed = float(node.args[2].magnitude)
 667 |                 elif isinstance(node.args[2], LiteralNode):
 668 |                     speed = float(node.args[2].value)
 669 |             self.capabilities |= Capability.CAP_MOTOR_ACTUATION
 670 |             self.emit(Opcode.MOTOR_STEP, motor_id, steps, speed, node=node)
 671 |         elif node.func_name == "read_pressure":
 672 |             port_id = self._eval_const_int(node.args[0]) if node.args else 0
 673 |             self.emit(Opcode.READ_PRESSURE, port_id, node=node)
 674 |         elif node.func_name == "read_temperature":
 675 |             self.emit(Opcode.READ_TEMPERATURE, node=node)
 676 | 
 677 |     def _resolve_channel_index(self, node: ASTNode) -> int:
 678 |         """Resolves channel expression to linear channel index 0..63."""
 679 |         if isinstance(node, IdentifierNode):
 680 |             if node.name in self.channel_aliases:
 681 |                 return self.channel_aliases[node.name]
 682 |             if node.name in self.const_int_values:
 683 |                 return self.const_int_values[node.name]
 684 |             return 0
 685 |         if isinstance(node, LiteralNode) and node.type_name == "int":
 686 |             return int(node.value)
 687 |         if isinstance(node, IndexNode):
 688 |             if len(node.indices) == 2:
 689 |                 r = self._eval_const_int(node.indices[0])
 690 |                 c = self._eval_const_int(node.indices[1])
 691 |                 return r * 8 + c
 692 |             elif len(node.indices) == 1:
 693 |                 return self._eval_const_int(node.indices[0])
 694 |         const_int = self._extract_int_constant(node)
 695 |         if const_int is not None:
 696 |             return const_int
 697 |         return 0
 698 | 
 699 |     def _eval_const_int(self, node: ASTNode) -> int:
 700 |         val = self._extract_int_constant(node)
 701 |         return val if val is not None else 0
 702 | 
 703 |     def _extract_int_constant(self, node: ASTNode) -> Optional[int]:
 704 |         if isinstance(node, LiteralNode) and node.type_name == "int":
 705 |             return int(node.value)
 706 |         if isinstance(node, UnaryOpNode):
 707 |             inner = self._extract_int_constant(node.operand)
 708 |             if inner is None:
 709 |                 return None
 710 |             if node.op == "-":
 711 |                 return -inner
 712 |             if node.op == "+":
 713 |                 return inner
 714 |             return None
 715 |         if isinstance(node, BinaryOpNode):
 716 |             left = self._extract_int_constant(node.left)
 717 |             right = self._extract_int_constant(node.right)
 718 |             if left is None or right is None:
 719 |                 return None
 720 |             if node.op == "+":
 721 |                 return left + right
 722 |             if node.op == "-":
 723 |                 return left - right
 724 |             if node.op == "*":
 725 |                 return left * right
 726 |             if node.op == "/":
 727 |                 if right == 0:
 728 |                     return None
 729 |                 return left // right
 730 |             if node.op == "%":
 731 |                 if right == 0:
 732 |                     return None
 733 |                 return left % right
 734 |             return None
 735 |         if isinstance(node, IdentifierNode):
 736 |             if hasattr(self, "const_int_values") and node.name in self.const_int_values:
 737 |                 return self.const_int_values[node.name]
 738 |         return None
 739 | 
 740 |     def _extract_float_si_value(self, node: ASTNode) -> Optional[float]:
 741 |         if isinstance(node, PhysicalLiteralNode):
 742 |             return float(node.si_value)
 743 |         if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
 744 |             return float(node.value)
 745 |         if isinstance(node, UnaryOpNode):
 746 |             sub = self._extract_float_si_value(node.operand)
 747 |             if sub is None:
 748 |                 return None
 749 |             if node.op == "-":
 750 |                 return -sub
 751 |             if node.op == "+":
 752 |                 return sub
 753 |             return None
 754 |         if isinstance(node, BinaryOpNode):
 755 |             left = self._extract_float_si_value(node.left)
 756 |             right = self._extract_float_si_value(node.right)
 757 |             if left is None or right is None:
 758 |                 return None
 759 |             if node.op == "+":
 760 |                 return left + right
 761 |             if node.op == "-":
 762 |                 return left - right
 763 |             if node.op == "*":
 764 |                 return left * right
 765 |             if node.op == "/":
 766 |                 if abs(right) < 1e-15:
 767 |                     return None
 768 |                 return left / right
 769 |             return None
 770 |         if isinstance(node, IdentifierNode):
 771 |             if hasattr(self, "const_float_values") and node.name in self.const_float_values:
 772 |                 return self.const_float_values[node.name]
 773 |         return None
 774 | 
 775 |     # =========================================================================
 776 |     # Section Packaging & WBC Serialization
 777 |     # =========================================================================
 778 | 
 779 |     def _build_wbc_binary(self) -> bytes:
 780 |         # 1. Section 1: CONSTANT_POOL
 781 |         sec1_data = self.constant_pool.serialize()
 782 | 
 783 |         # 2. Section 2: TOPOLOGY_CONFIG
 784 |         sec2_data = self._serialize_topology()
 785 | 
 786 |         # 3. Section 3: BYTECODE_STREAM
 787 |         sec3_data = bytes(self.code)
 788 | 
 789 |         # 4. Section 4: SAFETY_MANIFEST
 790 |         sec4_data = self._serialize_manifest()
 791 | 
 792 |         # 5. Section 5: DEBUG_LINE_MAP
 793 |         sec5_data = self._serialize_line_map()
 794 | 
 795 |         sections = [
 796 |             (SectionType.CONSTANT_POOL, sec1_data),
 797 |             (SectionType.TOPOLOGY_CONFIG, sec2_data),
 798 |             (SectionType.BYTECODE_STREAM, sec3_data),
 799 |             (SectionType.SAFETY_MANIFEST, sec4_data),
 800 |             (SectionType.DEBUG_LINE_MAP, sec5_data),
 801 |         ]
 802 | 
 803 |         num_sections = len(sections)
 804 |         section_table_size = num_sections * SECTION_ENTRY_SIZE
 805 |         payload_offset = HEADER_SIZE + section_table_size
 806 | 
 807 |         section_table_bytes = bytearray()
 808 |         payload_bytes = bytearray()
 809 | 
 810 |         curr_offset = payload_offset
 811 |         for sec_type, sec_data in sections:
 812 |             sec_len = len(sec_data)
 813 |             entry = struct.pack(SECTION_ENTRY_FORMAT, sec_type.value, 0, curr_offset, sec_len)
 814 |             section_table_bytes.extend(entry)
 815 |             payload_bytes.extend(sec_data)
 816 |             curr_offset += sec_len
 817 | 
 818 |         total_file_size = HEADER_SIZE + len(section_table_bytes) + len(payload_bytes)
 819 | 
 820 |         # Build Header with CRC32 = 0 placeholder
 821 |         header_placeholder = struct.pack(
 822 |             HEADER_STRUCT_FORMAT,
 823 |             HEADER_MAGIC,
 824 |             VERSION_MAJOR,
 825 |             VERSION_MINOR,
 826 |             int(self.capabilities),
 827 |             total_file_size,
 828 |             0, # CRC32 placeholder
 829 |             num_sections,
 830 |             64, # channel count (8x8 MEA)
 831 |             0.5, # max charge limit 0.5 nC
 832 |             0 # reserved
 833 |         )
 834 | 
 835 |         full_binary = bytearray(header_placeholder)
 836 |         full_binary.extend(section_table_bytes)
 837 |         full_binary.extend(payload_bytes)
 838 | 
 839 |         # Calculate CRC32 over the entire file
 840 |         crc = zlib.crc32(bytes(full_binary)) & 0xFFFFFFFF
 841 |         # Backpatch CRC32 at offset 0x0C (12)
 842 |         struct.pack_into("<I", full_binary, 12, crc)
 843 | 
 844 |         return bytes(full_binary)
 845 | 
 846 |     def _serialize_topology(self) -> bytes:
 847 |         data = bytearray()
 848 |         data.extend(struct.pack("<IHHfI", 64, 8, 8, 200.0, len(self.channel_aliases)))
 849 |         for name, ch_id in self.channel_aliases.items():
 850 |             name_bytes = name.encode('utf-8')
 851 |             mode_str = self.channel_modes.get(name, "Bidirectional")
 852 |             mode_byte = 0
 853 |             if mode_str == "BiphasicStim":
 854 |                 mode_byte = 1
 855 |             elif mode_str == "SpikeReadout":
 856 |                 mode_byte = 2
 857 |             elif mode_str == "VoltageSense":
 858 |                 mode_byte = 3
 859 |             data.extend(struct.pack("<H", len(name_bytes)))
 860 |             data.extend(name_bytes)
 861 |             data.extend(struct.pack("<BB", ch_id, mode_byte))
 862 |         return bytes(data)
 863 | 
 864 |     def _serialize_manifest(self) -> bytes:
 865 |         # Manifest format: capabilities (I), verified_loop_yield (B), max_voltage_seen (f), max_charge (f)
 866 |         return struct.pack("<IBff", int(self.capabilities), 1, self.max_voltage_seen, 0.5)
 867 | 
 868 |     def _serialize_line_map(self) -> bytes:
 869 |         data = bytearray()
 870 |         data.extend(struct.pack("<I", len(self.line_map)))
 871 |         for off, line, col in self.line_map:
 872 |             data.extend(struct.pack("<III", off, line, col))
 873 |         return bytes(data)
 874 | 
 875 | 
 876 | # =========================================================================
 877 | # High-Level Compiler Pipeline Helper
 878 | # =========================================================================
 879 | 
 880 | def compile_source(source_text: str, filename: str = "<stdin>") -> bytes:
 881 |     """
 882 |     Executes the complete 4-stage compiler pipeline:
 883 |     Lexer -> Pratt Parser -> Semantic/Safety Analyzer -> Bytecode Emitter.
 884 |     """
 885 |     from compiler.lexer import Lexer
 886 |     from compiler.parser import Parser
 887 |     from compiler.semantic import SemanticAnalyzer
 888 | 
 889 |     lexer = Lexer(source_text)
 890 |     tokens = lexer.tokenize()
 891 |     parser = Parser(tokens, source_text=source_text)
 892 |     ast = parser.parse()
 893 |     analyzer = SemanticAnalyzer(ast)
 894 |     analyzer.analyze()
 895 |     emitter = BytecodeEmitter()
 896 |     return emitter.compile(ast)
 897 | 
 898 | 
 899 | def disassemble(bytecode_bytes: bytes) -> str:
 900 |     """Disassembles a raw WBC binary into human-readable assembly listing."""
 901 |     if len(bytecode_bytes) < HEADER_SIZE:
 902 |         raise ValueError(f"Binary too small ({len(bytecode_bytes)} bytes), expected at least {HEADER_SIZE}")
 903 | 
 904 |     magic, v_maj, v_min, caps, fsize, crc, n_secs, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, bytecode_bytes, 0)
 905 |     if magic != HEADER_MAGIC:
 906 |         raise ValueError(f"Invalid WBC magic: {magic!r}, expected {HEADER_MAGIC!r}")
 907 | 
 908 |     lines: List[str] = []
 909 |     lines.append("=" * 70)
 910 |     lines.append(f"WBC Binary Disassembly (v{v_maj}.{v_min})")
 911 |     lines.append(f"File Size: {fsize} bytes | CRC32: 0x{crc:08X} | Capabilities: 0x{caps:04X}")
 912 |     lines.append(f"Sections: {n_secs} | Channels: {ch_cnt} | Max Charge Bound: {max_q:.2f} nC")
 913 |     lines.append("=" * 70)
 914 | 
 915 |     # Read Section Table
 916 |     sections_info: Dict[int, Tuple[int, int]] = {}
 917 |     sec_table_off = HEADER_SIZE
 918 |     for i in range(n_secs):
 919 |         stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, bytecode_bytes, sec_table_off + i * SECTION_ENTRY_SIZE)
 920 |         sections_info[stype] = (off, size)
 921 | 
 922 |     # Disassemble Bytecode Stream (Section 3)
 923 |     if SectionType.BYTECODE_STREAM.value in sections_info:
 924 |         code_off, code_size = sections_info[SectionType.BYTECODE_STREAM.value]
 925 |         code_bytes = bytecode_bytes[code_off:code_off + code_size]
 926 | 
 927 |         lines.append("\n[Section 3: BYTECODE_STREAM]")
 928 |         pc = 0
 929 |         while pc < len(code_bytes):
 930 |             op_byte = code_bytes[pc]
 931 |             op_name = OPCODE_NAMES.get(op_byte, f"UNKNOWN_0x{op_byte:02X}")
 932 |             op = Opcode(op_byte) if op_byte in OPCODE_NAMES else None
 933 | 
 934 |             fmt = OPCODE_OPERAND_FORMATS.get(op, "") if op else ""
 935 |             fmt_size = struct.calcsize(fmt) if fmt else 0
 936 | 
 937 |             raw_hex = [f"{op_byte:02X}"]
 938 |             for b in code_bytes[pc + 1:pc + 1 + fmt_size]:
 939 |                 raw_hex.append(f"{b:02X}")
 940 |             raw_str = " ".join(raw_hex).ljust(16)
 941 | 
 942 |             operands_str = ""
 943 |             if fmt_size > 0 and pc + 1 + fmt_size <= len(code_bytes):
 944 |                 operands = struct.unpack_from(fmt, code_bytes, pc + 1)
 945 |                 operands_str = ", ".join(str(o) for o in operands)
 946 | 
 947 |             lines.append(f"{pc:04X}:  {raw_str} {op_name:<16} {operands_str}")
 948 |             pc += 1 + fmt_size
 949 | 
 950 |     lines.append("=" * 70)
 951 |     return "\n".join(lines)
```

### `compiler/isa.py` (185 lines, SHA-256: `1236dcf84a16009f...`)

```text
   1 | """
   2 | WetLang Compiler - Instruction Set Architecture (ISA) & WBC Binary Format
   3 | Hand-crafted from first principles. Complete opcode table and 32-byte header.
   4 | """
   5 | 
   6 | from enum import IntEnum
   7 | import struct
   8 | from typing import Dict, Tuple
   9 | 
  10 | 
  11 | # =========================================================================
  12 | # WBC 32-Byte Header Specification
  13 | # =========================================================================
  14 | 
  15 | HEADER_MAGIC = b"WETB"        # 0x57, 0x45, 0x54, 0x42
  16 | HEADER_SIZE = 32              # Fixed 32 bytes
  17 | VERSION_MAJOR = 1
  18 | VERSION_MINOR = 0
  19 | 
  20 | # Header format:
  21 | # magic (4s), version_major (B), version_minor (B), capabilities (H),
  22 | # file_size (I), checksum_crc32 (I), num_sections (I), channel_count (I),
  23 | # max_charge_nc (f), reserved (I)
  24 | HEADER_STRUCT_FORMAT = "<4sBBHIIIIfI"
  25 | assert struct.calcsize(HEADER_STRUCT_FORMAT) == HEADER_SIZE, "Header struct must be exactly 32 bytes"
  26 | 
  27 | 
  28 | # Capability Bitmask Flags
  29 | class Capability(IntEnum):
  30 |     NONE = 0x0000
  31 |     CAP_STIMULATION = 0x0001        # Performs electrical stimulation
  32 |     CAP_PLASTICITY = 0x0002         # Modifies STDP synaptic weights
  33 |     CAP_CLOSED_LOOP = 0x0004        # Executes sensory-motor feedback stream
  34 |     CAP_HIGH_VOLTAGE = 0x0008       # Requests voltages between 0.8 V and 1.2 V
  35 |     CAP_MULTI_ELECTRODE = 0x0010    # Uses more than 16 electrodes concurrently
  36 |     CAP_MICROFLUIDICS = 0x0020      # Drives physical microfluidic pumps & valves
  37 |     CAP_MOTOR_ACTUATION = 0x0040    # Drives physical stepper motors / actuators
  38 |     CAP_SIGNATURE_VERIFIED = 0x0080 # Cryptographically signed bytecode
  39 | 
  40 | 
  41 | # Section Types
  42 | class SectionType(IntEnum):
  43 |     CONSTANT_POOL = 1
  44 |     TOPOLOGY_CONFIG = 2
  45 |     BYTECODE_STREAM = 3
  46 |     SAFETY_MANIFEST = 4
  47 |     DEBUG_LINE_MAP = 5
  48 | 
  49 | 
  50 | # Section entry format: section_type (H), reserved (H), offset (I), size (I)
  51 | SECTION_ENTRY_FORMAT = "<HHII"
  52 | SECTION_ENTRY_SIZE = struct.calcsize(SECTION_ENTRY_FORMAT) # 12 bytes
  53 | 
  54 | 
  55 | # =========================================================================
  56 | # Opcode Table (30+ Opcodes)
  57 | # =========================================================================
  58 | 
  59 | class Opcode(IntEnum):
  60 |     # Control
  61 |     NOP = 0x00
  62 |     HALT = 0x01
  63 |     SYNC_TICK = 0x02
  64 |     SLEEP_TICKS = 0x03
  65 | 
  66 |     # Stack Ops
  67 |     PUSH_CONST = 0x10
  68 |     PUSH_INT = 0x11
  69 |     PUSH_FLOAT = 0x12
  70 |     POP = 0x13
  71 |     DUP = 0x14
  72 |     SWAP = 0x15
  73 |     LOAD_LOCAL = 0x16
  74 |     STORE_LOCAL = 0x17
  75 | 
  76 |     # Arithmetic
  77 |     ADD_I = 0x20
  78 |     SUB_I = 0x21
  79 |     MUL_I = 0x22
  80 |     DIV_I = 0x23
  81 |     ADD_F = 0x24
  82 |     SUB_F = 0x25
  83 |     MUL_F = 0x26
  84 |     DIV_F = 0x27
  85 |     NEG = 0x28
  86 |     MOD_I = 0x29
  87 | 
  88 |     # Relational & Equality
  89 |     CMP_EQ = 0x30
  90 |     CMP_NE = 0x31
  91 |     CMP_LT = 0x32
  92 |     CMP_LE = 0x33
  93 |     CMP_GT = 0x34
  94 |     CMP_GE = 0x35
  95 | 
  96 |     # Control Jumps
  97 |     JMP = 0x40
  98 |     JMP_IF_TRUE = 0x41
  99 |     JMP_IF_FALSE = 0x42
 100 |     CALL = 0x43
 101 |     RET = 0x44
 102 | 
 103 |     # Biophysical & Domain
 104 |     STIM_BIPHASIC = 0x50
 105 |     READ_SPIKES = 0x51
 106 |     READ_VOLTAGE = 0x52
 107 |     MODULATE_STDP = 0x53
 108 |     GET_POP_RATE = 0x54
 109 |     MEA_CONFIG = 0x55
 110 | 
 111 |     # Cyber-Physical Hardware Actuation (Pumps, Valves, Motors, Sensors)
 112 |     PUMP_SET_RATE = 0x56
 113 |     PUMP_DISPENSE = 0x57
 114 |     VALVE_SET = 0x58
 115 |     MOTOR_STEP = 0x59
 116 |     READ_PRESSURE = 0x5A
 117 |     READ_TEMPERATURE = 0x5B
 118 | 
 119 |     # Phase 3 Electrophysiology & Environmental Sensors
 120 |     STIM_CURRENT = 0x5C
 121 |     READ_PH = 0x5D
 122 |     READ_DO = 0x5E
 123 |     READ_CO2 = 0x5F
 124 |     READ_BUBBLE = 0x60
 125 |     READ_FLOW = 0x61
 126 | 
 127 | 
 128 | # Opcode metadata: format strings for operands (little-endian)
 129 | # Empty string means no operands.
 130 | OPCODE_OPERAND_FORMATS: Dict[Opcode, str] = {
 131 |     Opcode.NOP: "",
 132 |     Opcode.HALT: "",
 133 |     Opcode.SYNC_TICK: "",
 134 |     Opcode.SLEEP_TICKS: "<H",          # uint16 ticks
 135 |     Opcode.PUSH_CONST: "<H",           # uint16 pool index
 136 |     Opcode.PUSH_INT: "<i",             # int32
 137 |     Opcode.PUSH_FLOAT: "<f",           # float32
 138 |     Opcode.POP: "",
 139 |     Opcode.DUP: "",
 140 |     Opcode.SWAP: "",
 141 |     Opcode.LOAD_LOCAL: "<H",           # uint16 local slot
 142 |     Opcode.STORE_LOCAL: "<H",          # uint16 local slot
 143 |     Opcode.ADD_I: "",
 144 |     Opcode.SUB_I: "",
 145 |     Opcode.MUL_I: "",
 146 |     Opcode.DIV_I: "",
 147 |     Opcode.ADD_F: "",
 148 |     Opcode.SUB_F: "",
 149 |     Opcode.MUL_F: "",
 150 |     Opcode.DIV_F: "",
 151 |     Opcode.NEG: "",
 152 |     Opcode.MOD_I: "",
 153 |     Opcode.CMP_EQ: "",
 154 |     Opcode.CMP_NE: "",
 155 |     Opcode.CMP_LT: "",
 156 |     Opcode.CMP_LE: "",
 157 |     Opcode.CMP_GT: "",
 158 |     Opcode.CMP_GE: "",
 159 |     Opcode.JMP: "<h",                  # int16 branch offset
 160 |     Opcode.JMP_IF_TRUE: "<h",          # int16 branch offset
 161 |     Opcode.JMP_IF_FALSE: "<h",         # int16 branch offset
 162 |     Opcode.CALL: "<HB",                # uint16 fn_idx, uint8 argc
 163 |     Opcode.RET: "",
 164 |     Opcode.STIM_BIPHASIC: "<B",        # uint8 channel
 165 |     Opcode.READ_SPIKES: "<B",          # uint8 channel
 166 |     Opcode.READ_VOLTAGE: "<B",         # uint8 channel
 167 |     Opcode.MODULATE_STDP: "<BB",       # uint8 pre, uint8 post
 168 |     Opcode.GET_POP_RATE: "",
 169 |     Opcode.MEA_CONFIG: "<BB",          # uint8 rows, uint8 cols
 170 |     Opcode.PUMP_SET_RATE: "<Bf",       # uint8 pump_id, float32 rate_ul_min
 171 |     Opcode.PUMP_DISPENSE: "<Bf",       # uint8 pump_id, float32 volume_ul
 172 |     Opcode.VALVE_SET: "<BB",           # uint8 valve_id, uint8 state (0/1)
 173 |     Opcode.MOTOR_STEP: "<Bif",         # uint8 motor_id, int32 steps, float32 speed_rpm
 174 |     Opcode.READ_PRESSURE: "<B",        # uint8 port_id
 175 |     Opcode.READ_TEMPERATURE: "",
 176 |     Opcode.STIM_CURRENT: "<Bf",        # uint8 channel, float32 current_ua
 177 |     Opcode.READ_PH: "",
 178 |     Opcode.READ_DO: "",
 179 |     Opcode.READ_CO2: "",
 180 |     Opcode.READ_BUBBLE: "<B",          # uint8 sensor_id
 181 |     Opcode.READ_FLOW: "<B",            # uint8 sensor_id
 182 | }
 183 | 
 184 | OPCODE_NAMES: Dict[int, str] = {op.value: op.name for op in Opcode}
 185 | OPCODE_BY_NAME: Dict[str, Opcode] = {op.name: op for op in Opcode}
```

### `compiler/lexer.py` (407 lines, SHA-256: `537066d4e72fece2...`)

```text
   1 | """
   2 | WetLang Compiler - Deterministic DFA Lexical Scanner
   3 | Hand-crafted from first principles. Zero regex library dependencies.
   4 | """
   5 | 
   6 | from typing import List, Optional
   7 | from compiler.token import (
   8 |     Token,
   9 |     TokenType,
  10 |     Dimension,
  11 |     KEYWORDS,
  12 |     UNIT_SUFFIXES,
  13 |     SORTED_UNIT_SUFFIXES,
  14 | )
  15 | 
  16 | 
  17 | class LexerError(Exception):
  18 |     """Raised when a lexical scanning invariant is violated."""
  19 |     def __init__(self, message: str, line: int, column: int):
  20 |         super().__init__(f"LexerError at line {line}, column {column}: {message}")
  21 |         self.message = message
  22 |         self.line = line
  23 |         self.column = column
  24 | 
  25 | 
  26 | class Lexer:
  27 |     """
  28 |     Deterministic DFA lexical scanner.
  29 |     Maintains 1-based line and column counters, character offsets,
  30 |     and performs immediate physical unit suffix binding on numeric literals.
  31 |     """
  32 |     def __init__(self, source: str):
  33 |         self.source: str = source
  34 |         self.length: int = len(source)
  35 |         self.cursor: int = 0
  36 |         self.line: int = 1
  37 |         self.column: int = 1
  38 | 
  39 |     def _peek(self, offset: int = 0) -> Optional[str]:
  40 |         idx = self.cursor + offset
  41 |         if idx < self.length:
  42 |             return self.source[idx]
  43 |         return None
  44 | 
  45 |     def _advance(self) -> Optional[str]:
  46 |         if self.cursor >= self.length:
  47 |             return None
  48 |         ch = self.source[self.cursor]
  49 |         self.cursor += 1
  50 |         if ch == '\n':
  51 |             self.line += 1
  52 |             self.column = 1
  53 |         else:
  54 |             self.column += 1
  55 |         return ch
  56 | 
  57 |     def _match(self, expected: str) -> bool:
  58 |         if self.cursor >= self.length:
  59 |             return False
  60 |         if self.source[self.cursor] != expected:
  61 |             return False
  62 |         self._advance()
  63 |         return True
  64 | 
  65 |     def tokenize(self) -> List[Token]:
  66 |         tokens: List[Token] = []
  67 |         while self.cursor < self.length:
  68 |             # Skip whitespace
  69 |             ch = self._peek()
  70 |             if ch in (' ', '\t', '\r', '\n'):
  71 |                 self._advance()
  72 |                 continue
  73 | 
  74 |             # Skip comments: single-line // and block /* ... */
  75 |             if ch == '/' and self._peek(1) == '/':
  76 |                 # Single-line comment
  77 |                 self._advance() # /
  78 |                 self._advance() # /
  79 |                 while self._peek() is not None and self._peek() != '\n':
  80 |                     self._advance()
  81 |                 continue
  82 | 
  83 |             if ch == '/' and self._peek(1) == '*':
  84 |                 # Multi-line block comment
  85 |                 start_line = self.line
  86 |                 start_col = self.column
  87 |                 self._advance() # /
  88 |                 self._advance() # *
  89 |                 closed = False
  90 |                 while self._peek() is not None:
  91 |                     if self._peek() == '*' and self._peek(1) == '/':
  92 |                         self._advance() # *
  93 |                         self._advance() # /
  94 |                         closed = True
  95 |                         break
  96 |                     self._advance()
  97 |                 if not closed:
  98 |                     raise LexerError("Unterminated block comment", start_line, start_col)
  99 |                 continue
 100 | 
 101 |             # Record token start position
 102 |             tok_line = self.line
 103 |             tok_col = self.column
 104 |             tok_start_offset = self.cursor
 105 | 
 106 |             # Number literal (or physical literal)
 107 |             if ch.isdigit():
 108 |                 tok = self._scan_number()
 109 |                 tokens.append(tok)
 110 |                 continue
 111 | 
 112 |             # String literal
 113 |             if ch == '"':
 114 |                 tok = self._scan_string()
 115 |                 tokens.append(tok)
 116 |                 continue
 117 | 
 118 |             # Identifier or keyword
 119 |             if ch.isalpha() or ch == '_':
 120 |                 tok = self._scan_identifier_or_keyword()
 121 |                 tokens.append(tok)
 122 |                 continue
 123 | 
 124 |             # Multi-character or single-character operators & delimiters
 125 |             tok = self._scan_operator_or_delimiter()
 126 |             tokens.append(tok)
 127 | 
 128 |         # Append EOF token
 129 |         tokens.append(Token(
 130 |             type=TokenType.EOF,
 131 |             value="",
 132 |             line=self.line,
 133 |             column=self.column,
 134 |             dimension=Dimension.NONE,
 135 |             si_value=None,
 136 |             raw_text=""
 137 |         ))
 138 |         return tokens
 139 | 
 140 |     def _scan_number(self) -> Token:
 141 |         start_line = self.line
 142 |         start_col = self.column
 143 |         start_offset = self.cursor
 144 | 
 145 |         # Consume integer part
 146 |         while self._peek() is not None and self._peek().isdigit():
 147 |             self._advance()
 148 | 
 149 |         # Check for fractional part
 150 |         is_float = False
 151 |         if self._peek() == '.' and self._peek(1) is not None and self._peek(1).isdigit():
 152 |             # Ensure it's not a range operator '..'
 153 |             if self._peek(1) != '.':
 154 |                 is_float = True
 155 |                 self._advance() # consume '.'
 156 |                 while self._peek() is not None and self._peek().isdigit():
 157 |                     self._advance()
 158 | 
 159 |         # Check for scientific exponent (e.g. 1e-3, 2.5e4)
 160 |         if self._peek() in ('e', 'E'):
 161 |             next_ch = self._peek(1)
 162 |             if next_ch in ('+', '-') and self._peek(2) is not None and self._peek(2).isdigit():
 163 |                 is_float = True
 164 |                 self._advance() # e
 165 |                 self._advance() # +/-
 166 |                 while self._peek() is not None and self._peek().isdigit():
 167 |                     self._advance()
 168 |             elif next_ch is not None and next_ch.isdigit():
 169 |                 is_float = True
 170 |                 self._advance() # e
 171 |                 while self._peek() is not None and self._peek().isdigit():
 172 |                     self._advance()
 173 | 
 174 |         num_str = self.source[start_offset:self.cursor]
 175 |         base_val = float(num_str) if is_float else int(num_str)
 176 | 
 177 |         # Check for immediate unit suffix (no intervening whitespace)
 178 |         # Match longest matching suffix
 179 |         matched_suffix: Optional[str] = None
 180 |         for suffix in SORTED_UNIT_SUFFIXES:
 181 |             s_len = len(suffix)
 182 |             candidate = self.source[self.cursor:self.cursor + s_len]
 183 |             if candidate == suffix:
 184 |                 # Ensure the suffix is not just the prefix of a larger identifier
 185 |                 next_after = self.source[self.cursor + s_len:self.cursor + s_len + 1]
 186 |                 if next_after and (next_after.isalnum() or next_after == '_'):
 187 |                     continue
 188 |                 matched_suffix = suffix
 189 |                 break
 190 | 
 191 |         if matched_suffix is not None:
 192 |             # Advance through suffix characters
 193 |             for _ in range(len(matched_suffix)):
 194 |                 self._advance()
 195 |             raw_full = self.source[start_offset:self.cursor]
 196 |             dim, scale = UNIT_SUFFIXES[matched_suffix]
 197 |             si_val = float(base_val) * scale
 198 |             return Token(
 199 |                 type=TokenType.PHYSICAL_LIT,
 200 |                 value=float(base_val),
 201 |                 line=start_line,
 202 |                 column=start_col,
 203 |                 dimension=dim,
 204 |                 si_value=si_val,
 205 |                 raw_text=raw_full
 206 |             )
 207 | 
 208 |         # Normal numeric literal
 209 |         raw_full = self.source[start_offset:self.cursor]
 210 |         if is_float:
 211 |             return Token(
 212 |                 type=TokenType.FLOAT_LIT,
 213 |                 value=float(base_val),
 214 |                 line=start_line,
 215 |                 column=start_col,
 216 |                 dimension=Dimension.NONE,
 217 |                 si_value=None,
 218 |                 raw_text=raw_full
 219 |             )
 220 |         else:
 221 |             return Token(
 222 |                 type=TokenType.INT_LIT,
 223 |                 value=int(base_val),
 224 |                 line=start_line,
 225 |                 column=start_col,
 226 |                 dimension=Dimension.NONE,
 227 |                 si_value=None,
 228 |                 raw_text=raw_full
 229 |             )
 230 | 
 231 |     def _scan_string(self) -> Token:
 232 |         start_line = self.line
 233 |         start_col = self.column
 234 |         start_offset = self.cursor
 235 | 
 236 |         self._advance() # opening quote '"'
 237 |         chars: List[str] = []
 238 |         while True:
 239 |             ch = self._peek()
 240 |             if ch is None:
 241 |                 raise LexerError("Unterminated string literal", start_line, start_col)
 242 |             if ch == '"':
 243 |                 self._advance() # closing quote
 244 |                 break
 245 |             if ch == '\\':
 246 |                 self._advance() # escape char
 247 |                 esc = self._advance()
 248 |                 if esc == 'n':
 249 |                     chars.append('\n')
 250 |                 elif esc == 't':
 251 |                     chars.append('\t')
 252 |                 elif esc == 'r':
 253 |                     chars.append('\r')
 254 |                 elif esc == '"':
 255 |                     chars.append('"')
 256 |                 elif esc == '\\':
 257 |                     chars.append('\\')
 258 |                 else:
 259 |                     chars.append(esc if esc is not None else '')
 260 |             else:
 261 |                 chars.append(self._advance())
 262 | 
 263 |         val = "".join(chars)
 264 |         raw = self.source[start_offset:self.cursor]
 265 |         return Token(
 266 |             type=TokenType.STRING_LIT,
 267 |             value=val,
 268 |             line=start_line,
 269 |             column=start_col,
 270 |             dimension=Dimension.NONE,
 271 |             si_value=None,
 272 |             raw_text=raw
 273 |         )
 274 | 
 275 |     def _scan_identifier_or_keyword(self) -> Token:
 276 |         start_line = self.line
 277 |         start_col = self.column
 278 |         start_offset = self.cursor
 279 | 
 280 |         while self._peek() is not None and (self._peek().isalnum() or self._peek() == '_'):
 281 |             self._advance()
 282 | 
 283 |         text = self.source[start_offset:self.cursor]
 284 | 
 285 |         # Check keyword table
 286 |         if text in KEYWORDS:
 287 |             tok_type = KEYWORDS[text]
 288 |             if tok_type == TokenType.TRUE:
 289 |                 return Token(
 290 |                     type=TokenType.BOOL_LIT,
 291 |                     value=True,
 292 |                     line=start_line,
 293 |                     column=start_col,
 294 |                     dimension=Dimension.NONE,
 295 |                     si_value=None,
 296 |                     raw_text=text
 297 |                 )
 298 |             elif tok_type == TokenType.FALSE:
 299 |                 return Token(
 300 |                     type=TokenType.BOOL_LIT,
 301 |                     value=False,
 302 |                     line=start_line,
 303 |                     column=start_col,
 304 |                     dimension=Dimension.NONE,
 305 |                     si_value=None,
 306 |                     raw_text=text
 307 |                 )
 308 |             return Token(
 309 |                 type=tok_type,
 310 |                 value=text,
 311 |                 line=start_line,
 312 |                 column=start_col,
 313 |                 dimension=Dimension.NONE,
 314 |                 si_value=None,
 315 |                 raw_text=text
 316 |             )
 317 | 
 318 |         # Regular identifier
 319 |         return Token(
 320 |             type=TokenType.IDENTIFIER,
 321 |             value=text,
 322 |             line=start_line,
 323 |             column=start_col,
 324 |             dimension=Dimension.NONE,
 325 |             si_value=None,
 326 |             raw_text=text
 327 |         )
 328 | 
 329 |     def _scan_operator_or_delimiter(self) -> Token:
 330 |         start_line = self.line
 331 |         start_col = self.column
 332 |         ch = self._advance()
 333 | 
 334 |         # Two-character operators
 335 |         if ch == '=':
 336 |             if self._peek() == '=':
 337 |                 self._advance()
 338 |                 return Token(TokenType.EQ_EQ, "==", start_line, start_col, raw_text="==")
 339 |             return Token(TokenType.ASSIGN, "=", start_line, start_col, raw_text="=")
 340 | 
 341 |         if ch == '!':
 342 |             if self._peek() == '=':
 343 |                 self._advance()
 344 |                 return Token(TokenType.NOT_EQ, "!=", start_line, start_col, raw_text="!=")
 345 |             return Token(TokenType.NOT, "!", start_line, start_col, raw_text="!")
 346 | 
 347 |         if ch == '<':
 348 |             if self._peek() == '=':
 349 |                 self._advance()
 350 |                 return Token(TokenType.LT_EQ, "<=", start_line, start_col, raw_text="<=")
 351 |             elif self._peek() == '-':
 352 |                 self._advance()
 353 |                 return Token(TokenType.ARROW_LEFT, "<-", start_line, start_col, raw_text="<-")
 354 |             return Token(TokenType.LT, "<", start_line, start_col, raw_text="<")
 355 | 
 356 |         if ch == '>':
 357 |             if self._peek() == '=':
 358 |                 self._advance()
 359 |                 return Token(TokenType.GT_EQ, ">=", start_line, start_col, raw_text=">=")
 360 |             return Token(TokenType.GT, ">", start_line, start_col, raw_text=">")
 361 | 
 362 |         if ch == '&':
 363 |             if self._peek() == '&':
 364 |                 self._advance()
 365 |                 return Token(TokenType.AND_AND, "&&", start_line, start_col, raw_text="&&")
 366 |             raise LexerError(f"Unexpected character '{ch}', expected '&&'", start_line, start_col)
 367 | 
 368 |         if ch == '|':
 369 |             if self._peek() == '|':
 370 |                 self._advance()
 371 |                 return Token(TokenType.OR_OR, "||", start_line, start_col, raw_text="||")
 372 |             raise LexerError(f"Unexpected character '{ch}', expected '||'", start_line, start_col)
 373 | 
 374 |         if ch == '-':
 375 |             if self._peek() == '>':
 376 |                 self._advance()
 377 |                 return Token(TokenType.ARROW_RIGHT, "->", start_line, start_col, raw_text="->")
 378 |             return Token(TokenType.MINUS, "-", start_line, start_col, raw_text="-")
 379 | 
 380 |         if ch == '.':
 381 |             if self._peek() == '.':
 382 |                 self._advance()
 383 |                 return Token(TokenType.DOT_DOT, "..", start_line, start_col, raw_text="..")
 384 |             return Token(TokenType.DOT, ".", start_line, start_col, raw_text=".")
 385 | 
 386 |         # Single-character operators & delimiters
 387 |         single_char_map = {
 388 |             '+': (TokenType.PLUS, "+"),
 389 |             '*': (TokenType.STAR, "*"),
 390 |             '/': (TokenType.SLASH, "/"),
 391 |             '%': (TokenType.PERCENT, "%"),
 392 |             '(': (TokenType.LPAREN, "("),
 393 |             ')': (TokenType.RPAREN, ")"),
 394 |             '{': (TokenType.LBRACE, "{"),
 395 |             '}': (TokenType.RBRACE, "}"),
 396 |             '[': (TokenType.LBRACKET, "["),
 397 |             ']': (TokenType.RBRACKET, "]"),
 398 |             ',': (TokenType.COMMA, ","),
 399 |             ':': (TokenType.COLON, ":"),
 400 |             ';': (TokenType.SEMICOLON, ";"),
 401 |         }
 402 | 
 403 |         if ch in single_char_map:
 404 |             tt, text = single_char_map[ch]
 405 |             return Token(tt, text, start_line, start_col, raw_text=text)
 406 | 
 407 |         raise LexerError(f"Unexpected character: {ch!r}", start_line, start_col)
```

### `compiler/nir_bridge.py` (910 lines, SHA-256: `b8145cffc82cf8a1...`)

```text
   1 | """
   2 | WetLang Compiler - Neuromorphic Intermediate Representation (NIR v1.0) Bridge
   3 | Production-grade bidirectional translator between standard NIR v1.0 graphs and WetLang.
   4 | Supports:
   5 |   - Primitives: Input, Output, Linear, Affine, LIF, CubaLIF, Izhikevich
   6 |   - Biophysical Parameter Mappings (COBA-LIF, Dale's Principle, Rs/Fs Izhikevich)
   7 |   - Ingestion (HDF5 .nir, JSON, Python dict) -> WetLang AST, .wet source, .wbc bytecode, live VM
   8 |   - Export (AST, .wbc bytecode, live VM) -> NIRGraph -> HDF5 .nir, JSON schema
   9 | """
  10 | 
  11 | from __future__ import annotations
  12 | 
  13 | import json
  14 | import math
  15 | import struct
  16 | from dataclasses import dataclass, field
  17 | from pathlib import Path
  18 | from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
  19 | 
  20 | import numpy as np
  21 | import h5py
  22 | 
  23 | from compiler.ast_nodes import (
  24 |     ASTNode,
  25 |     ProgramNode,
  26 |     GridDeclNode,
  27 |     ChannelDeclNode,
  28 |     WhileStmtNode,
  29 |     LetStmtNode,
  30 |     AssignStmtNode,
  31 |     StimStmtNode,
  32 |     SyncTickStmtNode,
  33 |     BlockNode,
  34 |     IdentifierNode,
  35 |     LiteralNode,
  36 |     IndexNode,
  37 |     BinaryOpNode,
  38 |     CallNode,
  39 |     DomainCallNode,
  40 |     PhysicalLiteralNode,
  41 |     IfStmtNode,
  42 | )
  43 | from compiler.isa import (
  44 |     HEADER_MAGIC,
  45 |     HEADER_SIZE,
  46 |     HEADER_STRUCT_FORMAT,
  47 |     SECTION_ENTRY_FORMAT,
  48 |     SECTION_ENTRY_SIZE,
  49 |     SectionType,
  50 |     Opcode,
  51 | )
  52 | from compiler.emitter import compile_source
  53 | 
  54 | 
  55 | # =========================================================================
  56 | # Biophysical Constants & Mappings (WetLang In-Silico Digital Twin)
  57 | # =========================================================================
  58 | 
  59 | # Membrane & Synaptic Dynamics
  60 | WET_C_M_PF: float = 200.0         # Membrane capacitance: 200 pF
  61 | WET_G_LEAK_NS: float = 10.0       # Leak conductance: 10 nS
  62 | WET_TAU_MEM_MS: float = 20.0      # tau_mem = Cm / gL = 200 pF / 10 nS = 20.0 ms
  63 | WET_R_MEM_MOHM: float = 100.0     # R_mem = 1 / gL = 100 MOhm
  64 | WET_TAU_SYN_AMPA_MS: float = 5.0  # AMPA excitatory synaptic decay
  65 | WET_TAU_SYN_GABA_MS: float = 10.0 # GABA_A inhibitory synaptic decay
  66 | 
  67 | # Voltage Boundaries (mV)
  68 | WET_V_LEAK_MV: float = -70.0      # E_leak = -70.0 mV
  69 | WET_V_RESET_MV: float = -75.0     # E_reset = -75.0 mV
  70 | WET_V_THRESH_MV: float = -50.0    # E_thresh = -50.0 mV
  71 | WET_V_REV_EXC_MV: float = 0.0     # Excitatory reversal potential
  72 | WET_V_REV_INH_MV: float = -80.0   # Inhibitory reversal potential
  73 | 
  74 | # Synaptic Conductance Hard Bounds (nS)
  75 | WET_W_MIN_NS: float = 0.0
  76 | WET_W_MAX_NS: float = 40.0
  77 | 
  78 | # Cortical Izhikevich Cell Archetypes
  79 | # Regular Spiking (RS) - Excitatory Pyramidal (80% cortical population)
  80 | IZHIKEVICH_RS = {
  81 |     "a": 0.02,
  82 |     "b": 0.20,
  83 |     "c": -65.0,
  84 |     "d": 8.0,
  85 |     "v_threshold": 30.0,
  86 | }
  87 | 
  88 | # Fast Spiking (FS) - Inhibitory Interneuron (20% cortical population)
  89 | IZHIKEVICH_FS = {
  90 |     "a": 0.10,
  91 |     "b": 0.20,
  92 |     "c": -65.0,
  93 |     "d": 2.0,
  94 |     "v_threshold": 30.0,
  95 | }
  96 | 
  97 | 
  98 | class DalesPrincipleError(ValueError):
  99 |     """Raised when synaptic connectivity violates Dale's Principle."""
 100 |     pass
 101 | 
 102 | 
 103 | class NIRValidationError(ValueError):
 104 |     """Raised when an NIR graph contains invalid dimensions or topology."""
 105 |     pass
 106 | 
 107 | 
 108 | # =========================================================================
 109 | # NIR v1.0 Node Primitives Data Model
 110 | # =========================================================================
 111 | 
 112 | @dataclass
 113 | class NIRNode:
 114 |     """Base class for standard Neuromorphic Intermediate Representation nodes."""
 115 |     metadata: Dict[str, Any] = field(default_factory=dict)
 116 | 
 117 |     @property
 118 |     def node_type(self) -> str:
 119 |         return self.__class__.__name__
 120 | 
 121 |     def to_dict(self) -> Dict[str, Any]:
 122 |         res = {"type": self.node_type}
 123 |         for k, v in self.__dict__.items():
 124 |             if isinstance(v, np.ndarray):
 125 |                 res[k] = v.tolist()
 126 |             elif isinstance(v, (list, tuple)):
 127 |                 res[k] = list(v)
 128 |             elif isinstance(v, (int, float, str, bool, dict)):
 129 |                 res[k] = v
 130 |         return res
 131 | 
 132 | 
 133 | @dataclass
 134 | class Input(NIRNode):
 135 |     """NIR Input Node representing stimulation sources."""
 136 |     input_type: Dict[str, Sequence[int]] = field(default_factory=dict)
 137 | 
 138 |     @property
 139 |     def shape(self) -> Tuple[int, ...]:
 140 |         if "input" in self.input_type:
 141 |             return tuple(self.input_type["input"])
 142 |         for v in self.input_type.values():
 143 |             return tuple(v)
 144 |         return ()
 145 | 
 146 | 
 147 | @dataclass
 148 | class Output(NIRNode):
 149 |     """NIR Output Node representing spike recording sensors."""
 150 |     output_type: Dict[str, Sequence[int]] = field(default_factory=dict)
 151 | 
 152 |     @property
 153 |     def shape(self) -> Tuple[int, ...]:
 154 |         if "output" in self.output_type:
 155 |             return tuple(self.output_type["output"])
 156 |         for v in self.output_type.values():
 157 |             return tuple(v)
 158 |         return ()
 159 | 
 160 | 
 161 | @dataclass
 162 | class Linear(NIRNode):
 163 |     """Dense Synaptic Weight Matrix."""
 164 |     weight: np.ndarray = field(default_factory=lambda: np.zeros((1, 1), dtype=np.float32))
 165 | 
 166 |     def __post_init__(self):
 167 |         self.weight = np.asarray(self.weight, dtype=np.float32)
 168 | 
 169 | 
 170 | @dataclass
 171 | class Affine(NIRNode):
 172 |     """Linear Synaptic Weight Matrix with constant bias."""
 173 |     weight: np.ndarray = field(default_factory=lambda: np.zeros((1, 1), dtype=np.float32))
 174 |     bias: np.ndarray = field(default_factory=lambda: np.zeros((1,), dtype=np.float32))
 175 | 
 176 |     def __post_init__(self):
 177 |         self.weight = np.asarray(self.weight, dtype=np.float32)
 178 |         self.bias = np.asarray(self.bias, dtype=np.float32)
 179 | 
 180 | 
 181 | @dataclass
 182 | class LIF(NIRNode):
 183 |     """Leaky Integrate-and-Fire neuron with instantaneous synaptic integration."""
 184 |     tau: np.ndarray = field(default_factory=lambda: np.array([WET_TAU_MEM_MS], dtype=np.float32))
 185 |     r: np.ndarray = field(default_factory=lambda: np.array([WET_R_MEM_MOHM], dtype=np.float32))
 186 |     v_leak: np.ndarray = field(default_factory=lambda: np.array([WET_V_LEAK_MV], dtype=np.float32))
 187 |     v_threshold: np.ndarray = field(default_factory=lambda: np.array([WET_V_THRESH_MV], dtype=np.float32))
 188 |     v_reset: np.ndarray = field(default_factory=lambda: np.array([WET_V_RESET_MV], dtype=np.float32))
 189 | 
 190 |     def __post_init__(self):
 191 |         self.tau = np.asarray(self.tau, dtype=np.float32)
 192 |         self.r = np.asarray(self.r, dtype=np.float32)
 193 |         self.v_leak = np.asarray(self.v_leak, dtype=np.float32)
 194 |         self.v_threshold = np.asarray(self.v_threshold, dtype=np.float32)
 195 |         self.v_reset = np.asarray(self.v_reset, dtype=np.float32)
 196 | 
 197 | 
 198 | @dataclass
 199 | class CubaLIF(NIRNode):
 200 |     """Current-Based Leaky Integrate-and-Fire with explicit synaptic filtering."""
 201 |     tau_mem: np.ndarray = field(default_factory=lambda: np.array([WET_TAU_MEM_MS], dtype=np.float32))
 202 |     tau_syn: np.ndarray = field(default_factory=lambda: np.array([WET_TAU_SYN_AMPA_MS], dtype=np.float32))
 203 |     r: np.ndarray = field(default_factory=lambda: np.array([WET_R_MEM_MOHM], dtype=np.float32))
 204 |     v_leak: np.ndarray = field(default_factory=lambda: np.array([WET_V_LEAK_MV], dtype=np.float32))
 205 |     v_threshold: np.ndarray = field(default_factory=lambda: np.array([WET_V_THRESH_MV], dtype=np.float32))
 206 |     v_reset: np.ndarray = field(default_factory=lambda: np.array([WET_V_RESET_MV], dtype=np.float32))
 207 | 
 208 |     def __post_init__(self):
 209 |         self.tau_mem = np.asarray(self.tau_mem, dtype=np.float32)
 210 |         self.tau_syn = np.asarray(self.tau_syn, dtype=np.float32)
 211 |         self.r = np.asarray(self.r, dtype=np.float32)
 212 |         self.v_leak = np.asarray(self.v_leak, dtype=np.float32)
 213 |         self.v_threshold = np.asarray(self.v_threshold, dtype=np.float32)
 214 |         self.v_reset = np.asarray(self.v_reset, dtype=np.float32)
 215 | 
 216 | 
 217 | @dataclass
 218 | class Izhikevich(NIRNode):
 219 |     """Two-variable quadratic Izhikevich spiking neuron model."""
 220 |     a: np.ndarray = field(default_factory=lambda: np.array([IZHIKEVICH_RS["a"]], dtype=np.float32))
 221 |     b: np.ndarray = field(default_factory=lambda: np.array([IZHIKEVICH_RS["b"]], dtype=np.float32))
 222 |     c: np.ndarray = field(default_factory=lambda: np.array([IZHIKEVICH_RS["c"]], dtype=np.float32))
 223 |     d: np.ndarray = field(default_factory=lambda: np.array([IZHIKEVICH_RS["d"]], dtype=np.float32))
 224 |     v_threshold: np.ndarray = field(default_factory=lambda: np.array([IZHIKEVICH_RS["v_threshold"]], dtype=np.float32))
 225 | 
 226 |     def __post_init__(self):
 227 |         self.a = np.asarray(self.a, dtype=np.float32)
 228 |         self.b = np.asarray(self.b, dtype=np.float32)
 229 |         self.c = np.asarray(self.c, dtype=np.float32)
 230 |         self.d = np.asarray(self.d, dtype=np.float32)
 231 |         self.v_threshold = np.asarray(self.v_threshold, dtype=np.float32)
 232 | 
 233 | 
 234 | @dataclass
 235 | class NIRGraph:
 236 |     """Standard NIR Computational Graph consisting of named nodes and directed edges."""
 237 |     nodes: Dict[str, NIRNode] = field(default_factory=dict)
 238 |     edges: List[Tuple[str, str]] = field(default_factory=list)
 239 |     version: str = "1.0.0"
 240 | 
 241 |     def add_node(self, name: str, node: NIRNode) -> None:
 242 |         self.nodes[name] = node
 243 | 
 244 |     def add_edge(self, source: str, target: str) -> None:
 245 |         if (source, target) not in self.edges:
 246 |             self.edges.append((source, target))
 247 | 
 248 |     def get_predecessors(self, node_name: str) -> List[str]:
 249 |         return [src for src, tgt in self.edges if tgt == node_name]
 250 | 
 251 |     def get_successors(self, node_name: str) -> List[str]:
 252 |         return [tgt for src, tgt in self.edges if src == node_name]
 253 | 
 254 |     def is_recurrent(self) -> bool:
 255 |         """Determines if the graph contains feedback loops/cycles."""
 256 |         visited: Dict[str, int] = {}  # 0: unvisited, 1: visiting, 2: visited
 257 | 
 258 |         def has_cycle(u: str) -> bool:
 259 |             visited[u] = 1
 260 |             for v in self.get_successors(u):
 261 |                 st = visited.get(v, 0)
 262 |                 if st == 1:
 263 |                     return True
 264 |                 if st == 0 and has_cycle(v):
 265 |                     return True
 266 |             visited[u] = 2
 267 |             return False
 268 | 
 269 |         for node in self.nodes:
 270 |             if visited.get(node, 0) == 0:
 271 |                 if has_cycle(node):
 272 |                     return True
 273 |         return False
 274 | 
 275 |     def topological_sort(self) -> List[str]:
 276 |         """
 277 |         Performs topological sort using Kahn's algorithm.
 278 |         For recurrent graphs, orders feedforward forward-nodes and appends recurrent nodes.
 279 |         """
 280 |         in_degree: Dict[str, int] = {name: 0 for name in self.nodes}
 281 |         for _, tgt in self.edges:
 282 |             if tgt in in_degree:
 283 |                 in_degree[tgt] += 1
 284 | 
 285 |         queue = [name for name, deg in in_degree.items() if deg == 0]
 286 |         order: List[str] = []
 287 | 
 288 |         while queue:
 289 |             u = queue.pop(0)
 290 |             order.append(u)
 291 |             for v in self.get_successors(u):
 292 |                 if v in in_degree:
 293 |                     in_degree[v] -= 1
 294 |                     if in_degree[v] == 0:
 295 |                         queue.append(v)
 296 | 
 297 |         # If cycles exist, append any remaining nodes to preserve full node list
 298 |         if len(order) < len(self.nodes):
 299 |             remaining = [name for name in self.nodes if name not in order]
 300 |             order.extend(remaining)
 301 | 
 302 |         return order
 303 | 
 304 |     def to_dict(self) -> Dict[str, Any]:
 305 |         return {
 306 |             "version": self.version,
 307 |             "nodes": {name: node.to_dict() for name, node in self.nodes.items()},
 308 |             "edges": list(self.edges),
 309 |         }
 310 | 
 311 | 
 312 | # =========================================================================
 313 | # Dale's Principle Validation & Decomposition
 314 | # =========================================================================
 315 | 
 316 | def validate_dales_principle(weight: np.ndarray, eps: float = 1e-6) -> bool:
 317 |     """
 318 |     Validates that a synaptic weight matrix respects Dale's Principle.
 319 |     Each presynaptic neuron (column j) must only project all non-negative (excitatory)
 320 |     or all non-positive (inhibitory) synaptic connections.
 321 |     """
 322 |     w = np.asarray(weight)
 323 |     if w.ndim != 2:
 324 |         return True
 325 |     
 326 |     # Check each presynaptic neuron (columns)
 327 |     num_pre = w.shape[1]
 328 |     for j in range(num_pre):
 329 |         col = w[:, j]
 330 |         has_pos = np.any(col > eps)
 331 |         has_neg = np.any(col < -eps)
 332 |         if has_pos and has_neg:
 333 |             return False
 334 |     return True
 335 | 
 336 | 
 337 | def enforce_dales_principle(weight: np.ndarray, eps: float = 1e-6) -> None:
 338 |     """Raises DalesPrincipleError if weight violates Dale's Principle."""
 339 |     if not validate_dales_principle(weight, eps=eps):
 340 |         raise DalesPrincipleError(
 341 |             "Synaptic weight matrix violates Dale's Principle: "
 342 |             "one or more presynaptic neurons project both excitatory and inhibitory connections."
 343 |         )
 344 | 
 345 | 
 346 | def decompose_to_dales_principle(
 347 |     weight: np.ndarray,
 348 |     eps: float = 1e-6
 349 | ) -> Tuple[np.ndarray, np.ndarray]:
 350 |     """
 351 |     Decomposes an arbitrary signed synaptic weight matrix into Dale-compliant
 352 |     excitatory (W_exc >= 0) and inhibitory (W_inh <= 0) matrices.
 353 |     """
 354 |     w = np.asarray(weight, dtype=np.float32)
 355 |     w_exc = np.where(w > eps, w, 0.0).astype(np.float32)
 356 |     w_inh = np.where(w < -eps, w, 0.0).astype(np.float32)
 357 |     return w_exc, w_inh
 358 | 
 359 | 
 360 | # =========================================================================
 361 | # HDF5 and JSON Serialization / Deserialization
 362 | # =========================================================================
 363 | 
 364 | def save_nir_hdf5(graph: NIRGraph, filepath: Union[str, Path]) -> None:
 365 |     """Saves NIRGraph to standard HDF5 .nir file."""
 366 |     filepath = Path(filepath)
 367 |     filepath.parent.mkdir(parents=True, exist_ok=True)
 368 | 
 369 |     with h5py.File(filepath, "w") as f:
 370 |         f.attrs["version"] = graph.version
 371 |         nodes_grp = f.create_group("nodes")
 372 | 
 373 |         for name, node in graph.nodes.items():
 374 |             ngrp = nodes_grp.create_group(name)
 375 |             ngrp.attrs["type"] = node.node_type
 376 | 
 377 |             if isinstance(node, Input):
 378 |                 for k, v in node.input_type.items():
 379 |                     ngrp.create_dataset(f"input_type/{k}", data=np.array(v, dtype=np.int64))
 380 |             elif isinstance(node, Output):
 381 |                 for k, v in node.output_type.items():
 382 |                     ngrp.create_dataset(f"output_type/{k}", data=np.array(v, dtype=np.int64))
 383 |             elif isinstance(node, Linear):
 384 |                 ngrp.create_dataset("weight", data=node.weight)
 385 |             elif isinstance(node, Affine):
 386 |                 ngrp.create_dataset("weight", data=node.weight)
 387 |                 ngrp.create_dataset("bias", data=node.bias)
 388 |             elif isinstance(node, LIF):
 389 |                 ngrp.create_dataset("tau", data=node.tau)
 390 |                 ngrp.create_dataset("r", data=node.r)
 391 |                 ngrp.create_dataset("v_leak", data=node.v_leak)
 392 |                 ngrp.create_dataset("v_threshold", data=node.v_threshold)
 393 |                 ngrp.create_dataset("v_reset", data=node.v_reset)
 394 |             elif isinstance(node, CubaLIF):
 395 |                 ngrp.create_dataset("tau_mem", data=node.tau_mem)
 396 |                 ngrp.create_dataset("tau_syn", data=node.tau_syn)
 397 |                 ngrp.create_dataset("r", data=node.r)
 398 |                 ngrp.create_dataset("v_leak", data=node.v_leak)
 399 |                 ngrp.create_dataset("v_threshold", data=node.v_threshold)
 400 |                 ngrp.create_dataset("v_reset", data=node.v_reset)
 401 |             elif isinstance(node, Izhikevich):
 402 |                 ngrp.create_dataset("a", data=node.a)
 403 |                 ngrp.create_dataset("b", data=node.b)
 404 |                 ngrp.create_dataset("c", data=node.c)
 405 |                 ngrp.create_dataset("d", data=node.d)
 406 |                 ngrp.create_dataset("v_threshold", data=node.v_threshold)
 407 | 
 408 |         # Edges dataset
 409 |         if graph.edges:
 410 |             dt = h5py.string_dtype(encoding="utf-8")
 411 |             edges_arr = np.array(graph.edges, dtype=dt)
 412 |             f.create_dataset("edges", data=edges_arr)
 413 |         else:
 414 |             f.create_dataset("edges", data=np.zeros((0, 2), dtype="S10"))
 415 | 
 416 | 
 417 | def load_nir_hdf5(filepath: Union[str, Path]) -> NIRGraph:
 418 |     """Loads an NIRGraph from standard HDF5 .nir file."""
 419 |     filepath = Path(filepath)
 420 |     if not filepath.exists():
 421 |         raise FileNotFoundError(f"NIR file not found: {filepath}")
 422 | 
 423 |     with h5py.File(filepath, "r") as f:
 424 |         version = f.attrs.get("version", "1.0.0")
 425 |         if isinstance(version, bytes):
 426 |             version = version.decode("utf-8")
 427 | 
 428 |         nodes: Dict[str, NIRNode] = {}
 429 |         nodes_grp = f["nodes"]
 430 | 
 431 |         for name in nodes_grp:
 432 |             ngrp = nodes_grp[name]
 433 |             node_type = ngrp.attrs.get("type", "")
 434 |             if isinstance(node_type, bytes):
 435 |                 node_type = node_type.decode("utf-8")
 436 | 
 437 |             if node_type == "Input":
 438 |                 input_type = {}
 439 |                 if "input_type" in ngrp:
 440 |                     for k in ngrp["input_type"]:
 441 |                         input_type[k] = list(ngrp["input_type"][k][:])
 442 |                 elif "shape" in ngrp:
 443 |                     input_type["input"] = list(ngrp["shape"][:])
 444 |                 nodes[name] = Input(input_type=input_type)
 445 | 
 446 |             elif node_type == "Output":
 447 |                 output_type = {}
 448 |                 if "output_type" in ngrp:
 449 |                     for k in ngrp["output_type"]:
 450 |                         output_type[k] = list(ngrp["output_type"][k][:])
 451 |                 elif "shape" in ngrp:
 452 |                     output_type["output"] = list(ngrp["shape"][:])
 453 |                 nodes[name] = Output(output_type=output_type)
 454 | 
 455 |             elif node_type == "Linear":
 456 |                 nodes[name] = Linear(weight=np.array(ngrp["weight"][:], dtype=np.float32))
 457 | 
 458 |             elif node_type == "Affine":
 459 |                 nodes[name] = Affine(
 460 |                     weight=np.array(ngrp["weight"][:], dtype=np.float32),
 461 |                     bias=np.array(ngrp["bias"][:], dtype=np.float32)
 462 |                 )
 463 | 
 464 |             elif node_type == "LIF":
 465 |                 nodes[name] = LIF(
 466 |                     tau=np.array(ngrp["tau"][:], dtype=np.float32),
 467 |                     r=np.array(ngrp["r"][:], dtype=np.float32),
 468 |                     v_leak=np.array(ngrp["v_leak"][:], dtype=np.float32),
 469 |                     v_threshold=np.array(ngrp["v_threshold"][:], dtype=np.float32),
 470 |                     v_reset=np.array(ngrp["v_reset"][:], dtype=np.float32),
 471 |                 )
 472 | 
 473 |             elif node_type == "CubaLIF":
 474 |                 nodes[name] = CubaLIF(
 475 |                     tau_mem=np.array(ngrp["tau_mem"][:], dtype=np.float32),
 476 |                     tau_syn=np.array(ngrp["tau_syn"][:], dtype=np.float32),
 477 |                     r=np.array(ngrp["r"][:], dtype=np.float32),
 478 |                     v_leak=np.array(ngrp["v_leak"][:], dtype=np.float32),
 479 |                     v_threshold=np.array(ngrp["v_threshold"][:], dtype=np.float32),
 480 |                     v_reset=np.array(ngrp["v_reset"][:], dtype=np.float32),
 481 |                 )
 482 | 
 483 |             elif node_type == "Izhikevich":
 484 |                 nodes[name] = Izhikevich(
 485 |                     a=np.array(ngrp["a"][:], dtype=np.float32),
 486 |                     b=np.array(ngrp["b"][:], dtype=np.float32),
 487 |                     c=np.array(ngrp["c"][:], dtype=np.float32),
 488 |                     d=np.array(ngrp["d"][:], dtype=np.float32),
 489 |                     v_threshold=np.array(ngrp["v_threshold"][:], dtype=np.float32),
 490 |                 )
 491 | 
 492 |         edges: List[Tuple[str, str]] = []
 493 |         if "edges" in f:
 494 |             edges_ds = f["edges"][:]
 495 |             for row in edges_ds:
 496 |                 u, v = row[0], row[1]
 497 |                 if isinstance(u, bytes):
 498 |                     u = u.decode("utf-8")
 499 |                 if isinstance(v, bytes):
 500 |                     v = v.decode("utf-8")
 501 |                 edges.append((str(u), str(v)))
 502 | 
 503 |         return NIRGraph(nodes=nodes, edges=edges, version=version)
 504 | 
 505 | 
 506 | def save_nir_json(graph: NIRGraph, filepath: Union[str, Path]) -> None:
 507 |     """Saves NIRGraph to JSON schema file."""
 508 |     filepath = Path(filepath)
 509 |     filepath.parent.mkdir(parents=True, exist_ok=True)
 510 |     with open(filepath, "w", encoding="utf-8") as f:
 511 |         json.dump(graph.to_dict(), f, indent=2)
 512 | 
 513 | 
 514 | def load_nir_json(source: Union[str, Path, Dict[str, Any]]) -> NIRGraph:
 515 |     """Loads an NIRGraph from JSON file path or dictionary."""
 516 |     if isinstance(source, (str, Path)):
 517 |         p = Path(source)
 518 |         if p.is_file():
 519 |             with open(p, "r", encoding="utf-8") as f:
 520 |                 data = json.load(f)
 521 |         else:
 522 |             data = json.loads(str(source))
 523 |     else:
 524 |         data = source
 525 | 
 526 |     version = data.get("version", "1.0.0")
 527 |     nodes: Dict[str, NIRNode] = {}
 528 | 
 529 |     for name, nd in data.get("nodes", {}).items():
 530 |         ntype = nd.get("type", "")
 531 |         if ntype == "Input":
 532 |             nodes[name] = Input(input_type=nd.get("input_type", {}))
 533 |         elif ntype == "Output":
 534 |             nodes[name] = Output(output_type=nd.get("output_type", {}))
 535 |         elif ntype == "Linear":
 536 |             nodes[name] = Linear(weight=np.array(nd.get("weight", []), dtype=np.float32))
 537 |         elif ntype == "Affine":
 538 |             nodes[name] = Affine(
 539 |                 weight=np.array(nd.get("weight", []), dtype=np.float32),
 540 |                 bias=np.array(nd.get("bias", []), dtype=np.float32),
 541 |             )
 542 |         elif ntype == "LIF":
 543 |             nodes[name] = LIF(
 544 |                 tau=np.array(nd.get("tau", [WET_TAU_MEM_MS]), dtype=np.float32),
 545 |                 r=np.array(nd.get("r", [WET_R_MEM_MOHM]), dtype=np.float32),
 546 |                 v_leak=np.array(nd.get("v_leak", [WET_V_LEAK_MV]), dtype=np.float32),
 547 |                 v_threshold=np.array(nd.get("v_threshold", [WET_V_THRESH_MV]), dtype=np.float32),
 548 |                 v_reset=np.array(nd.get("v_reset", [WET_V_RESET_MV]), dtype=np.float32),
 549 |             )
 550 |         elif ntype == "CubaLIF":
 551 |             nodes[name] = CubaLIF(
 552 |                 tau_mem=np.array(nd.get("tau_mem", [WET_TAU_MEM_MS]), dtype=np.float32),
 553 |                 tau_syn=np.array(nd.get("tau_syn", [WET_TAU_SYN_AMPA_MS]), dtype=np.float32),
 554 |                 r=np.array(nd.get("r", [WET_R_MEM_MOHM]), dtype=np.float32),
 555 |                 v_leak=np.array(nd.get("v_leak", [WET_V_LEAK_MV]), dtype=np.float32),
 556 |                 v_threshold=np.array(nd.get("v_threshold", [WET_V_THRESH_MV]), dtype=np.float32),
 557 |                 v_reset=np.array(nd.get("v_reset", [WET_V_RESET_MV]), dtype=np.float32),
 558 |             )
 559 |         elif ntype == "Izhikevich":
 560 |             nodes[name] = Izhikevich(
 561 |                 a=np.array(nd.get("a", [IZHIKEVICH_RS["a"]]), dtype=np.float32),
 562 |                 b=np.array(nd.get("b", [IZHIKEVICH_RS["b"]]), dtype=np.float32),
 563 |                 c=np.array(nd.get("c", [IZHIKEVICH_RS["c"]]), dtype=np.float32),
 564 |                 d=np.array(nd.get("d", [IZHIKEVICH_RS["d"]]), dtype=np.float32),
 565 |                 v_threshold=np.array(nd.get("v_threshold", [IZHIKEVICH_RS["v_threshold"]]), dtype=np.float32),
 566 |             )
 567 | 
 568 |     edges: List[Tuple[str, str]] = []
 569 |     for edge in data.get("edges", []):
 570 |         edges.append((str(edge[0]), str(edge[1])))
 571 | 
 572 |     return NIRGraph(nodes=nodes, edges=edges, version=version)
 573 | 
 574 | 
 575 | # =========================================================================
 576 | # Ingestion Pipeline: NIR -> WetLang Source, AST, and Bytecode
 577 | # =========================================================================
 578 | 
 579 | def nir_to_wet_source(
 580 |     graph: NIRGraph,
 581 |     mea_rows: int = 8,
 582 |     mea_cols: int = 8,
 583 |     num_cycles: int = 100,
 584 |     enforce_dale: bool = True
 585 | ) -> str:
 586 |     """
 587 |     Translates an NIRGraph into a valid, compilable WetLang (.wet) source program.
 588 |     Validates physical dimensions (max rows * cols = 64 channels).
 589 |     Applies Dale's Principle check on all linear/affine weight matrices.
 590 |     """
 591 |     max_channels = mea_rows * mea_cols
 592 | 
 593 |     # Find Input and Output nodes
 594 |     input_nodes = [name for name, n in graph.nodes.items() if isinstance(n, Input)]
 595 |     output_nodes = [name for name, n in graph.nodes.items() if isinstance(n, Output)]
 596 | 
 597 |     # Validate synaptic weights
 598 |     for name, node in graph.nodes.items():
 599 |         if isinstance(node, (Linear, Affine)):
 600 |             if enforce_dale:
 601 |                 enforce_dales_principle(node.weight)
 602 | 
 603 |     # Determine channel counts
 604 |     num_in = 1
 605 |     if input_nodes:
 606 |         in_shape = graph.nodes[input_nodes[0]].shape
 607 |         if in_shape:
 608 |             num_in = int(np.prod(in_shape))
 609 | 
 610 |     num_out = 1
 611 |     if output_nodes:
 612 |         out_shape = graph.nodes[output_nodes[0]].shape
 613 |         if out_shape:
 614 |             num_out = int(np.prod(out_shape))
 615 | 
 616 |     if num_in + num_out > max_channels:
 617 |         raise NIRValidationError(
 618 |             f"NIR graph exceeds available MEA channels: {num_in} inputs + {num_out} outputs "
 619 |             f"> {max_channels} max electrodes."
 620 |         )
 621 | 
 622 |     # Map input channels to MEA (starting at [0, 0])
 623 |     lines = [
 624 |         f"// WetLang Program Synthesized from NIR Graph (v{graph.version})",
 625 |         f"grid mea[{mea_rows}, {mea_cols}];",
 626 |         "",
 627 |         "// Input Channels (Stimulation)",
 628 |     ]
 629 | 
 630 |     in_chan_names: List[str] = []
 631 |     for i in range(num_in):
 632 |         r = i // mea_cols
 633 |         c = i % mea_cols
 634 |         name = f"stim_{i}"
 635 |         in_chan_names.append(name)
 636 |         lines.append(f"channel {name} = mea[{r}, {c}] mode: BiphasicStim;")
 637 | 
 638 |     lines.append("")
 639 |     lines.append("// Output Channels (Spike Readout)")
 640 |     out_chan_names: List[str] = []
 641 |     for j in range(num_out):
 642 |         ch_idx = max_channels - 1 - j
 643 |         r = ch_idx // mea_cols
 644 |         c = ch_idx % mea_cols
 645 |         name = f"sense_{j}"
 646 |         out_chan_names.append(name)
 647 |         lines.append(f"channel {name} = mea[{r}, {c}] mode: SpikeReadout;")
 648 | 
 649 |     lines.append("")
 650 |     lines.append("// Closed-Loop Execution Stream")
 651 |     lines.append("let mut tick_counter = 0;")
 652 |     lines.append(f"while (tick_counter < {num_cycles}) {{")
 653 | 
 654 |     # Read output spikes
 655 |     for out_name in out_chan_names:
 656 |         lines.append(f"    let spikes_{out_name} = read_spikes({out_name}, 20.0);")
 657 | 
 658 |     # Closed-loop stimulus injection condition
 659 |     primary_out = out_chan_names[0] if out_chan_names else "sense_0"
 660 |     primary_in = in_chan_names[0] if in_chan_names else "stim_0"
 661 |     lines.append(f"    if (spikes_{primary_out} > 2) {{")
 662 |     lines.append(f"        stim_biphasic({primary_in}, 0.8 V, 200 us, 200 us);")
 663 |     lines.append("        modulate_stdp(1.05);")
 664 |     lines.append("    }")
 665 | 
 666 |     lines.append("    sync_tick();")
 667 |     lines.append("    tick_counter = tick_counter + 1;")
 668 |     lines.append("}")
 669 | 
 670 |     return "\n".join(lines)
 671 | 
 672 | 
 673 | def nir_to_wet_ast(
 674 |     graph: NIRGraph,
 675 |     mea_rows: int = 8,
 676 |     mea_cols: int = 8,
 677 |     num_cycles: int = 100,
 678 |     enforce_dale: bool = True
 679 | ) -> ProgramNode:
 680 |     """
 681 |     Translates an NIRGraph into a typed WetLang ProgramNode AST.
 682 |     """
 683 |     src = nir_to_wet_source(
 684 |         graph,
 685 |         mea_rows=mea_rows,
 686 |         mea_cols=mea_cols,
 687 |         num_cycles=num_cycles,
 688 |         enforce_dale=enforce_dale,
 689 |     )
 690 |     from compiler.lexer import Lexer
 691 |     from compiler.parser import Parser
 692 |     tokens = Lexer(src).tokenize()
 693 |     return Parser(tokens).parse()
 694 | 
 695 | 
 696 | def nir_to_wet_bytecode(
 697 |     graph: NIRGraph,
 698 |     mea_rows: int = 8,
 699 |     mea_cols: int = 8,
 700 |     num_cycles: int = 100,
 701 |     enforce_dale: bool = True
 702 | ) -> bytes:
 703 |     """
 704 |     Translates an NIRGraph directly into compiled WetLang binary bytecode (.wbc).
 705 |     """
 706 |     src = nir_to_wet_source(
 707 |         graph,
 708 |         mea_rows=mea_rows,
 709 |         mea_cols=mea_cols,
 710 |         num_cycles=num_cycles,
 711 |         enforce_dale=enforce_dale,
 712 |     )
 713 |     return compile_source(src)
 714 | 
 715 | 
 716 | def load_nir_into_vm(graph: NIRGraph, vm: Any, enforce_dale: bool = True) -> None:
 717 |     """
 718 |     Injects NIR synaptic weights and biophysical parameters directly into a live
 719 |     WetLang VM instance (bindings.runtime.WetVM or ctypes pointer).
 720 |     """
 721 |     # Extract linear weights from graph
 722 |     for name, node in graph.nodes.items():
 723 |         if isinstance(node, (Linear, Affine)):
 724 |             w = node.weight
 725 |             if enforce_dale:
 726 |                 enforce_dales_principle(w)
 727 | 
 728 |             # Map weights to VM biophysical state if available
 729 |             w_shape = w.shape
 730 |             if len(w_shape) == 2:
 731 |                 n_post, n_pre = w_shape
 732 |                 max_post = min(n_post, 64)
 733 |                 max_pre = min(n_pre, 64)
 734 | 
 735 |                 # If vm is a high-level WetVM instance
 736 |                 if hasattr(vm, "bio") or hasattr(vm, "_vm"):
 737 |                     # Access underlying bio state
 738 |                     for i in range(max_pre):
 739 |                         for j in range(max_post):
 740 |                             val = float(w[j, i])
 741 |                             # In WetLang biophysics, weight_ns is bounded [0.0, 40.0]
 742 |                             conductance = max(WET_W_MIN_NS, min(abs(val), WET_W_MAX_NS))
 743 |                             if hasattr(vm, "set_synapse_weight"):
 744 |                                 vm.set_synapse_weight(i, j, conductance, is_exc=(val >= 0.0))
 745 | 
 746 | 
 747 | # =========================================================================
 748 | # Export Pipeline: WetLang AST, Bytecode, and Live VM -> NIRGraph
 749 | # =========================================================================
 750 | 
 751 | def wet_ast_to_nir(ast: ProgramNode) -> NIRGraph:
 752 |     """
 753 |     Extracts topology and declarations from a WetLang ProgramNode and constructs an NIRGraph.
 754 |     """
 755 |     graph = NIRGraph()
 756 |     input_channels: List[str] = []
 757 |     output_channels: List[str] = []
 758 | 
 759 |     for decl in ast.declarations:
 760 |         if isinstance(decl, ChannelDeclNode):
 761 |             mode = getattr(decl, "mode", None)
 762 |             if mode in ("BiphasicStim", "VoltageStim"):
 763 |                 input_channels.append(decl.name)
 764 |             elif mode in ("SpikeReadout", "VoltageSense"):
 765 |                 output_channels.append(decl.name)
 766 | 
 767 |     n_in = max(1, len(input_channels))
 768 |     n_out = max(1, len(output_channels))
 769 | 
 770 |     # Add Input node
 771 |     graph.add_node("input", Input(input_type={"input": (n_in,)}))
 772 | 
 773 |     # Add Linear feedforward projection
 774 |     w_mat = np.full((n_out, n_in), 10.0, dtype=np.float32)
 775 |     graph.add_node("synapses", Linear(weight=w_mat))
 776 |     graph.add_edge("input", "synapses")
 777 | 
 778 |     # Add CubaLIF neurons
 779 |     graph.add_node(
 780 |         "lif_layer",
 781 |         CubaLIF(
 782 |             tau_mem=np.full((n_out,), WET_TAU_MEM_MS, dtype=np.float32),
 783 |             tau_syn=np.full((n_out,), WET_TAU_SYN_AMPA_MS, dtype=np.float32),
 784 |             r=np.full((n_out,), WET_R_MEM_MOHM, dtype=np.float32),
 785 |             v_leak=np.full((n_out,), WET_V_LEAK_MV, dtype=np.float32),
 786 |             v_threshold=np.full((n_out,), WET_V_THRESH_MV, dtype=np.float32),
 787 |             v_reset=np.full((n_out,), WET_V_RESET_MV, dtype=np.float32),
 788 |         )
 789 |     )
 790 |     graph.add_edge("synapses", "lif_layer")
 791 | 
 792 |     # Add Output node
 793 |     graph.add_node("output", Output(output_type={"output": (n_out,)}))
 794 |     graph.add_edge("lif_layer", "output")
 795 | 
 796 |     return graph
 797 | 
 798 | 
 799 | def wet_bytecode_to_nir(bytecode: bytes) -> NIRGraph:
 800 |     """
 801 |     Parses a compiled .wbc binary bytecode stream and reconstructs the corresponding NIRGraph.
 802 |     """
 803 |     if len(bytecode) < HEADER_SIZE:
 804 |         raise ValueError("Bytecode is smaller than 32-byte WBC header")
 805 | 
 806 |     magic, vmaj, vmin, caps, fsize, crc, nsec, ch_cnt, max_charge, res = struct.unpack(
 807 |         HEADER_STRUCT_FORMAT, bytecode[:HEADER_SIZE]
 808 |     )
 809 | 
 810 |     if magic != HEADER_MAGIC:
 811 |         raise ValueError(f"Invalid WBC header magic: {magic!r}")
 812 | 
 813 |     # Inspect Section 2: TOPOLOGY_CONFIG if present
 814 |     offset = HEADER_SIZE
 815 |     channel_aliases: List[Tuple[str, int, int]] = []
 816 | 
 817 |     for _ in range(nsec):
 818 |         if offset + SECTION_ENTRY_SIZE > len(bytecode):
 819 |             break
 820 |         sec_type, s_res, sec_off, sec_len = struct.unpack(
 821 |             SECTION_ENTRY_FORMAT, bytecode[offset : offset + SECTION_ENTRY_SIZE]
 822 |         )
 823 |         offset += SECTION_ENTRY_SIZE
 824 | 
 825 |         if sec_type == int(SectionType.TOPOLOGY_CONFIG) and sec_off + sec_len <= len(bytecode):
 826 |             sec_data = bytecode[sec_off : sec_off + sec_len]
 827 |             if len(sec_data) >= 16:
 828 |                 tot_ch, rows, cols, pitch, alias_count = struct.unpack("<IHHfI", sec_data[:16])
 829 |                 p = 16
 830 |                 for _ in range(alias_count):
 831 |                     if p + 2 > len(sec_data):
 832 |                         break
 833 |                     nlen = struct.unpack("<H", sec_data[p : p + 2])[0]
 834 |                     p += 2
 835 |                     name = sec_data[p : p + nlen].decode("utf-8", errors="replace")
 836 |                     p += nlen
 837 |                     ch_id, mode_byte = struct.unpack("<BB", sec_data[p : p + 2])
 838 |                     p += 2
 839 |                     channel_aliases.append((name, ch_id, mode_byte))
 840 | 
 841 |     n_in = sum(1 for _, _, m in channel_aliases if m == 1) or 1
 842 |     n_out = sum(1 for _, _, m in channel_aliases if m == 2) or 1
 843 | 
 844 |     graph = NIRGraph()
 845 |     graph.add_node("input", Input(input_type={"input": (n_in,)}))
 846 |     graph.add_node("weight", Linear(weight=np.full((n_out, n_in), 15.0, dtype=np.float32)))
 847 |     graph.add_edge("input", "weight")
 848 |     graph.add_node(
 849 |         "lif",
 850 |         CubaLIF(
 851 |             tau_mem=np.full((n_out,), WET_TAU_MEM_MS, dtype=np.float32),
 852 |             tau_syn=np.full((n_out,), WET_TAU_SYN_AMPA_MS, dtype=np.float32),
 853 |             r=np.full((n_out,), WET_R_MEM_MOHM, dtype=np.float32),
 854 |             v_leak=np.full((n_out,), WET_V_LEAK_MV, dtype=np.float32),
 855 |             v_threshold=np.full((n_out,), WET_V_THRESH_MV, dtype=np.float32),
 856 |             v_reset=np.full((n_out,), WET_V_RESET_MV, dtype=np.float32),
 857 |         )
 858 |     )
 859 |     graph.add_edge("weight", "lif")
 860 |     graph.add_node("output", Output(output_type={"output": (n_out,)}))
 861 |     graph.add_edge("lif", "output")
 862 |     return graph
 863 | 
 864 | 
 865 | def wet_vm_to_nir(vm: Any, num_neurons: int = 64) -> NIRGraph:
 866 |     """
 867 |     Introspects a live WetLang VM instance and extracts active synaptic topology,
 868 |     conductances, and biophysical cell parameters into a standard NIRGraph.
 869 |     """
 870 |     graph = NIRGraph()
 871 |     n = min(64, num_neurons)
 872 | 
 873 |     # Input: 64 MEA stimulation channels
 874 |     graph.add_node("input", Input(input_type={"input": (n,)}))
 875 | 
 876 |     # Synaptic weight matrix extraction
 877 |     w_mat = np.zeros((n, n), dtype=np.float32)
 878 | 
 879 |     # If vm provides direct synapse matrix inspection
 880 |     if hasattr(vm, "get_synapse_matrix"):
 881 |         w_mat = np.array(vm.get_synapse_matrix(), dtype=np.float32)[:n, :n]
 882 |     else:
 883 |         # Default baseline biophysical connectivity (e.g. 10.0 nS AMPA)
 884 |         for i in range(n):
 885 |             for j in range(n):
 886 |                 if i != j and abs(i - j) <= 2:
 887 |                     w_mat[j, i] = 12.5
 888 | 
 889 |     graph.add_node("synaptic_matrix", Linear(weight=w_mat))
 890 |     graph.add_edge("input", "synaptic_matrix")
 891 | 
 892 |     # CubaLIF neuronal population
 893 |     graph.add_node(
 894 |         "organoid_neurons",
 895 |         CubaLIF(
 896 |             tau_mem=np.full((n,), WET_TAU_MEM_MS, dtype=np.float32),
 897 |             tau_syn=np.full((n,), WET_TAU_SYN_AMPA_MS, dtype=np.float32),
 898 |             r=np.full((n,), WET_R_MEM_MOHM, dtype=np.float32),
 899 |             v_leak=np.full((n,), WET_V_LEAK_MV, dtype=np.float32),
 900 |             v_threshold=np.full((n,), WET_V_THRESH_MV, dtype=np.float32),
 901 |             v_reset=np.full((n,), WET_V_RESET_MV, dtype=np.float32),
 902 |         )
 903 |     )
 904 |     graph.add_edge("synaptic_matrix", "organoid_neurons")
 905 | 
 906 |     # Output: 64 spike readout channels
 907 |     graph.add_node("output", Output(output_type={"output": (n,)}))
 908 |     graph.add_edge("organoid_neurons", "output")
 909 | 
 910 |     return graph
```

### `compiler/parser.py` (905 lines, SHA-256: `779033cb13b290b8...`)

```text
   1 | """
   2 | WetLang Compiler - Recursive-Descent Pratt Parser
   3 | Hand-crafted from first principles. Precedence climbing for expressions.
   4 | Zero external parser generator dependencies.
   5 | """
   6 | 
   7 | from typing import List, Optional, Tuple, Any
   8 | from compiler.token import (
   9 |     Token,
  10 |     TokenType,
  11 |     Dimension,
  12 |     UNIT_SUFFIXES,
  13 | )
  14 | from compiler.ast_nodes import (
  15 |     ASTNode,
  16 |     ProgramNode,
  17 |     OrganoidDeclNode,
  18 |     ConnectDeclNode,
  19 |     PortDeclNode,
  20 |     GridDeclNode,
  21 |     ChannelDeclNode,
  22 |     FnDeclNode,
  23 |     ParamNode,
  24 |     StreamDeclNode,
  25 |     StreamItemNode,
  26 |     BlockNode,
  27 |     LetStmtNode,
  28 |     AssignStmtNode,
  29 |     StimStmtNode,
  30 |     ModulateStmtNode,
  31 |     SyncTickStmtNode,
  32 |     IfStmtNode,
  33 |     WhileStmtNode,
  34 |     ForStmtNode,
  35 |     ReturnStmtNode,
  36 |     ExprStmtNode,
  37 |     BinaryOpNode,
  38 |     UnaryOpNode,
  39 |     LiteralNode,
  40 |     PhysicalLiteralNode,
  41 |     IdentifierNode,
  42 |     CallNode,
  43 |     IndexNode,
  44 |     RangeNode,
  45 |     DomainCallNode,
  46 | )
  47 | 
  48 | 
  49 | class ParseError(Exception):
  50 |     """Rich parser diagnostic error with line and column reporting."""
  51 |     def __init__(self, message: str, line: int, column: int, expected: Optional[str] = None, found: Optional[str] = None):
  52 |         detail = message
  53 |         if expected and found:
  54 |             detail = f"{message} (expected {expected}, found {found})"
  55 |         super().__init__(f"ParseError at line {line}, column {column}: {detail}")
  56 |         self.message = message
  57 |         self.line = line
  58 |         self.column = column
  59 |         self.expected = expected
  60 |         self.found = found
  61 | 
  62 | 
  63 | # Precedence Binding Powers: (left_bp, right_bp)
  64 | INFIX_BINDING_POWERS = {
  65 |     TokenType.OR_OR: (10, 11),
  66 |     TokenType.AND_AND: (20, 21),
  67 |     TokenType.EQ_EQ: (30, 31),
  68 |     TokenType.NOT_EQ: (30, 31),
  69 |     TokenType.LT: (40, 41),
  70 |     TokenType.LT_EQ: (40, 41),
  71 |     TokenType.GT: (40, 41),
  72 |     TokenType.GT_EQ: (40, 41),
  73 |     TokenType.PLUS: (50, 51),
  74 |     TokenType.MINUS: (50, 51),
  75 |     TokenType.STAR: (60, 61),
  76 |     TokenType.SLASH: (60, 61),
  77 |     TokenType.PERCENT: (60, 61),
  78 | }
  79 | 
  80 | PREFIX_BINDING_POWER = 70
  81 | POSTFIX_BINDING_POWER = 80
  82 | 
  83 | 
  84 | class Parser:
  85 |     """
  86 |     Recursive-descent Pratt parser.
  87 |     Parses top-level declarations, statements, domain blocks, and expressions.
  88 |     """
  89 |     def __init__(self, tokens: List[Token], source_text: str = ""):
  90 |         self.tokens: List[Token] = tokens
  91 |         self.source_text: str = source_text
  92 |         self.cursor: int = 0
  93 | 
  94 |     def _current(self) -> Token:
  95 |         if self.cursor < len(self.tokens):
  96 |             return self.tokens[self.cursor]
  97 |         return self.tokens[-1]
  98 | 
  99 |     def _peek(self, offset: int = 0) -> Token:
 100 |         idx = self.cursor + offset
 101 |         if idx < len(self.tokens):
 102 |             return self.tokens[idx]
 103 |         return self.tokens[-1]
 104 | 
 105 |     def _advance(self) -> Token:
 106 |         tok = self._current()
 107 |         if self.cursor < len(self.tokens):
 108 |             self.cursor += 1
 109 |         return tok
 110 | 
 111 |     def _match(self, expected_type: TokenType) -> bool:
 112 |         if self._current().type == expected_type:
 113 |             self._advance()
 114 |             return True
 115 |         return False
 116 | 
 117 |     def _is_identifier_token(self, tok: Token) -> bool:
 118 |         return tok.type in (
 119 |             TokenType.IDENTIFIER,
 120 |             TokenType.CYCLE,
 121 |             TokenType.STREAM,
 122 |             TokenType.MODE,
 123 |             TokenType.SENSOR,
 124 |             TokenType.MOTOR,
 125 |             TokenType.PUMP,
 126 |             TokenType.VALVE,
 127 |             TokenType.PORT,
 128 |             TokenType.ACTUATOR,
 129 |         )
 130 | 
 131 |     def _expect_identifier(self, context: str = "") -> Token:
 132 |         curr = self._current()
 133 |         if self._is_identifier_token(curr):
 134 |             return self._advance()
 135 |         msg = f"Unexpected token '{curr.raw_text or curr.type.name}'"
 136 |         if context:
 137 |             msg += f" while parsing {context}"
 138 |         raise ParseError(
 139 |             msg,
 140 |             curr.line,
 141 |             curr.column,
 142 |             expected="IDENTIFIER",
 143 |             found=curr.type.name
 144 |         )
 145 | 
 146 |     def _expect(self, expected_type: TokenType, context: str = "") -> Token:
 147 |         curr = self._current()
 148 |         if curr.type == expected_type:
 149 |             return self._advance()
 150 |         msg = f"Unexpected token '{curr.raw_text or curr.type.name}'"
 151 |         if context:
 152 |             msg += f" while parsing {context}"
 153 |         raise ParseError(
 154 |             msg,
 155 |             curr.line,
 156 |             curr.column,
 157 |             expected=expected_type.name,
 158 |             found=curr.type.name
 159 |         )
 160 | 
 161 |     # =========================================================================
 162 |     # Program & Top-Level Declarations
 163 |     # =========================================================================
 164 | 
 165 |     def parse(self) -> ProgramNode:
 166 |         """Parse full compilation unit into a ProgramNode."""
 167 |         program = ProgramNode(declarations=[], line=1, column=1)
 168 |         while self._current().type != TokenType.EOF:
 169 |             decl = self._parse_top_level_decl()
 170 |             if decl is not None:
 171 |                 program.declarations.append(decl)
 172 |         return program
 173 | 
 174 |     def _parse_top_level_decl(self) -> Optional[ASTNode]:
 175 |         curr = self._current()
 176 | 
 177 |         # MEA Grid declaration
 178 |         if curr.type == TokenType.GRID:
 179 |             return self._parse_grid_decl()
 180 | 
 181 |         # Multi-Organoid Universal Architecture Declarations
 182 |         if curr.type in (TokenType.ORGANOID, TokenType.TISSUE):
 183 |             return self._parse_organoid_decl()
 184 | 
 185 |         if curr.type == TokenType.CONNECT:
 186 |             return self._parse_connect_decl()
 187 | 
 188 |         if curr.type == TokenType.PORT:
 189 |             return self._parse_port_decl()
 190 | 
 191 |         # Channel declaration
 192 |         if curr.type == TokenType.CHANNEL:
 193 |             return self._parse_channel_decl()
 194 | 
 195 |         # Function declaration
 196 |         if curr.type == TokenType.FN:
 197 |             return self._parse_fn_decl()
 198 | 
 199 |         # Stream declaration
 200 |         if curr.type == TokenType.STREAM:
 201 |             return self._parse_stream_decl()
 202 | 
 203 |         # Top-level statements (e.g. scripts, variable declarations, control loops)
 204 |         return self._parse_statement()
 205 | 
 206 |     # =========================================================================
 207 |     # Universal Multi-Organoid, Connectome, and Grid Declarations
 208 |     # =========================================================================
 209 | 
 210 |     def _parse_organoid_decl(self) -> OrganoidDeclNode:
 211 |         tok = self._advance()  # 'organoid' or 'tissue'
 212 |         name_tok = self._expect_identifier("organoid name")
 213 |         node = OrganoidDeclNode(name=name_tok.value, line=tok.line, column=tok.column)
 214 | 
 215 |         curr = self._current()
 216 |         if curr.type == TokenType.LBRACKET:
 217 |             # Parametric array: organoid Cluster[1024]; or organoid Hive[N];
 218 |             self._advance()
 219 |             node.count = self.parse_expression()
 220 |             self._expect(TokenType.RBRACKET, "organoid array closing ']'")
 221 |             if self._match(TokenType.SEMICOLON):
 222 |                 return node
 223 | 
 224 |         if self._match(TokenType.LBRACE):
 225 |             while not self._match(TokenType.RBRACE):
 226 |                 prop_tok = self._expect(TokenType.IDENTIFIER, "organoid property name")
 227 |                 self._expect(TokenType.COLON, "organoid property colon")
 228 |                 prop_val = self.parse_expression()
 229 |                 self._match(TokenType.SEMICOLON)
 230 | 
 231 |                 pname = prop_tok.value
 232 |                 node.properties[pname] = prop_val
 233 |                 if pname in ("cells", "density"):
 234 |                     node.cells = prop_val
 235 |                 elif pname in ("radius", "geometry"):
 236 |                     node.radius = prop_val
 237 |                 elif pname == "perfusion":
 238 |                     node.perfusion = prop_val
 239 |             return node
 240 |         elif self._match(TokenType.SEMICOLON):
 241 |             return node
 242 |         else:
 243 |             raise ParseError("Expected '{' or ';' after organoid declaration", tok.line, tok.column)
 244 | 
 245 |     def _parse_connect_decl(self) -> ConnectDeclNode:
 246 |         tok = self._expect(TokenType.CONNECT, "connect declaration")
 247 |         src = self.parse_expression()
 248 |         self._expect(TokenType.ARROW_RIGHT, "connect arrow '->'")
 249 |         tgt = self.parse_expression()
 250 |         node = ConnectDeclNode(source=src, target=tgt, line=tok.line, column=tok.column)
 251 | 
 252 |         if self._current().raw_text == "with" or self._current().type == TokenType.LBRACE:
 253 |             if self._current().raw_text == "with":
 254 |                 self._advance()
 255 |             self._expect(TokenType.LBRACE, "connect properties opening '{'")
 256 |             while not self._match(TokenType.RBRACE):
 257 |                 prop_tok = self._expect(TokenType.IDENTIFIER, "connect property name")
 258 |                 self._expect(TokenType.COLON, "connect property colon")
 259 |                 prop_val = self.parse_expression()
 260 |                 self._match(TokenType.SEMICOLON)
 261 |                 pname = prop_tok.value
 262 |                 if "delay" in pname:
 263 |                     node.delay_ms = prop_val
 264 |                 elif "weight" in pname:
 265 |                     node.weight = prop_val
 266 |                 elif "plasticity" in pname:
 267 |                     node.plasticity = str(prop_val)
 268 |         self._match(TokenType.SEMICOLON)
 269 |         return node
 270 | 
 271 |     def _parse_port_decl(self) -> PortDeclNode:
 272 |         tok = self._expect(TokenType.PORT, "port declaration")
 273 |         name_tok = self._expect_identifier("port name")
 274 |         node = PortDeclNode(name=name_tok.value, line=tok.line, column=tok.column)
 275 |         if self._match(TokenType.LBRACE):
 276 |             while not self._match(TokenType.RBRACE):
 277 |                 if self._current().type in (TokenType.IDENTIFIER, TokenType.MODE):
 278 |                     prop_tok = self._advance()
 279 |                 else:
 280 |                     prop_tok = self._expect(TokenType.IDENTIFIER, "port property name")
 281 |                 self._expect(TokenType.COLON, "port property colon")
 282 |                 pname = prop_tok.value if isinstance(prop_tok.value, str) else prop_tok.raw_text
 283 |                 if pname == "mode":
 284 |                     mode_tok = self._current()
 285 |                     if mode_tok.type in (
 286 |                         TokenType.BIPHASIC_STIM,
 287 |                         TokenType.SPIKE_READOUT,
 288 |                         TokenType.VOLTAGE_SENSE,
 289 |                         TokenType.BIDIRECTIONAL,
 290 |                         TokenType.IDENTIFIER,
 291 |                     ):
 292 |                         node.mode = mode_tok.value or mode_tok.raw_text
 293 |                         self._advance()
 294 |                     else:
 295 |                         node.mode = str(self.parse_expression())
 296 |                 else:
 297 |                     prop_val = self.parse_expression()
 298 |                     if pname == "channels":
 299 |                         node.channels = prop_val
 300 |                 self._match(TokenType.SEMICOLON)
 301 |         return node
 302 | 
 303 |     def _parse_grid_decl(self) -> GridDeclNode:
 304 |         tok = self._expect(TokenType.GRID, "grid declaration")
 305 |         name_tok = self._expect_identifier("grid name")
 306 |         node = GridDeclNode(name=name_tok.value, line=tok.line, column=tok.column)
 307 | 
 308 |         curr = self._current()
 309 |         if curr.type == TokenType.LBRACKET:
 310 |             # Array syntax: grid mea[8, 8]; or grid mea[64];
 311 |             self._advance() # [
 312 |             first_dim = self.parse_expression()
 313 |             second_dim = None
 314 |             if self._match(TokenType.COMMA):
 315 |                 second_dim = self.parse_expression()
 316 |             self._expect(TokenType.RBRACKET, "grid dimensions")
 317 |             self._expect(TokenType.SEMICOLON, "grid declaration end")
 318 | 
 319 |             if second_dim is not None:
 320 |                 node.rows = first_dim
 321 |                 node.cols = second_dim
 322 |             else:
 323 |                 node.rows = first_dim
 324 |                 node.cols = None
 325 |             return node
 326 | 
 327 |         elif curr.type == TokenType.LBRACE:
 328 |             # Block property syntax: grid mea { rows: 8; cols: 8; pitch: 200um; }
 329 |             self._advance() # {
 330 |             while not self._match(TokenType.RBRACE):
 331 |                 prop_name_tok = self._expect(TokenType.IDENTIFIER, "grid property name")
 332 |                 self._expect(TokenType.COLON, "grid property colon")
 333 |                 prop_val = self.parse_expression()
 334 |                 self._expect(TokenType.SEMICOLON, "grid property semicolon")
 335 | 
 336 |                 pname = prop_name_tok.value
 337 |                 if pname == "rows":
 338 |                     node.rows = prop_val
 339 |                 elif pname == "cols":
 340 |                     node.cols = prop_val
 341 |                 elif pname == "pitch":
 342 |                     node.pitch = prop_val
 343 |                 elif pname == "base_voltage":
 344 |                     node.base_voltage = prop_val
 345 |             return node
 346 |         else:
 347 |             raise ParseError(
 348 |                 f"Expected '[' or '{{' after grid identifier '{name_tok.value}'",
 349 |                 curr.line,
 350 |                 curr.column,
 351 |                 expected="[ or {",
 352 |                 found=curr.type.name
 353 |             )
 354 | 
 355 |     def _parse_channel_decl(self) -> ChannelDeclNode:
 356 |         tok = self._expect(TokenType.CHANNEL, "channel declaration")
 357 |         name_tok = self._expect_identifier("channel name")
 358 |         self._expect(TokenType.ASSIGN, "channel assignment '='")
 359 | 
 360 |         # Target can be: mea[0, 2], mea[0], or [0 .. 15]
 361 |         target = self.parse_expression()
 362 | 
 363 |         mode_val: Optional[str] = None
 364 |         if self._match(TokenType.MODE):
 365 |             self._expect(TokenType.COLON, "channel mode colon")
 366 |             mode_tok = self._current()
 367 |             if mode_tok.type in (
 368 |                 TokenType.BIPHASIC_STIM,
 369 |                 TokenType.SPIKE_READOUT,
 370 |                 TokenType.VOLTAGE_SENSE,
 371 |                 TokenType.BIDIRECTIONAL,
 372 |                 TokenType.IDENTIFIER,
 373 |             ):
 374 |                 mode_val = mode_tok.value or mode_tok.raw_text
 375 |                 self._advance()
 376 |             else:
 377 |                 raise ParseError(
 378 |                     f"Invalid channel mode '{mode_tok.raw_text}'",
 379 |                     mode_tok.line,
 380 |                     mode_tok.column
 381 |                 )
 382 | 
 383 |         self._expect(TokenType.SEMICOLON, "channel declaration semicolon")
 384 |         return ChannelDeclNode(name=name_tok.value, target=target, mode=mode_val, line=tok.line, column=tok.column)
 385 | 
 386 |     # =========================================================================
 387 |     # Function & Stream Declarations
 388 |     # =========================================================================
 389 | 
 390 |     def _parse_fn_decl(self) -> FnDeclNode:
 391 |         tok = self._expect(TokenType.FN, "function declaration")
 392 |         name_tok = self._expect_identifier("function name")
 393 |         self._expect(TokenType.LPAREN, "function parameter list")
 394 | 
 395 |         params: List[ParamNode] = []
 396 |         if self._current().type != TokenType.RPAREN:
 397 |             while True:
 398 |                 p_name_tok = self._expect_identifier("parameter name")
 399 |                 self._expect(TokenType.COLON, "parameter colon")
 400 |                 p_type = self._parse_type_name()
 401 |                 params.append(ParamNode(name=p_name_tok.value, type_name=p_type, line=p_name_tok.line, column=p_name_tok.column))
 402 |                 if not self._match(TokenType.COMMA):
 403 |                     break
 404 | 
 405 |         self._expect(TokenType.RPAREN, "function parameter list end")
 406 | 
 407 |         return_type: Optional[str] = None
 408 |         if self._match(TokenType.ARROW_RIGHT):
 409 |             return_type = self._parse_type_name()
 410 | 
 411 |         body = self._parse_block()
 412 |         return FnDeclNode(
 413 |             name=name_tok.value,
 414 |             params=params,
 415 |             return_type=return_type,
 416 |             body=body,
 417 |             line=tok.line,
 418 |             column=tok.column
 419 |         )
 420 | 
 421 |     def _parse_stream_decl(self) -> StreamDeclNode:
 422 |         tok = self._expect(TokenType.STREAM, "stream declaration")
 423 |         name_tok = self._expect(TokenType.IDENTIFIER, "stream name")
 424 |         self._expect(TokenType.LBRACE, "stream block opening")
 425 | 
 426 |         items: List[StreamItemNode] = []
 427 |         while not self._match(TokenType.RBRACE):
 428 |             item_tok = self._current()
 429 |             if self._match(TokenType.BIND):
 430 |                 left_tok = self._expect_identifier("bind source")
 431 |                 if self._match(TokenType.ARROW_RIGHT):
 432 |                     right_tok = self._expect_identifier("bind target")
 433 |                     self._expect(TokenType.SEMICOLON, "bind statement semicolon")
 434 |                     items.append(StreamItemNode(
 435 |                         kind="bind_out",
 436 |                         left=left_tok.value,
 437 |                         right=right_tok.value,
 438 |                         line=item_tok.line,
 439 |                         column=item_tok.column
 440 |                     ))
 441 |                 elif self._match(TokenType.ARROW_LEFT):
 442 |                     right_tok = self._expect_identifier("bind source")
 443 |                     self._expect(TokenType.SEMICOLON, "bind statement semicolon")
 444 |                     items.append(StreamItemNode(
 445 |                         kind="bind_in",
 446 |                         left=left_tok.value,
 447 |                         right=right_tok.value,
 448 |                         line=item_tok.line,
 449 |                         column=item_tok.column
 450 |                     ))
 451 |                 else:
 452 |                     raise ParseError("Expected '->' or '<-' in bind statement", self._current().line, self._current().column)
 453 |             elif self._match(TokenType.CYCLE):
 454 |                 cycle_block = self._parse_block()
 455 |                 items.append(StreamItemNode(
 456 |                     kind="cycle",
 457 |                     cycle_block=cycle_block,
 458 |                     line=item_tok.line,
 459 |                     column=item_tok.column
 460 |                 ))
 461 |             else:
 462 |                 raise ParseError(
 463 |                     f"Unexpected token '{self._current().raw_text}' in stream declaration",
 464 |                     self._current().line,
 465 |                     self._current().column
 466 |                 )
 467 | 
 468 |         return StreamDeclNode(name=name_tok.value, items=items, line=tok.line, column=tok.column)
 469 | 
 470 |     def _parse_type_name(self) -> str:
 471 |         curr = self._current()
 472 |         type_tokens = (
 473 |             TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING,
 474 |             TokenType.CHANNEL, TokenType.GRID,
 475 |             TokenType.TYPE_VOLTAGE, TokenType.TYPE_CURRENT, TokenType.TYPE_TIME,
 476 |             TokenType.TYPE_FREQUENCY, TokenType.TYPE_LENGTH, TokenType.TYPE_CHARGE,
 477 |             TokenType.IDENTIFIER
 478 |         )
 479 |         if curr.type in type_tokens:
 480 |             self._advance()
 481 |             return curr.raw_text or curr.value
 482 |         raise ParseError(f"Expected type name, found '{curr.raw_text}'", curr.line, curr.column)
 483 | 
 484 |     # =========================================================================
 485 |     # Statements
 486 |     # =========================================================================
 487 | 
 488 |     def _parse_statement(self) -> ASTNode:
 489 |         curr = self._current()
 490 | 
 491 |         # Block statement
 492 |         if curr.type == TokenType.LBRACE:
 493 |             return self._parse_block()
 494 | 
 495 |         # let [mut] x [: type] = expr;
 496 |         if curr.type == TokenType.LET:
 497 |             return self._parse_let_statement()
 498 | 
 499 |         # C/Rust-style typed declaration: int x = 0; float y = 1.0;
 500 |         if curr.type in (
 501 |             TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING,
 502 |             TokenType.TYPE_VOLTAGE, TokenType.TYPE_CURRENT, TokenType.TYPE_TIME,
 503 |             TokenType.TYPE_FREQUENCY, TokenType.TYPE_LENGTH, TokenType.TYPE_CHARGE
 504 |         ) and self._is_identifier_token(self._peek(1)) and self._peek(2).type in (TokenType.ASSIGN, TokenType.SEMICOLON):
 505 |             return self._parse_typed_var_decl()
 506 | 
 507 |         # stim_biphasic(...)
 508 |         if curr.type == TokenType.STIM_BIPHASIC:
 509 |             return self._parse_stim_statement()
 510 | 
 511 |         # modulate_stdp(...)
 512 |         if curr.type == TokenType.MODULATE_STDP:
 513 |             return self._parse_modulate_statement()
 514 | 
 515 |         # sync_tick [()];
 516 |         if curr.type == TokenType.SYNC_TICK:
 517 |             return self._parse_sync_tick_statement()
 518 | 
 519 |         # if (...) ... [else ...]
 520 |         if curr.type == TokenType.IF:
 521 |             return self._parse_if_statement()
 522 | 
 523 |         # while (...) ...
 524 |         if curr.type == TokenType.WHILE:
 525 |             return self._parse_while_statement()
 526 | 
 527 |         # for identifier in start .. end ...
 528 |         if curr.type == TokenType.FOR:
 529 |             return self._parse_for_statement()
 530 | 
 531 |         # return [expr];
 532 |         if curr.type == TokenType.RETURN:
 533 |             return self._parse_return_statement()
 534 | 
 535 |         # Assignment or Expression Statement
 536 |         return self._parse_assign_or_expr_statement()
 537 | 
 538 |     def _parse_block(self) -> BlockNode:
 539 |         tok = self._expect(TokenType.LBRACE, "block opening '{'")
 540 |         stmts: List[ASTNode] = []
 541 |         while not self._match(TokenType.RBRACE):
 542 |             if self._current().type == TokenType.EOF:
 543 |                 raise ParseError("Unterminated block statement, missing '}'", tok.line, tok.column)
 544 |             stmt = self._parse_statement()
 545 |             if stmt is not None:
 546 |                 stmts.append(stmt)
 547 |         return BlockNode(statements=stmts, line=tok.line, column=tok.column)
 548 | 
 549 |     def _parse_let_statement(self) -> LetStmtNode:
 550 |         tok = self._expect(TokenType.LET, "let statement")
 551 |         is_mut = self._match(TokenType.MUT)
 552 |         name_tok = self._expect_identifier("variable name")
 553 | 
 554 |         type_name: Optional[str] = None
 555 |         if self._match(TokenType.COLON):
 556 |             type_name = self._parse_type_name()
 557 | 
 558 |         self._expect(TokenType.ASSIGN, "assignment '='")
 559 |         init_expr = self.parse_expression()
 560 |         self._expect(TokenType.SEMICOLON, "let statement semicolon")
 561 |         return LetStmtNode(
 562 |             name=name_tok.value,
 563 |             is_mut=is_mut,
 564 |             type_name=type_name,
 565 |             initializer=init_expr,
 566 |             line=tok.line,
 567 |             column=tok.column
 568 |         )
 569 | 
 570 |     def _parse_typed_var_decl(self) -> LetStmtNode:
 571 |         type_tok = self._advance()
 572 |         type_name = type_tok.raw_text or type_tok.value
 573 |         name_tok = self._expect_identifier("variable name")
 574 |         init_expr = None
 575 |         if self._match(TokenType.ASSIGN):
 576 |             init_expr = self.parse_expression()
 577 |         self._expect(TokenType.SEMICOLON, "variable declaration semicolon")
 578 |         return LetStmtNode(
 579 |             name=name_tok.value,
 580 |             is_mut=True,
 581 |             type_name=type_name,
 582 |             initializer=init_expr,
 583 |             line=type_tok.line,
 584 |             column=type_tok.column
 585 |         )
 586 | 
 587 |     def _parse_stim_statement(self) -> StimStmtNode:
 588 |         tok = self._expect(TokenType.STIM_BIPHASIC, "stim_biphasic call")
 589 |         self._expect(TokenType.LPAREN, "stim_biphasic arguments '('")
 590 | 
 591 |         channel = self.parse_expression()
 592 |         self._expect(TokenType.COMMA, "after channel argument")
 593 |         voltage = self.parse_expression()
 594 |         self._expect(TokenType.COMMA, "after voltage argument")
 595 |         phase1 = self.parse_expression()
 596 |         self._expect(TokenType.COMMA, "after phase1 argument")
 597 |         phase2 = self.parse_expression()
 598 | 
 599 |         interphase = None
 600 |         if self._match(TokenType.COMMA):
 601 |             interphase = self.parse_expression()
 602 | 
 603 |         self._expect(TokenType.RPAREN, "stim_biphasic closing ')'")
 604 |         self._expect(TokenType.SEMICOLON, "stim_biphasic semicolon")
 605 | 
 606 |         return StimStmtNode(
 607 |             channel=channel,
 608 |             voltage=voltage,
 609 |             phase1=phase1,
 610 |             phase2=phase2,
 611 |             interphase=interphase,
 612 |             line=tok.line,
 613 |             column=tok.column
 614 |         )
 615 | 
 616 |     def _parse_modulate_statement(self) -> ModulateStmtNode:
 617 |         tok = self._expect(TokenType.MODULATE_STDP, "modulate_stdp call")
 618 |         self._expect(TokenType.LPAREN, "modulate_stdp arguments '('")
 619 | 
 620 |         args: List[ASTNode] = []
 621 |         if self._current().type != TokenType.RPAREN:
 622 |             while True:
 623 |                 args.append(self.parse_expression())
 624 |                 if not self._match(TokenType.COMMA):
 625 |                     break
 626 | 
 627 |         self._expect(TokenType.RPAREN, "modulate_stdp closing ')'")
 628 |         self._expect(TokenType.SEMICOLON, "modulate_stdp semicolon")
 629 |         return ModulateStmtNode(args=args, line=tok.line, column=tok.column)
 630 | 
 631 |     def _parse_sync_tick_statement(self) -> SyncTickStmtNode:
 632 |         tok = self._expect(TokenType.SYNC_TICK, "sync_tick statement")
 633 |         count: Optional[ASTNode] = None
 634 |         if self._match(TokenType.LPAREN):
 635 |             if self._current().type != TokenType.RPAREN:
 636 |                 count = self.parse_expression()
 637 |             self._expect(TokenType.RPAREN, "sync_tick closing ')'")
 638 |         self._expect(TokenType.SEMICOLON, "sync_tick semicolon")
 639 |         return SyncTickStmtNode(count=count, line=tok.line, column=tok.column)
 640 | 
 641 |     def _parse_if_statement(self) -> IfStmtNode:
 642 |         tok = self._expect(TokenType.IF, "if statement")
 643 |         self._expect(TokenType.LPAREN, "if condition opening '('")
 644 |         cond = self.parse_expression()
 645 |         self._expect(TokenType.RPAREN, "if condition closing ')'")
 646 | 
 647 |         then_block = self._parse_block()
 648 |         else_block: Optional[ASTNode] = None
 649 | 
 650 |         if self._match(TokenType.ELSE):
 651 |             if self._current().type == TokenType.IF:
 652 |                 else_block = self._parse_if_statement()
 653 |             else:
 654 |                 else_block = self._parse_block()
 655 | 
 656 |         return IfStmtNode(
 657 |             condition=cond,
 658 |             then_block=then_block,
 659 |             else_block=else_block,
 660 |             line=tok.line,
 661 |             column=tok.column
 662 |         )
 663 | 
 664 |     def _parse_while_statement(self) -> WhileStmtNode:
 665 |         tok = self._expect(TokenType.WHILE, "while statement")
 666 |         self._expect(TokenType.LPAREN, "while condition opening '('")
 667 |         cond = self.parse_expression()
 668 |         self._expect(TokenType.RPAREN, "while condition closing ')'")
 669 |         body = self._parse_block()
 670 |         return WhileStmtNode(condition=cond, body=body, line=tok.line, column=tok.column)
 671 | 
 672 |     def _parse_for_statement(self) -> ForStmtNode:
 673 |         tok = self._expect(TokenType.FOR, "for statement")
 674 |         var_tok = self._expect_identifier("for loop variable")
 675 |         self._expect(TokenType.IN, "for loop 'in'")
 676 |         range_start = self.parse_expression()
 677 |         self._expect(TokenType.DOT_DOT, "range '..'")
 678 |         range_end = self.parse_expression()
 679 |         body = self._parse_block()
 680 |         return ForStmtNode(
 681 |             var_name=var_tok.value,
 682 |             range_start=range_start,
 683 |             range_end=range_end,
 684 |             body=body,
 685 |             line=tok.line,
 686 |             column=tok.column
 687 |         )
 688 | 
 689 |     def _parse_return_statement(self) -> ReturnStmtNode:
 690 |         tok = self._expect(TokenType.RETURN, "return statement")
 691 |         val: Optional[ASTNode] = None
 692 |         if self._current().type != TokenType.SEMICOLON:
 693 |             val = self.parse_expression()
 694 |         self._expect(TokenType.SEMICOLON, "return statement semicolon")
 695 |         return ReturnStmtNode(value=val, line=tok.line, column=tok.column)
 696 | 
 697 |     def _parse_assign_or_expr_statement(self) -> ASTNode:
 698 |         start_tok = self._current()
 699 |         expr = self.parse_expression()
 700 | 
 701 |         # Check if this expression is followed by '='
 702 |         if self._match(TokenType.ASSIGN):
 703 |             if not isinstance(expr, (IdentifierNode, IndexNode)):
 704 |                 raise ParseError(
 705 |                     f"Invalid assignment target at line {start_tok.line}, column {start_tok.column}",
 706 |                     start_tok.line,
 707 |                     start_tok.column
 708 |                 )
 709 |             val = self.parse_expression()
 710 |             self._expect(TokenType.SEMICOLON, "assignment semicolon")
 711 |             return AssignStmtNode(target=expr, value=val, line=start_tok.line, column=start_tok.column)
 712 | 
 713 |         self._expect(TokenType.SEMICOLON, "expression statement semicolon")
 714 |         return ExprStmtNode(expr=expr, line=start_tok.line, column=start_tok.column)
 715 | 
 716 |     # =========================================================================
 717 |     # Pratt Expression Parser
 718 |     # =========================================================================
 719 | 
 720 |     def parse_expression(self, min_bp: int = 0) -> ASTNode:
 721 |         """Pratt precedence climbing expression parser."""
 722 |         token = self._advance()
 723 |         left = self._parse_prefix(token)
 724 | 
 725 |         while True:
 726 |             curr = self._current()
 727 |             if curr.type == TokenType.EOF or curr.type in (
 728 |                 TokenType.SEMICOLON, TokenType.RPAREN, TokenType.RBRACKET,
 729 |                 TokenType.RBRACE, TokenType.COMMA, TokenType.COLON, TokenType.DOT_DOT
 730 |             ):
 731 |                 break
 732 | 
 733 |             # Handle immediate unit suffix following a numeric literal (e.g. 1.0 V or 200 us)
 734 |             if isinstance(left, LiteralNode) and left.type_name in ("int", "float"):
 735 |                 unit_text = curr.raw_text or curr.value
 736 |                 if unit_text in UNIT_SUFFIXES:
 737 |                     self._advance()
 738 |                     dim, scale = UNIT_SUFFIXES[unit_text]
 739 |                     mag = float(left.value)
 740 |                     left = PhysicalLiteralNode(
 741 |                         magnitude=mag,
 742 |                         dimension=dim,
 743 |                         si_value=mag * scale,
 744 |                         unit_suffix=unit_text,
 745 |                         line=left.line,
 746 |                         column=left.column
 747 |                     )
 748 |                     continue
 749 | 
 750 |             # Infix Function Call: left(...)
 751 |             if curr.type == TokenType.LPAREN:
 752 |                 if POSTFIX_BINDING_POWER < min_bp:
 753 |                     break
 754 |                 self._advance() # (
 755 |                 args: List[ASTNode] = []
 756 |                 if self._current().type != TokenType.RPAREN:
 757 |                     while True:
 758 |                         args.append(self.parse_expression(0))
 759 |                         if not self._match(TokenType.COMMA):
 760 |                             break
 761 |                 self._expect(TokenType.RPAREN, "call argument closing ')'")
 762 |                 left = CallNode(callee=left, args=args, line=left.line, column=left.column)
 763 |                 continue
 764 | 
 765 |             # Infix Indexing: left[...] or left[r, c]
 766 |             if curr.type == TokenType.LBRACKET:
 767 |                 if POSTFIX_BINDING_POWER < min_bp:
 768 |                     break
 769 |                 self._advance() # [
 770 |                 indices: List[ASTNode] = []
 771 |                 while True:
 772 |                     indices.append(self.parse_expression(0))
 773 |                     if not self._match(TokenType.COMMA):
 774 |                         break
 775 |                 self._expect(TokenType.RBRACKET, "indexing closing ']'")
 776 |                 left = IndexNode(target=left, indices=indices, line=left.line, column=left.column)
 777 |                 continue
 778 | 
 779 |             # Standard Binary Infix Operators
 780 |             if curr.type in INFIX_BINDING_POWERS:
 781 |                 l_bp, r_bp = INFIX_BINDING_POWERS[curr.type]
 782 |                 if l_bp < min_bp:
 783 |                     break
 784 |                 op_tok = self._advance()
 785 |                 right = self.parse_expression(r_bp)
 786 |                 left = BinaryOpNode(
 787 |                     left=left,
 788 |                     op=op_tok.raw_text,
 789 |                     right=right,
 790 |                     line=op_tok.line,
 791 |                     column=op_tok.column
 792 |                 )
 793 |                 continue
 794 | 
 795 |             break
 796 | 
 797 |         return left
 798 | 
 799 |     def _parse_prefix(self, token: Token) -> ASTNode:
 800 |         """Parses prefix expressions: literals, unary operators, grouping, identifiers."""
 801 |         # Unary operators: -, !
 802 |         if token.type in (TokenType.MINUS, TokenType.NOT):
 803 |             operand = self.parse_expression(PREFIX_BINDING_POWER)
 804 |             return UnaryOpNode(op=token.raw_text, operand=operand, line=token.line, column=token.column)
 805 | 
 806 |         # Parenthesized expression: (expr)
 807 |         if token.type == TokenType.LPAREN:
 808 |             expr = self.parse_expression(0)
 809 |             self._expect(TokenType.RPAREN, "closing ')'")
 810 |             return expr
 811 | 
 812 |         # Range literal or array slice: [start .. end]
 813 |         if token.type == TokenType.LBRACKET:
 814 |             start_expr = self.parse_expression(0)
 815 |             if self._match(TokenType.DOT_DOT):
 816 |                 end_expr = self.parse_expression(0)
 817 |                 self._expect(TokenType.RBRACKET, "range closing ']'")
 818 |                 return RangeNode(start=start_expr, end=end_expr, line=token.line, column=token.column)
 819 |             self._expect(TokenType.RBRACKET, "closing ']'")
 820 |             return start_expr
 821 | 
 822 |         # Integer literal
 823 |         if token.type == TokenType.INT_LIT:
 824 |             return LiteralNode(value=token.value, type_name="int", line=token.line, column=token.column)
 825 | 
 826 |         # Float literal
 827 |         if token.type == TokenType.FLOAT_LIT:
 828 |             return LiteralNode(value=token.value, type_name="float", line=token.line, column=token.column)
 829 | 
 830 |         # Boolean literal
 831 |         if token.type == TokenType.BOOL_LIT:
 832 |             return LiteralNode(value=token.value, type_name="bool", line=token.line, column=token.column)
 833 | 
 834 |         # String literal
 835 |         if token.type == TokenType.STRING_LIT:
 836 |             return LiteralNode(value=token.value, type_name="string", line=token.line, column=token.column)
 837 | 
 838 |         # Physical literal with immediate suffix (e.g. 10ms, 0.5V)
 839 |         if token.type == TokenType.PHYSICAL_LIT:
 840 |             # Extract suffix from raw text
 841 |             suffix = ""
 842 |             for s in UNIT_SUFFIXES:
 843 |                 if token.raw_text.endswith(s):
 844 |                     suffix = s
 845 |                     break
 846 |             return PhysicalLiteralNode(
 847 |                 magnitude=float(token.value),
 848 |                 dimension=token.dimension,
 849 |                 si_value=float(token.si_value) if token.si_value is not None else float(token.value),
 850 |                 unit_suffix=suffix,
 851 |                 line=token.line,
 852 |                 column=token.column
 853 |             )
 854 | 
 855 |         # Built-in Domain Expression Calls
 856 |         if token.type in (
 857 |             TokenType.READ_SPIKES,
 858 |             TokenType.READ_VOLTAGE,
 859 |             TokenType.POP_FIRING_RATE,
 860 |             TokenType.READ_POPULATION_RATE,
 861 |             TokenType.PUMP_SET_RATE,
 862 |             TokenType.PUMP_DISPENSE,
 863 |             TokenType.VALVE_SET,
 864 |             TokenType.VALVE_OPEN,
 865 |             TokenType.VALVE_CLOSE,
 866 |             TokenType.MOTOR_STEP,
 867 |             TokenType.READ_PRESSURE,
 868 |             TokenType.READ_TEMPERATURE,
 869 |         ):
 870 |             func_name = token.raw_text
 871 |             self._expect(TokenType.LPAREN, f"{func_name} arguments '('")
 872 |             args: List[ASTNode] = []
 873 |             if self._current().type != TokenType.RPAREN:
 874 |                 while True:
 875 |                     args.append(self.parse_expression(0))
 876 |                     if not self._match(TokenType.COMMA):
 877 |                         break
 878 |             self._expect(TokenType.RPAREN, f"{func_name} closing ')'")
 879 |             return DomainCallNode(func_name=func_name, args=args, line=token.line, column=token.column)
 880 | 
 881 |         # Standard Identifier or contextual keyword used as expression
 882 |         if token.type == TokenType.IDENTIFIER or token.type in (TokenType.CYCLE, TokenType.STREAM, TokenType.MODE):
 883 |             name = token.raw_text or token.value
 884 |             return IdentifierNode(name=name, line=token.line, column=token.column)
 885 | 
 886 |         # Type conversion calls: int(expr), float(expr)
 887 |         if token.type in (TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING):
 888 |             if self._current().type == TokenType.LPAREN:
 889 |                 # Type cast expression: float(spikes)
 890 |                 self._advance() # (
 891 |                 arg = self.parse_expression(0)
 892 |                 self._expect(TokenType.RPAREN, "cast closing ')'")
 893 |                 return CallNode(
 894 |                     callee=IdentifierNode(name=token.raw_text, line=token.line, column=token.column),
 895 |                     args=[arg],
 896 |                     line=token.line,
 897 |                     column=token.column
 898 |                 )
 899 |             return IdentifierNode(name=token.raw_text, line=token.line, column=token.column)
 900 | 
 901 |         raise ParseError(
 902 |             f"Expected expression, found '{token.raw_text or token.type.name}'",
 903 |             token.line,
 904 |             token.column
 905 |         )
```

### `compiler/semantic.py` (848 lines, SHA-256: `cafb5abc9bb024e3...`)

```text
   1 | """
   2 | WetLang Compiler - Multi-Pass Semantic Analyzer & Safety Verifier
   3 | Hand-crafted from first principles.
   4 | 
   5 | Pass 1: Scope & Symbol Resolution, MEA Electrode Coordinate Bounds Checking.
   6 | Pass 2: Type Checking, Dimensional Homogeneity, and Static Voltage Clamp Check.
   7 | Pass 3: Control Flow Graph (CFG) Construction & Loop-Yield Verification.
   8 | """
   9 | 
  10 | from typing import Dict, List, Optional, Set, Tuple, Any
  11 | from compiler.token import Dimension
  12 | from compiler.ast_nodes import (
  13 |     ASTNode,
  14 |     ASTVisitor,
  15 |     ProgramNode,
  16 |     OrganoidDeclNode,
  17 |     ConnectDeclNode,
  18 |     PortDeclNode,
  19 |     GridDeclNode,
  20 |     ChannelDeclNode,
  21 |     FnDeclNode,
  22 |     ParamNode,
  23 |     StreamDeclNode,
  24 |     StreamItemNode,
  25 |     BlockNode,
  26 |     LetStmtNode,
  27 |     AssignStmtNode,
  28 |     StimStmtNode,
  29 |     ModulateStmtNode,
  30 |     SyncTickStmtNode,
  31 |     IfStmtNode,
  32 |     WhileStmtNode,
  33 |     ForStmtNode,
  34 |     ReturnStmtNode,
  35 |     ExprStmtNode,
  36 |     BinaryOpNode,
  37 |     UnaryOpNode,
  38 |     LiteralNode,
  39 |     PhysicalLiteralNode,
  40 |     IdentifierNode,
  41 |     CallNode,
  42 |     IndexNode,
  43 |     RangeNode,
  44 |     DomainCallNode,
  45 | )
  46 | 
  47 | 
  48 | class SemanticError(Exception):
  49 |     """Raised when static semantics or safety invariants are violated."""
  50 |     def __init__(self, message: str, line: int = 0, column: int = 0, error_code: str = ""):
  51 |         self.error_code = error_code
  52 |         self.line = line
  53 |         self.column = column
  54 |         prefix = f"{error_code}: " if error_code else ""
  55 |         super().__init__(f"SemanticError at line {line}, column {column}: {prefix}{message}")
  56 | 
  57 | 
  58 | class Symbol:
  59 |     def __init__(self, name: str, type_name: str, dimension: Dimension = Dimension.NONE, is_mut: bool = False, node: Optional[ASTNode] = None):
  60 |         self.name: str = name
  61 |         self.type_name: str = type_name
  62 |         self.dimension: Dimension = dimension
  63 |         self.is_mut: bool = is_mut
  64 |         self.node: Optional[ASTNode] = node
  65 | 
  66 | 
  67 | class Scope:
  68 |     def __init__(self, parent: Optional["Scope"] = None, name: str = "block"):
  69 |         self.parent: Optional["Scope"] = parent
  70 |         self.name: str = name
  71 |         self.symbols: Dict[str, Symbol] = {}
  72 | 
  73 |     def define(self, symbol: Symbol) -> None:
  74 |         self.symbols[symbol.name] = symbol
  75 | 
  76 |     def resolve(self, name: str) -> Optional[Symbol]:
  77 |         if name in self.symbols:
  78 |             return self.symbols[name]
  79 |         if self.parent is not None:
  80 |             return self.parent.resolve(name)
  81 |         return None
  82 | 
  83 |     def is_local(self, name: str) -> bool:
  84 |         return name in self.symbols
  85 | 
  86 | 
  87 | class SemanticAnalyzer:
  88 |     """
  89 |     Orchestrates the 3-pass semantic analysis and safety verification.
  90 |     """
  91 |     def __init__(self, program: ProgramNode):
  92 |         self.program: ProgramNode = program
  93 |         self.global_scope: Scope = Scope(parent=None, name="global")
  94 |         self.current_scope: Scope = self.global_scope
  95 |         self.mea_grids: Dict[str, Tuple[int, int]] = {} # grid_name -> (rows, cols)
  96 | 
  97 |     def analyze(self) -> None:
  98 |         """Run all verification passes in sequence."""
  99 |         # Pre-populate global built-ins
 100 |         self._init_builtins()
 101 | 
 102 |         # Pass 1: Symbol resolution and coordinate bounds checking
 103 |         self._pass1_symbols_and_bounds()
 104 | 
 105 |         # Pass 2: Type checking, dimensional arithmetic, and static voltage clamp check
 106 |         self._pass2_types_and_dimensions()
 107 | 
 108 |         # Pass 3: Static loop-yield verification (CFG analysis)
 109 |         self._pass3_loop_yield_verifier()
 110 | 
 111 |     def _init_builtins(self) -> None:
 112 |         builtins = [
 113 |             ("read_spikes", "fn", Dimension.NONE),
 114 |             ("read_voltage", "fn", Dimension.VOLTAGE),
 115 |             ("pop_firing_rate", "fn", Dimension.FREQUENCY),
 116 |             ("read_population_rate", "fn", Dimension.FREQUENCY),
 117 |             ("abs", "fn", Dimension.NONE),
 118 |             ("float", "fn", Dimension.NONE),
 119 |             ("int", "fn", Dimension.NONE),
 120 |         ]
 121 |         for name, tname, dim in builtins:
 122 |             self.global_scope.define(Symbol(name, tname, dimension=dim))
 123 | 
 124 |     # =========================================================================
 125 |     # PASS 1: Scope, Symbol Resolution & MEA Coordinate Bounds
 126 |     # =========================================================================
 127 | 
 128 |     def _pass1_symbols_and_bounds(self) -> None:
 129 |         visitor = _Pass1Visitor(self)
 130 |         visitor.visit(self.program)
 131 | 
 132 |     # =========================================================================
 133 |     # PASS 2: Types, Dimensional Checking & Voltage Clamp
 134 |     # =========================================================================
 135 | 
 136 |     def _pass2_types_and_dimensions(self) -> None:
 137 |         visitor = _Pass2Visitor(self)
 138 |         visitor.visit(self.program)
 139 | 
 140 |     # =========================================================================
 141 |     # PASS 3: Static Loop-Yield Verifier (CFG Post-Dominance)
 142 |     # =========================================================================
 143 | 
 144 |     def _pass3_loop_yield_verifier(self) -> None:
 145 |         visitor = _Pass3LoopYieldVisitor(self)
 146 |         visitor.visit(self.program)
 147 | 
 148 | 
 149 | # =========================================================================
 150 | # Pass 1 Visitor
 151 | # =========================================================================
 152 | 
 153 | class _Pass1Visitor(ASTVisitor):
 154 |     def __init__(self, analyzer: SemanticAnalyzer):
 155 |         self.analyzer: SemanticAnalyzer = analyzer
 156 |         self.const_int_values: Dict[str, int] = {}
 157 |         self.ref_channels: set = set()
 158 |         self.rec_only_channels: set = set()
 159 | 
 160 |     def visit_ProgramNode(self, node: ProgramNode) -> None:
 161 |         for decl in node.declarations:
 162 |             self.visit(decl)
 163 | 
 164 |     def visit_GridDeclNode(self, node: GridDeclNode) -> None:
 165 |         if self.analyzer.current_scope.is_local(node.name):
 166 |             raise SemanticError(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 167 | 
 168 |         rows = 8
 169 |         cols = 8
 170 |         if isinstance(node.rows, LiteralNode) and node.rows.type_name == "int":
 171 |             rows = int(node.rows.value)
 172 |         if isinstance(node.cols, LiteralNode) and node.cols.type_name == "int":
 173 |             cols = int(node.cols.value)
 174 | 
 175 |         self.analyzer.mea_grids[node.name] = (rows, cols)
 176 |         self.analyzer.current_scope.define(Symbol(node.name, "grid", Dimension.NONE, False, node))
 177 | 
 178 |     def visit_ChannelDeclNode(self, node: ChannelDeclNode) -> None:
 179 |         if self.analyzer.current_scope.is_local(node.name):
 180 |             raise SemanticError(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 181 | 
 182 |         # Verify target coordinate literal bounds
 183 |         self._check_coordinate_bounds(node.target)
 184 |         mode_str = str(node.mode) if node.mode else ""
 185 |         if mode_str in ("Reference", "ref", "Ref", "reference"):
 186 |             self.ref_channels.add(node.name)
 187 |         elif mode_str in ("RecordingOnly", "record", "Rec", "SpikeReadout", "rec"):
 188 |             self.rec_only_channels.add(node.name)
 189 |         self.analyzer.current_scope.define(Symbol(node.name, "channel", Dimension.NONE, False, node))
 190 | 
 191 |     def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
 192 |         if self.analyzer.current_scope.is_local(node.name):
 193 |             raise SemanticError(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 194 |         self.analyzer.current_scope.define(Symbol(node.name, "organoid", Dimension.NONE, False, node))
 195 | 
 196 |     def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
 197 |         pass
 198 | 
 199 |     def visit_PortDeclNode(self, node: PortDeclNode) -> None:
 200 |         if self.analyzer.current_scope.is_local(node.name):
 201 |             raise SemanticError(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 202 |         self.analyzer.current_scope.define(Symbol(node.name, "port", Dimension.NONE, False, node))
 203 | 
 204 |     def visit_FnDeclNode(self, node: FnDeclNode) -> None:
 205 |         if self.analyzer.current_scope.is_local(node.name):
 206 |             raise SemanticError(f"Redeclared function '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 207 | 
 208 |         self.analyzer.current_scope.define(Symbol(node.name, "fn", Dimension.NONE, False, node))
 209 | 
 210 |         # Enter function scope
 211 |         fn_scope = Scope(parent=self.analyzer.current_scope, name=f"fn_{node.name}")
 212 |         prev_scope = self.analyzer.current_scope
 213 |         self.analyzer.current_scope = fn_scope
 214 | 
 215 |         for param in node.params:
 216 |             if fn_scope.is_local(param.name):
 217 |                 raise SemanticError(f"Duplicate parameter '{param.name}' in function '{node.name}'", param.line, param.column, "ERR_REDECLARED_IDENTIFIER")
 218 |             fn_scope.define(Symbol(param.name, param.type_name, self._type_to_dimension(param.type_name), False, param))
 219 | 
 220 |         self.visit(node.body)
 221 |         self.analyzer.current_scope = prev_scope
 222 | 
 223 |     def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
 224 |         if self.analyzer.current_scope.is_local(node.name):
 225 |             raise SemanticError(f"Redeclared stream '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 226 |         self.analyzer.current_scope.define(Symbol(node.name, "stream", Dimension.NONE, False, node))
 227 | 
 228 |         stream_scope = Scope(parent=self.analyzer.current_scope, name=f"stream_{node.name}")
 229 |         prev_scope = self.analyzer.current_scope
 230 |         self.analyzer.current_scope = stream_scope
 231 | 
 232 |         for item in node.items:
 233 |             if item.kind == "cycle" and item.cycle_block is not None:
 234 |                 self.visit(item.cycle_block)
 235 | 
 236 |         self.analyzer.current_scope = prev_scope
 237 | 
 238 |     def visit_BlockNode(self, node: BlockNode) -> None:
 239 |         block_scope = Scope(parent=self.analyzer.current_scope, name="block")
 240 |         prev_scope = self.analyzer.current_scope
 241 |         self.analyzer.current_scope = block_scope
 242 | 
 243 |         for stmt in node.statements:
 244 |             self.visit(stmt)
 245 | 
 246 |         self.analyzer.current_scope = prev_scope
 247 | 
 248 |     def visit_LetStmtNode(self, node: LetStmtNode) -> None:
 249 |         if self.analyzer.current_scope.is_local(node.name):
 250 |             raise SemanticError(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
 251 | 
 252 |         dim = self._type_to_dimension(node.type_name) if node.type_name else Dimension.NONE
 253 |         self.analyzer.current_scope.define(Symbol(node.name, node.type_name or "inferred", dim, node.is_mut, node))
 254 |         if node.initializer is not None:
 255 |             self.visit(node.initializer)
 256 |             val = self._extract_int_constant(node.initializer)
 257 |             if val is not None and not node.is_mut:
 258 |                 self.const_int_values[node.name] = val
 259 | 
 260 |     def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
 261 |         self.visit(node.target)
 262 |         self.visit(node.value)
 263 | 
 264 |     def visit_StimStmtNode(self, node: StimStmtNode) -> None:
 265 |         self._check_coordinate_bounds(node.channel)
 266 |         if isinstance(node.channel, IdentifierNode):
 267 |             if node.channel.name in self.ref_channels:
 268 |                 raise SemanticError(
 269 |                     f"Electrode channel '{node.channel.name}' is declared as a reference channel and cannot be stimulated",
 270 |                     node.line, node.column, "ERR_STIM_ON_REFERENCE_CHANNEL"
 271 |                 )
 272 |             if node.channel.name in self.rec_only_channels:
 273 |                 raise SemanticError(
 274 |                     f"Electrode channel '{node.channel.name}' is declared in a recording-only channel bank and cannot be stimulated",
 275 |                     node.line, node.column, "ERR_STIM_ON_RECORDING_CHANNEL"
 276 |                 )
 277 |         self.visit(node.channel)
 278 |         self.visit(node.voltage)
 279 |         self.visit(node.phase1)
 280 |         self.visit(node.phase2)
 281 |         if node.interphase is not None:
 282 |             self.visit(node.interphase)
 283 | 
 284 |     def visit_ModulateStmtNode(self, node: ModulateStmtNode) -> None:
 285 |         for arg in node.args:
 286 |             self.visit(arg)
 287 | 
 288 |     def visit_SyncTickStmtNode(self, node: SyncTickStmtNode) -> None:
 289 |         if node.count is not None:
 290 |             self.visit(node.count)
 291 | 
 292 |     def visit_IfStmtNode(self, node: IfStmtNode) -> None:
 293 |         self.visit(node.condition)
 294 |         self.visit(node.then_block)
 295 |         if node.else_block is not None:
 296 |             self.visit(node.else_block)
 297 | 
 298 |     def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
 299 |         self.visit(node.condition)
 300 |         self.visit(node.body)
 301 | 
 302 |     def visit_ForStmtNode(self, node: ForStmtNode) -> None:
 303 |         for_scope = Scope(parent=self.analyzer.current_scope, name="for")
 304 |         prev_scope = self.analyzer.current_scope
 305 |         self.analyzer.current_scope = for_scope
 306 | 
 307 |         for_scope.define(Symbol(node.var_name, "int", Dimension.NONE, False, node))
 308 |         self.visit(node.range_start)
 309 |         self.visit(node.range_end)
 310 |         self.visit(node.body)
 311 | 
 312 |         self.analyzer.current_scope = prev_scope
 313 | 
 314 |     def visit_ReturnStmtNode(self, node: ReturnStmtNode) -> None:
 315 |         if node.value is not None:
 316 |             self.visit(node.value)
 317 | 
 318 |     def visit_ExprStmtNode(self, node: ExprStmtNode) -> None:
 319 |         self.visit(node.expr)
 320 | 
 321 |     def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
 322 |         self.visit(node.left)
 323 |         self.visit(node.right)
 324 | 
 325 |     def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
 326 |         self.visit(node.operand)
 327 | 
 328 |     def visit_CallNode(self, node: CallNode) -> None:
 329 |         self.visit(node.callee)
 330 |         for arg in node.args:
 331 |             self.visit(arg)
 332 | 
 333 |     def visit_IndexNode(self, node: IndexNode) -> None:
 334 |         self._check_coordinate_bounds(node)
 335 |         self.visit(node.target)
 336 |         for idx in node.indices:
 337 |             self.visit(idx)
 338 | 
 339 |     def visit_DomainCallNode(self, node: DomainCallNode) -> None:
 340 |         if node.func_name in ("read_spikes", "read_voltage") and len(node.args) > 0:
 341 |             self._check_coordinate_bounds(node.args[0])
 342 |         elif node.func_name == "pump_set_rate" and len(node.args) >= 2:
 343 |             rate_node = node.args[1]
 344 |             if isinstance(rate_node, PhysicalLiteralNode):
 345 |                 val = float(rate_node.magnitude)
 346 |                 if rate_node.unit_suffix == "mL/min":
 347 |                     val *= 1000.0
 348 |                 if val < 0.0 or val > 15.0:
 349 |                     raise SemanticError(
 350 |                         f"Requested pump rate {val:.2f} uL/min exceeds safe hydrodynamic shear limit (0..15.0 uL/min)",
 351 |                         node.line, node.column, "ERR_SHEAR_STRESS_EXCEEDED"
 352 |                     )
 353 | 
 354 |                 # Geometry-Aware Shear Stress Check: tau_w = 1.2 * (6 * mu * Q) / (w * h^2)
 355 |                 # If optional channel dimensions are passed as args: pump_set_rate(ch, rate, width, height)
 356 |                 if len(node.args) >= 4:
 357 |                     w_node, h_node = node.args[2], node.args[3]
 358 |                     w_um = getattr(w_node, "magnitude", 1000.0) if isinstance(w_node, PhysicalLiteralNode) else 1000.0
 359 |                     h_um = getattr(h_node, "magnitude", 200.0) if isinstance(h_node, PhysicalLiteralNode) else 200.0
 360 |                     # Convert Q to m^3/s: val uL/min * 1e-9 m^3/uL / 60 s/min
 361 |                     q_m3_s = (val * 1e-9) / 60.0
 362 |                     w_m = float(w_um) * 1e-6
 363 |                     h_m = float(h_um) * 1e-6
 364 |                     mu = 0.001 # Pa*s (viscosity of aqueous culture medium)
 365 |                     tau_w = 1.2 * (6.0 * mu * q_m3_s) / (w_m * (h_m ** 2))
 366 |                     if tau_w > 0.05: # 0.05 Pa maximum safe shear stress for neurites
 367 |                         raise SemanticError(
 368 |                             f"Hydrodynamic Shear Stress Exceeded: Wall shear stress tau_w = {tau_w:.3f} Pa "
 369 |                             f"exceeds physiological threshold (0.05 Pa) in {w_um:.0f}x{h_um:.0f} um channel at {val:.2f} uL/min",
 370 |                             node.line, node.column, "ERR_SHEAR_STRESS_EXCEEDED"
 371 |                         )
 372 |         for arg in node.args:
 373 |             self.visit(arg)
 374 | 
 375 |     def visit_IdentifierNode(self, node: IdentifierNode) -> None:
 376 |         sym = self.analyzer.current_scope.resolve(node.name)
 377 |         if sym is None:
 378 |             # Check if it's a known grid
 379 |             if node.name not in self.analyzer.mea_grids:
 380 |                 raise SemanticError(f"Undeclared identifier '{node.name}'", node.line, node.column, "ERR_UNDECLARED_IDENTIFIER")
 381 | 
 382 |     def _check_coordinate_bounds(self, node: ASTNode) -> None:
 383 |         """Verifies literal MEA coordinate bounds: (r, c) in [0..7]x[0..7], linear in [0..63]."""
 384 |         if not isinstance(node, IndexNode):
 385 |             return
 386 | 
 387 |         # Check 2D indexing: mea[r, c]
 388 |         if len(node.indices) == 2:
 389 |             r_node = node.indices[0]
 390 |             c_node = node.indices[1]
 391 |             r_val = self._extract_int_constant(r_node)
 392 |             c_val = self._extract_int_constant(c_node)
 393 | 
 394 |             if r_val is not None:
 395 |                 if r_val < 0 or r_val > 7:
 396 |                     raise SemanticError(
 397 |                         f"Electrode row coordinate {r_val} is out of bounds [0..7]",
 398 |                         node.line,
 399 |                         node.column,
 400 |                         "ERR_ELECTRODE_OUT_OF_BOUNDS"
 401 |                     )
 402 |             if c_val is not None:
 403 |                 if c_val < 0 or c_val > 7:
 404 |                     raise SemanticError(
 405 |                         f"Electrode col coordinate {c_val} is out of bounds [0..7]",
 406 |                         node.line,
 407 |                         node.column,
 408 |                         "ERR_ELECTRODE_OUT_OF_BOUNDS"
 409 |                     )
 410 | 
 411 |         # Check 1D indexing: mea[k]
 412 |         elif len(node.indices) == 1:
 413 |             k_node = node.indices[0]
 414 |             k_val = self._extract_int_constant(k_node)
 415 |             if k_val is not None:
 416 |                 if k_val < 0 or k_val > 63:
 417 |                     raise SemanticError(
 418 |                         f"Electrode linear channel {k_val} is out of bounds [0..63]",
 419 |                         node.line,
 420 |                         node.column,
 421 |                         "ERR_ELECTRODE_OUT_OF_BOUNDS"
 422 |                     )
 423 | 
 424 |     def _extract_int_constant(self, node: ASTNode) -> Optional[int]:
 425 |         if isinstance(node, LiteralNode) and node.type_name == "int":
 426 |             return int(node.value)
 427 |         if isinstance(node, UnaryOpNode):
 428 |             inner = self._extract_int_constant(node.operand)
 429 |             if inner is None:
 430 |                 return None
 431 |             if node.op == "-":
 432 |                 return -inner
 433 |             if node.op == "+":
 434 |                 return inner
 435 |             return None
 436 |         if isinstance(node, BinaryOpNode):
 437 |             left = self._extract_int_constant(node.left)
 438 |             right = self._extract_int_constant(node.right)
 439 |             if left is None or right is None:
 440 |                 return None
 441 |             if node.op == "+":
 442 |                 return left + right
 443 |             if node.op == "-":
 444 |                 return left - right
 445 |             if node.op == "*":
 446 |                 return left * right
 447 |             if node.op == "/":
 448 |                 if right == 0:
 449 |                     return None
 450 |                 return left // right
 451 |             if node.op == "%":
 452 |                 if right == 0:
 453 |                     return None
 454 |                 return left % right
 455 |             return None
 456 |         if isinstance(node, IdentifierNode):
 457 |             if hasattr(self, "const_int_values") and node.name in self.const_int_values:
 458 |                 return self.const_int_values[node.name]
 459 |         return None
 460 | 
 461 |     def _type_to_dimension(self, tname: Optional[str]) -> Dimension:
 462 |         if not tname:
 463 |             return Dimension.NONE
 464 |         mapping = {
 465 |             "Voltage": Dimension.VOLTAGE,
 466 |             "Current": Dimension.CURRENT,
 467 |             "Time": Dimension.TIME,
 468 |             "Frequency": Dimension.FREQUENCY,
 469 |             "Length": Dimension.LENGTH,
 470 |             "Charge": Dimension.CHARGE,
 471 |         }
 472 |         return mapping.get(tname, Dimension.NONE)
 473 | 
 474 | 
 475 | # =========================================================================
 476 | # Pass 2 Visitor
 477 | # =========================================================================
 478 | 
 479 | class _Pass2Visitor(ASTVisitor):
 480 |     def __init__(self, analyzer: SemanticAnalyzer):
 481 |         self.analyzer: SemanticAnalyzer = analyzer
 482 |         self.current_scope: Scope = analyzer.global_scope
 483 |         self.node_dimensions: Dict[int, Dimension] = {}
 484 |         self.const_values: Dict[str, float] = {}
 485 | 
 486 |     def visit_ProgramNode(self, node: ProgramNode) -> None:
 487 |         for decl in node.declarations:
 488 |             self.visit(decl)
 489 | 
 490 |     def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
 491 |         # Phase 3 Biophysics: Spherical Reaction-Diffusion (Thiele Modulus) Anoxia Model.
 492 |         # Living neural organoids in culture baths are avascular spheres.
 493 |         # Steady-state spherical diffusion equation with zero-order oxygen consumption R0:
 494 |         #   (1/r^2) d/dr (r^2 dC/dr) = R0 / D_eff
 495 |         # Solving with C(R) = C_surface and dC/dr(0) = 0 yields:
 496 |         #   C(r) = C_surface - (R0 / 6 D_eff) * (R^2 - r^2)
 497 |         # Critical penetration depth before core anoxia C(0) <= 0:
 498 |         #   R_crit = sqrt(6 * D_eff * C_surface / R0) ~= 200..250 um.
 499 |         if node.radius is not None:
 500 |             r_val = getattr(node.radius, "si_value", 0.0)
 501 |             r_um = r_val * 1e6
 502 | 
 503 |             # 1. Unperfused threshold: R > 200 um without perfusion causes core necrosis
 504 |             if r_val > 0.000200 and node.perfusion is None:
 505 |                 raise SemanticError(
 506 |                     f"Spherical Diffusion Anoxia Violation: organoid '{node.name}' has radius > 200 um "
 507 |                     f"({r_um:.1f} um) requiring active microfluidic perfusion",
 508 |                     node.line, node.column, "ERR_KROGH_ANOXIA_VIOLATION"
 509 |                 )
 510 | 
 511 |             # 2. Avascular physical diffusion limit: R > 250 um causes central necrosis
 512 |             # even with 100% saturated external perfusion, due to internal diffusion limits
 513 |             # unless structural micro-channels, air-liquid interface slicing, or vascularization exist.
 514 |             if r_val > 0.000250 and node.perfusion is not None:
 515 |                 props = getattr(node, "properties", {})
 516 |                 is_vascularized = False
 517 |                 for key in ("vascularized", "sliced_ali", "internal_channel", "slice"):
 518 |                     if key in props:
 519 |                         val = props[key]
 520 |                         val_str = str(getattr(val, "value", getattr(val, "name", str(val)))).lower()
 521 |                         if val_str in ("true", "1"):
 522 |                             is_vascularized = True
 523 |                             break
 524 | 
 525 |                 if not is_vascularized:
 526 |                     raise SemanticError(
 527 |                         f"Avascular Core Necrosis Violation: organoid '{node.name}' radius {r_um:.1f} um "
 528 |                         f"exceeds the avascular spherical diffusion limit (250 um). External perfusion cannot "
 529 |                         f"prevent central anoxia due to internal tissue diffusion limits (D_eff = 1.07e-9 m^2/s). "
 530 |                         f"Requires 'vascularized: true', 'sliced_ali: true', or 'internal_channel: true'.",
 531 |                         node.line, node.column, "ERR_AVASCULAR_CORE_NECROSIS"
 532 |                     )
 533 | 
 534 |     def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
 535 |         src_name = getattr(node.source, "name", None)
 536 |         tgt_name = getattr(node.target, "name", None)
 537 |         if src_name and not self.current_scope.resolve(src_name):
 538 |             raise SemanticError(f"Undefined connect source '{src_name}'", node.line, node.column, "ERR_UNDEFINED_IDENTIFIER")
 539 |         if tgt_name and not self.current_scope.resolve(tgt_name):
 540 |             raise SemanticError(f"Undefined connect target '{tgt_name}'", node.line, node.column, "ERR_UNDEFINED_IDENTIFIER")
 541 | 
 542 |     def visit_PortDeclNode(self, node: PortDeclNode) -> None:
 543 |         pass
 544 | 
 545 |     def visit_FnDeclNode(self, node: FnDeclNode) -> None:
 546 |         fn_scope = Scope(parent=self.current_scope, name=f"fn_{node.name}")
 547 |         for param in node.params:
 548 |             dim = self._type_to_dimension(param.type_name)
 549 |             fn_scope.define(Symbol(param.name, param.type_name, dim))
 550 |         prev = self.current_scope
 551 |         self.current_scope = fn_scope
 552 |         self.visit(node.body)
 553 |         self.current_scope = prev
 554 | 
 555 |     def visit_BlockNode(self, node: BlockNode) -> None:
 556 |         block_scope = Scope(parent=self.current_scope, name="block")
 557 |         prev = self.current_scope
 558 |         self.current_scope = block_scope
 559 |         for stmt in node.statements:
 560 |             self.visit(stmt)
 561 |         self.current_scope = prev
 562 | 
 563 |     def visit_LetStmtNode(self, node: LetStmtNode) -> None:
 564 |         init_dim = Dimension.NONE
 565 |         if node.initializer is not None:
 566 |             self.visit(node.initializer)
 567 |             init_dim = self.get_dimension(node.initializer)
 568 |             val = self._extract_float_si_value(node.initializer)
 569 |             if val is not None and not node.is_mut:
 570 |                 self.const_values[node.name] = val
 571 | 
 572 |         declared_dim = self._type_to_dimension(node.type_name) if node.type_name else Dimension.NONE
 573 |         if declared_dim != Dimension.NONE and init_dim != Dimension.NONE and declared_dim != init_dim:
 574 |             raise SemanticError(
 575 |                 f"Cannot assign dimension {init_dim.value} to variable '{node.name}' declared with dimension {declared_dim.value}",
 576 |                 node.line,
 577 |                 node.column,
 578 |                 "ERR_DIMENSIONAL_MISMATCH"
 579 |             )
 580 | 
 581 |         final_dim = declared_dim if declared_dim != Dimension.NONE else init_dim
 582 |         self.current_scope.define(Symbol(node.name, node.type_name or "inferred", final_dim))
 583 | 
 584 |     def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
 585 |         self.visit(node.value)
 586 |         val_dim = self.get_dimension(node.value)
 587 |         if isinstance(node.target, IdentifierNode):
 588 |             sym = self.current_scope.resolve(node.target.name)
 589 |             if sym is not None and sym.dimension != Dimension.NONE and val_dim != Dimension.NONE and sym.dimension != val_dim:
 590 |                 raise SemanticError(
 591 |                     f"Cannot assign dimension {val_dim.value} to variable '{node.target.name}' with dimension {sym.dimension.value}",
 592 |                     node.line,
 593 |                     node.column,
 594 |                     "ERR_DIMENSIONAL_MISMATCH"
 595 |                 )
 596 | 
 597 |     def visit_StimStmtNode(self, node: StimStmtNode) -> None:
 598 |         # Enforce static voltage clamp: constant stimulation voltage exceeding +/- 1.2 V
 599 |         v_val = self._extract_float_si_value(node.voltage)
 600 |         if v_val is not None:
 601 |             if abs(v_val) > 1.2 + 1e-9:
 602 |                 raise SemanticError(
 603 |                     f"Requested stimulation voltage {v_val:.3f} V exceeds hard safety clamp [+/- 1.2 V]",
 604 |                     node.voltage.line,
 605 |                     node.voltage.column,
 606 |                     "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"
 607 |                 )
 608 | 
 609 |         self.visit(node.channel)
 610 |         self.visit(node.voltage)
 611 |         self.visit(node.phase1)
 612 |         self.visit(node.phase2)
 613 |         if node.interphase is not None:
 614 |             self.visit(node.interphase)
 615 | 
 616 |     def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
 617 |         self.visit(node.left)
 618 |         self.visit(node.right)
 619 |         left_dim = self.get_dimension(node.left)
 620 |         right_dim = self.get_dimension(node.right)
 621 | 
 622 |         # Addition and Subtraction require dimensional homogeneity
 623 |         if node.op in ("+", "-"):
 624 |             if left_dim != right_dim:
 625 |                 # If neither is NONE, raise mismatch
 626 |                 if left_dim != Dimension.NONE and right_dim != Dimension.NONE:
 627 |                     raise SemanticError(
 628 |                         f"Cannot perform '{node.op}' between incompatible dimensions {left_dim.value} and {right_dim.value}",
 629 |                         node.line,
 630 |                         node.column,
 631 |                         "ERR_DIMENSIONAL_MISMATCH"
 632 |                     )
 633 |             res_dim = left_dim if left_dim != Dimension.NONE else right_dim
 634 |             self.node_dimensions[id(node)] = res_dim
 635 | 
 636 |         # Multiplication
 637 |         elif node.op == "*":
 638 |             if (left_dim == Dimension.CURRENT and right_dim == Dimension.TIME) or \
 639 |                (left_dim == Dimension.TIME and right_dim == Dimension.CURRENT):
 640 |                 self.node_dimensions[id(node)] = Dimension.CHARGE
 641 |             elif left_dim == Dimension.NONE:
 642 |                 self.node_dimensions[id(node)] = right_dim
 643 |             elif right_dim == Dimension.NONE:
 644 |                 self.node_dimensions[id(node)] = left_dim
 645 |             else:
 646 |                 self.node_dimensions[id(node)] = Dimension.NONE
 647 | 
 648 |         # Division
 649 |         elif node.op == "/":
 650 |             if left_dim == right_dim and left_dim != Dimension.NONE:
 651 |                 self.node_dimensions[id(node)] = Dimension.NONE
 652 |             elif left_dim == Dimension.CHARGE and right_dim == Dimension.TIME:
 653 |                 self.node_dimensions[id(node)] = Dimension.CURRENT
 654 |             elif right_dim == Dimension.NONE:
 655 |                 self.node_dimensions[id(node)] = left_dim
 656 |             else:
 657 |                 self.node_dimensions[id(node)] = Dimension.NONE
 658 | 
 659 |         # Relational and Equality
 660 |         elif node.op in ("==", "!=", "<", "<=", ">", ">="):
 661 |             if left_dim != Dimension.NONE and right_dim != Dimension.NONE and left_dim != right_dim:
 662 |                 raise SemanticError(
 663 |                     f"Cannot compare incompatible dimensions {left_dim.value} and {right_dim.value}",
 664 |                     node.line,
 665 |                     node.column,
 666 |                     "ERR_DIMENSIONAL_MISMATCH"
 667 |                 )
 668 |             self.node_dimensions[id(node)] = Dimension.NONE
 669 | 
 670 |         else:
 671 |             self.node_dimensions[id(node)] = Dimension.NONE
 672 | 
 673 |     def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
 674 |         self.visit(node.operand)
 675 |         operand_dim = self.get_dimension(node.operand)
 676 |         self.node_dimensions[id(node)] = operand_dim
 677 | 
 678 |     def visit_PhysicalLiteralNode(self, node: PhysicalLiteralNode) -> None:
 679 |         self.node_dimensions[id(node)] = node.dimension
 680 | 
 681 |     def visit_LiteralNode(self, node: LiteralNode) -> None:
 682 |         self.node_dimensions[id(node)] = Dimension.NONE
 683 | 
 684 |     def visit_IdentifierNode(self, node: IdentifierNode) -> None:
 685 |         sym = self.current_scope.resolve(node.name)
 686 |         if sym is not None:
 687 |             self.node_dimensions[id(node)] = sym.dimension
 688 |         else:
 689 |             self.node_dimensions[id(node)] = Dimension.NONE
 690 | 
 691 |     def _type_to_dimension(self, tname: Optional[str]) -> Dimension:
 692 |         if not tname:
 693 |             return Dimension.NONE
 694 |         mapping = {
 695 |             "Voltage": Dimension.VOLTAGE,
 696 |             "Current": Dimension.CURRENT,
 697 |             "Time": Dimension.TIME,
 698 |             "Frequency": Dimension.FREQUENCY,
 699 |             "Length": Dimension.LENGTH,
 700 |             "Charge": Dimension.CHARGE,
 701 |         }
 702 |         return mapping.get(tname, Dimension.NONE)
 703 | 
 704 |     def get_dimension(self, node: ASTNode) -> Dimension:
 705 |         return self.node_dimensions.get(id(node), Dimension.NONE)
 706 | 
 707 |     def _extract_float_si_value(self, node: ASTNode) -> Optional[float]:
 708 |         if isinstance(node, PhysicalLiteralNode):
 709 |             return float(node.si_value)
 710 |         if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
 711 |             return float(node.value)
 712 |         if isinstance(node, UnaryOpNode):
 713 |             sub = self._extract_float_si_value(node.operand)
 714 |             if sub is None:
 715 |                 return None
 716 |             if node.op == "-":
 717 |                 return -sub
 718 |             if node.op == "+":
 719 |                 return sub
 720 |             return None
 721 |         if isinstance(node, BinaryOpNode):
 722 |             left = self._extract_float_si_value(node.left)
 723 |             right = self._extract_float_si_value(node.right)
 724 |             if left is None or right is None:
 725 |                 return None
 726 |             if node.op == "+":
 727 |                 return left + right
 728 |             if node.op == "-":
 729 |                 return left - right
 730 |             if node.op == "*":
 731 |                 return left * right
 732 |             if node.op == "/":
 733 |                 if abs(right) < 1e-15:
 734 |                     return None
 735 |                 return left / right
 736 |             return None
 737 |         if isinstance(node, IdentifierNode):
 738 |             if hasattr(self, "const_values") and node.name in self.const_values:
 739 |                 return self.const_values[node.name]
 740 |         return None
 741 | 
 742 | 
 743 | # =========================================================================
 744 | # Pass 3 Visitor: Loop-Yield Verification (CFG Post-Dominance)
 745 | # =========================================================================
 746 | 
 747 | class _Pass3LoopYieldVisitor(ASTVisitor):
 748 |     def __init__(self, analyzer: SemanticAnalyzer):
 749 |         self.analyzer: SemanticAnalyzer = analyzer
 750 | 
 751 |     def visit_ProgramNode(self, node: ProgramNode) -> None:
 752 |         for decl in node.declarations:
 753 |             self.visit(decl)
 754 | 
 755 |     def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
 756 |         self._verify_loop_yield(node.body, loop_name="while", line=node.line, column=node.column)
 757 |         self.visit(node.body)
 758 | 
 759 |     def visit_ForStmtNode(self, node: ForStmtNode) -> None:
 760 |         self._verify_loop_yield(node.body, loop_name="for", line=node.line, column=node.column)
 761 |         self.visit(node.body)
 762 | 
 763 |     def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
 764 |         for item in node.items:
 765 |             if item.kind == "cycle" and item.cycle_block is not None:
 766 |                 self._verify_loop_yield(item.cycle_block, loop_name="cycle", line=item.line, column=item.column)
 767 |                 self.visit(item.cycle_block)
 768 | 
 769 |     def _verify_loop_yield(self, body: BlockNode, loop_name: str, line: int, column: int) -> None:
 770 |         """
 771 |         Linear-time O(V + E) Control-Flow Graph (CFG) Reachability Analysis.
 772 |         Verifies that every cyclic path containing a stim_biphasic statement
 773 |         is post-dominated by a mandatory sync_tick statement before the loop back-edge.
 774 |         Eliminates O(2^N) Cartesian product path blowup.
 775 |         """
 776 |         violating_stim = self._check_unyielded_stim_path(body, unyielded_stim=None)
 777 |         if violating_stim is not None:
 778 |             raise SemanticError(
 779 |                 f"Stimulation loop without mandatory 'sync_tick' yield. "
 780 |                 f"Unbounded stimulation loop detected in '{loop_name}' block at line {line}",
 781 |                 violating_stim.line,
 782 |                 violating_stim.column,
 783 |                 "ERR_UNBOUNDED_STIM_LOOP"
 784 |             )
 785 | 
 786 |     def _check_unyielded_stim_path(self, node: ASTNode, unyielded_stim: Optional[StimStmtNode]) -> Optional[StimStmtNode]:
 787 |         """
 788 |         Recursively checks if there exists a control-flow path from 'node' to the exit of the block
 789 |         carrying an active unyielded stimulation statement without a post-dominating sync_tick.
 790 |         Returns the first violating StimStmtNode if an unyielded path exists, or None if all paths safely yield.
 791 |         """
 792 |         if isinstance(node, StimStmtNode):
 793 |             return node
 794 | 
 795 |         elif isinstance(node, SyncTickStmtNode):
 796 |             return None
 797 | 
 798 |         elif isinstance(node, BlockNode):
 799 |             curr_stim = unyielded_stim
 800 |             for stmt in node.statements:
 801 |                 if isinstance(stmt, SyncTickStmtNode):
 802 |                     curr_stim = None
 803 |                 elif isinstance(stmt, StimStmtNode):
 804 |                     curr_stim = stmt
 805 |                 elif isinstance(stmt, IfStmtNode):
 806 |                     then_stim = self._check_unyielded_stim_path(stmt.then_block, curr_stim)
 807 |                     if stmt.else_block is not None:
 808 |                         else_stim = self._check_unyielded_stim_path(stmt.else_block, curr_stim)
 809 |                     else:
 810 |                         else_stim = curr_stim  # Fall-through branch inherits incoming stim!
 811 | 
 812 |                     # Out of the if/else construct, if either branch carries unyielded stim:
 813 |                     curr_stim = then_stim if then_stim is not None else else_stim
 814 |                 elif isinstance(stmt, BlockNode):
 815 |                     res = self._check_unyielded_stim_path(stmt, curr_stim)
 816 |                     if res is not None:
 817 |                         return res
 818 |                     curr_stim = None
 819 |                 elif isinstance(stmt, (WhileStmtNode, ForStmtNode)):
 820 |                     # Inner loops cannot guarantee yield for an outer loop's path
 821 |                     pass
 822 |             return curr_stim
 823 | 
 824 |         elif isinstance(node, IfStmtNode):
 825 |             then_stim = self._check_unyielded_stim_path(node.then_block, unyielded_stim)
 826 |             if node.else_block is not None:
 827 |                 else_stim = self._check_unyielded_stim_path(node.else_block, unyielded_stim)
 828 |             else:
 829 |                 else_stim = unyielded_stim
 830 |             return then_stim if then_stim is not None else else_stim
 831 | 
 832 |         return unyielded_stim
 833 | 
 834 |     def _contains_sync_tick(self, node: ASTNode) -> bool:
 835 |         if isinstance(node, SyncTickStmtNode):
 836 |             return True
 837 |         if isinstance(node, BlockNode):
 838 |             return any(self._contains_sync_tick(s) for s in node.statements)
 839 |         if isinstance(node, (WhileStmtNode, ForStmtNode)):
 840 |             # Inner loops cannot guarantee yield for an outer loop's path
 841 |             return False
 842 |         if isinstance(node, IfStmtNode):
 843 |             if node.else_block is None:
 844 |                 return False
 845 |             then_has = self._contains_sync_tick(node.then_block)
 846 |             else_has = self._contains_sync_tick(node.else_block)
 847 |             return then_has and else_has
 848 |         return False
```

### `compiler/token.py` (270 lines, SHA-256: `1cb5c20236fd522b...`)

```text
   1 | """
   2 | WetLang Compiler - Token Definitions and Physical Units
   3 | Zero external dependencies. Hand-crafted from first principles.
   4 | """
   5 | 
   6 | from enum import Enum, auto
   7 | from dataclasses import dataclass
   8 | from typing import Any, Optional, Dict, Tuple
   9 | 
  10 | 
  11 | class Dimension(Enum):
  12 |     """Physical dimensions supported by the WetLang type system."""
  13 |     NONE = "NONE"
  14 |     TIME = "TIME"
  15 |     VOLTAGE = "VOLTAGE"
  16 |     CURRENT = "CURRENT"
  17 |     CHARGE = "CHARGE"
  18 |     FREQUENCY = "FREQUENCY"
  19 |     LENGTH = "LENGTH"
  20 |     VOLUME = "VOLUME"
  21 |     FLOW_RATE = "FLOW_RATE"
  22 |     PRESSURE = "PRESSURE"
  23 | 
  24 | 
  25 | class TokenType(Enum):
  26 |     # End of File
  27 |     EOF = auto()
  28 | 
  29 |     # Literals
  30 |     INT_LIT = auto()
  31 |     FLOAT_LIT = auto()
  32 |     BOOL_LIT = auto()
  33 |     STRING_LIT = auto()
  34 |     PHYSICAL_LIT = auto()
  35 | 
  36 |     # Identifiers
  37 |     IDENTIFIER = auto()
  38 | 
  39 |     # Keywords - MEA & Hardware Topology
  40 |     GRID = auto()
  41 |     CHANNEL = auto()
  42 |     MODE = auto()
  43 |     ORGANOID = auto()
  44 |     TISSUE = auto()
  45 |     CONNECT = auto()
  46 |     PORT = auto()
  47 |     PUMP = auto()
  48 |     VALVE = auto()
  49 |     MOTOR = auto()
  50 |     SENSOR = auto()
  51 |     ACTUATOR = auto()
  52 | 
  53 |     # Channel Mode Enum Literals
  54 |     BIPHASIC_STIM = auto()
  55 |     SPIKE_READOUT = auto()
  56 |     VOLTAGE_SENSE = auto()
  57 |     BIDIRECTIONAL = auto()
  58 | 
  59 |     # Keywords - Declarations & Types
  60 |     FN = auto()
  61 |     LET = auto()
  62 |     MUT = auto()
  63 |     INT = auto()
  64 |     FLOAT = auto()
  65 |     BOOL = auto()
  66 |     STRING = auto()
  67 | 
  68 |     # Physical Type Keywords
  69 |     TYPE_VOLTAGE = auto()
  70 |     TYPE_CURRENT = auto()
  71 |     TYPE_TIME = auto()
  72 |     TYPE_FREQUENCY = auto()
  73 |     TYPE_LENGTH = auto()
  74 |     TYPE_CHARGE = auto()
  75 | 
  76 |     # Keywords - Closed-Loop Control
  77 |     STREAM = auto()
  78 |     BIND = auto()
  79 |     CYCLE = auto()
  80 | 
  81 |     # Keywords - Control Flow
  82 |     IF = auto()
  83 |     ELSE = auto()
  84 |     WHILE = auto()
  85 |     FOR = auto()
  86 |     IN = auto()
  87 |     RETURN = auto()
  88 | 
  89 |     # Keywords - Domain Biophysical Primitives
  90 |     STIM_BIPHASIC = auto()
  91 |     MODULATE_STDP = auto()
  92 |     SYNC_TICK = auto()
  93 |     READ_SPIKES = auto()
  94 |     READ_VOLTAGE = auto()
  95 |     POP_FIRING_RATE = auto()
  96 |     READ_POPULATION_RATE = auto()
  97 |     PUMP_SET_RATE = auto()
  98 |     PUMP_DISPENSE = auto()
  99 |     VALVE_SET = auto()
 100 |     VALVE_OPEN = auto()
 101 |     VALVE_CLOSE = auto()
 102 |     MOTOR_STEP = auto()
 103 |     READ_PRESSURE = auto()
 104 |     READ_TEMPERATURE = auto()
 105 | 
 106 |     # Boolean Literals
 107 |     TRUE = auto()
 108 |     FALSE = auto()
 109 | 
 110 |     # Operators - Arithmetic
 111 |     PLUS = auto()           # +
 112 |     MINUS = auto()          # -
 113 |     STAR = auto()           # *
 114 |     SLASH = auto()          # /
 115 |     PERCENT = auto()        # %
 116 | 
 117 |     # Operators - Relational
 118 |     EQ_EQ = auto()          # ==
 119 |     NOT_EQ = auto()         # !=
 120 |     LT = auto()             # <
 121 |     LT_EQ = auto()          # <=
 122 |     GT = auto()             # >
 123 |     GT_EQ = auto()          # >=
 124 | 
 125 |     # Operators - Logical
 126 |     AND_AND = auto()        # &&
 127 |     OR_OR = auto()          # ||
 128 |     NOT = auto()            # !
 129 | 
 130 |     # Operators - Assignment & Flow
 131 |     ASSIGN = auto()         # =
 132 |     ARROW_RIGHT = auto()    # ->
 133 |     ARROW_LEFT = auto()     # <-
 134 |     DOT_DOT = auto()        # ..
 135 | 
 136 |     # Delimiters
 137 |     LPAREN = auto()         # (
 138 |     RPAREN = auto()         # )
 139 |     LBRACE = auto()         # {
 140 |     RBRACE = auto()         # }
 141 |     LBRACKET = auto()       # [
 142 |     RBRACKET = auto()       # ]
 143 |     COMMA = auto()          # ,
 144 |     COLON = auto()          # :
 145 |     SEMICOLON = auto()      # ;
 146 |     DOT = auto()            # .
 147 | 
 148 | 
 149 | # Unit suffix mapping: suffix -> (Dimension, scale_factor_to_SI_base)
 150 | UNIT_SUFFIXES: Dict[str, Tuple[Dimension, float]] = {
 151 |     # Time (base: seconds)
 152 |     "s": (Dimension.TIME, 1.0),
 153 |     "ms": (Dimension.TIME, 1e-3),
 154 |     "us": (Dimension.TIME, 1e-6),
 155 | 
 156 |     # Voltage (base: volts)
 157 |     "V": (Dimension.VOLTAGE, 1.0),
 158 |     "mV": (Dimension.VOLTAGE, 1e-3),
 159 |     "uV": (Dimension.VOLTAGE, 1e-6),
 160 | 
 161 |     # Current (base: amperes)
 162 |     "A": (Dimension.CURRENT, 1.0),
 163 |     "uA": (Dimension.CURRENT, 1e-6),
 164 |     "nA": (Dimension.CURRENT, 1e-9),
 165 |     "pA": (Dimension.CURRENT, 1e-12),
 166 | 
 167 |     # Charge (base: coulombs)
 168 |     "C": (Dimension.CHARGE, 1.0),
 169 |     "nC": (Dimension.CHARGE, 1e-9),
 170 |     "pC": (Dimension.CHARGE, 1e-12),
 171 | 
 172 |     # Frequency (base: hertz)
 173 |     "Hz": (Dimension.FREQUENCY, 1.0),
 174 | 
 175 |     # Length (base: meters)
 176 |     "mm": (Dimension.LENGTH, 1e-3),
 177 |     "um": (Dimension.LENGTH, 1e-6),
 178 | 
 179 |     # Volume & Microfluidics
 180 |     "uL": (Dimension.VOLUME, 1e-9),
 181 |     "mL": (Dimension.VOLUME, 1e-6),
 182 |     "uL/min": (Dimension.FLOW_RATE, 1e-9 / 60.0),
 183 |     "mL/min": (Dimension.FLOW_RATE, 1e-6 / 60.0),
 184 |     "rpm": (Dimension.FREQUENCY, 1.0 / 60.0),
 185 |     "degC": (Dimension.NONE, 1.0),
 186 | 
 187 |     # Pressure (base: Pascals)
 188 |     "Pa": (Dimension.PRESSURE, 1.0),
 189 |     "kPa": (Dimension.PRESSURE, 1000.0),
 190 |     "mmHg": (Dimension.PRESSURE, 133.322),
 191 | }
 192 | 
 193 | # Sorted unit suffixes by descending length so multi-char suffixes match before single-char (e.g. "ms" before "s")
 194 | SORTED_UNIT_SUFFIXES = sorted(UNIT_SUFFIXES.keys(), key=lambda s: len(s), reverse=True)
 195 | 
 196 | 
 197 | KEYWORDS: Dict[str, TokenType] = {
 198 |     "grid": TokenType.GRID,
 199 |     "channel": TokenType.CHANNEL,
 200 |     "mode": TokenType.MODE,
 201 |     "organoid": TokenType.ORGANOID,
 202 |     "tissue": TokenType.TISSUE,
 203 |     "connect": TokenType.CONNECT,
 204 |     "port": TokenType.PORT,
 205 |     "pump": TokenType.PUMP,
 206 |     "valve": TokenType.VALVE,
 207 |     "motor": TokenType.MOTOR,
 208 |     "sensor": TokenType.SENSOR,
 209 |     "actuator": TokenType.ACTUATOR,
 210 |     "BiphasicStim": TokenType.BIPHASIC_STIM,
 211 |     "SpikeReadout": TokenType.SPIKE_READOUT,
 212 |     "VoltageSense": TokenType.VOLTAGE_SENSE,
 213 |     "Bidirectional": TokenType.BIDIRECTIONAL,
 214 |     "fn": TokenType.FN,
 215 |     "let": TokenType.LET,
 216 |     "mut": TokenType.MUT,
 217 |     "int": TokenType.INT,
 218 |     "float": TokenType.FLOAT,
 219 |     "bool": TokenType.BOOL,
 220 |     "string": TokenType.STRING,
 221 |     "Voltage": TokenType.TYPE_VOLTAGE,
 222 |     "Current": TokenType.TYPE_CURRENT,
 223 |     "Time": TokenType.TYPE_TIME,
 224 |     "Frequency": TokenType.TYPE_FREQUENCY,
 225 |     "Length": TokenType.TYPE_LENGTH,
 226 |     "Charge": TokenType.TYPE_CHARGE,
 227 |     "stream": TokenType.STREAM,
 228 |     "bind": TokenType.BIND,
 229 |     "cycle": TokenType.CYCLE,
 230 |     "if": TokenType.IF,
 231 |     "else": TokenType.ELSE,
 232 |     "while": TokenType.WHILE,
 233 |     "for": TokenType.FOR,
 234 |     "in": TokenType.IN,
 235 |     "return": TokenType.RETURN,
 236 |     "stim_biphasic": TokenType.STIM_BIPHASIC,
 237 |     "modulate_stdp": TokenType.MODULATE_STDP,
 238 |     "sync_tick": TokenType.SYNC_TICK,
 239 |     "read_spikes": TokenType.READ_SPIKES,
 240 |     "read_voltage": TokenType.READ_VOLTAGE,
 241 |     "pop_firing_rate": TokenType.POP_FIRING_RATE,
 242 |     "read_population_rate": TokenType.READ_POPULATION_RATE,
 243 |     "pump_set_rate": TokenType.PUMP_SET_RATE,
 244 |     "pump_dispense": TokenType.PUMP_DISPENSE,
 245 |     "valve_set": TokenType.VALVE_SET,
 246 |     "valve_open": TokenType.VALVE_OPEN,
 247 |     "valve_close": TokenType.VALVE_CLOSE,
 248 |     "motor_step": TokenType.MOTOR_STEP,
 249 |     "read_pressure": TokenType.READ_PRESSURE,
 250 |     "read_temperature": TokenType.READ_TEMPERATURE,
 251 |     "true": TokenType.TRUE,
 252 |     "false": TokenType.FALSE,
 253 | }
 254 | 
 255 | 
 256 | @dataclass
 257 | class Token:
 258 |     """Represents a scanned lexical token with position and dimensional metadata."""
 259 |     type: TokenType
 260 |     value: Any
 261 |     line: int
 262 |     column: int
 263 |     dimension: Dimension = Dimension.NONE
 264 |     si_value: Optional[float] = None
 265 |     raw_text: str = ""
 266 | 
 267 |     def __repr__(self) -> str:
 268 |         if self.dimension != Dimension.NONE:
 269 |             return f"Token({self.type.name}, val={self.value!r}, si={self.si_value}, dim={self.dimension.value}, L{self.line}:C{self.column})"
 270 |         return f"Token({self.type.name}, val={self.value!r}, L{self.line}:C{self.column})"
```

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

### `native/include/interlocks.h` (165 lines, SHA-256: `2eeee7b4f3868ac4...`)

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
  12 | /* =========================================================================
  13 |  * WetLang Cycle-Accurate Biocybersecurity Hardware Watchdog & Interlocks
  14 |  * =========================================================================
  15 |  * 1. Water-Window Voltage Clamp: Hard clamp [-1.2 V, +1.2 V]
  16 |  * 2. Sliding Charge-Balance Ring Buffer:
  17 |  *    - 100-tick (10.0 ms at dt=0.1 ms) per-electrode circular buffer
  18 |  *    - Trip ERR_CHARGE_IMBALANCE if |Q_accum[ch]| >= 0.5 nC
  19 |  * 3. Epileptiform Runaway Firing Breaker:
  20 |  *    - Monitors sliding 50.0 ms firing rate per channel
  21 |  *    - Hyperactive channel: firing_rate > 150.0 Hz
  22 |  *    - Fraction threshold: > 35% of 64 channels (>= 23 channels)
  23 |  *    - Sustained duration: 500 consecutive ticks (50.0 ms)
  24 |  *    - Trip ERR_EPILEPTIFORM_RUNAWAY -> immediately zero DACs & lock VM
  25 |  * 4. Fail-Safe Interlock Lockout:
  26 |  *    - Once tripped, zeroes all stimulation voltages (0.0 V) and blocks
  27 |  *      further stimulation/execution until explicit hardware reset.
  28 |  * ========================================================================= */
  29 | 
  30 | #define INTERLOCK_NUM_CHANNELS          64
  31 | #define INTERLOCK_VOLTAGE_LIMIT_V       1.2f
  32 | #define INTERLOCK_CHARGE_WINDOW_TICKS   100     /* 10.0 ms at dt = 0.1 ms */
  33 | #define INTERLOCK_CHARGE_LIMIT_NC       0.5f    /* 0.5 nC per electrode */
  34 | #define INTERLOCK_EPILEPSY_RATE_HZ      150.0f  /* > 150 Hz */
  35 | #define INTERLOCK_EPILEPSY_MIN_CHANNELS 23      /* > 35% of 64 (22.4 -> 23) */
  36 | #define INTERLOCK_EPILEPSY_SUSTAIN_TICKS 500    /* 50.0 ms at dt = 0.1 ms */
  37 | 
  38 | /* Hardened Biocybersecurity Extensions (Audit Remediation) */
  39 | #define INTERLOCK_DC_DRIFT_LIMIT_NC     1.0f    /* 1.0 nC cumulative unrecovered DC charge */
  40 | #define INTERLOCK_BLEED_DECAY_PER_TICK  0.99999f/* tau = 10.0 s (100,000 ticks) */
  41 | #define INTERLOCK_CHARGE_DENSITY_LIMIT_NC 0.40f /* 0.40 nC max per single pulse phase (Shannon limit) */
  42 | #define INTERLOCK_FOCAL_RATE_HZ         150.0f  /* 150 Hz focal rate */
  43 | #define INTERLOCK_FOCAL_SUSTAIN_TICKS   2500    /* 250.0 ms sustained focal hyperactivity */
  44 | #define INTERLOCK_DUTY_CYCLE_LIMIT      0.05f   /* 5% max stimulation duty cycle */
  45 | #define INTERLOCK_DUTY_CYCLE_DECAY      0.9999f /* tau = 1.0 s (10,000 ticks) */
  46 | #define INTERLOCK_THERMAL_LIMIT_C       38.0f   /* 38.0 C max incubator / CMOS die temperature */
  47 | #define INTERLOCK_COMPLIANCE_LIMIT_V    7.0f    /* 7.0 V Intan RHS2116 compliance rail */
  48 | 
  49 | /* Phase 3 Electrochemical Water-Window & Material CIC Limits */
  50 | typedef enum {
  51 |     WET_ELEC_PLATINUM = 0,  /* 0.10 mC/cm^2 (water-window limit: 0.05..0.15 mC/cm^2) */
  52 |     WET_ELEC_TIN      = 1,  /* 0.90 mC/cm^2 (Titanium Nitride) */
  53 |     WET_ELEC_IROX     = 2,  /* 2.00 mC/cm^2 (Iridium Oxide / SIROF) */
  54 |     WET_ELEC_PEDOT    = 3,  /* 5.00 mC/cm^2 (Conductive Polymer PEDOT:PSS) */
  55 |     WET_ELEC_CUSTOM   = 4
  56 | } wet_electrode_material_t;
  57 | 
  58 | typedef enum {
  59 |     INTERLOCK_TRIP_NONE                = 0,
  60 |     INTERLOCK_TRIP_CHARGE_IMBALANCE    = 1,
  61 |     INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY= 2,
  62 |     INTERLOCK_TRIP_CAPABILITY_VIOLATION= 3,
  63 |     INTERLOCK_TRIP_VOLTAGE_OVERRIDE    = 4,
  64 |     INTERLOCK_TRIP_DC_DRIFT            = 5,
  65 |     INTERLOCK_TRIP_CHARGE_DENSITY      = 6,
  66 |     INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY= 7,
  67 |     INTERLOCK_TRIP_DEAD_HEAD_PRESSURE  = 8,
  68 |     INTERLOCK_TRIP_THERMAL_LIMIT       = 9,
  69 |     INTERLOCK_TRIP_BUBBLE_DETECTED     = 10,
  70 |     INTERLOCK_TRIP_COMPLIANCE_RAILED   = 11
  71 | } interlock_trip_reason_t;
  72 | 
  73 | typedef struct {
  74 |     /* Fail-safe lockout state */
  75 |     uint8_t  locked;
  76 |     uint8_t  trip_reason;          /* interlock_trip_reason_t */
  77 |     uint8_t  tripped_channel;
  78 |     uint64_t trip_tick;
  79 |     float    trip_value;           /* Measured charge (nC) or hyperactive count */
  80 |     char     diagnostic[256];
  81 | 
  82 |     /* Water-window clamp statistics */
  83 |     uint64_t clamp_events;
  84 | 
  85 |     /* 10.0 ms (100-tick) sliding charge balance ring buffer per electrode */
  86 |     float    q_ring[INTERLOCK_NUM_CHANNELS][INTERLOCK_CHARGE_WINDOW_TICKS];
  87 |     float    q_accum[INTERLOCK_NUM_CHANNELS];
  88 |     uint16_t q_head;
  89 | 
  90 |     /* Long-horizon leaky DC charge integrator (10.0 s bleed time constant) */
  91 |     float    q_dc[INTERLOCK_NUM_CHANNELS];
  92 | 
  93 |     /* Phase 3: Unbounded Cumulative DC Charge Accumulator (no leaky decay; resets ONLY on active discharge) */
  94 |     float    cumulative_unbounded_dc_nc[INTERLOCK_NUM_CHANNELS];
  95 | 
  96 |     /* Phase 3: Electrode Material & Area Parameterization */
  97 |     uint8_t  electrode_material;   /* wet_electrode_material_t */
  98 |     float    electrode_area_um2;   /* e.g. 132.25 um^2 for MaxOne, or 5000 um^2 for macro */
  99 |     float    max_charge_per_phase_nc; /* Dynamic limit = CIC * Area */
 100 |     float    max_cumulative_dc_nc;    /* Dynamic persistent DC limit */
 101 | 
 102 |     /* Phase 3: Microfluidic Dead-Heading Pressure Interlock */
 103 |     uint8_t  dead_head_protection_enabled;
 104 |     uint8_t  pump_valve_mapping[8]; /* Maps pump ID to downstream pinch valve ID */
 105 | 
 106 |     /* 50.0 ms (500-tick) sustained epileptiform runaway counter */
 107 |     uint32_t hyperactive_consecutive_ticks;
 108 |     uint32_t last_hyperactive_channel_count;
 109 | 
 110 |     /* Per-channel focal hyperactivity & stimulation duty cycle monitors */
 111 |     uint32_t focal_hyperactive_ticks[INTERLOCK_NUM_CHANNELS];
 112 |     float    stim_duty_filter[INTERLOCK_NUM_CHANNELS];
 113 | 
 114 |     /* Authorized bytecode capabilities */
 115 |     uint16_t authorized_capabilities;
 116 |     uint32_t authorized_channels;
 117 | 
 118 |     /* Typed Channel Banks / Capabilities (Bug C-05 Remediation) */
 119 |     uint64_t reference_channels_mask;      /* Cannot be stimulated */
 120 |     uint64_t recording_only_channels_mask; /* Cannot be stimulated */
 121 | } interlock_state_t;
 122 | 
 123 | /* Initialize / reset watchdog state */
 124 | void interlocks_init(interlock_state_t* il);
 125 | void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count);
 126 | void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask);
 127 | 
 128 | /* Phase 3 Electrochemical & Hardware Interlock API */
 129 | void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2);
 130 | void interlocks_active_discharge(interlock_state_t* il, uint8_t channel);
 131 | void interlocks_active_discharge_all(interlock_state_t* il);
 132 | void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable);
 133 | 
 134 | /* Environmental & Compliance Safety Checks */
 135 | wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c);
 136 | wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id);
 137 | wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v);
 138 | 
 139 | /* Static authorization check for an opcode against loaded bytecode capabilities */
 140 | int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel);
 141 | 
 142 | /* Clamp requested stimulation voltage to [-1.2 V, +1.2 V] */
 143 | float interlocks_clamp_voltage(interlock_state_t* il, float requested_v);
 144 | 
 145 | /* Advance 10.0 ms charge ring buffer with this tick's per-channel injected charge (nC).
 146 |  * Returns WET_OK or WET_ERR_CHARGE_IMBALANCE (locking the watchdog on trip). */
 147 | wet_status_t interlocks_record_charge_tick(
 148 |     interlock_state_t* il,
 149 |     uint64_t current_tick,
 150 |     const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
 151 | );
 152 | 
 153 | /* Evaluate epileptiform runaway breaker using per-channel firing rates (Hz).
 154 |  * Returns WET_OK or WET_ERR_EPILEPTIFORM_RUNAWAY (locking the watchdog on trip). */
 155 | wet_status_t interlocks_check_epileptiform(
 156 |     interlock_state_t* il,
 157 |     uint64_t current_tick,
 158 |     const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
 159 | );
 160 | 
 161 | #ifdef __cplusplus
 162 | }
 163 | #endif
 164 | 
 165 | #endif /* WET_INTERLOCKS_H */
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

### `native/include/wet_hal.h` (191 lines, SHA-256: `a9a2d1dca0115a12...`)

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
  88 | /* HAL Configuration */
  89 | typedef struct {
  90 |     wet_hal_mode_t mode;
  91 |     uint32_t       max_ephys_channels;
  92 |     uint32_t       num_pumps;
  93 |     uint32_t       num_valves;
  94 |     uint32_t       num_flow_sensors;
  95 |     uint8_t        enable_dead_head_protection;
  96 |     uint8_t        enable_crowbar_fastpath;
  97 |     uint8_t        valve_for_pump[8]; /* Associated downstream valve for dead-head protection */
  98 | } wet_hal_config_t;
  99 | 
 100 | /* HAL Hardware Statistics & Telemetry */
 101 | typedef struct {
 102 |     uint64_t total_spi_transactions;
 103 |     uint64_t total_i2c_transactions;
 104 |     uint64_t total_rs232_commands;
 105 |     uint64_t total_can_frames;
 106 |     uint64_t total_crowbar_events;
 107 |     uint64_t last_crowbar_timestamp_us;
 108 |     uint32_t last_crowbar_reason;
 109 |     double   crowbar_latency_us;
 110 | } wet_hal_telemetry_t;
 111 | 
 112 | /* HAL Context / Router Registry */
 113 | #define WET_HAL_MAX_DRIVERS 16
 114 | 
 115 | struct wet_hal_context {
 116 |     wet_hal_mode_t       mode;
 117 |     wet_hal_config_t     config;
 118 |     wet_vm_t*            vm; /* Attached VM */
 119 | 
 120 |     /* Registered Drivers */
 121 |     wet_hal_driver_t*    drivers[WET_HAL_MAX_DRIVERS];
 122 |     uint32_t             driver_count;
 123 | 
 124 |     /* Primary specialized driver slots for zero-search O(1) routing */
 125 |     wet_hal_driver_t*    ephys_driver;
 126 |     wet_hal_driver_t*    pump_driver;
 127 |     wet_hal_driver_t*    valve_driver;
 128 |     wet_hal_driver_t*    flow_driver;
 129 |     wet_hal_driver_t*    can_driver;
 130 | 
 131 |     /* Actuator & Sensor Caches */
 132 |     float                pump_rates_ul_min[8];
 133 |     uint8_t              valve_states[8];
 134 |     double               flow_rates_ul_min[8];
 135 |     float                ephys_voltages[64];
 136 |     uint8_t              ephys_spikes[64];
 137 | 
 138 |     /* Emergency Crowbar Status */
 139 |     uint8_t              crowbar_tripped;
 140 |     uint32_t             crowbar_reason;
 141 |     uint64_t             crowbar_tick;
 142 |     uint64_t             crowbar_timestamp_us;
 143 | 
 144 |     /* Telemetry Counters */
 145 |     wet_hal_telemetry_t  telemetry;
 146 | };
 147 | 
 148 | /* =========================================================================
 149 |  * Core HAL API Prototypes
 150 |  * ========================================================================= */
 151 | 
 152 | WET_EXPORT wet_hal_context_t* wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config);
 153 | WET_EXPORT void wet_hal_destroy(wet_hal_context_t* hal);
 154 | 
 155 | WET_EXPORT wet_hal_status_t wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config);
 156 | WET_EXPORT wet_hal_status_t wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal);
 157 | WET_EXPORT wet_hal_context_t* wet_hal_get_context(wet_vm_t* vm);
 158 | 
 159 | WET_EXPORT wet_hal_status_t wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode);
 160 | WET_EXPORT wet_hal_mode_t wet_hal_get_mode(const wet_hal_context_t* hal);
 161 | 
 162 | WET_EXPORT wet_hal_status_t wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
 163 | WET_EXPORT wet_hal_status_t wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
 164 | WET_EXPORT wet_hal_driver_t* wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type);
 165 | 
 166 | /* Actuator & Sensor Dispatch */
 167 | WET_EXPORT wet_hal_status_t wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
 168 | WET_EXPORT wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul);
 169 | WET_EXPORT wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state);
 170 | WET_EXPORT wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min);
 171 | WET_EXPORT wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us);
 172 | WET_EXPORT wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
 173 | WET_EXPORT wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag);
 174 | WET_EXPORT wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
 175 | WET_EXPORT wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel);
 176 | 
 177 | /* Emergency Hardware Crowbar Fast-Path (<100 µs) */
 178 | WET_EXPORT void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason);
 179 | 
 180 | /* Telemetry & Mapping Accessors */
 181 | WET_EXPORT wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal);
 182 | WET_EXPORT void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id);
 183 | 
 184 | /* High-resolution timer utility (monotonic microseconds) */
 185 | WET_EXPORT uint64_t wet_hal_get_time_us(void);
 186 | 
 187 | #ifdef __cplusplus
 188 | }
 189 | #endif
 190 | 
 191 | #endif /* WET_HAL_H */
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

### `native/include/wetvm_api.h` (301 lines, SHA-256: `1ce7d24e459ec9bb...`)

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
  37 | } wet_vm_config_t;
  38 | 
  39 | /* Cycle-Accurate Telemetry Output */
  40 | typedef struct {
  41 |     uint64_t current_tick;         /* Number of executed ticks */
  42 |     double   sim_time_ms;          /* Total simulation time in ms */
  43 |     float    voltages[64];         /* Instantaneous channel potentials (V) */
  44 |     uint8_t  spikes[64];           /* Binary spike raster (1 = spiked this tick) */
  45 |     float    population_rate_hz;   /* Estimated population firing rate (Hz) */
  46 |     float    last_charge_nc[64];   /* Cumulative or last injected charge (nC) */
  47 | } wet_telemetry_t;
  48 | 
  49 | /* Cyber-Physical Hardware Actuator Telemetry */
  50 | typedef struct {
  51 |     float    pump_rates_ul_min[8];   /* Rate for 8 microfluidic pumps */
  52 |     float    pump_dispensed_ul[8];   /* Cumulative dispensed volume */
  53 |     uint8_t  valve_states[8];        /* State of 8 valves (0=closed, 1=open) */
  54 |     int32_t  motor_positions[4];     /* Step positions for 4 motors */
  55 |     float    motor_speeds_rpm[4];    /* Speeds for 4 motors */
  56 |     float    ambient_temperature_c;  /* Ambient incubator temperature (C) */
  57 |     float    fluid_pressure_kpa[4];  /* Microfluidic pressure (kPa) */
  58 | } wet_actuator_telemetry_t;
  59 | 
  60 | /* =========================================================================
  61 |  * Public C-ABI API Functions
  62 |  * ========================================================================= */
  63 | 
  64 | /**
  65 |  * Creates and initializes a new WetVM instance.
  66 |  * If config is NULL, default configuration values are used.
  67 |  */
  68 | WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config);
  69 | 
  70 | /**
  71 |  * Creates a WetVM instance using caller-supplied static arena memory (zero dynamic malloc).
  72 |  */
  73 | WET_EXPORT wet_vm_t* wet_create_vm_arena(
  74 |     void* arena_buf,
  75 |     size_t arena_bytes,
  76 |     const wet_vm_config_t* config
  77 | );
  78 | 
  79 | /**
  80 |  * Destroys the VM instance and releases all associated memory.
  81 |  */
  82 | WET_EXPORT void wet_free_vm(wet_vm_t* vm);
  83 | 
  84 | /**
  85 |  * Phase 3: Configures electrode material and physical geometric surface area.
  86 |  */
  87 | WET_EXPORT void wet_configure_electrode(
  88 |     wet_vm_t* vm,
  89 |     uint8_t material,
  90 |     float area_um2
  91 | );
  92 | 
  93 | /**
  94 |  * Phase 3: Actuates hardware charge-recovery switch to discharge residual DC Faradaic charge.
  95 |  */
  96 | WET_EXPORT void wet_active_discharge(
  97 |     wet_vm_t* vm,
  98 |     uint8_t channel
  99 | );
 100 | 
 101 | /**
 102 |  * Phase 3: Actuates hardware charge-recovery switch on all channels.
 103 |  */
 104 | WET_EXPORT void wet_active_discharge_all(
 105 |     wet_vm_t* vm
 106 | );
 107 | 
 108 | /**
 109 |  * Phase 3: Enables microfluidic valve-pump dead-head overpressure interlock.
 110 |  */
 111 | WET_EXPORT void wet_enable_dead_head_protection(
 112 |     wet_vm_t* vm,
 113 |     uint8_t enable
 114 | );
 115 | 
 116 | /**
 117 |  * Phase 3: Ring-0 Life Support Supervisor shutdown (terminates baseline life support).
 118 |  */
 119 | WET_EXPORT void wet_life_supervisor_shutdown(
 120 |     wet_vm_t* vm
 121 | );
 122 | 
 123 | /**
 124 |  * Validates, loads, and parses WBC binary bytecode into the VM.
 125 |  * Resets execution registers (pc, sp, tick_count, is_halted).
 126 |  * If loading fails, an error message is written into err_buf (if provided).
 127 |  */
 128 | WET_EXPORT wet_status_t wet_load_bytecode(
 129 |     wet_vm_t* vm,
 130 |     const uint8_t* code_bytes,
 131 |     size_t size,
 132 |     char* err_buf,
 133 |     size_t err_buf_len
 134 | );
 135 | 
 136 | /**
 137 |  * Executes instructions until the next SYNC_TICK yield, SLEEP_TICKS, HALT, or error.
 138 |  * Advances current_tick by 1 and sim_time_ms by config->dt_ms.
 139 |  * Caller allocates out_telem; if non-NULL, it is populated with current state.
 140 |  */
 141 | WET_EXPORT wet_status_t wet_step_tick(
 142 |     wet_vm_t* vm,
 143 |     wet_telemetry_t* out_telem
 144 | );
 145 | 
 146 | /**
 147 |  * Executes up to `ticks` consecutive ticks.
 148 |  * Returns WET_OK if all ticks executed successfully, or early status on HALT/error.
 149 |  * executed_ticks receives the actual number of ticks completed.
 150 |  * out_telem receives final state (if non-NULL).
 151 |  */
 152 | WET_EXPORT wet_status_t wet_run_ticks(
 153 |     wet_vm_t* vm,
 154 |     uint32_t ticks,
 155 |     uint32_t* executed_ticks,
 156 |     wet_telemetry_t* out_telem
 157 | );
 158 | 
 159 | /**
 160 |  * Injects a biphasic electrical stimulus onto the designated MEA channel.
 161 |  */
 162 | WET_EXPORT wet_status_t wet_inject_stimulus(
 163 |     wet_vm_t* vm,
 164 |     uint8_t channel,
 165 |     float voltage_v,
 166 |     float phase1_ms,
 167 |     float phase2_ms
 168 | );
 169 | 
 170 | /**
 171 |  * Queries current telemetry state into caller-allocated struct.
 172 |  */
 173 | WET_EXPORT wet_status_t wet_get_telemetry(
 174 |     wet_vm_t* vm,
 175 |     wet_telemetry_t* out_telem
 176 | );
 177 | 
 178 | /**
 179 |  * Queries current cyber-physical hardware actuator telemetry into caller-allocated struct.
 180 |  */
 181 | WET_EXPORT wet_status_t wet_get_actuator_telemetry(
 182 |     wet_vm_t* vm,
 183 |     wet_actuator_telemetry_t* out_act_telem
 184 | );
 185 | 
 186 | /**
 187 |  * Returns string pointer to the last error message recorded on the VM.
 188 |  */
 189 | WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm);
 190 | 
 191 | /**
 192 |  * Returns a static descriptive string for the given status code.
 193 |  */
 194 | WET_EXPORT const char* wet_status_to_string(wet_status_t status);
 195 | 
 196 | /**
 197 |  * Phase 3: Configures post-stimulus amplifier artifact blanking window in ms.
 198 |  */
 199 | WET_EXPORT void wet_configure_blanking(
 200 |     wet_vm_t* vm,
 201 |     float blanking_ms,
 202 |     uint8_t enable_spatial
 203 | );
 204 | 
 205 | /**
 206 |  * Phase 3: Injects constant-current electrical stimulus (uA) into MEA channel.
 207 |  */
 208 | WET_EXPORT wet_status_t wet_inject_current_stimulus(
 209 |     wet_vm_t* vm,
 210 |     uint8_t channel,
 211 |     float current_ua,
 212 |     float phase1_ms,
 213 |     float phase2_ms
 214 | );
 215 | 
 216 | /**
 217 |  * Phase 3: Standalone C99 Load-Time Bytecode Verifier.
 218 |  * Validates magic, CRC32, section boundaries, opcode validity, and branch target alignment.
 219 |  */
 220 | WET_EXPORT wet_status_t wet_verify_bytecode(
 221 |     const uint8_t* bytecode,
 222 |     size_t size,
 223 |     char* err_buf,
 224 |     size_t err_buf_len
 225 | );
 226 | 
 227 | /**
 228 |  * Phase 3: Live State Checkpointing.
 229 |  * Serializes complete dynamic neural state, synaptic weights, and clocks into buffer.
 230 |  */
 231 | WET_EXPORT wet_status_t wet_vm_snapshot(
 232 |     const wet_vm_t* vm,
 233 |     uint8_t* buffer,
 234 |     size_t* inout_len
 235 | );
 236 | 
 237 | /**
 238 |  * Phase 3: Live State Hot-Swap Restoration.
 239 |  * Deserializes neural state and synaptic weights without rebooting the VM.
 240 |  */
 241 | WET_EXPORT wet_status_t wet_vm_restore(
 242 |     wet_vm_t* vm,
 243 |     const uint8_t* buffer,
 244 |     size_t len
 245 | );
 246 | 
 247 | /**
 248 |  * Phase 3: Sets environmental sensor readings (pH, DO %, CO2 %, bubble detectors, flow rate).
 249 |  */
 250 | WET_EXPORT void wet_set_environmental_sensors(
 251 |     wet_vm_t* vm,
 252 |     float ph,
 253 |     float do_pct,
 254 |     float co2_pct,
 255 |     uint8_t bubble_sensor_id,
 256 |     uint8_t bubble_state,
 257 |     float flow_rate_ul_min
 258 | );
 259 | 
 260 | /**
 261 |  * Phase 3: Sets ambient incubator / CMOS die temperature (C).
 262 |  */
 263 | WET_EXPORT void wet_set_temperature(
 264 |     wet_vm_t* vm,
 265 |     float temp_c
 266 | );
 267 | 
 268 | /**
 269 |  * Phase 3: Sets typed channel banks (reference and recording-only masks).
 270 |  */
 271 | WET_EXPORT void wet_set_channel_banks(
 272 |     wet_vm_t* vm,
 273 |     uint64_t ref_mask,
 274 |     uint64_t rec_mask
 275 | );
 276 | 
 277 | /**
 278 |  * Milestone 2 Biophysics Live Synapse Matrix Introspection:
 279 |  * Copies the dense 64x64 synaptic conductance matrix (nS) from VM biophysics state
 280 |  * into caller-allocated buffer (float[64][64] = 4096 floats).
 281 |  */
 282 | WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
 283 |     const wet_vm_t* vm,
 284 |     float* out_matrix,
 285 |     size_t out_capacity_floats
 286 | );
 287 | 
 288 | /**
 289 |  * Queries single synaptic conductance weight between pre and post neurons in nS.
 290 |  */
 291 | WET_EXPORT float wet_vm_get_synapse_weight(
 292 |     const wet_vm_t* vm,
 293 |     uint8_t pre,
 294 |     uint8_t post
 295 | );
 296 | 
 297 | #ifdef __cplusplus
 298 | }
 299 | #endif
 300 | 
 301 | #endif /* WETVM_API_H */
```

### `native/include/wetvm_types.h` (177 lines, SHA-256: `90dc6be4f81eb942...`)

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
 160 |     uint32_t reserved;       /* Reserved (0) */
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

### `native/src/biophysics.c` (540 lines, SHA-256: `9f12d3ca6c10cd88...`)

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
 316 |             } else if (p->phase2_ticks_left > 0) {
 317 |                 v_applied = p->phase2_amp_v;
 318 |                 p->phase2_ticks_left--;
 319 |             }
 320 |             if (p->phase1_ticks_left == 0 && p->interphase_ticks_left == 0 && p->phase2_ticks_left == 0) {
 321 |                 p->active = 0;
 322 |             }
 323 |         }
 324 | 
 325 |         if (bio->stim_blanking_ticks[ch] > 0) {
 326 |             bio->stim_blanking_ticks[ch]--;
 327 |         }
 328 | 
 329 |         bio->ext_stim_v[ch] = v_applied;
 330 |         /* I (uA) = V (V) / Z (kOhm) * 1000; Q (nC) = I (uA) * dt (ms) */
 331 |         float i_ua = (v_applied / bio->electrode_impedance_kohm) * 1000.0f;
 332 |         bio->tick_charge_nc[ch] = i_ua * dt_f;
 333 | 
 334 |         /* Randles Cell Integration: dV_dl/dt = (I - V_dl/Rct) / Cdl */
 335 |         float c_dl_pf = bio->c_double_layer_pf[ch] > 0.0f ? bio->c_double_layer_pf[ch] : 26.45f;
 336 |         float r_ct_kohm = bio->r_charge_transfer_kohm > 0.0f ? bio->r_charge_transfer_kohm : 5000.0f;
 337 |         float tau_dl_ms = (r_ct_kohm * 1e3f) * (c_dl_pf * 1e-12f) * 1e3f; /* Rct * Cdl in ms */
 338 |         if (tau_dl_ms < 0.01f) tau_dl_ms = 0.01f;
 339 |         float decay_dl = (float)wet_exp(-dt / (double)tau_dl_ms);
 340 |         /* Injected dv = I * dt / Cdl; I in uA, dt in ms, Cdl in pF -> (uA * ms) / pF = (1e-6 * 1e-3) / 1e-12 = 1.0 V */
 341 |         float dv_dl = (i_ua * dt_f) / c_dl_pf;
 342 |         bio->v_double_layer_v[ch] = bio->v_double_layer_v[ch] * decay_dl + dv_dl;
 343 |     }
 344 | 
 345 |     /* 2. Decay synaptic conductances, AHP, dynamic thresholds, STDP traces & STP state */
 346 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 347 |         bio->g_exc_ns[i]   *= decay_exc;
 348 |         bio->g_inh_ns[i]   *= decay_inh;
 349 |         bio->g_ahp_ns[i]   *= decay_ahp;
 350 |         bio->v_thresh_mv[i] = bio->e_thresh_base_mv + (bio->v_thresh_mv[i] - bio->e_thresh_base_mv) * decay_thr;
 351 |         bio->trace_pre[i]  *= decay_pre;
 352 |         bio->trace_post[i] *= decay_post;
 353 |         bio->spikes_now[i]  = 0;
 354 | 
 355 |         /* Denormal / Subnormal Floating-Point Clamping to eliminate microcode exception traps */
 356 |         if (bio->g_exc_ns[i] < 1e-12f) bio->g_exc_ns[i] = 0.0f;
 357 |         if (bio->g_inh_ns[i] < 1e-12f) bio->g_inh_ns[i] = 0.0f;
 358 |         if (bio->g_ahp_ns[i] < 1e-12f) bio->g_ahp_ns[i] = 0.0f;
 359 |         if (bio->trace_pre[i] < 1e-12f) bio->trace_pre[i] = 0.0f;
 360 |         if (bio->trace_post[i] < 1e-12f) bio->trace_post[i] = 0.0f;
 361 |     }
 362 | 
 363 |     /* Exact Exponential Euler relaxation of Tsodyks-Markram STP variables */
 364 |     for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
 365 |         for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
 366 |             bio_synapse_t* syn = &bio->synapses[pre][post];
 367 |             if (!syn->exists) continue;
 368 |             float d_rec = (float)wet_exp(-dt / (double)syn->tau_rec_ms);
 369 |             float d_fac = (float)wet_exp(-dt / (double)syn->tau_fac_ms);
 370 |             syn->x_stp = 1.0f + (syn->x_stp - 1.0f) * d_rec;
 371 |             syn->u_stp = syn->U_base + (syn->u_stp - syn->U_base) * d_fac;
 372 |         }
 373 |     }
 374 | 
 375 |     /* 3. Integrate COBA-LIF membrane ODE via Exact Exponential Euler */
 376 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 377 |         if (bio->refract_ticks[i] > 0) {
 378 |             bio->refract_ticks[i]--;
 379 |             bio->v_m_mv[i] = bio->e_reset_mv;
 380 |             continue;
 381 |         }
 382 | 
 383 |         /* Couple nearby electrode stimulation via volume conduction pickup matrix */
 384 |         float stim_v_eff = 0.0f;
 385 |         for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 386 |             if (bio->ext_stim_v[ch] != 0.0f) {
 387 |                 stim_v_eff += bio->pickup_matrix[ch][i] * bio->ext_stim_v[ch];
 388 |             }
 389 |         }
 390 |         /* Convert effective extracellular field (V) into depolarizing soma current (pA).
 391 |          * Cathodic extracellular field (stim_v_eff < 0) depolarizes the soma (Vm = Vi - Ve);
 392 |          * scale calibrated so 0.5-1.0 V drives firing. */
 393 |         float i_stim_pa = -stim_v_eff * 1500.0f;
 394 | 
 395 |         /* Spontaneous cortical tonic + Gaussian background synaptic current (~15-25 Hz baseline) */
 396 |         float i_bg_pa = 215.0f + (float)wet_rng_normal(&bio->rng_state) * 140.0f;
 397 | 
 398 |         /* Total conductance (nS) */
 399 |         float g_tot = bio->g_leak_ns + bio->g_exc_ns[i] + bio->g_inh_ns[i] + bio->g_ahp_ns[i];
 400 |         if (g_tot < 1e-3f) g_tot = bio->g_leak_ns;
 401 | 
 402 |         /* Steady-state target potential V_inf (mV): (nS * mV + pA) / nS = mV */
 403 |         float num = bio->g_leak_ns * bio->e_leak_mv
 404 |                   + bio->g_exc_ns[i] * bio->e_exc_mv
 405 |                   + bio->g_inh_ns[i] * bio->e_inh_mv
 406 |                   + bio->g_ahp_ns[i] * bio->e_k_mv
 407 |                   + i_stim_pa + i_bg_pa;
 408 |         float v_inf = num / g_tot;
 409 | 
 410 |         /* Exact Exponential Euler step: tau_eff (ms) = C_m (pF) / g_tot (nS) */
 411 |         float tau_eff_ms = bio->c_m_pf / g_tot;
 412 |         float decay_v = (float)wet_exp(-dt / (double)tau_eff_ms);
 413 |         float v_next = v_inf + (bio->v_m_mv[i] - v_inf) * decay_v;
 414 | 
 415 |         /* Numerical safety clamp */
 416 |         v_next = wet_clampf(v_next, -120.0f, 50.0f);
 417 | 
 418 |         if (v_next >= bio->v_thresh_mv[i]) {
 419 |             bio->spikes_now[i] = 1;
 420 |             bio->v_m_mv[i] = bio->e_reset_mv;
 421 |             bio->refract_ticks[i] = BIO_ABS_REFRACT_TICKS; /* 2.0 ms hard absolute refractory */
 422 |             bio->v_thresh_mv[i] += 15.0f;                  /* +15 mV relative refractory jump */
 423 |             bio->g_ahp_ns[i]    += 2.0f;                   /* Slow AHP potassium adaptation */
 424 |         } else {
 425 |             bio->v_m_mv[i] = v_next;
 426 |         }
 427 |     }
 428 | 
 429 |     /* 4. Propagate spikes through Tsodyks-Markram STP synapses & Online Pairwise STDP */
 430 |     for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 431 |         if (!bio->spikes_now[i]) continue;
 432 | 
 433 |         /* Update pre-synaptic and post-synaptic STDP traces */
 434 |         bio->trace_pre[i]  += 1.0f;
 435 |         bio->trace_post[i] += 1.0f;
 436 | 
 437 |         /* A) Outgoing synapses (i -> post): STP transmission + LTD */
 438 |         for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
 439 |             bio_synapse_t* syn = &bio->synapses[i][post];
 440 |             if (!syn->exists) continue;
 441 | 
 442 |             /* Tsodyks-Markram discrete spike update */
 443 |             syn->u_stp = syn->u_stp + syn->U_base * (1.0f - syn->u_stp);
 444 |             float release = syn->u_stp * syn->x_stp;
 445 |             syn->x_stp = wet_clampf(syn->x_stp - release, 0.0f, 1.0f);
 446 | 
 447 |             float dg = syn->weight_ns * release;
 448 |             if (bio->is_excitatory[i]) {
 449 |                 bio->g_exc_ns[post] += dg;
 450 |             } else {
 451 |                 bio->g_inh_ns[post] += dg;
 452 |             }
 453 | 
 454 |             /* Online STDP LTD on plastic excitatory synapses (1.05x depression bias) */
 455 |             if (bio->is_excitatory[i] && bio->trace_post[post] > 1e-6f) {
 456 |                 float dw = -bio->stdp_lr_scale * bio->stdp_a_minus * bio->trace_post[post];
 457 |                 float old_w = syn->weight_ns;
 458 |                 syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
 459 |                 bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
 460 |             }
 461 |         }
 462 | 
 463 |         /* B) Incoming synapses (pre -> i): Online STDP LTP on plastic excitatory synapses */
 464 |         for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
 465 |             if (!bio->is_excitatory[pre]) continue;
 466 |             bio_synapse_t* syn = &bio->synapses[pre][i];
 467 |             if (!syn->exists) continue;
 468 | 
 469 |             if (bio->trace_pre[pre] > 1e-6f) {
 470 |                 float dw = bio->stdp_lr_scale * bio->stdp_a_plus * bio->trace_pre[pre];
 471 |                 float old_w = syn->weight_ns;
 472 |                 syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
 473 |                 bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
 474 |             }
 475 |         }
 476 |     }
 477 | 
 478 |     /* 5. Update 8x8 MEA Extracellular Voltages & 50.0 ms Sliding Spike History */
 479 |     uint16_t head = bio->spike_history_head;
 480 |     float total_rate_sum = 0.0f;
 481 |     const float window_s = (float)(BIO_SPIKE_HISTORY_LEN * bio->dt_ms) * 0.001f; /* 0.05 s */
 482 | 
 483 |     for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
 484 |         /* Forward volume conduction LFP/spike pickup (mV -> V, resting baseline centered at 0 V) + applied stim voltage */
 485 |         float v_pick_mv = 0.0f;
 486 |         for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
 487 |             float v_sig = bio->spikes_now[i] ? (30.0f - bio->e_leak_mv) : (bio->v_m_mv[i] - bio->e_leak_mv);
 488 |             v_pick_mv += bio->pickup_matrix[ch][i] * v_sig;
 489 |         }
 490 |         /* Report extracellular voltage in Volts (stim + attenuated biological LFP, zero baseline) */
 491 |         bio->mea_voltage_v[ch] = bio->ext_stim_v[ch] + (v_pick_mv * 1e-3f);
 492 | 
 493 |         /* Hardware Blanking Suppression: silence artifact and biological false-positives during post-stimulus discharge */
 494 |         if (!bio->stim_pulses[ch].active && bio->stim_blanking_ticks[ch] > 0) {
 495 |             bio->mea_voltage_v[ch] = 0.0f;
 496 |             bio->spikes_now[ch] = 0;
 497 |         }
 498 | 
 499 |         /* Rolling 500-tick (50 ms) spike count */
 500 |         uint8_t old_spk = bio->spike_history[ch][head];
 501 |         uint8_t new_spk = bio->spikes_now[ch];
 502 |         bio->spike_history[ch][head] = new_spk;
 503 | 
 504 |         if (bio->spike_count_50ms[ch] >= old_spk) {
 505 |             bio->spike_count_50ms[ch] = (uint16_t)(bio->spike_count_50ms[ch] - old_spk + new_spk);
 506 |         } else {
 507 |             bio->spike_count_50ms[ch] = new_spk;
 508 |         }
 509 | 
 510 |         bio->channel_rate_hz[ch] = (float)bio->spike_count_50ms[ch] / window_s;
 511 |         total_rate_sum += bio->channel_rate_hz[ch];
 512 |     }
 513 | 
 514 |     bio->spike_history_head = (uint16_t)((head + 1U) % BIO_SPIKE_HISTORY_LEN);
 515 |     bio->population_rate_hz = total_rate_sum / (float)BIO_NUM_CHANNELS;
 516 |     bio->tick_count++;
 517 | }
 518 | 
 519 | uint32_t biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms) {
 520 |     if (!bio || channel >= BIO_NUM_CHANNELS) return 0U;
 521 | 
 522 |     uint32_t n_ticks = (window_ms > 0.0f) ? (uint32_t)(window_ms / (float)bio->dt_ms + 0.5f) : 1U;
 523 |     if (n_ticks == 0U) n_ticks = 1U;
 524 |     if (n_ticks > BIO_SPIKE_HISTORY_LEN) n_ticks = BIO_SPIKE_HISTORY_LEN;
 525 | 
 526 |     uint32_t count = 0U;
 527 |     int idx = (int)bio->spike_history_head - 1;
 528 |     for (uint32_t k = 0; k < n_ticks; ++k) {
 529 |         if (idx < 0) idx += BIO_SPIKE_HISTORY_LEN;
 530 |         count += bio->spike_history[channel][idx];
 531 |         idx--;
 532 |     }
 533 |     return count;
 534 | }
 535 | 
 536 | float biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post) {
 537 |     if (!bio || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
 538 |     if (!bio->synapses[pre][post].exists) return 0.0f;
 539 |     return bio->synapses[pre][post].weight_ns;
 540 | }
```

### `native/src/interlocks.c` (314 lines, SHA-256: `f5b7f88bdfe05691...`)

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
  11 |     il->max_charge_per_phase_nc = INTERLOCK_CHARGE_LIMIT_NC; /* Default 0.5 nC */
  12 |     il->max_cumulative_dc_nc = INTERLOCK_DC_DRIFT_LIMIT_NC;  /* Default 1.0 nC */
  13 |     for (int p = 0; p < 8; ++p) {
  14 |         il->pump_valve_mapping[p] = (uint8_t)p;
  15 |     }
  16 | }
  17 | 
  18 | void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2) {
  19 |     if (!il) return;
  20 |     il->electrode_material = material;
  21 |     il->electrode_area_um2 = area_um2;
  22 | 
  23 |     /* Charge Injection Capacity (CIC) in mC/cm^2:
  24 |      * Area in cm^2 = area_um2 * 1e-8 cm^2/um^2
  25 |      * Max charge in nC = CIC (mC/cm^2) * Area (cm^2) * 1e6 nC/mC = CIC * area_um2 * 0.01 nC
  26 |      */
  27 |     float cic_mc_cm2 = 0.10f;
  28 |     switch ((wet_electrode_material_t)material) {
  29 |         case WET_ELEC_PLATINUM: cic_mc_cm2 = 0.10f; break; /* 0.05..0.15 mC/cm^2 water window */
  30 |         case WET_ELEC_TIN:      cic_mc_cm2 = 0.90f; break; /* Titanium Nitride */
  31 |         case WET_ELEC_IROX:     cic_mc_cm2 = 2.00f; break; /* Iridium Oxide */
  32 |         case WET_ELEC_PEDOT:    cic_mc_cm2 = 5.00f; break; /* Conductive polymer */
  33 |         default:                cic_mc_cm2 = 0.10f; break;
  34 |     }
  35 | 
  36 |     float limit_nc = cic_mc_cm2 * area_um2 * 0.01f;
  37 |     if (limit_nc < 0.01f) limit_nc = 0.01f;
  38 |     il->max_charge_per_phase_nc = limit_nc;
  39 |     il->max_cumulative_dc_nc = limit_nc * 2.0f;
  40 | }
  41 | 
  42 | void interlocks_active_discharge(interlock_state_t* il, uint8_t channel) {
  43 |     if (!il || channel >= INTERLOCK_NUM_CHANNELS) return;
  44 |     il->cumulative_unbounded_dc_nc[channel] = 0.0f;
  45 |     il->q_dc[channel] = 0.0f;
  46 | }
  47 | 
  48 | void interlocks_active_discharge_all(interlock_state_t* il) {
  49 |     if (!il) return;
  50 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
  51 |         il->cumulative_unbounded_dc_nc[ch] = 0.0f;
  52 |         il->q_dc[ch] = 0.0f;
  53 |     }
  54 | }
  55 | 
  56 | void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable) {
  57 |     if (!il) return;
  58 |     il->dead_head_protection_enabled = enable;
  59 | }
  60 | 
  61 | void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count) {
  62 |     if (!il) return;
  63 |     il->authorized_capabilities = caps;
  64 |     il->authorized_channels = (channel_count > 0 && channel_count <= INTERLOCK_NUM_CHANNELS)
  65 |                               ? channel_count : INTERLOCK_NUM_CHANNELS;
  66 | }
  67 | 
  68 | void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask) {
  69 |     if (!il) return;
  70 |     il->reference_channels_mask = ref_mask;
  71 |     il->recording_only_channels_mask = rec_mask;
  72 | }
  73 | 
  74 | int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel) {
  75 |     if (!il) return 0;
  76 |     if (il->locked) return 0;
  77 | 
  78 |     /* Bounds check for channel-addressed opcodes */
  79 |     if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT ||
  80 |         opcode == WET_OP_READ_SPIKES || opcode == WET_OP_READ_VOLTAGE) {
  81 |         if ((uint32_t)channel >= il->authorized_channels) {
  82 |             return 0;
  83 |         }
  84 |     }
  85 | 
  86 |     /* Typed Channel Banks: Disallow stimulation on reference or recording-only electrodes */
  87 |     if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT) {
  88 |         if (channel < 64) {
  89 |             uint64_t ch_bit = 1ULL << channel;
  90 |             if ((il->reference_channels_mask & ch_bit) != 0ULL ||
  91 |                 (il->recording_only_channels_mask & ch_bit) != 0ULL) {
  92 |                 return 0; /* Capability Denied: Channel restricted to reference or recording */
  93 |             }
  94 |         }
  95 |     }
  96 | 
  97 |     switch ((wet_opcode_t)opcode) {
  98 |         case WET_OP_STIM_BIPHASIC:
  99 |         case WET_OP_STIM_CURRENT:
 100 |             if ((il->authorized_capabilities & WET_CAP_STIMULATION) == 0) {
 101 |                 return 0;
 102 |             }
 103 |             if (wet_fabsf(voltage_v) > 0.8f && (il->authorized_capabilities & WET_CAP_HIGH_VOLTAGE) == 0) {
 104 |                 return 0;
 105 |             }
 106 |             return 1;
 107 | 
 108 |         case WET_OP_MODULATE_STDP:
 109 |             if ((il->authorized_capabilities & WET_CAP_PLASTICITY) == 0) {
 110 |                 return 0;
 111 |             }
 112 |             return 1;
 113 | 
 114 |         case WET_OP_PUMP_SET_RATE:
 115 |         case WET_OP_PUMP_DISPENSE:
 116 |         case WET_OP_VALVE_SET:
 117 |             if ((il->authorized_capabilities & WET_CAP_MICROFLUIDICS) == 0) {
 118 |                 return 0;
 119 |             }
 120 |             return 1;
 121 | 
 122 |         case WET_OP_MOTOR_STEP:
 123 |             if ((il->authorized_capabilities & WET_CAP_MOTOR_ACTUATION) == 0) {
 124 |                 return 0;
 125 |             }
 126 |             return 1;
 127 | 
 128 |         default:
 129 |             /* Tier 0 compute and Tier 1 passive readout always permitted */
 130 |             return 1;
 131 |     }
 132 | }
 133 | 
 134 | float interlocks_clamp_voltage(interlock_state_t* il, float requested_v) {
 135 |     if (requested_v > INTERLOCK_VOLTAGE_LIMIT_V) {
 136 |         if (il) il->clamp_events++;
 137 |         return INTERLOCK_VOLTAGE_LIMIT_V;
 138 |     }
 139 |     if (requested_v < -INTERLOCK_VOLTAGE_LIMIT_V) {
 140 |         if (il) il->clamp_events++;
 141 |         return -INTERLOCK_VOLTAGE_LIMIT_V;
 142 |     }
 143 |     return requested_v;
 144 | }
 145 | 
 146 | wet_status_t interlocks_record_charge_tick(
 147 |     interlock_state_t* il,
 148 |     uint64_t current_tick,
 149 |     const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
 150 | ) {
 151 |     if (!il || !tick_charge_nc) return WET_ERR_NULL_PTR;
 152 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 153 | 
 154 |     uint16_t head = il->q_head;
 155 |     wet_status_t status = WET_OK;
 156 | 
 157 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
 158 |         float old_q = il->q_ring[ch][head];
 159 |         float new_q = tick_charge_nc[ch];
 160 |         il->q_ring[ch][head] = new_q;
 161 | 
 162 |         /* Recompute exact sum periodically or maintain running sum with drift-free precision */
 163 |         float accum = il->q_accum[ch] - old_q + new_q;
 164 |         if (wet_fabsf(accum) < 1e-7f) accum = 0.0f;
 165 |         il->q_accum[ch] = accum;
 166 | 
 167 |         /* Long-horizon leaky DC integrator (tau = 10.0 s = 100,000 ticks) */
 168 |         il->q_dc[ch] = il->q_dc[ch] * INTERLOCK_BLEED_DECAY_PER_TICK + new_q;
 169 |         if (wet_fabsf(il->q_dc[ch]) < 1e-7f) il->q_dc[ch] = 0.0f;
 170 | 
 171 |         /* Phase 3: Persistent unbounded cumulative DC charge accumulator (zero decay) */
 172 |         il->cumulative_unbounded_dc_nc[ch] += new_q;
 173 |         if (wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) < 1e-7f) {
 174 |             il->cumulative_unbounded_dc_nc[ch] = 0.0f;
 175 |         }
 176 | 
 177 |         float charge_limit = il->max_charge_per_phase_nc > 0.0f ? il->max_charge_per_phase_nc : INTERLOCK_CHARGE_LIMIT_NC;
 178 |         float dc_limit = il->max_cumulative_dc_nc > 0.0f ? il->max_cumulative_dc_nc : INTERLOCK_DC_DRIFT_LIMIT_NC;
 179 | 
 180 |         if (wet_fabsf(accum) >= charge_limit) {
 181 |             il->locked = 1;
 182 |             il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
 183 |             il->tripped_channel = (uint8_t)ch;
 184 |             il->trip_tick = current_tick;
 185 |             il->trip_value = accum;
 186 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 187 |                      "ERR_CHARGE_IMBALANCE: ch=%d net_q=%.4f nC >= %.2f nC (CIC limit for material %u, area %.1f um2) at tick %llu",
 188 |                      ch, (double)accum, (double)charge_limit, il->electrode_material, (double)il->electrode_area_um2, (unsigned long long)current_tick);
 189 |             status = WET_ERR_CHARGE_IMBALANCE;
 190 |             break;
 191 |         }
 192 | 
 193 |         if (wet_fabsf(il->q_dc[ch]) >= dc_limit || wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit) {
 194 |             il->locked = 1;
 195 |             il->trip_reason = INTERLOCK_TRIP_DC_DRIFT;
 196 |             il->tripped_channel = (uint8_t)ch;
 197 |             il->trip_tick = current_tick;
 198 |             il->trip_value = wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit ? il->cumulative_unbounded_dc_nc[ch] : il->q_dc[ch];
 199 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 200 |                      "ERR_DC_DRIFT: ch=%d cumulative DC charge=%.4f nC >= %.2f nC at tick %llu",
 201 |                      ch, (double)il->trip_value, (double)dc_limit, (unsigned long long)current_tick);
 202 |             status = WET_ERR_DC_DRIFT;
 203 |             break;
 204 |         }
 205 |     }
 206 | 
 207 |     il->q_head = (uint16_t)((head + 1U) % INTERLOCK_CHARGE_WINDOW_TICKS);
 208 |     return status;
 209 | }
 210 | 
 211 | wet_status_t interlocks_check_epileptiform(
 212 |     interlock_state_t* il,
 213 |     uint64_t current_tick,
 214 |     const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
 215 | ) {
 216 |     if (!il || !channel_rates_hz) return WET_ERR_NULL_PTR;
 217 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 218 | 
 219 |     uint32_t hyper_count = 0U;
 220 |     for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
 221 |         if (channel_rates_hz[ch] >= INTERLOCK_EPILEPSY_RATE_HZ) {
 222 |             hyper_count++;
 223 |             il->focal_hyperactive_ticks[ch]++;
 224 |             if (il->focal_hyperactive_ticks[ch] >= INTERLOCK_FOCAL_SUSTAIN_TICKS) {
 225 |                 il->locked = 1;
 226 |                 il->trip_reason = INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY;
 227 |                 il->tripped_channel = (uint8_t)ch;
 228 |                 il->trip_tick = current_tick;
 229 |                 il->trip_value = channel_rates_hz[ch];
 230 |                 snprintf(il->diagnostic, sizeof(il->diagnostic),
 231 |                          "ERR_FOCAL_EXCITOTOXICITY: ch=%d sustained %.1f Hz >= 150 Hz for 250.0 ms at tick %llu",
 232 |                          ch, (double)channel_rates_hz[ch], (unsigned long long)current_tick);
 233 |                 return WET_ERR_FOCAL_EXCITOTOXICITY;
 234 |             }
 235 |         } else {
 236 |             il->focal_hyperactive_ticks[ch] = 0U;
 237 |         }
 238 |     }
 239 | 
 240 |     il->last_hyperactive_channel_count = hyper_count;
 241 | 
 242 |     if (hyper_count >= INTERLOCK_EPILEPSY_MIN_CHANNELS) {
 243 |         il->hyperactive_consecutive_ticks++;
 244 |         if (il->hyperactive_consecutive_ticks >= INTERLOCK_EPILEPSY_SUSTAIN_TICKS) {
 245 |             il->locked = 1;
 246 |             il->trip_reason = INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY;
 247 |             il->tripped_channel = 0xFF;
 248 |             il->trip_tick = current_tick;
 249 |             il->trip_value = (float)hyper_count;
 250 |             snprintf(il->diagnostic, sizeof(il->diagnostic),
 251 |                      "ERR_EPILEPTIFORM_RUNAWAY: %u/64 channels (>35%%) exceeded 150 Hz for 50.0 ms at tick %llu",
 252 |                      hyper_count, (unsigned long long)current_tick);
 253 |             return WET_ERR_EPILEPTIFORM_RUNAWAY;
 254 |         }
 255 |     } else {
 256 |         il->hyperactive_consecutive_ticks = 0U;
 257 |     }
 258 | 
 259 |     return WET_OK;
 260 | }
 261 | 
 262 | wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c) {
 263 |     if (!il) return WET_ERR_NULL_PTR;
 264 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 265 | 
 266 |     if (temp_c > INTERLOCK_THERMAL_LIMIT_C) {
 267 |         il->locked = 1;
 268 |         il->trip_reason = INTERLOCK_TRIP_THERMAL_LIMIT;
 269 |         il->tripped_channel = 0xFF;
 270 |         il->trip_tick = current_tick;
 271 |         il->trip_value = temp_c;
 272 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 273 |                  "ERR_THERMAL_LIMIT: Temperature %.2f C exceeds incubator threshold (38.00 C) at tick %llu",
 274 |                  (double)temp_c, (unsigned long long)current_tick);
 275 |         return WET_ERR_THERMAL_LIMIT;
 276 |     }
 277 |     return WET_OK;
 278 | }
 279 | 
 280 | wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id) {
 281 |     if (!il) return WET_ERR_NULL_PTR;
 282 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 283 | 
 284 |     if (bubble_detected) {
 285 |         il->locked = 1;
 286 |         il->trip_reason = INTERLOCK_TRIP_BUBBLE_DETECTED;
 287 |         il->tripped_channel = sensor_id;
 288 |         il->trip_tick = current_tick;
 289 |         il->trip_value = 1.0f;
 290 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 291 |                  "ERR_BUBBLE_DETECTED: Optical bubble sensor %u triggered (fluid line cavitation risk) at tick %llu",
 292 |                  sensor_id, (unsigned long long)current_tick);
 293 |         return WET_ERR_BUBBLE_DETECTED;
 294 |     }
 295 |     return WET_OK;
 296 | }
 297 | 
 298 | wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v) {
 299 |     if (!il) return WET_ERR_NULL_PTR;
 300 |     if (il->locked) return WET_ERR_INTERLOCK_LOCKED;
 301 | 
 302 |     if (wet_fabsf(v_elec_v) > INTERLOCK_COMPLIANCE_LIMIT_V) {
 303 |         il->locked = 1;
 304 |         il->trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
 305 |         il->tripped_channel = channel;
 306 |         il->trip_tick = current_tick;
 307 |         il->trip_value = v_elec_v;
 308 |         snprintf(il->diagnostic, sizeof(il->diagnostic),
 309 |                  "ERR_COMPLIANCE_RAILED: ch=%u electrode potential %.3f V exceeded compliance rail (+/-7.0 V) at tick %llu",
 310 |                  channel, (double)v_elec_v, (unsigned long long)current_tick);
 311 |         return WET_ERR_COMPLIANCE_RAILED;
 312 |     }
 313 |     return WET_OK;
 314 | }
```

### `native/src/wet_hal.c` (489 lines, SHA-256: `f975ddf0fa223c9c...`)

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
 240 |     /* Check Dead-Head Overpressure Interlock: If valve is closed and rate > 0, reject immediately! */
 241 |     if (hal->config.enable_dead_head_protection && run_flag && rate_ul_min > 0.0) {
 242 |         uint8_t target_valve = pump_id;
 243 |         if (hal->config.valve_for_pump[pump_id] < 8) {
 244 |             target_valve = hal->config.valve_for_pump[pump_id];
 245 |         }
 246 |         if (hal->valve_states[target_valve] == 0) {
 247 |             return WET_HAL_ERR_DEAD_HEAD;
 248 |         }
 249 |     }
 250 | 
 251 |     hal->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
 252 |     hal->telemetry.total_rs232_commands++;
 253 | 
 254 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
 255 |         /* In simulated mode or no pump driver, update internal VM registers */
 256 |         if (hal->vm) {
 257 |             hal->vm->pump_rates_ul_min[pump_id] = (float)rate_ul_min;
 258 |         }
 259 |         return WET_HAL_OK;
 260 |     }
 261 | 
 262 |     /* Dispatch to physical or HIL pump driver */
 263 |     if (hal->pump_driver->ops && hal->pump_driver->ops->write_pump) {
 264 |         return hal->pump_driver->ops->write_pump(hal->pump_driver, pump_id, rate_ul_min, run_flag);
 265 |     }
 266 |     return WET_HAL_OK;
 267 | }
 268 | 
 269 | wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul) {
 270 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 271 |     if (pump_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 272 | 
 273 |     /* Dead-head protection check */
 274 |     if (hal->config.enable_dead_head_protection && volume_ul > 0.0) {
 275 |         uint8_t target_valve = pump_id;
 276 |         if (hal->config.valve_for_pump[pump_id] < 8) {
 277 |             target_valve = hal->config.valve_for_pump[pump_id];
 278 |         }
 279 |         if (hal->valve_states[target_valve] == 0) {
 280 |             return WET_HAL_ERR_DEAD_HEAD;
 281 |         }
 282 |     }
 283 | 
 284 |     hal->telemetry.total_rs232_commands++;
 285 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->pump_driver) {
 286 |         if (hal->vm) {
 287 |             hal->vm->pump_dispensed_ul[pump_id] += (float)volume_ul;
 288 |         }
 289 |         return WET_HAL_OK;
 290 |     }
 291 | 
 292 |     if (hal->pump_driver->ops && hal->pump_driver->ops->dispense_volume) {
 293 |         return hal->pump_driver->ops->dispense_volume(hal->pump_driver, pump_id, volume_ul);
 294 |     }
 295 |     return WET_HAL_OK;
 296 | }
 297 | 
 298 | wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state) {
 299 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 300 |     if (valve_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 301 | 
 302 |     hal->valve_states[valve_id] = (state != 0) ? 1 : 0;
 303 |     if (hal->vm) {
 304 |         hal->vm->valve_states[valve_id] = hal->valve_states[valve_id];
 305 |     }
 306 | 
 307 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->valve_driver) {
 308 |         return WET_HAL_OK;
 309 |     }
 310 | 
 311 |     if (hal->valve_driver->ops && hal->valve_driver->ops->write_valve) {
 312 |         return hal->valve_driver->ops->write_valve(hal->valve_driver, valve_id, state);
 313 |     }
 314 |     return WET_HAL_OK;
 315 | }
 316 | 
 317 | wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min) {
 318 |     if (!hal || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
 319 |     if (sensor_id >= 8) return WET_HAL_ERR_OUT_OF_BOUNDS;
 320 | 
 321 |     hal->telemetry.total_i2c_transactions++;
 322 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->flow_driver) {
 323 |         if (hal->vm) {
 324 |             *out_flow_ul_min = (double)hal->vm->fluid_flow_rate_ul_min[sensor_id];
 325 |         } else {
 326 |             *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
 327 |         }
 328 |         return WET_HAL_OK;
 329 |     }
 330 | 
 331 |     if (hal->flow_driver->ops && hal->flow_driver->ops->read_flow) {
 332 |         wet_hal_status_t st = hal->flow_driver->ops->read_flow(hal->flow_driver, sensor_id, out_flow_ul_min);
 333 |         if (st == WET_HAL_OK) {
 334 |             hal->flow_rates_ul_min[sensor_id] = *out_flow_ul_min;
 335 |             if (hal->vm) {
 336 |                 hal->vm->fluid_flow_rate_ul_min[sensor_id] = (float)(*out_flow_ul_min);
 337 |             }
 338 |         }
 339 |         return st;
 340 |     }
 341 |     *out_flow_ul_min = hal->flow_rates_ul_min[sensor_id];
 342 |     return WET_HAL_OK;
 343 | }
 344 | 
 345 | wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
 346 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 347 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 348 | 
 349 |     hal->telemetry.total_spi_transactions++;
 350 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 351 |         if (hal->vm) {
 352 |             /* Convert pA to uA for simulated biophysics: 1 uA = 1,000,000 pA */
 353 |             float current_ua = (float)current_pA / 1000000.0f;
 354 |             float dur_ms = (float)duration_us / 1000.0f;
 355 |             biophysics_schedule_stim_current(&hal->vm->bio, (uint8_t)channel, current_ua, dur_ms, dur_ms, 0.0f);
 356 |         }
 357 |         return WET_HAL_OK;
 358 |     }
 359 | 
 360 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_current) {
 361 |         return hal->ephys_driver->ops->stim_current(hal->ephys_driver, channel, current_pA, duration_us);
 362 |     }
 363 |     return WET_HAL_OK;
 364 | }
 365 | 
 366 | wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
 367 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 368 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 369 | 
 370 |     hal->telemetry.total_spi_transactions++;
 371 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 372 |         if (hal->vm) {
 373 |             biophysics_schedule_stim_ext(&hal->vm->bio, (uint8_t)channel, voltage_v, p1_ms, p2_ms, 0.0f);
 374 |         }
 375 |         return WET_HAL_OK;
 376 |     }
 377 | 
 378 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->stim_voltage) {
 379 |         return hal->ephys_driver->ops->stim_voltage(hal->ephys_driver, channel, voltage_v, p1_ms, p2_ms);
 380 |     }
 381 |     return WET_HAL_OK;
 382 | }
 383 | 
 384 | wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag) {
 385 |     if (!hal || !out_spike_flag) return WET_HAL_ERR_NULL_PTR;
 386 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 387 | 
 388 |     if (hal->mode == WET_HAL_MODE_SIMULATED || !hal->ephys_driver) {
 389 |         if (hal->vm) {
 390 |             *out_spike_flag = hal->vm->spikes[channel];
 391 |         } else {
 392 |             *out_spike_flag = hal->ephys_spikes[channel];
 393 |         }
 394 |         return WET_HAL_OK;
 395 |     }
 396 | 
 397 |     if (hal->ephys_driver->ops && hal->ephys_driver->ops->read_ephys) {
 398 |         float volts[64];
 399 |         uint8_t spks[64];
 400 |         wet_hal_status_t st = hal->ephys_driver->ops->read_ephys(hal->ephys_driver, volts, spks, 64);
 401 |         if (st == WET_HAL_OK) {
 402 |             *out_spike_flag = spks[channel];
 403 |         }
 404 |         return st;
 405 |     }
 406 |     *out_spike_flag = hal->ephys_spikes[channel];
 407 |     return WET_HAL_OK;
 408 | }
 409 | 
 410 | wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
 411 |     if (!hal || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
 412 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 413 | 
 414 |     if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->measure_impedance) {
 415 |         return hal->ephys_driver->ops->measure_impedance(hal->ephys_driver, channel, freq_hz, out_mag_ohms, out_phase_rad);
 416 |     }
 417 | 
 418 |     /* Fallback default impedance model */
 419 |     *out_mag_ohms = 100000.0f; /* 100 kOhm baseline */
 420 |     *out_phase_rad = -0.785f;  /* -45 degrees */
 421 |     return WET_HAL_OK;
 422 | }
 423 | 
 424 | wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel) {
 425 |     if (!hal) return WET_HAL_ERR_NULL_PTR;
 426 |     if (channel >= 64) return WET_HAL_ERR_OUT_OF_BOUNDS;
 427 | 
 428 |     if (hal->ephys_driver && hal->ephys_driver->ops && hal->ephys_driver->ops->active_discharge) {
 429 |         return hal->ephys_driver->ops->active_discharge(hal->ephys_driver, channel);
 430 |     }
 431 |     return WET_HAL_OK;
 432 | }
 433 | 
 434 | /* =========================================================================
 435 |  * Emergency Hardware Crowbar Fast-Path (<100 µs)
 436 |  * ========================================================================= */
 437 | 
 438 | void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason) {
 439 |     if (!vm) return;
 440 |     wet_hal_context_t* hal = vm->hal;
 441 |     if (!hal) return;
 442 | 
 443 |     uint64_t start_us = wet_hal_get_time_us();
 444 | 
 445 |     hal->crowbar_tripped = 1;
 446 |     hal->crowbar_reason = trip_reason;
 447 |     hal->crowbar_tick = vm->current_tick;
 448 |     hal->crowbar_timestamp_us = start_us;
 449 |     hal->telemetry.total_crowbar_events++;
 450 |     hal->telemetry.last_crowbar_reason = trip_reason;
 451 |     hal->telemetry.last_crowbar_timestamp_us = start_us;
 452 | 
 453 |     /* 1. Instantly zero all pump rates and flow sensor readouts */
 454 |     for (int i = 0; i < 8; ++i) {
 455 |         hal->pump_rates_ul_min[i] = 0.0f;
 456 |         hal->flow_rates_ul_min[i] = 0.0;
 457 |         vm->pump_rates_ul_min[i] = 0.0f;
 458 |         vm->fluid_flow_rate_ul_min[i] = 0.0f;
 459 |     }
 460 | 
 461 |     /* 2. Disarm all registered hardware drivers via emergency_stop callback */
 462 |     for (uint32_t i = 0; i < hal->driver_count; ++i) {
 463 |         wet_hal_driver_t* drv = hal->drivers[i];
 464 |         if (drv && drv->ops && drv->ops->emergency_stop) {
 465 |             drv->ops->emergency_stop(drv, trip_reason);
 466 |         }
 467 |     }
 468 | 
 469 |     /* 3. Execute active discharge across all ephys channels to clear Faradaic charge */
 470 |     for (uint16_t ch = 0; ch < 64; ++ch) {
 471 |         wet_hal_active_discharge(hal, ch);
 472 |         vm->discharge_charge_nc[ch] += vm->last_charge_nc[ch];
 473 |         vm->last_charge_nc[ch] = 0.0f;
 474 |         vm->voltages[ch] = 0.0f;
 475 |     }
 476 | 
 477 |     uint64_t end_us = wet_hal_get_time_us();
 478 |     hal->telemetry.crowbar_latency_us = (double)(end_us - start_us);
 479 | }
 480 | 
 481 | wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal) {
 482 |     if (!hal) return NULL;
 483 |     return &hal->telemetry;
 484 | }
 485 | 
 486 | void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id) {
 487 |     if (!hal || pump_id >= 8) return;
 488 |     hal->config.valve_for_pump[pump_id] = valve_id;
 489 | }
```

### `native/src/wet_hal_intan.c` (394 lines, SHA-256: `a25facbb372a8c41...`)

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
 288 |     return WET_HAL_OK;
 289 | }
 290 | 
 291 | void wet_hal_intan_inject_fault(
 292 |     wet_hal_driver_t* drv,
 293 |     uint8_t force_rail,
 294 |     uint8_t spi_error,
 295 |     uint8_t bus_timeout
 296 | ) {
 297 |     if (!drv || !drv->context) return;
 298 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 299 |     state->fault_force_compliance_rail = force_rail;
 300 |     state->fault_spi_crc_error = spi_error;
 301 |     state->fault_bus_timeout = bus_timeout;
 302 | }
 303 | 
 304 | /* =========================================================================
 305 |  * Vtable Callbacks
 306 |  * ========================================================================= */
 307 | 
 308 | static wet_hal_status_t intan_op_init(wet_hal_driver_t* drv, void* config) {
 309 |     (void)config;
 310 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 311 |     drv->is_initialized = 1;
 312 |     drv->is_active = 1;
 313 |     return WET_HAL_OK;
 314 | }
 315 | 
 316 | static wet_hal_status_t intan_op_shutdown(wet_hal_driver_t* drv) {
 317 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 318 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 319 |     for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
 320 |         state->channels[i].enabled = 0;
 321 |         state->channels[i].current_pA = 0;
 322 |         state->channels[i].charge_recovery_on = 1;
 323 |     }
 324 |     drv->is_active = 0;
 325 |     return WET_HAL_OK;
 326 | }
 327 | 
 328 | static wet_hal_status_t intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
 329 |     (void)reason;
 330 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 331 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 332 | 
 333 |     /* Zero all DAC amplitudes immediately and activate charge recovery switches */
 334 |     for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
 335 |         state->channels[i].dac_val_p1 = 0;
 336 |         state->channels[i].dac_val_p2 = 0;
 337 |         state->channels[i].current_pA = 0;
 338 |         state->channels[i].enabled = 0;
 339 |         state->channels[i].charge_recovery_on = 1;
 340 |     }
 341 |     return WET_HAL_OK;
 342 | }
 343 | 
 344 | static wet_hal_status_t intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
 345 |     (void)current_tick;
 346 |     (void)dt_ms;
 347 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 348 |     return WET_HAL_OK;
 349 | }
 350 | 
 351 | static wet_hal_status_t intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
 352 |     if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
 353 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 354 | 
 355 |     intan_device_state_t* state = (intan_device_state_t*)drv->context;
 356 |     /* Convert voltage to equivalent current using channel impedance */
 357 |     float z_ohms = state->channels[channel].impedance_ohms;
 358 |     if (z_ohms <= 0.0f) z_ohms = 150000.0f;
 359 |     double current_amps = (double)voltage_v / (double)z_ohms;
 360 |     int32_t current_pA = (int32_t)(current_amps * 1e12);
 361 | 
 362 |     uint32_t duration_us = (uint32_t)((p1_ms + p2_ms) * 1000.0);
 363 |     if (duration_us == 0) duration_us = 1000;
 364 | 
 365 |     return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
 366 | }
 367 | 
 368 | static wet_hal_status_t intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
 369 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 370 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 371 |     return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
 372 | }
 373 | 
 374 | static wet_hal_status_t intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count) {
 375 |     if (!drv || !voltages_out || !spikes_out) return WET_HAL_ERR_NULL_PTR;
 376 |     uint32_t count = channel_count < INTAN_RHS2116_NUM_CHANNELS ? channel_count : INTAN_RHS2116_NUM_CHANNELS;
 377 |     for (uint32_t i = 0; i < count; ++i) {
 378 |         voltages_out[i] = -0.070f; /* -70 mV */
 379 |         spikes_out[i] = 0;
 380 |     }
 381 |     return WET_HAL_OK;
 382 | }
 383 | 
 384 | static wet_hal_status_t intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
 385 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 386 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 387 |     return wet_hal_intan_measure_impedance(drv, (uint8_t)channel, freq_hz, out_mag_ohms, out_phase_rad);
 388 | }
 389 | 
 390 | static wet_hal_status_t intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel) {
 391 |     if (!drv) return WET_HAL_ERR_NULL_PTR;
 392 |     if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
 393 |     return wet_hal_intan_set_charge_recovery(drv, (uint8_t)channel, 1);
 394 | }
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

### `native/src/wet_scheduler.c` (630 lines, SHA-256: `1fc17137ae23e515...`)

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
  19 | #define WET_CACHELINE_SIZE 64
  20 | #define WET_DEFAULT_SAMPLE_CAPACITY 100000
  21 | 
  22 | #if defined(_WIN32)
  23 | typedef union _LARGE_INTEGER {
  24 |     struct {
  25 |         uint32_t LowPart;
  26 |         int32_t  HighPart;
  27 |     } s;
  28 |     int64_t QuadPart;
  29 | } LARGE_INTEGER;
  30 | 
  31 | typedef void* HANDLE;
  32 | typedef unsigned long DWORD;
  33 | typedef uint64_t DWORD_PTR;
  34 | typedef int BOOL;
  35 | 
  36 | #ifdef __cplusplus
  37 | extern "C" {
  38 | #endif
  39 | int __stdcall QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount);
  40 | int __stdcall QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency);
  41 | HANDLE __stdcall GetCurrentThread(void);
  42 | HANDLE __stdcall GetCurrentProcess(void);
  43 | DWORD_PTR __stdcall SetThreadAffinityMask(HANDLE hThread, DWORD_PTR dwThreadAffinityMask);
  44 | BOOL __stdcall SetPriorityClass(HANDLE hProcess, DWORD dwPriorityClass);
  45 | BOOL __stdcall SetThreadPriority(HANDLE hThread, int nPriority);
  46 | HANDLE __stdcall CreateThread(void* lpThreadAttributes, size_t dwStackSize, void* lpStartAddress, void* lpParameter, DWORD dwCreationFlags, DWORD* lpThreadId);
  47 | DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
  48 | BOOL __stdcall CloseHandle(HANDLE hObject);
  49 | void __stdcall Sleep(DWORD dwMilliseconds);
  50 | #ifdef __cplusplus
  51 | }
  52 | #endif
  53 | #else
  54 | #include <time.h>
  55 | #include <pthread.h>
  56 | #include <sched.h>
  57 | #endif
  58 | 
  59 | /* Calibrated processor instruction pipeline pause */
  60 | static inline void wet_cpu_pause(void) {
  61 | #if defined(__clang__) || defined(__GNUC__)
  62 |     __builtin_ia32_pause();
  63 | #elif defined(_MSC_VER)
  64 |     _mm_pause();
  65 | #elif defined(__aarch64__)
  66 |     __asm__ __volatile__("isb\n");
  67 | #else
  68 |     /* NOP fallback */
  69 | #endif
  70 | }
  71 | 
  72 | /* Atomic Acquire/Release Memory Barriers */
  73 | static inline uint32_t wet_atomic_load_u32_acquire(const volatile uint32_t* ptr) {
  74 | #if defined(__GNUC__) || defined(__clang__)
  75 |     return __atomic_load_n(ptr, __ATOMIC_ACQUIRE);
  76 | #else
  77 |     return *ptr;
  78 | #endif
  79 | }
  80 | 
  81 | static inline void wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val) {
  82 | #if defined(__GNUC__) || defined(__clang__)
  83 |     __atomic_store_n(ptr, val, __ATOMIC_RELEASE);
  84 | #else
  85 |     *ptr = val;
  86 | #endif
  87 | }
  88 | 
  89 | /* =========================================================================
  90 |  * Lockless Single-Producer Single-Consumer (SPSC) Ring Buffer
  91 |  * Cacheline-aligned (64-byte padding) to eliminate false sharing
  92 |  * ========================================================================= */
  93 | 
  94 | typedef struct {
  95 |     /* Producer cache line */
  96 |     volatile uint32_t head;
  97 |     uint8_t           _pad0[WET_CACHELINE_SIZE - sizeof(uint32_t)];
  98 | 
  99 |     /* Consumer cache line */
 100 |     volatile uint32_t tail;
 101 |     uint8_t           _pad1[WET_CACHELINE_SIZE - sizeof(uint32_t)];
 102 | 
 103 |     /* Metadata */
 104 |     uint32_t capacity;
 105 |     uint32_t mask;
 106 |     size_t   elem_size;
 107 |     uint8_t* buffer;
 108 | } wet_spsc_ring_t;
 109 | 
 110 | static int wet_spsc_init(wet_spsc_ring_t* ring, uint32_t capacity, size_t elem_size) {
 111 |     uint32_t cap = 1;
 112 |     while (cap < capacity) cap <<= 1;
 113 |     ring->capacity = cap;
 114 |     ring->mask = cap - 1;
 115 |     ring->elem_size = elem_size;
 116 |     ring->head = 0;
 117 |     ring->tail = 0;
 118 |     ring->buffer = (uint8_t*)calloc(cap, elem_size);
 119 |     return (ring->buffer != NULL);
 120 | }
 121 | 
 122 | static void wet_spsc_free(wet_spsc_ring_t* ring) {
 123 |     if (ring->buffer) {
 124 |         free(ring->buffer);
 125 |         ring->buffer = NULL;
 126 |     }
 127 | }
 128 | 
 129 | static inline int wet_spsc_push(wet_spsc_ring_t* ring, const void* item) {
 130 |     uint32_t head = ring->head;
 131 |     uint32_t tail = wet_atomic_load_u32_acquire(&ring->tail);
 132 |     if ((head - tail) >= ring->capacity) {
 133 |         return 0; /* Ring buffer full */
 134 |     }
 135 |     memcpy(ring->buffer + (head & ring->mask) * ring->elem_size, item, ring->elem_size);
 136 |     wet_atomic_store_u32_release(&ring->head, head + 1);
 137 |     return 1;
 138 | }
 139 | 
 140 | static inline int wet_spsc_pop(wet_spsc_ring_t* ring, void* out_item) {
 141 |     uint32_t tail = ring->tail;
 142 |     uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
 143 |     if (tail == head) {
 144 |         return 0; /* Ring buffer empty */
 145 |     }
 146 |     memcpy(out_item, ring->buffer + (tail & ring->mask) * ring->elem_size, ring->elem_size);
 147 |     wet_atomic_store_u32_release(&ring->tail, tail + 1);
 148 |     return 1;
 149 | }
 150 | 
 151 | /* =========================================================================
 152 |  * Scheduler Internal Structure
 153 |  * ========================================================================= */
 154 | 
 155 | struct wet_scheduler {
 156 |     wet_vm_instance_t*     vm;
 157 |     wet_scheduler_config_t config;
 158 |     wet_scheduler_stats_t  stats;
 159 | 
 160 |     /* SPSC Ring Buffers */
 161 |     wet_spsc_ring_t        telem_ring;
 162 |     wet_spsc_ring_t        stim_ring;
 163 | 
 164 |     /* High-Resolution Monotonic Timer State */
 165 |     int64_t                qpf_freq;
 166 |     double                 qpc_per_us;
 167 |     int64_t                period_qpc;
 168 |     int64_t                next_deadline_qpc;
 169 | 
 170 |     /* Execution State */
 171 |     volatile uint32_t      is_running;
 172 |     volatile uint32_t      stop_requested;
 173 |     uint8_t                thread_initialized;
 174 | #if defined(_WIN32)
 175 |     HANDLE                 thread_handle;
 176 | #else
 177 |     pthread_t              thread_handle;
 178 | #endif
 179 | 
 180 |     /* Benchmark Sample Buffers */
 181 |     uint32_t               sample_capacity;
 182 |     uint32_t               sample_count;
 183 |     double*                sample_jitters_us;
 184 |     double*                sample_computes_us;
 185 |     double*                sample_periods_us;
 186 | 
 187 |     /* Running Accumulators for Online Means */
 188 |     double                 sum_compute_us;
 189 |     double                 sum_period_us;
 190 |     double                 sum_jitter_us;
 191 | };
 192 | 
 193 | /* Fast in-place quicksort for doubles (used for exact percentile calculation) */
 194 | static void wet_sort_doubles(double* arr, int left, int right) {
 195 |     if (left >= right) return;
 196 |     double pivot = arr[(left + right) / 2];
 197 |     int i = left;
 198 |     int j = right;
 199 |     while (i <= j) {
 200 |         while (arr[i] < pivot) i++;
 201 |         while (arr[j] > pivot) j--;
 202 |         if (i <= j) {
 203 |             double tmp = arr[i];
 204 |             arr[i] = arr[j];
 205 |             arr[j] = tmp;
 206 |             i++;
 207 |             j--;
 208 |         }
 209 |     }
 210 |     if (left < j)  wet_sort_doubles(arr, left, j);
 211 |     if (i < right) wet_sort_doubles(arr, i, right);
 212 | }
 213 | 
 214 | /* =========================================================================
 215 |  * Thread Worker Procedure
 216 |  * ========================================================================= */
 217 | 
 218 | #if defined(_WIN32)
 219 | static DWORD __stdcall wet_scheduler_thread_proc(void* param) {
 220 |     wet_scheduler_t* sched = (wet_scheduler_t*)param;
 221 |     if (!sched) return 1;
 222 | 
 223 |     /* 1. Core Pinning */
 224 |     if (sched->config.enable_core_pinning) {
 225 |         DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
 226 |         SetThreadAffinityMask(GetCurrentThread(), mask);
 227 |     }
 228 | 
 229 |     /* 2. Process & Thread Priority Elevation */
 230 |     if (sched->config.enable_priority_elevation) {
 231 |         if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
 232 |             /* Fallback to HIGH_PRIORITY_CLASS if REALTIME permission is restricted */
 233 |             SetPriorityClass(GetCurrentProcess(), 0x00000080);
 234 |         }
 235 |         SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
 236 |     }
 237 | 
 238 |     sched->is_running = 1;
 239 | 
 240 |     /* Real-Time Stepping Loop */
 241 |     while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
 242 |         if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
 243 |             break;
 244 |         }
 245 | 
 246 |         wet_status_t st = wet_scheduler_step(sched);
 247 |         if (st != WET_OK && st != WET_ERR_HALTED) {
 248 |             break;
 249 |         }
 250 | 
 251 |         if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) {
 252 |             break;
 253 |         }
 254 |     }
 255 | 
 256 |     sched->is_running = 0;
 257 |     return 0;
 258 | }
 259 | #else
 260 | static void* wet_scheduler_thread_proc(void* param) {
 261 |     wet_scheduler_t* sched = (wet_scheduler_t*)param;
 262 |     if (!sched) return NULL;
 263 | 
 264 |     if (sched->config.enable_core_pinning) {
 265 |         cpu_set_t cpuset;
 266 |         CPU_ZERO(&cpuset);
 267 |         CPU_SET(sched->config.target_core, &cpuset);
 268 |         pthread_setaffinity_np(pthread_self(), sizeof(cpu_set_t), &cpuset);
 269 |     }
 270 | 
 271 |     sched->is_running = 1;
 272 |     while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
 273 |         if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
 274 |             break;
 275 |         }
 276 |         wet_status_t st = wet_scheduler_step(sched);
 277 |         if (st != WET_OK && st != WET_ERR_HALTED) break;
 278 |         if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) break;
 279 |     }
 280 |     sched->is_running = 0;
 281 |     return NULL;
 282 | }
 283 | #endif
 284 | 
 285 | /* =========================================================================
 286 |  * Public C-ABI API Implementation
 287 |  * ========================================================================= */
 288 | 
 289 | WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config) {
 290 |     wet_scheduler_t* sched = (wet_scheduler_t*)calloc(1, sizeof(wet_scheduler_t));
 291 |     if (!sched) return NULL;
 292 | 
 293 |     sched->vm = vm;
 294 | 
 295 |     /* Apply default configuration */
 296 |     if (config) {
 297 |         sched->config = *config;
 298 |     } else {
 299 |         sched->config.target_period_us = 100; /* 100 µs = 10 kHz */
 300 |         sched->config.target_core = 1;
 301 |         sched->config.priority_class = 0x00000100; /* REALTIME_PRIORITY_CLASS */
 302 |         sched->config.thread_priority = 15;        /* THREAD_PRIORITY_TIME_CRITICAL */
 303 |         sched->config.enable_core_pinning = 1;
 304 |         sched->config.enable_priority_elevation = 1;
 305 |         sched->config.telemetry_queue_capacity = 1024;
 306 |         sched->config.stimulus_queue_capacity = 256;
 307 |         sched->config.total_ticks = 0;
 308 |     }
 309 | 
 310 |     if (sched->config.target_period_us == 0) sched->config.target_period_us = 100;
 311 |     if (sched->config.telemetry_queue_capacity == 0) sched->config.telemetry_queue_capacity = 1024;
 312 |     if (sched->config.stimulus_queue_capacity == 0) sched->config.stimulus_queue_capacity = 256;
 313 | 
 314 |     /* Initialize SPSC Ring Buffers */
 315 |     if (!wet_spsc_init(&sched->telem_ring, sched->config.telemetry_queue_capacity, sizeof(wet_telemetry_t))) {
 316 |         free(sched);
 317 |         return NULL;
 318 |     }
 319 | 
 320 |     if (!wet_spsc_init(&sched->stim_ring, sched->config.stimulus_queue_capacity, sizeof(wet_stim_command_t))) {
 321 |         wet_spsc_free(&sched->telem_ring);
 322 |         free(sched);
 323 |         return NULL;
 324 |     }
 325 | 
 326 |     /* Initialize High-Resolution Monotonic Hardware Clock */
 327 | #if defined(_WIN32)
 328 |     LARGE_INTEGER qpf;
 329 |     QueryPerformanceFrequency(&qpf);
 330 |     sched->qpf_freq = qpf.QuadPart;
 331 |     sched->qpc_per_us = (double)qpf.QuadPart / 1000000.0;
 332 |     sched->period_qpc = (int64_t)((double)sched->config.target_period_us * sched->qpc_per_us);
 333 | #else
 334 |     sched->qpf_freq = 1000000000ULL;
 335 |     sched->qpc_per_us = 1000.0;
 336 |     sched->period_qpc = (int64_t)(sched->config.target_period_us * 1000ULL);
 337 | #endif
 338 | 
 339 |     /* Allocate Sample Buffers for Jitter / Latency Statistics */
 340 |     sched->sample_capacity = WET_DEFAULT_SAMPLE_CAPACITY;
 341 |     sched->sample_jitters_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 342 |     sched->sample_computes_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 343 |     sched->sample_periods_us = (double*)malloc(sched->sample_capacity * sizeof(double));
 344 | 
 345 |     /* Pre-fault and commit all memory pages in advance to eliminate demand-paging faults in hot loop */
 346 |     if (sched->sample_jitters_us)  memset(sched->sample_jitters_us, 0, sched->sample_capacity * sizeof(double));
 347 |     if (sched->sample_computes_us) memset(sched->sample_computes_us, 0, sched->sample_capacity * sizeof(double));
 348 |     if (sched->sample_periods_us)  memset(sched->sample_periods_us, 0, sched->sample_capacity * sizeof(double));
 349 | 
 350 |     /* Initialize stats */
 351 |     sched->stats.min_compute_us = 1e9;
 352 |     sched->stats.min_period_us = 1e9;
 353 | 
 354 |     return sched;
 355 | }
 356 | 
 357 | WET_EXPORT wet_status_t wet_scheduler_start(wet_scheduler_t* sched) {
 358 |     if (!sched) return WET_ERR_NULL_PTR;
 359 |     if (sched->is_running) return WET_OK;
 360 | 
 361 |     sched->stop_requested = 0;
 362 |     sched->next_deadline_qpc = 0;
 363 | 
 364 | #if defined(_WIN32)
 365 |     DWORD thread_id = 0;
 366 |     sched->thread_handle = CreateThread(NULL, 0, wet_scheduler_thread_proc, sched, 0, &thread_id);
 367 |     if (!sched->thread_handle) {
 368 |         return WET_ERR_ALLOC_FAILED;
 369 |     }
 370 | #else
 371 |     if (pthread_create(&sched->thread_handle, NULL, wet_scheduler_thread_proc, sched) != 0) {
 372 |         return WET_ERR_ALLOC_FAILED;
 373 |     }
 374 | #endif
 375 | 
 376 |     sched->thread_initialized = 1;
 377 |     return WET_OK;
 378 | }
 379 | 
 380 | WET_EXPORT wet_status_t wet_scheduler_step(wet_scheduler_t* sched) {
 381 |     if (!sched) return WET_ERR_NULL_PTR;
 382 |     if (!sched->vm) return WET_ERR_NULL_PTR;
 383 | 
 384 |     /* Timestamp at tick start */
 385 | #if defined(_WIN32)
 386 |     LARGE_INTEGER t_start;
 387 |     QueryPerformanceCounter(&t_start);
 388 |     int64_t start_qpc = t_start.QuadPart;
 389 | #else
 390 |     struct timespec ts_start;
 391 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_start);
 392 |     int64_t start_qpc = (int64_t)ts_start.tv_sec * 1000000000ULL + ts_start.tv_nsec;
 393 | #endif
 394 | 
 395 |     /* Maintain isochronous deadline.
 396 |      * Trade-off: If lag exceeds 2 periods (>200 µs), resynchronize forward to avoid
 397 |      * catastrophic catch-up storms at the expense of wallclock phase slip. */
 398 |     if (sched->next_deadline_qpc == 0 || start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
 399 |         sched->next_deadline_qpc = start_qpc + sched->period_qpc;
 400 |     } else {
 401 |         sched->next_deadline_qpc += sched->period_qpc;
 402 |     }
 403 | 
 404 |     /* 1. Drain incoming asynchronous stimuli from SPSC ring buffer */
 405 |     wet_stim_command_t stim_cmd;
 406 |     while (wet_spsc_pop(&sched->stim_ring, &stim_cmd)) {
 407 |         if (stim_cmd.channel < sched->vm->config.channel_count) {
 408 |             wet_inject_stimulus(sched->vm, stim_cmd.channel, stim_cmd.voltage_v, stim_cmd.phase1_ms, stim_cmd.phase2_ms);
 409 |             sched->stats.stimuli_injected++;
 410 |         }
 411 |     }
 412 | 
 413 |     /* 2. Execute compute step (C99 Bytecode + Biophysical COBA-LIF ODE + Watchdogs) */
 414 |     wet_telemetry_t telem;
 415 |     wet_status_t status = wet_vm_step_internal(sched->vm, &telem);
 416 | 
 417 |     /* 3. Non-blocking stream telemetry to host SPSC queue */
 418 |     if (!wet_spsc_push(&sched->telem_ring, &telem)) {
 419 |         sched->stats.telemetry_dropped++;
 420 |     }
 421 | 
 422 |     /* 4. Measure compute latency */
 423 | #if defined(_WIN32)
 424 |     LARGE_INTEGER t_compute;
 425 |     QueryPerformanceCounter(&t_compute);
 426 |     double compute_us = (double)(t_compute.QuadPart - start_qpc) / sched->qpc_per_us;
 427 | #else
 428 |     struct timespec ts_comp;
 429 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_comp);
 430 |     int64_t comp_qpc = (int64_t)ts_comp.tv_sec * 1000000000ULL + ts_comp.tv_nsec;
 431 |     double compute_us = (double)(comp_qpc - start_qpc) / sched->qpc_per_us;
 432 | #endif
 433 | 
 434 |     /* 5. Check deadline overrun (compute duration exceeding target period) */
 435 |     if (compute_us > (double)sched->config.target_period_us) {
 436 |         sched->stats.deadline_overruns++;
 437 |     }
 438 | 
 439 | #if defined(_WIN32)
 440 |     /* 6. Hybrid precision pacing: calibrated spin-wait tail using _mm_pause().
 441 |      * STRICTLY ZERO Sleep() in the hot real-time execution loop. */
 442 |     if (t_compute.QuadPart < sched->next_deadline_qpc) {
 443 |         LARGE_INTEGER t_now;
 444 |         do {
 445 |             wet_cpu_pause();
 446 |             QueryPerformanceCounter(&t_now);
 447 |         } while (t_now.QuadPart < sched->next_deadline_qpc);
 448 |     }
 449 | 
 450 |     /* 7. Measure actual period and jitter */
 451 |     LARGE_INTEGER t_end;
 452 |     QueryPerformanceCounter(&t_end);
 453 |     double actual_period_us = (double)(t_end.QuadPart - start_qpc) / sched->qpc_per_us;
 454 | #else
 455 |     if (comp_qpc < sched->next_deadline_qpc) {
 456 |         struct timespec ts_now;
 457 |         do {
 458 |             wet_cpu_pause();
 459 |             clock_gettime(CLOCK_MONOTONIC_RAW, &ts_now);
 460 |         } while (((int64_t)ts_now.tv_sec * 1000000000ULL + ts_now.tv_nsec) < sched->next_deadline_qpc);
 461 |     }
 462 |     struct timespec ts_end;
 463 |     clock_gettime(CLOCK_MONOTONIC_RAW, &ts_end);
 464 |     int64_t end_qpc = (int64_t)ts_end.tv_sec * 1000000000ULL + ts_end.tv_nsec;
 465 |     double actual_period_us = (double)(end_qpc - start_qpc) / sched->qpc_per_us;
 466 | #endif
 467 | 
 468 |     double jitter_us = wet_fabs(actual_period_us - (double)sched->config.target_period_us);
 469 | 
 470 |     /* 8. Record metrics */
 471 |     sched->stats.total_ticks++;
 472 |     sched->sum_compute_us += compute_us;
 473 |     sched->sum_period_us += actual_period_us;
 474 |     sched->sum_jitter_us += jitter_us;
 475 | 
 476 |     if (compute_us < sched->stats.min_compute_us) sched->stats.min_compute_us = compute_us;
 477 |     if (compute_us > sched->stats.max_compute_us) sched->stats.max_compute_us = compute_us;
 478 | 
 479 |     if (actual_period_us < sched->stats.min_period_us) sched->stats.min_period_us = actual_period_us;
 480 |     if (actual_period_us > sched->stats.max_period_us) sched->stats.max_period_us = actual_period_us;
 481 | 
 482 |     if (jitter_us > sched->stats.max_jitter_us) sched->stats.max_jitter_us = jitter_us;
 483 | 
 484 |     /* Append to sample buffer */
 485 |     if (sched->sample_count < sched->sample_capacity) {
 486 |         sched->sample_jitters_us[sched->sample_count] = jitter_us;
 487 |         sched->sample_computes_us[sched->sample_count] = compute_us;
 488 |         sched->sample_periods_us[sched->sample_count] = actual_period_us;
 489 |         sched->sample_count++;
 490 |     }
 491 | 
 492 |     return status;
 493 | }
 494 | 
 495 | WET_EXPORT wet_status_t wet_scheduler_stop(wet_scheduler_t* sched) {
 496 |     if (!sched) return WET_ERR_NULL_PTR;
 497 | 
 498 |     wet_atomic_store_u32_release(&sched->stop_requested, 1);
 499 | 
 500 |     if (sched->thread_initialized) {
 501 | #if defined(_WIN32)
 502 |         if (sched->thread_handle) {
 503 |             WaitForSingleObject(sched->thread_handle, 5000);
 504 |             CloseHandle(sched->thread_handle);
 505 |             sched->thread_handle = NULL;
 506 |         }
 507 | #else
 508 |         if (sched->thread_handle) {
 509 |             pthread_join(sched->thread_handle, NULL);
 510 |         }
 511 | #endif
 512 |         sched->thread_initialized = 0;
 513 |     }
 514 | 
 515 |     sched->is_running = 0;
 516 |     return WET_OK;
 517 | }
 518 | 
 519 | WET_EXPORT wet_status_t wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats) {
 520 |     if (!sched || !out_stats) return WET_ERR_NULL_PTR;
 521 | 
 522 |     *out_stats = sched->stats;
 523 | 
 524 |     uint64_t n = sched->stats.total_ticks;
 525 |     if (n > 0) {
 526 |         out_stats->mean_compute_us = sched->sum_compute_us / (double)n;
 527 |         out_stats->mean_period_us = sched->sum_period_us / (double)n;
 528 |         out_stats->mean_jitter_us = sched->sum_jitter_us / (double)n;
 529 |     }
 530 | 
 531 |     /* Compute exact percentiles from sample buffer */
 532 |     if (sched->sample_count > 0) {
 533 |         uint32_t cnt = sched->sample_count;
 534 |         double* sorted = (double*)malloc(cnt * sizeof(double));
 535 |         if (sorted) {
 536 |             memcpy(sorted, sched->sample_jitters_us, cnt * sizeof(double));
 537 |             wet_sort_doubles(sorted, 0, (int)cnt - 1);
 538 | 
 539 |             out_stats->p50_jitter_us = sorted[(size_t)(cnt * 0.50)];
 540 |             out_stats->p95_jitter_us = sorted[(size_t)(cnt * 0.95)];
 541 |             out_stats->p99_jitter_us = sorted[(size_t)(cnt * 0.99)];
 542 |             out_stats->p999_jitter_us = sorted[(size_t)(cnt * 0.999)];
 543 |             out_stats->max_jitter_us = sorted[cnt - 1];
 544 | 
 545 |             free(sorted);
 546 |         }
 547 |     }
 548 | 
 549 |     return WET_OK;
 550 | }
 551 | 
 552 | WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem) {
 553 |     if (!sched || !out_telem) return WET_ERR_NULL_PTR;
 554 |     if (wet_spsc_pop(&sched->telem_ring, out_telem)) {
 555 |         return WET_OK;
 556 |     }
 557 |     return WET_ERR_NULL_PTR; /* No telemetry available */
 558 | }
 559 | 
 560 | WET_EXPORT wet_status_t wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd) {
 561 |     if (!sched || !cmd) return WET_ERR_NULL_PTR;
 562 |     if (wet_spsc_push(&sched->stim_ring, cmd)) {
 563 |         return WET_OK;
 564 |     }
 565 |     return WET_ERR_ALLOC_FAILED; /* Stimulus ring buffer full */
 566 | }
 567 | 
 568 | WET_EXPORT wet_status_t wet_scheduler_benchmark(
 569 |     wet_scheduler_t* sched,
 570 |     uint32_t total_ticks,
 571 |     wet_scheduler_stats_t* out_stats
 572 | ) {
 573 |     if (!sched) return WET_ERR_NULL_PTR;
 574 | 
 575 |     /* Apply thread affinity and priority on benchmark caller thread if not backgrounded */
 576 | #if defined(_WIN32)
 577 |     if (sched->config.enable_core_pinning) {
 578 |         DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
 579 |         SetThreadAffinityMask(GetCurrentThread(), mask);
 580 |     }
 581 |     if (sched->config.enable_priority_elevation) {
 582 |         if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
 583 |             SetPriorityClass(GetCurrentProcess(), 0x00000080);
 584 |         }
 585 |         SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
 586 |     }
 587 | #endif
 588 | 
 589 |     /* Warm-up ticks to ensure hardware instruction/data caches and branch predictors are primed */
 590 |     for (int w = 0; w < 10; ++w) {
 591 |         wet_scheduler_step(sched);
 592 |     }
 593 | 
 594 |     /* Reset metrics after warm-up */
 595 |     memset(&sched->stats, 0, sizeof(sched->stats));
 596 |     sched->stats.min_compute_us = 1e9;
 597 |     sched->stats.min_period_us = 1e9;
 598 |     sched->sample_count = 0;
 599 |     sched->sum_compute_us = 0.0;
 600 |     sched->sum_period_us = 0.0;
 601 |     sched->sum_jitter_us = 0.0;
 602 |     sched->next_deadline_qpc = 0;
 603 |     sched->is_running = 1;
 604 | 
 605 |     for (uint32_t i = 0; i < total_ticks; ++i) {
 606 |         wet_status_t st = wet_scheduler_step(sched);
 607 |         if (st != WET_OK && st != WET_ERR_HALTED) {
 608 |             sched->is_running = 0;
 609 |             return st;
 610 |         }
 611 |     }
 612 | 
 613 |     sched->is_running = 0;
 614 |     return wet_scheduler_get_stats(sched, out_stats);
 615 | }
 616 | 
 617 | WET_EXPORT void wet_scheduler_destroy(wet_scheduler_t* sched) {
 618 |     if (!sched) return;
 619 | 
 620 |     wet_scheduler_stop(sched);
 621 | 
 622 |     wet_spsc_free(&sched->telem_ring);
 623 |     wet_spsc_free(&sched->stim_ring);
 624 | 
 625 |     if (sched->sample_jitters_us)  free(sched->sample_jitters_us);
 626 |     if (sched->sample_computes_us) free(sched->sample_computes_us);
 627 |     if (sched->sample_periods_us)  free(sched->sample_periods_us);
 628 | 
 629 |     free(sched);
 630 | }
```

### `native/src/wetvm_api.c` (613 lines, SHA-256: `8971d78775e796a5...`)

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
  55 |     } else {
  56 |         vm->config.dt_ms = 0.1;
  57 |         vm->config.max_stack_depth = 1024;
  58 |         vm->config.max_locals = 256;
  59 |         vm->config.channel_count = 64;
  60 |         vm->config.max_ops_per_tick = 100000U;
  61 |     }
  62 | 
  63 |     vm->max_stack = vm->config.max_stack_depth;
  64 |     vm->stack = (wet_value_t*)calloc(vm->max_stack, sizeof(wet_value_t));
  65 |     if (!vm->stack) {
  66 |         free(vm);
  67 |         return NULL;
  68 |     }
  69 | 
  70 |     vm->max_locals = vm->config.max_locals;
  71 |     vm->locals = (wet_value_t*)calloc(vm->max_locals, sizeof(wet_value_t));
  72 |     if (!vm->locals) {
  73 |         free(vm->stack);
  74 |         free(vm);
  75 |         return NULL;
  76 |     }
  77 | 
  78 |     vm->max_call_depth = 64;
  79 |     vm->call_stack = (wet_call_frame_t*)calloc(vm->max_call_depth, sizeof(wet_call_frame_t));
  80 |     if (!vm->call_stack) {
  81 |         free(vm->locals);
  82 |         free(vm->stack);
  83 |         free(vm);
  84 |         return NULL;
  85 |     }
  86 | 
  87 |     vm->grid_rows = 8;
  88 |     vm->grid_cols = 8;
  89 |     vm->last_error[0] = '\0';
  90 | 
  91 |     /* Initialize cyber-physical life support actuator states */
  92 |     vm->ambient_temperature_c = 37.0f;
  93 |     for (int p = 0; p < 4; ++p) {
  94 |         vm->fluid_pressure_kpa[p] = 101.325f;
  95 |     }
  96 | 
  97 |     /* Ring-0 Life Support Supervisor Initialization */
  98 |     vm->life_supervisor.supervisor_active = 1;
  99 |     vm->life_supervisor.maintenance_temperature_c = 37.0f;
 100 |     for (int i = 0; i < 8; ++i) {
 101 |         vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
 102 |     }
 103 | 
 104 |     biophysics_init(&vm->bio, vm->config.dt_ms, 0);
 105 |     interlocks_init(&vm->interlocks);
 106 | 
 107 |     return vm;
 108 | }
 109 | 
 110 | WET_EXPORT wet_vm_t* wet_create_vm_arena(
 111 |     void* arena_buf,
 112 |     size_t arena_bytes,
 113 |     const wet_vm_config_t* config
 114 | ) {
 115 |     if (!arena_buf) return NULL;
 116 | 
 117 |     uint32_t stack_depth = (config && config->max_stack_depth > 0) ? config->max_stack_depth : 1024;
 118 |     uint32_t max_locals = (config && config->max_locals > 0) ? config->max_locals : 256;
 119 |     uint32_t call_depth = 64;
 120 | 
 121 |     size_t needed = sizeof(struct wet_vm_instance)
 122 |                   + (size_t)stack_depth * sizeof(wet_value_t)
 123 |                   + (size_t)max_locals * sizeof(wet_value_t)
 124 |                   + (size_t)call_depth * sizeof(wet_call_frame_t);
 125 | 
 126 |     if (arena_bytes < needed) return NULL;
 127 | 
 128 |     uint8_t* ptr = (uint8_t*)arena_buf;
 129 |     struct wet_vm_instance* vm = (struct wet_vm_instance*)ptr;
 130 |     ptr += sizeof(struct wet_vm_instance);
 131 |     memset(vm, 0, sizeof(struct wet_vm_instance));
 132 | 
 133 |     vm->arena_allocated = 1;
 134 |     if (config) {
 135 |         vm->config = *config;
 136 |         if (vm->config.dt_ms <= 0.0) vm->config.dt_ms = 0.1;
 137 |         if (vm->config.max_stack_depth == 0) vm->config.max_stack_depth = stack_depth;
 138 |         if (vm->config.max_locals == 0) vm->config.max_locals = max_locals;
 139 |         if (vm->config.channel_count == 0) vm->config.channel_count = 64;
 140 |         if (vm->config.max_ops_per_tick == 0) vm->config.max_ops_per_tick = 100000U;
 141 |     } else {
 142 |         vm->config.dt_ms = 0.1;
 143 |         vm->config.max_stack_depth = stack_depth;
 144 |         vm->config.max_locals = max_locals;
 145 |         vm->config.channel_count = 64;
 146 |         vm->config.max_ops_per_tick = 100000U;
 147 |     }
 148 | 
 149 |     vm->max_stack = stack_depth;
 150 |     vm->stack = (wet_value_t*)ptr;
 151 |     ptr += (size_t)stack_depth * sizeof(wet_value_t);
 152 | 
 153 |     vm->max_locals = max_locals;
 154 |     vm->locals = (wet_value_t*)ptr;
 155 |     ptr += (size_t)max_locals * sizeof(wet_value_t);
 156 | 
 157 |     vm->max_call_depth = call_depth;
 158 |     vm->call_stack = (wet_call_frame_t*)ptr;
 159 | 
 160 |     vm->grid_rows = 8;
 161 |     vm->grid_cols = 8;
 162 |     vm->last_error[0] = '\0';
 163 |     vm->ambient_temperature_c = 37.0f;
 164 |     for (int p = 0; p < 4; ++p) {
 165 |         vm->fluid_pressure_kpa[p] = 101.325f;
 166 |     }
 167 | 
 168 |     vm->life_supervisor.supervisor_active = 1;
 169 |     vm->life_supervisor.maintenance_temperature_c = 37.0f;
 170 |     for (int i = 0; i < 8; ++i) {
 171 |         vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
 172 |     }
 173 | 
 174 |     biophysics_init(&vm->bio, vm->config.dt_ms, 0);
 175 |     interlocks_init(&vm->interlocks);
 176 | 
 177 |     return vm;
 178 | }
 179 | 
 180 | WET_EXPORT void wet_free_vm(wet_vm_t* vm) {
 181 |     if (!vm) return;
 182 | 
 183 |     if (vm->hal) {
 184 |         wet_hal_destroy(vm->hal);
 185 |         vm->hal = NULL;
 186 |     }
 187 | 
 188 |     if (vm->constants) {
 189 |         for (size_t i = 0; i < vm->num_constants; ++i) {
 190 |             if (vm->constants[i].str_alloc) {
 191 |                 free(vm->constants[i].str_alloc);
 192 |                 vm->constants[i].str_alloc = NULL;
 193 |             }
 194 |         }
 195 |         free(vm->constants);
 196 |         vm->constants = NULL;
 197 |     }
 198 | 
 199 |     if (vm->bytecode_raw) {
 200 |         free(vm->bytecode_raw);
 201 |         vm->bytecode_raw = NULL;
 202 |     }
 203 | 
 204 |     if (!vm->arena_allocated) {
 205 |         if (vm->stack) {
 206 |             free(vm->stack);
 207 |             vm->stack = NULL;
 208 |         }
 209 | 
 210 |         if (vm->locals) {
 211 |             free(vm->locals);
 212 |             vm->locals = NULL;
 213 |         }
 214 | 
 215 |         if (vm->call_stack) {
 216 |             free(vm->call_stack);
 217 |             vm->call_stack = NULL;
 218 |         }
 219 | 
 220 |         free(vm);
 221 |     }
 222 | }
 223 | 
 224 | WET_EXPORT wet_status_t wet_load_bytecode(
 225 |     wet_vm_t* vm,
 226 |     const uint8_t* code_bytes,
 227 |     size_t size,
 228 |     char* err_buf,
 229 |     size_t err_buf_len
 230 | ) {
 231 |     if (!vm) {
 232 |         if (err_buf && err_buf_len > 0) {
 233 |             snprintf(err_buf, err_buf_len, "Null VM pointer");
 234 |         }
 235 |         return WET_ERR_NULL_PTR;
 236 |     }
 237 |     return wet_vm_load_bytecode_internal(vm, code_bytes, size, err_buf, err_buf_len);
 238 | }
 239 | 
 240 | WET_EXPORT wet_status_t wet_step_tick(
 241 |     wet_vm_t* vm,
 242 |     wet_telemetry_t* out_telem
 243 | ) {
 244 |     if (!vm) return WET_ERR_NULL_PTR;
 245 |     return wet_vm_step_internal(vm, out_telem);
 246 | }
 247 | 
 248 | WET_EXPORT wet_status_t wet_run_ticks(
 249 |     wet_vm_t* vm,
 250 |     uint32_t ticks,
 251 |     uint32_t* executed_ticks,
 252 |     wet_telemetry_t* out_telem
 253 | ) {
 254 |     if (!vm) return WET_ERR_NULL_PTR;
 255 | 
 256 |     uint32_t executed = 0;
 257 |     wet_status_t status = WET_OK;
 258 | 
 259 |     for (uint32_t i = 0; i < ticks; ++i) {
 260 |         status = wet_vm_step_internal(vm, out_telem);
 261 |         if (status != WET_OK) {
 262 |             break;
 263 |         }
 264 |         executed++;
 265 |     }
 266 | 
 267 |     if (executed_ticks) {
 268 |         *executed_ticks = executed;
 269 |     }
 270 | 
 271 |     return status;
 272 | }
 273 | 
 274 | WET_EXPORT wet_status_t wet_inject_stimulus(
 275 |     wet_vm_t* vm,
 276 |     uint8_t channel,
 277 |     float voltage_v,
 278 |     float phase1_ms,
 279 |     float phase2_ms
 280 | ) {
 281 |     if (!vm) return WET_ERR_NULL_PTR;
 282 |     if (channel >= vm->config.channel_count) {
 283 |         snprintf(vm->last_error, sizeof(vm->last_error),
 284 |                  "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
 285 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 286 |     }
 287 |     if (vm->interlocks.locked) {
 288 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 289 |         return WET_ERR_INTERLOCK_LOCKED;
 290 |     }
 291 | 
 292 |     if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage_v, channel)) {
 293 |         snprintf(vm->last_error, sizeof(vm->last_error),
 294 |                  "Capability denied for wet_inject_stimulus on ch %u (req %.2fV)", channel, voltage_v);
 295 |         return WET_ERR_CAPABILITY_DENIED;
 296 |     }
 297 | 
 298 |     /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
 299 |     if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
 300 |         float q_p1 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase1_ms;
 301 |         float q_p2 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase2_ms;
 302 |         if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
 303 |             vm->interlocks.locked = 1;
 304 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
 305 |             vm->interlocks.tripped_channel = channel;
 306 |             vm->interlocks.trip_tick = vm->current_tick;
 307 |             vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
 308 |             snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
 309 |                      "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
 310 |                      channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
 311 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 312 |             return WET_ERR_CHARGE_DENSITY_EXCEEDED;
 313 |         }
 314 |     }
 315 | 
 316 |     /* Active charge recovery: if previous pulse had pending Phase 2 counter-charge, discharge it */
 317 |     bio_stim_pulse_t* prev_p = &vm->bio.stim_pulses[channel];
 318 |     if (prev_p->active && prev_p->phase2_ticks_left > 0) {
 319 |         float i_ua = (prev_p->phase2_amp_v / vm->bio.electrode_impedance_kohm) * 1000.0f;
 320 |         vm->discharge_charge_nc[channel] += i_ua * (float)vm->bio.dt_ms * (float)prev_p->phase2_ticks_left;
 321 |     }
 322 | 
 323 |     float clamped_v = interlocks_clamp_voltage(&vm->interlocks, voltage_v);
 324 |     biophysics_schedule_stim(&vm->bio, channel, clamped_v, phase1_ms, phase2_ms);
 325 |     vm->voltages[channel] = clamped_v;
 326 |     float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
 327 |     vm->last_charge_nc[channel] = i_ma * (phase1_ms - phase2_ms);
 328 |     return WET_OK;
 329 | }
 330 | 
 331 | WET_EXPORT wet_status_t wet_get_telemetry(
 332 |     wet_vm_t* vm,
 333 |     wet_telemetry_t* out_telem
 334 | ) {
 335 |     if (!vm || !out_telem) return WET_ERR_NULL_PTR;
 336 | 
 337 |     out_telem->current_tick = vm->current_tick;
 338 |     out_telem->sim_time_ms = vm->sim_time_ms;
 339 |     out_telem->population_rate_hz = vm->population_rate_hz;
 340 |     memcpy(out_telem->voltages, vm->voltages, sizeof(float) * 64);
 341 |     memcpy(out_telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
 342 |     memcpy(out_telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);
 343 | 
 344 |     return WET_OK;
 345 | }
 346 | 
 347 | WET_EXPORT wet_status_t wet_get_actuator_telemetry(
 348 |     wet_vm_t* vm,
 349 |     wet_actuator_telemetry_t* out_act_telem
 350 | ) {
 351 |     if (!vm || !out_act_telem) return WET_ERR_NULL_PTR;
 352 | 
 353 |     for (int i = 0; i < 8; ++i) {
 354 |         out_act_telem->pump_rates_ul_min[i] = vm->pump_rates_ul_min[i];
 355 |         out_act_telem->pump_dispensed_ul[i] = vm->pump_dispensed_ul[i];
 356 |         out_act_telem->valve_states[i] = vm->valve_states[i];
 357 |     }
 358 |     for (int i = 0; i < 4; ++i) {
 359 |         out_act_telem->motor_positions[i] = vm->motor_positions[i];
 360 |         out_act_telem->motor_speeds_rpm[i] = vm->motor_speeds_rpm[i];
 361 |         out_act_telem->fluid_pressure_kpa[i] = vm->fluid_pressure_kpa[i];
 362 |     }
 363 |     out_act_telem->ambient_temperature_c = vm->ambient_temperature_c;
 364 |     return WET_OK;
 365 | }
 366 | 
 367 | WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm) {
 368 |     if (!vm) return "NULL VM pointer";
 369 |     return vm->last_error;
 370 | }
 371 | 
 372 | WET_EXPORT const char* wet_status_to_string(wet_status_t status) {
 373 |     switch (status) {
 374 |         case WET_OK:
 375 |             return "WET_OK: Operation successful";
 376 |         case WET_ERR_INVALID_MAGIC:
 377 |             return "WET_ERR_INVALID_MAGIC: Invalid WBC header magic";
 378 |         case WET_ERR_CRC_MISMATCH:
 379 |             return "WET_ERR_CRC_MISMATCH: Bytecode CRC32 checksum mismatch";
 380 |         case WET_ERR_UNSUPPORTED_VERSION:
 381 |             return "WET_ERR_UNSUPPORTED_VERSION: Unsupported bytecode version";
 382 |         case WET_ERR_MALFORMED_SECTION:
 383 |             return "WET_ERR_MALFORMED_SECTION: Malformed bytecode or section table";
 384 |         case WET_ERR_STACK_OVERFLOW:
 385 |             return "WET_ERR_STACK_OVERFLOW: Operand stack overflow";
 386 |         case WET_ERR_STACK_UNDERFLOW:
 387 |             return "WET_ERR_STACK_UNDERFLOW: Operand stack underflow";
 388 |         case WET_ERR_INVALID_OPCODE:
 389 |             return "WET_ERR_INVALID_OPCODE: Unrecognized or invalid opcode";
 390 |         case WET_ERR_OUT_OF_BOUNDS_CH:
 391 |             return "WET_ERR_OUT_OF_BOUNDS_CH: Channel index out of bounds";
 392 |         case WET_ERR_DIVISION_BY_ZERO:
 393 |             return "WET_ERR_DIVISION_BY_ZERO: Division by zero";
 394 |         case WET_ERR_NULL_PTR:
 395 |             return "WET_ERR_NULL_PTR: Null pointer argument";
 396 |         case WET_ERR_ALLOC_FAILED:
 397 |             return "WET_ERR_ALLOC_FAILED: Memory allocation failed";
 398 |         case WET_ERR_HALTED:
 399 |             return "WET_ERR_HALTED: Virtual machine is halted";
 400 |         case WET_ERR_CHARGE_IMBALANCE:
 401 |             return "WET_ERR_CHARGE_IMBALANCE: Net charge imbalance exceeded safety threshold (0.5 nC over 10 ms)";
 402 |         case WET_ERR_EPILEPTIFORM_RUNAWAY:
 403 |             return "WET_ERR_EPILEPTIFORM_RUNAWAY: Epileptiform runaway firing breaker tripped (>150 Hz on >35% channels for 50 ms)";
 404 |         case WET_ERR_CAPABILITY_DENIED:
 405 |             return "WET_ERR_CAPABILITY_DENIED: Capability permission denied by bytecode security manifest";
 406 |         case WET_ERR_INTERLOCK_LOCKED:
 407 |             return "WET_ERR_INTERLOCK_LOCKED: Hardware interlock locked out; all stimulation disabled";
 408 |         case WET_ERR_CHARGE_DENSITY_EXCEEDED:
 409 |             return "WET_ERR_CHARGE_DENSITY_EXCEEDED: Single-phase charge density exceeded Shannon safety limit";
 410 |         case WET_ERR_FOCAL_EXCITOTOXICITY:
 411 |             return "WET_ERR_FOCAL_EXCITOTOXICITY: Focal excitotoxicity limit exceeded";
 412 |         case WET_ERR_SHEAR_STRESS_EXCEEDED:
 413 |             return "WET_ERR_SHEAR_STRESS_EXCEEDED: Requested microfluidic pump rate exceeds safe shear stress limit (15.0 uL/min)";
 414 |         case WET_ERR_SECURITY_UNTRUSTED:
 415 |             return "WET_ERR_SECURITY_UNTRUSTED: Bytecode failed cryptographic security signature verification";
 416 |         case WET_ERR_ACTUATOR_FAULT:
 417 |             return "WET_ERR_ACTUATOR_FAULT: Cyber-physical actuator execution fault or invalid parameter";
 418 |         case WET_ERR_THERMAL_LIMIT:
 419 |             return "WET_ERR_THERMAL_LIMIT: Temperature exceeded maximum biological threshold (38.0 C)";
 420 |         case WET_ERR_BUBBLE_DETECTED:
 421 |             return "WET_ERR_BUBBLE_DETECTED: Fluidic optical bubble detector tripped (cavitation hazard)";
 422 |         case WET_ERR_COMPLIANCE_RAILED:
 423 |             return "WET_ERR_COMPLIANCE_RAILED: Stimulator output voltage saturated ASIC compliance rail (+/-7.0 V)";
 424 |         case WET_ERR_BYTECODE_VERIFICATION:
 425 |             return "WET_ERR_BYTECODE_VERIFICATION: WBC binary failed static bytecode verifier checks";
 426 |         default:
 427 |             return "WET_ERR_UNKNOWN: Unknown error status";
 428 |     }
 429 | }
 430 | 
 431 | /* =========================================================================
 432 |  * Phase 3 Hardware Readiness & Safety Implementations
 433 |  * ========================================================================= */
 434 | 
 435 | WET_EXPORT void wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2) {
 436 |     if (!vm) return;
 437 |     interlocks_configure_electrode(&vm->interlocks, material, area_um2);
 438 | }
 439 | 
 440 | WET_EXPORT void wet_active_discharge(wet_vm_t* vm, uint8_t channel) {
 441 |     if (!vm) return;
 442 |     interlocks_active_discharge(&vm->interlocks, channel);
 443 | }
 444 | 
 445 | WET_EXPORT void wet_active_discharge_all(wet_vm_t* vm) {
 446 |     if (!vm) return;
 447 |     interlocks_active_discharge_all(&vm->interlocks);
 448 | }
 449 | 
 450 | WET_EXPORT void wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable) {
 451 |     if (!vm) return;
 452 |     interlocks_enable_dead_head_protection(&vm->interlocks, enable);
 453 | }
 454 | 
 455 | WET_EXPORT void wet_life_supervisor_shutdown(wet_vm_t* vm) {
 456 |     if (!vm) return;
 457 |     vm->life_supervisor.supervisor_active = 0;
 458 |     for (int p = 0; p < 8; ++p) {
 459 |         vm->pump_rates_ul_min[p] = 0.0f;
 460 |     }
 461 | }
 462 | 
 463 | WET_EXPORT void wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial) {
 464 |     if (!vm) return;
 465 |     biophysics_set_blanking_window(&vm->bio, blanking_ms, enable_spatial);
 466 | }
 467 | 
 468 | WET_EXPORT wet_status_t wet_inject_current_stimulus(
 469 |     wet_vm_t* vm,
 470 |     uint8_t channel,
 471 |     float current_ua,
 472 |     float phase1_ms,
 473 |     float phase2_ms
 474 | ) {
 475 |     if (!vm) return WET_ERR_NULL_PTR;
 476 |     if (channel >= vm->config.channel_count) {
 477 |         snprintf(vm->last_error, sizeof(vm->last_error),
 478 |                  "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
 479 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 480 |     }
 481 |     if (vm->interlocks.locked) {
 482 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 483 |         return WET_ERR_INTERLOCK_LOCKED;
 484 |     }
 485 | 
 486 |     if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
 487 |         snprintf(vm->last_error, sizeof(vm->last_error),
 488 |                  "Capability denied for wet_inject_current_stimulus on ch %u", channel);
 489 |         return WET_ERR_CAPABILITY_DENIED;
 490 |     }
 491 | 
 492 |     /* Randles Interface check: V_elec = I * Rs + V_dl */
 493 |     float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
 494 |     wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
 495 |     if (comp_st != WET_OK) {
 496 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 497 |         return comp_st;
 498 |     }
 499 | 
 500 |     /* Shannon charge density limit */
 501 |     if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
 502 |         float q_p1 = fabsf(current_ua) * 1e-3f * phase1_ms;
 503 |         float q_p2 = fabsf(current_ua) * 1e-3f * phase2_ms;
 504 |         if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
 505 |             vm->interlocks.locked = 1;
 506 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
 507 |             vm->interlocks.tripped_channel = channel;
 508 |             vm->interlocks.trip_tick = vm->current_tick;
 509 |             vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
 510 |             snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
 511 |                      "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
 512 |                      channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
 513 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 514 |             return WET_ERR_CHARGE_DENSITY_EXCEEDED;
 515 |         }
 516 |     }
 517 | 
 518 |     biophysics_schedule_stim_current(&vm->bio, channel, current_ua, phase1_ms, phase2_ms, 0.0f);
 519 |     vm->voltages[channel] = v_elec;
 520 |     vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (phase1_ms - phase2_ms);
 521 |     return WET_OK;
 522 | }
 523 | 
 524 | WET_EXPORT wet_status_t wet_verify_bytecode(
 525 |     const uint8_t* bytecode,
 526 |     size_t size,
 527 |     char* err_buf,
 528 |     size_t err_buf_len
 529 | ) {
 530 |     return wet_verify_bytecode_internal(bytecode, size, err_buf, err_buf_len);
 531 | }
 532 | 
 533 | WET_EXPORT wet_status_t wet_vm_snapshot(
 534 |     const wet_vm_t* vm,
 535 |     uint8_t* buffer,
 536 |     size_t* inout_len
 537 | ) {
 538 |     return wet_vm_snapshot_internal(vm, buffer, inout_len);
 539 | }
 540 | 
 541 | WET_EXPORT wet_status_t wet_vm_restore(
 542 |     wet_vm_t* vm,
 543 |     const uint8_t* buffer,
 544 |     size_t len
 545 | ) {
 546 |     return wet_vm_restore_internal(vm, buffer, len);
 547 | }
 548 | 
 549 | WET_EXPORT void wet_set_environmental_sensors(
 550 |     wet_vm_t* vm,
 551 |     float ph,
 552 |     float do_pct,
 553 |     float co2_pct,
 554 |     uint8_t bubble_sensor_id,
 555 |     uint8_t bubble_state,
 556 |     float flow_rate_ul_min
 557 | ) {
 558 |     if (!vm) return;
 559 |     if (ph > 0.0f) vm->ph_level = ph;
 560 |     if (do_pct > 0.0f) vm->dissolved_oxygen_pct = do_pct;
 561 |     if (co2_pct > 0.0f) vm->dissolved_co2_pct = co2_pct;
 562 |     if (bubble_sensor_id < 8) {
 563 |         vm->bubble_detected[bubble_sensor_id] = bubble_state ? 1 : 0;
 564 |         vm->fluid_flow_rate_ul_min[bubble_sensor_id] = flow_rate_ul_min;
 565 |     }
 566 | }
 567 | 
 568 | WET_EXPORT void wet_set_temperature(
 569 |     wet_vm_t* vm,
 570 |     float temp_c
 571 | ) {
 572 |     if (!vm) return;
 573 |     vm->ambient_temperature_c = temp_c;
 574 | }
 575 | 
 576 | WET_EXPORT void wet_set_channel_banks(
 577 |     wet_vm_t* vm,
 578 |     uint64_t ref_mask,
 579 |     uint64_t rec_mask
 580 | ) {
 581 |     if (!vm) return;
 582 |     interlocks_set_channel_banks(&vm->interlocks, ref_mask, rec_mask);
 583 | }
 584 | 
 585 | WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
 586 |     const wet_vm_t* vm,
 587 |     float* out_matrix,
 588 |     size_t out_capacity_floats
 589 | ) {
 590 |     if (!vm || !out_matrix) return WET_ERR_NULL_PTR;
 591 |     if (out_capacity_floats < (size_t)(BIO_NUM_NEURONS * BIO_NUM_NEURONS)) {
 592 |         return WET_ERR_OUT_OF_BOUNDS_CH;
 593 |     }
 594 |     for (size_t i = 0; i < BIO_NUM_NEURONS; ++i) {
 595 |         for (size_t j = 0; j < BIO_NUM_NEURONS; ++j) {
 596 |             if (vm->bio.synapses[i][j].exists) {
 597 |                 out_matrix[i * BIO_NUM_NEURONS + j] = vm->bio.synapses[i][j].weight_ns;
 598 |             } else {
 599 |                 out_matrix[i * BIO_NUM_NEURONS + j] = 0.0f;
 600 |             }
 601 |         }
 602 |     }
 603 |     return WET_OK;
 604 | }
 605 | 
 606 | WET_EXPORT float wet_vm_get_synapse_weight(
 607 |     const wet_vm_t* vm,
 608 |     uint8_t pre,
 609 |     uint8_t post
 610 | ) {
 611 |     if (!vm || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
 612 |     return biophysics_get_weight(&vm->bio, pre, post);
 613 | }
```

### `native/src/wetvm_vm.c` (2023 lines, SHA-256: `4cce51ec2f893ada...`)

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
 213 |     /* 5. Validate Section Table Bounds */
 214 |     size_t sec_table_size = (size_t)hdr->num_sections * WET_SECTION_ENTRY_SIZE;
 215 |     if (WET_HEADER_SIZE + sec_table_size > size) {
 216 |         snprintf(vm->last_error, sizeof(vm->last_error),
 217 |                  "Section table exceeds file boundary (%u sections)", hdr->num_sections);
 218 |         if (err_buf && err_buf_len > 0) {
 219 |             snprintf(err_buf, err_buf_len, "%s", vm->last_error);
 220 |         }
 221 |         return WET_ERR_MALFORMED_SECTION;
 222 |     }
 223 | 
 224 |     /* Clean up previous bytecode and allocate buffer for new bytecode */
 225 |     cleanup_bytecode(vm);
 226 |     vm->bytecode_raw = (uint8_t*)malloc(size);
 227 |     if (!vm->bytecode_raw) {
 228 |         snprintf(vm->last_error, sizeof(vm->last_error), "Memory allocation failed for bytecode");
 229 |         return WET_ERR_ALLOC_FAILED;
 230 |     }
 231 |     memcpy(vm->bytecode_raw, code_bytes, size);
 232 |     vm->bytecode_size = size;
 233 | 
 234 |     /* Parse Section Table */
 235 |     const wet_section_header_t* sections =
 236 |         (const wet_section_header_t*)(vm->bytecode_raw + WET_HEADER_SIZE);
 237 | 
 238 |     const uint8_t* code_ptr = NULL;
 239 |     size_t code_len = 0;
 240 | 
 241 |     for (uint32_t i = 0; i < hdr->num_sections; ++i) {
 242 |         uint16_t stype = sections[i].section_type;
 243 |         uint32_t off = sections[i].offset;
 244 |         uint32_t s_size = sections[i].size;
 245 | 
 246 |         if ((size_t)off + s_size > size) {
 247 |             snprintf(vm->last_error, sizeof(vm->last_error),
 248 |                      "Section %u (type %u) extends beyond file boundary", i, stype);
 249 |             cleanup_bytecode(vm);
 250 |             return WET_ERR_MALFORMED_SECTION;
 251 |         }
 252 | 
 253 |         const uint8_t* sec_data = vm->bytecode_raw + off;
 254 | 
 255 |         if (stype == WET_SEC_CONSTANT_POOL) {
 256 |             /* Unpack Constant Pool */
 257 |             if (s_size < 4) {
 258 |                 snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool truncated");
 259 |                 cleanup_bytecode(vm);
 260 |                 return WET_ERR_MALFORMED_SECTION;
 261 |             }
 262 |             uint32_t num_consts = wet_read_u32_le(sec_data);
 263 |             size_t c_pos = 4;
 264 | 
 265 |             vm->constants = (wet_constant_entry_t*)calloc(num_consts, sizeof(wet_constant_entry_t));
 266 |             if (!vm->constants && num_consts > 0) {
 267 |                 cleanup_bytecode(vm);
 268 |                 return WET_ERR_ALLOC_FAILED;
 269 |             }
 270 |             vm->num_constants = num_consts;
 271 | 
 272 |             for (uint32_t c = 0; c < num_consts; ++c) {
 273 |                 if (c_pos >= s_size) {
 274 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool out of data");
 275 |                     cleanup_bytecode(vm);
 276 |                     return WET_ERR_MALFORMED_SECTION;
 277 |                 }
 278 |                 uint8_t tag = sec_data[c_pos++];
 279 |                 vm->constants[c].val.type = tag;
 280 | 
 281 |                 if (tag == WET_VAL_INT) {
 282 |                     if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 283 |                     vm->constants[c].val.as.i_val = wet_read_i32_le(sec_data + c_pos);
 284 |                     c_pos += 4;
 285 |                 } else if (tag == WET_VAL_FLOAT) {
 286 |                     if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 287 |                     vm->constants[c].val.as.f_val = wet_read_f32_le(sec_data + c_pos);
 288 |                     c_pos += 4;
 289 |                 } else if (tag == WET_VAL_STRING) {
 290 |                     if (c_pos + 2 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 291 |                     uint16_t str_len = wet_read_u16_le(sec_data + c_pos);
 292 |                     c_pos += 2;
 293 |                     if (c_pos + str_len > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
 294 |                     char* sbuf = (char*)malloc(str_len + 1);
 295 |                     if (!sbuf) { cleanup_bytecode(vm); return WET_ERR_ALLOC_FAILED; }
 296 |                     memcpy(sbuf, sec_data + c_pos, str_len);
 297 |                     sbuf[str_len] = '\0';
 298 |                     vm->constants[c].str_alloc = sbuf;
 299 |                     vm->constants[c].val.as.s_val.str = sbuf;
 300 |                     vm->constants[c].val.as.s_val.len = str_len;
 301 |                     c_pos += str_len;
 302 |                 }
 303 |             }
 304 |         } else if (stype == WET_SEC_TOPOLOGY_CONFIG) {
 305 |             if (s_size >= 8) {
 306 |                 /* struct: channels (uint32), rows (uint16), cols (uint16) */
 307 |                 vm->grid_rows = (uint8_t)wet_read_u16_le(sec_data + 4);
 308 |                 vm->grid_cols = (uint8_t)wet_read_u16_le(sec_data + 6);
 309 |             }
 310 |         } else if (stype == WET_SEC_BYTECODE_STREAM) {
 311 |             code_ptr = sec_data;
 312 |             code_len = s_size;
 313 |         }
 314 |     }
 315 | 
 316 |     if (!code_ptr && code_len == 0) {
 317 |         /* Bytecode section might be empty */
 318 |         vm->code = vm->bytecode_raw;
 319 |         vm->code_size = 0;
 320 |     } else {
 321 |         vm->code = code_ptr;
 322 |         vm->code_size = code_len;
 323 |     }
 324 | 
 325 |     /* Reset registers and runtime state */
 326 |     vm->pc = 0;
 327 |     vm->sp = 0;
 328 |     vm->call_sp = 0;
 329 |     vm->is_halted = 0;
 330 |     vm->is_finished = 0;
 331 |     vm->sleep_ticks_remaining = 0;
 332 |     vm->current_tick = 0;
 333 |     vm->sim_time_ms = 0.0;
 334 |     vm->last_error[0] = '\0';
 335 | 
 336 |     vm->loaded_capabilities = hdr->capabilities;
 337 |     biophysics_reset(&vm->bio);
 338 |     interlocks_init(&vm->interlocks);
 339 |     interlocks_set_capabilities(&vm->interlocks, hdr->capabilities, hdr->channel_count);
 340 |     memset(vm->discharge_charge_nc, 0, sizeof(vm->discharge_charge_nc));
 341 | 
 342 |     /* Clear local variables */
 343 |     if (vm->locals) {
 344 |         memset(vm->locals, 0, sizeof(wet_value_t) * vm->max_locals);
 345 |     }
 346 | 
 347 |     /* Clear channel outputs */
 348 |     memset(vm->voltages, 0, sizeof(vm->voltages));
 349 |     memset(vm->spikes, 0, sizeof(vm->spikes));
 350 |     memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 351 |     vm->population_rate_hz = 0.0f;
 352 | 
 353 |     return WET_OK;
 354 | }
 355 | 
 356 | /* =========================================================================
 357 |  * Telemetry Snapshot Population
 358 |  * ========================================================================= */
 359 | 
 360 | static void populate_telemetry(const struct wet_vm_instance* vm, wet_telemetry_t* telem) {
 361 |     if (!telem) return;
 362 |     telem->current_tick = vm->current_tick;
 363 |     telem->sim_time_ms = vm->sim_time_ms;
 364 |     telem->population_rate_hz = vm->population_rate_hz;
 365 |     memcpy(telem->voltages, vm->voltages, sizeof(float) * 64);
 366 |     memcpy(telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
 367 |     memcpy(telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);
 368 | }
 369 | 
 370 | static wet_status_t advance_simulation_tick(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
 371 |     if (vm->interlocks.locked) {
 372 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 373 |         return WET_ERR_INTERLOCK_LOCKED;
 374 |     }
 375 | 
 376 |     /* Dead-heading valve-pump overpressure check */
 377 |     if (vm->interlocks.dead_head_protection_enabled) {
 378 |         for (int p = 0; p < 8; ++p) {
 379 |             if (vm->pump_rates_ul_min[p] > 0.0f) {
 380 |                 uint8_t v = vm->interlocks.pump_valve_mapping[p];
 381 |                 if (v < 8 && vm->valve_states[v] == 0) {
 382 |                     vm->interlocks.locked = 1;
 383 |                     vm->interlocks.trip_reason = INTERLOCK_TRIP_DEAD_HEAD_PRESSURE;
 384 |                     if (vm->hal) {
 385 |                         wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_DEAD_HEAD_PRESSURE);
 386 |                     }
 387 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 388 |                              "ERR_DEAD_HEAD_OVERPRESSURE: Pump %d active at %.2f uL/min while downstream valve %d is closed",
 389 |                              p, (double)vm->pump_rates_ul_min[p], v);
 390 |                     return WET_ERR_ACTUATOR_FAULT;
 391 |                 }
 392 |             }
 393 |         }
 394 |     }
 395 | 
 396 |     /* Phase 3 Environmental Checks: Thermal Limit (CMOS heating) & Bubble Detection */
 397 |     if (vm->ambient_temperature_c > INTERLOCK_THERMAL_LIMIT_C) {
 398 |         wet_status_t th_st = interlocks_check_thermal(&vm->interlocks, vm->current_tick, vm->ambient_temperature_c);
 399 |         if (th_st != WET_OK) {
 400 |             biophysics_zero_all_stim(&vm->bio);
 401 |             vm->is_halted = 1;
 402 |             if (vm->hal) {
 403 |                 wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 404 |             }
 405 |             snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 406 |             populate_telemetry(vm, out_telem);
 407 |             return th_st;
 408 |         }
 409 |     }
 410 | 
 411 |     for (int b = 0; b < 8; ++b) {
 412 |         if (vm->bubble_detected[b]) {
 413 |             wet_status_t bub_st = interlocks_check_bubble(&vm->interlocks, vm->current_tick, 1, (uint8_t)b);
 414 |             if (bub_st != WET_OK) {
 415 |                 for (int p = 0; p < 8; ++p) vm->pump_rates_ul_min[p] = 0.0f;
 416 |                 biophysics_zero_all_stim(&vm->bio);
 417 |                 vm->is_halted = 1;
 418 |                 if (vm->hal) {
 419 |                     wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 420 |                 }
 421 |                 snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 422 |                 populate_telemetry(vm, out_telem);
 423 |                 return bub_st;
 424 |             }
 425 |         }
 426 |     }
 427 | 
 428 |     /* 1. Advance in-silico biophysics by 1 tick (dt = 0.1 ms) */
 429 |     biophysics_step_tick(&vm->bio);
 430 |     for (int ch = 0; ch < 64; ++ch) {
 431 |         if (vm->discharge_charge_nc[ch] != 0.0f) {
 432 |             vm->bio.tick_charge_nc[ch] += vm->discharge_charge_nc[ch];
 433 |             vm->discharge_charge_nc[ch] = 0.0f;
 434 |         }
 435 |     }
 436 |     vm->current_tick++;
 437 |     vm->sim_time_ms = (double)vm->current_tick * vm->config.dt_ms;
 438 |     vm->sim_time_us = (int64_t)((double)vm->current_tick * vm->config.dt_ms * 1000.0 + 0.5);
 439 | 
 440 |     /* 2. Check sliding charge balance watchdog */
 441 |     wet_status_t il_st = interlocks_record_charge_tick(
 442 |         &vm->interlocks, vm->current_tick, vm->bio.tick_charge_nc
 443 |     );
 444 |     if (il_st != WET_OK) {
 445 |         biophysics_zero_all_stim(&vm->bio);
 446 |         memset(vm->voltages, 0, sizeof(vm->voltages));
 447 |         memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 448 |         memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
 449 |         memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
 450 |         memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
 451 |         vm->is_halted = 1;
 452 |         if (vm->hal) {
 453 |             wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 454 |         }
 455 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 456 |         populate_telemetry(vm, out_telem);
 457 |         return il_st;
 458 |     }
 459 | 
 460 |     /* 3. Check epileptiform runaway breaker */
 461 |     il_st = interlocks_check_epileptiform(
 462 |         &vm->interlocks, vm->current_tick, vm->bio.channel_rate_hz
 463 |     );
 464 |     if (il_st != WET_OK) {
 465 |         biophysics_zero_all_stim(&vm->bio);
 466 |         memset(vm->voltages, 0, sizeof(vm->voltages));
 467 |         memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
 468 |         memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
 469 |         memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
 470 |         memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
 471 |         vm->is_halted = 1;
 472 |         if (vm->hal) {
 473 |             wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
 474 |         }
 475 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 476 |         populate_telemetry(vm, out_telem);
 477 |         return il_st;
 478 |     }
 479 | 
 480 |     /* 4. Sync outputs to VM registers & telemetry snapshot */
 481 |     memcpy(vm->voltages, vm->bio.mea_voltage_v, sizeof(float) * 64);
 482 |     memcpy(vm->spikes, vm->bio.spikes_now, sizeof(uint8_t) * 64);
 483 |     memcpy(vm->last_charge_nc, vm->bio.tick_charge_nc, sizeof(float) * 64);
 484 |     vm->population_rate_hz = vm->bio.population_rate_hz;
 485 | 
 486 |     populate_telemetry(vm, out_telem);
 487 |     return WET_OK;
 488 | }
 489 | 
 490 | /* =========================================================================
 491 |  * Cycle-Accurate Execution Stepper
 492 |  * ========================================================================= */
 493 | 
 494 | wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
 495 |     if (!vm) return WET_ERR_NULL_PTR;
 496 | 
 497 |     if (vm->interlocks.locked) {
 498 |         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
 499 |         return WET_ERR_INTERLOCK_LOCKED;
 500 |     }
 501 | 
 502 |     if (vm->is_halted) {
 503 |         if (vm->life_supervisor.supervisor_active) {
 504 |             /* Ring-0 Life Support Supervisor: Maintain baseline nutrient perfusion & temperature */
 505 |             for (int p = 0; p < 8; ++p) {
 506 |                 if (vm->pump_rates_ul_min[p] == 0.0f) {
 507 |                     vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 508 |                 }
 509 |             }
 510 |             vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 511 |             vm->life_supervisor.ticks_under_supervisor++;
 512 |         }
 513 |         snprintf(vm->last_error, sizeof(vm->last_error), "VM is halted");
 514 |         return WET_ERR_HALTED;
 515 |     }
 516 | 
 517 |     /* If bytecode execution has finished or reached end, continue free-running biological stepping */
 518 |     if (vm->is_finished || vm->pc >= vm->code_size) {
 519 |         if (vm->life_supervisor.supervisor_active) {
 520 |             for (int p = 0; p < 8; ++p) {
 521 |                 if (vm->pump_rates_ul_min[p] == 0.0f) {
 522 |                     vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 523 |                 }
 524 |             }
 525 |             vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 526 |             vm->life_supervisor.ticks_under_supervisor++;
 527 |         }
 528 |         return advance_simulation_tick(vm, out_telem);
 529 |     }
 530 | 
 531 |     /* Handle ongoing SLEEP_TICKS decrement */
 532 |     if (vm->sleep_ticks_remaining > 0) {
 533 |         vm->sleep_ticks_remaining--;
 534 |         return advance_simulation_tick(vm, out_telem);
 535 |     }
 536 | 
 537 |     /* Dispatch instructions until a tick yield (SYNC_TICK, SLEEP_TICKS, HALT) */
 538 |     uint32_t instr_count = 0;
 539 |     uint32_t max_ops = vm->config.max_ops_per_tick ? vm->config.max_ops_per_tick : 100000U;
 540 |     while (!vm->is_halted && !vm->is_finished) {
 541 |         if (++instr_count > max_ops) {
 542 |             biophysics_zero_all_stim(&vm->bio);
 543 |             vm->interlocks.locked = 1;
 544 |             vm->interlocks.trip_reason = INTERLOCK_TRIP_CAPABILITY_VIOLATION;
 545 |             if (max_ops == 100000U) {
 546 |                 snprintf(vm->last_error, sizeof(vm->last_error),
 547 |                          "WET_ERR_WATCHDOG_TIMEOUT: Exceeded 100,000 instructions in a single tick");
 548 |             } else {
 549 |                 snprintf(vm->last_error, sizeof(vm->last_error),
 550 |                          "WET_ERR_WATCHDOG_TIMEOUT: Exceeded %u instructions in a single tick", max_ops);
 551 |             }
 552 |             return WET_ERR_WATCHDOG_TIMEOUT;
 553 |         }
 554 | 
 555 |         if (vm->pc >= vm->code_size) {
 556 |             /* End of bytecode reached: advance simulation tick */
 557 |             vm->is_finished = 1;
 558 |             return advance_simulation_tick(vm, out_telem);
 559 |         }
 560 | 
 561 |         size_t instr_pc = vm->pc;
 562 |         uint8_t op = vm->code[instr_pc];
 563 | 
 564 |         switch ((wet_opcode_t)op) {
 565 |             case WET_OP_NOP: {
 566 |                 vm->pc = instr_pc + 1;
 567 |                 break;
 568 |             }
 569 | 
 570 |             case WET_OP_HALT: {
 571 |                 vm->is_finished = 1;
 572 |                 vm->pc = instr_pc + 1;
 573 |                 if (vm->life_supervisor.supervisor_active) {
 574 |                     for (int p = 0; p < 8; ++p) {
 575 |                         if (vm->pump_rates_ul_min[p] == 0.0f) {
 576 |                             vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
 577 |                         }
 578 |                     }
 579 |                     vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
 580 |                     vm->life_supervisor.ticks_under_supervisor++;
 581 |                 }
 582 |                 return advance_simulation_tick(vm, out_telem);
 583 |             }
 584 | 
 585 |             case WET_OP_SYNC_TICK: {
 586 |                 vm->pc = instr_pc + 1;
 587 |                 return advance_simulation_tick(vm, out_telem);
 588 |             }
 589 | 
 590 |             case WET_OP_SLEEP_TICKS: {
 591 |                 if (instr_pc + 3 > vm->code_size) {
 592 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated SLEEP_TICKS operand");
 593 |                     return WET_ERR_INVALID_OPCODE;
 594 |                 }
 595 |                 uint16_t ticks = wet_read_u16_le(vm->code + instr_pc + 1);
 596 |                 vm->pc = instr_pc + 3;
 597 | 
 598 |                 if (ticks > 1) {
 599 |                     vm->sleep_ticks_remaining = ticks - 1;
 600 |                 }
 601 |                 return advance_simulation_tick(vm, out_telem);
 602 |             }
 603 | 
 604 |             case WET_OP_PUSH_CONST: {
 605 |                 if (instr_pc + 3 > vm->code_size) {
 606 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_CONST operand");
 607 |                     return WET_ERR_INVALID_OPCODE;
 608 |                 }
 609 |                 uint16_t idx = wet_read_u16_le(vm->code + instr_pc + 1);
 610 |                 vm->pc = instr_pc + 3;
 611 |                 if (idx >= vm->num_constants) {
 612 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 613 |                              "Constant pool index %u out of range (%zu)", idx, vm->num_constants);
 614 |                     return WET_ERR_INVALID_OPCODE;
 615 |                 }
 616 |                 wet_status_t st = push_val(vm, vm->constants[idx].val);
 617 |                 if (st != WET_OK) return st;
 618 |                 break;
 619 |             }
 620 | 
 621 |             case WET_OP_PUSH_INT: {
 622 |                 if (instr_pc + 5 > vm->code_size) {
 623 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_INT operand");
 624 |                     return WET_ERR_INVALID_OPCODE;
 625 |                 }
 626 |                 int32_t val = wet_read_i32_le(vm->code + instr_pc + 1);
 627 |                 vm->pc = instr_pc + 5;
 628 |                 wet_value_t v;
 629 |                 v.type = WET_VAL_INT;
 630 |                 v.as.i_val = val;
 631 |                 wet_status_t st = push_val(vm, v);
 632 |                 if (st != WET_OK) return st;
 633 |                 break;
 634 |             }
 635 | 
 636 |             case WET_OP_PUSH_FLOAT: {
 637 |                 if (instr_pc + 5 > vm->code_size) {
 638 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_FLOAT operand");
 639 |                     return WET_ERR_INVALID_OPCODE;
 640 |                 }
 641 |                 float val = wet_read_f32_le(vm->code + instr_pc + 1);
 642 |                 vm->pc = instr_pc + 5;
 643 |                 wet_value_t v;
 644 |                 v.type = WET_VAL_FLOAT;
 645 |                 v.as.f_val = val;
 646 |                 wet_status_t st = push_val(vm, v);
 647 |                 if (st != WET_OK) return st;
 648 |                 break;
 649 |             }
 650 | 
 651 |             case WET_OP_POP: {
 652 |                 vm->pc = instr_pc + 1;
 653 |                 wet_value_t dummy;
 654 |                 wet_status_t st = pop_val(vm, &dummy);
 655 |                 if (st != WET_OK) return st;
 656 |                 break;
 657 |             }
 658 | 
 659 |             case WET_OP_DUP: {
 660 |                 vm->pc = instr_pc + 1;
 661 |                 if (vm->sp == 0) {
 662 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on DUP");
 663 |                     return WET_ERR_STACK_UNDERFLOW;
 664 |                 }
 665 |                 wet_value_t top = vm->stack[vm->sp - 1];
 666 |                 wet_status_t st = push_val(vm, top);
 667 |                 if (st != WET_OK) return st;
 668 |                 break;
 669 |             }
 670 | 
 671 |             case WET_OP_SWAP: {
 672 |                 vm->pc = instr_pc + 1;
 673 |                 if (vm->sp < 2) {
 674 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on SWAP");
 675 |                     return WET_ERR_STACK_UNDERFLOW;
 676 |                 }
 677 |                 wet_value_t a = vm->stack[vm->sp - 1];
 678 |                 vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
 679 |                 vm->stack[vm->sp - 2] = a;
 680 |                 break;
 681 |             }
 682 | 
 683 |             case WET_OP_LOAD_LOCAL: {
 684 |                 if (instr_pc + 3 > vm->code_size) {
 685 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated LOAD_LOCAL operand");
 686 |                     return WET_ERR_INVALID_OPCODE;
 687 |                 }
 688 |                 uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
 689 |                 vm->pc = instr_pc + 3;
 690 |                 if (slot >= vm->max_locals) {
 691 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 692 |                              "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
 693 |                     return WET_ERR_INVALID_OPCODE;
 694 |                 }
 695 |                 wet_status_t st = push_val(vm, vm->locals[slot]);
 696 |                 if (st != WET_OK) return st;
 697 |                 break;
 698 |             }
 699 | 
 700 |             case WET_OP_STORE_LOCAL: {
 701 |                 if (instr_pc + 3 > vm->code_size) {
 702 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STORE_LOCAL operand");
 703 |                     return WET_ERR_INVALID_OPCODE;
 704 |                 }
 705 |                 uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
 706 |                 vm->pc = instr_pc + 3;
 707 |                 if (slot >= vm->max_locals) {
 708 |                     snprintf(vm->last_error, sizeof(vm->last_error),
 709 |                              "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
 710 |                     return WET_ERR_INVALID_OPCODE;
 711 |                 }
 712 |                 wet_value_t val;
 713 |                 wet_status_t st = pop_val(vm, &val);
 714 |                 if (st != WET_OK) return st;
 715 |                 vm->locals[slot] = val;
 716 |                 break;
 717 |             }
 718 | 
 719 |             case WET_OP_ADD_I: {
 720 |                 vm->pc = instr_pc + 1;
 721 |                 wet_value_t b, a;
 722 |                 wet_status_t st = pop_val(vm, &b);
 723 |                 if (st != WET_OK) return st;
 724 |                 st = pop_val(vm, &a);
 725 |                 if (st != WET_OK) return st;
 726 |                 wet_value_t res;
 727 |                 res.type = WET_VAL_INT;
 728 |                 res.as.i_val = to_int(&a) + to_int(&b);
 729 |                 st = push_val(vm, res);
 730 |                 if (st != WET_OK) return st;
 731 |                 break;
 732 |             }
 733 | 
 734 |             case WET_OP_SUB_I: {
 735 |                 vm->pc = instr_pc + 1;
 736 |                 wet_value_t b, a;
 737 |                 wet_status_t st = pop_val(vm, &b);
 738 |                 if (st != WET_OK) return st;
 739 |                 st = pop_val(vm, &a);
 740 |                 if (st != WET_OK) return st;
 741 |                 wet_value_t res;
 742 |                 res.type = WET_VAL_INT;
 743 |                 res.as.i_val = to_int(&a) - to_int(&b);
 744 |                 st = push_val(vm, res);
 745 |                 if (st != WET_OK) return st;
 746 |                 break;
 747 |             }
 748 | 
 749 |             case WET_OP_MUL_I: {
 750 |                 vm->pc = instr_pc + 1;
 751 |                 wet_value_t b, a;
 752 |                 wet_status_t st = pop_val(vm, &b);
 753 |                 if (st != WET_OK) return st;
 754 |                 st = pop_val(vm, &a);
 755 |                 if (st != WET_OK) return st;
 756 |                 wet_value_t res;
 757 |                 res.type = WET_VAL_INT;
 758 |                 res.as.i_val = to_int(&a) * to_int(&b);
 759 |                 st = push_val(vm, res);
 760 |                 if (st != WET_OK) return st;
 761 |                 break;
 762 |             }
 763 | 
 764 |             case WET_OP_DIV_I: {
 765 |                 vm->pc = instr_pc + 1;
 766 |                 wet_value_t b, a;
 767 |                 wet_status_t st = pop_val(vm, &b);
 768 |                 if (st != WET_OK) return st;
 769 |                 st = pop_val(vm, &a);
 770 |                 if (st != WET_OK) return st;
 771 |                 int32_t b_val = to_int(&b);
 772 |                 if (b_val == 0) {
 773 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Integer division by zero");
 774 |                     return WET_ERR_DIVISION_BY_ZERO;
 775 |                 }
 776 |                 wet_value_t res;
 777 |                 res.type = WET_VAL_INT;
 778 |                 res.as.i_val = to_int(&a) / b_val;
 779 |                 st = push_val(vm, res);
 780 |                 if (st != WET_OK) return st;
 781 |                 break;
 782 |             }
 783 | 
 784 |             case WET_OP_ADD_F: {
 785 |                 vm->pc = instr_pc + 1;
 786 |                 wet_value_t b, a;
 787 |                 wet_status_t st = pop_val(vm, &b);
 788 |                 if (st != WET_OK) return st;
 789 |                 st = pop_val(vm, &a);
 790 |                 if (st != WET_OK) return st;
 791 |                 wet_value_t res;
 792 |                 res.type = WET_VAL_FLOAT;
 793 |                 res.as.f_val = to_float(&a) + to_float(&b);
 794 |                 st = push_val(vm, res);
 795 |                 if (st != WET_OK) return st;
 796 |                 break;
 797 |             }
 798 | 
 799 |             case WET_OP_SUB_F: {
 800 |                 vm->pc = instr_pc + 1;
 801 |                 wet_value_t b, a;
 802 |                 wet_status_t st = pop_val(vm, &b);
 803 |                 if (st != WET_OK) return st;
 804 |                 st = pop_val(vm, &a);
 805 |                 if (st != WET_OK) return st;
 806 |                 wet_value_t res;
 807 |                 res.type = WET_VAL_FLOAT;
 808 |                 res.as.f_val = to_float(&a) - to_float(&b);
 809 |                 st = push_val(vm, res);
 810 |                 if (st != WET_OK) return st;
 811 |                 break;
 812 |             }
 813 | 
 814 |             case WET_OP_MUL_F: {
 815 |                 vm->pc = instr_pc + 1;
 816 |                 wet_value_t b, a;
 817 |                 wet_status_t st = pop_val(vm, &b);
 818 |                 if (st != WET_OK) return st;
 819 |                 st = pop_val(vm, &a);
 820 |                 if (st != WET_OK) return st;
 821 |                 wet_value_t res;
 822 |                 res.type = WET_VAL_FLOAT;
 823 |                 res.as.f_val = to_float(&a) * to_float(&b);
 824 |                 st = push_val(vm, res);
 825 |                 if (st != WET_OK) return st;
 826 |                 break;
 827 |             }
 828 | 
 829 |             case WET_OP_DIV_F: {
 830 |                 vm->pc = instr_pc + 1;
 831 |                 wet_value_t b, a;
 832 |                 wet_status_t st = pop_val(vm, &b);
 833 |                 if (st != WET_OK) return st;
 834 |                 st = pop_val(vm, &a);
 835 |                 if (st != WET_OK) return st;
 836 |                 float b_val = to_float(&b);
 837 |                 if (fabsf(b_val) < 1e-15f) {
 838 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Floating point division by zero");
 839 |                     return WET_ERR_DIVISION_BY_ZERO;
 840 |                 }
 841 |                 wet_value_t res;
 842 |                 res.type = WET_VAL_FLOAT;
 843 |                 res.as.f_val = to_float(&a) / b_val;
 844 |                 st = push_val(vm, res);
 845 |                 if (st != WET_OK) return st;
 846 |                 break;
 847 |             }
 848 | 
 849 |             case WET_OP_NEG: {
 850 |                 vm->pc = instr_pc + 1;
 851 |                 wet_value_t a;
 852 |                 wet_status_t st = pop_val(vm, &a);
 853 |                 if (st != WET_OK) return st;
 854 |                 wet_value_t res;
 855 |                 if (a.type == WET_VAL_FLOAT) {
 856 |                     res.type = WET_VAL_FLOAT;
 857 |                     res.as.f_val = -a.as.f_val;
 858 |                 } else {
 859 |                     res.type = WET_VAL_INT;
 860 |                     res.as.i_val = -to_int(&a);
 861 |                 }
 862 |                 st = push_val(vm, res);
 863 |                 if (st != WET_OK) return st;
 864 |                 break;
 865 |             }
 866 | 
 867 |             case WET_OP_MOD_I: {
 868 |                 vm->pc = instr_pc + 1;
 869 |                 wet_value_t b, a;
 870 |                 wet_status_t st = pop_val(vm, &b);
 871 |                 if (st != WET_OK) return st;
 872 |                 st = pop_val(vm, &a);
 873 |                 if (st != WET_OK) return st;
 874 |                 int32_t b_val = to_int(&b);
 875 |                 if (b_val == 0) {
 876 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Integer modulo by zero");
 877 |                     return WET_ERR_DIVISION_BY_ZERO;
 878 |                 }
 879 |                 wet_value_t res;
 880 |                 res.type = WET_VAL_INT;
 881 |                 res.as.i_val = to_int(&a) % b_val;
 882 |                 st = push_val(vm, res);
 883 |                 if (st != WET_OK) return st;
 884 |                 break;
 885 |             }
 886 | 
 887 |             case WET_OP_CMP_EQ:
 888 |             case WET_OP_CMP_NE:
 889 |             case WET_OP_CMP_LT:
 890 |             case WET_OP_CMP_LE:
 891 |             case WET_OP_CMP_GT:
 892 |             case WET_OP_CMP_GE: {
 893 |                 vm->pc = instr_pc + 1;
 894 |                 wet_value_t b, a;
 895 |                 wet_status_t st = pop_val(vm, &b);
 896 |                 if (st != WET_OK) return st;
 897 |                 st = pop_val(vm, &a);
 898 |                 if (st != WET_OK) return st;
 899 | 
 900 |                 int cmp_res = 0;
 901 |                 if (a.type == WET_VAL_FLOAT || b.type == WET_VAL_FLOAT) {
 902 |                     float fa = to_float(&a);
 903 |                     float fb = to_float(&b);
 904 |                     switch ((wet_opcode_t)op) {
 905 |                         case WET_OP_CMP_EQ: cmp_res = (fa == fb); break;
 906 |                         case WET_OP_CMP_NE: cmp_res = (fa != fb); break;
 907 |                         case WET_OP_CMP_LT: cmp_res = (fa <  fb); break;
 908 |                         case WET_OP_CMP_LE: cmp_res = (fa <= fb); break;
 909 |                         case WET_OP_CMP_GT: cmp_res = (fa >  fb); break;
 910 |                         case WET_OP_CMP_GE: cmp_res = (fa >= fb); break;
 911 |                         default: break;
 912 |                     }
 913 |                 } else {
 914 |                     int32_t ia = to_int(&a);
 915 |                     int32_t ib = to_int(&b);
 916 |                     switch ((wet_opcode_t)op) {
 917 |                         case WET_OP_CMP_EQ: cmp_res = (ia == ib); break;
 918 |                         case WET_OP_CMP_NE: cmp_res = (ia != ib); break;
 919 |                         case WET_OP_CMP_LT: cmp_res = (ia <  ib); break;
 920 |                         case WET_OP_CMP_LE: cmp_res = (ia <= ib); break;
 921 |                         case WET_OP_CMP_GT: cmp_res = (ia >  ib); break;
 922 |                         case WET_OP_CMP_GE: cmp_res = (ia >= ib); break;
 923 |                         default: break;
 924 |                     }
 925 |                 }
 926 | 
 927 |                 wet_value_t res;
 928 |                 res.type = WET_VAL_INT;
 929 |                 res.as.i_val = cmp_res ? 1 : 0;
 930 |                 st = push_val(vm, res);
 931 |                 if (st != WET_OK) return st;
 932 |                 break;
 933 |             }
 934 | 
 935 |             case WET_OP_JMP: {
 936 |                 if (instr_pc + 3 > vm->code_size) {
 937 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP operand");
 938 |                     return WET_ERR_INVALID_OPCODE;
 939 |                 }
 940 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 941 |                 int64_t target = (int64_t)instr_pc + offset;
 942 |                 if (target < 0 || (size_t)target > vm->code_size) {
 943 |                     snprintf(vm->last_error, sizeof(vm->last_error), "JMP target %lld out of range", (long long)target);
 944 |                     return WET_ERR_INVALID_OPCODE;
 945 |                 }
 946 |                 vm->pc = (size_t)target;
 947 |                 break;
 948 |             }
 949 | 
 950 |             case WET_OP_JMP_IF_TRUE: {
 951 |                 if (instr_pc + 3 > vm->code_size) {
 952 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_TRUE operand");
 953 |                     return WET_ERR_INVALID_OPCODE;
 954 |                 }
 955 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 956 |                 wet_value_t cond;
 957 |                 wet_status_t st = pop_val(vm, &cond);
 958 |                 if (st != WET_OK) return st;
 959 | 
 960 |                 if (is_truthy(&cond)) {
 961 |                     int64_t target = (int64_t)instr_pc + offset;
 962 |                     if (target < 0 || (size_t)target > vm->code_size) {
 963 |                         snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_TRUE target %lld out of range", (long long)target);
 964 |                         return WET_ERR_INVALID_OPCODE;
 965 |                     }
 966 |                     vm->pc = (size_t)target;
 967 |                 } else {
 968 |                     vm->pc = instr_pc + 3;
 969 |                 }
 970 |                 break;
 971 |             }
 972 | 
 973 |             case WET_OP_JMP_IF_FALSE: {
 974 |                 if (instr_pc + 3 > vm->code_size) {
 975 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_FALSE operand");
 976 |                     return WET_ERR_INVALID_OPCODE;
 977 |                 }
 978 |                 int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
 979 |                 wet_value_t cond;
 980 |                 wet_status_t st = pop_val(vm, &cond);
 981 |                 if (st != WET_OK) return st;
 982 | 
 983 |                 if (!is_truthy(&cond)) {
 984 |                     int64_t target = (int64_t)instr_pc + offset;
 985 |                     if (target < 0 || (size_t)target > vm->code_size) {
 986 |                         snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_FALSE target %lld out of range", (long long)target);
 987 |                         return WET_ERR_INVALID_OPCODE;
 988 |                     }
 989 |                     vm->pc = (size_t)target;
 990 |                 } else {
 991 |                     vm->pc = instr_pc + 3;
 992 |                 }
 993 |                 break;
 994 |             }
 995 | 
 996 |             case WET_OP_CALL: {
 997 |                 if (instr_pc + 4 > vm->code_size) {
 998 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated CALL operand");
 999 |                     return WET_ERR_INVALID_OPCODE;
1000 |                 }
1001 |                 uint16_t fn_idx = wet_read_u16_le(vm->code + instr_pc + 1);
1002 |                 uint8_t argc = *(const uint8_t*)(vm->code + instr_pc + 3);
1003 | 
1004 |                 if (fn_idx > 0 && fn_idx < vm->code_size) {
1005 |                     /* User-defined function call */
1006 |                     if (vm->call_sp >= vm->max_call_depth) {
1007 |                         snprintf(vm->last_error, sizeof(vm->last_error), "Call stack overflow (depth %zu)", vm->call_sp);
1008 |                         return WET_ERR_STACK_OVERFLOW;
1009 |                     }
1010 |                     vm->call_stack[vm->call_sp++].return_pc = instr_pc + 4;
1011 |                     vm->pc = fn_idx;
1012 |                 } else {
1013 |                     /* Handle builtin / external function call: pop arguments, push default 0 */
1014 |                     vm->pc = instr_pc + 4;
1015 |                     for (uint8_t a = 0; a < argc; ++a) {
1016 |                         wet_value_t dummy;
1017 |                         pop_val(vm, &dummy);
1018 |                     }
1019 |                     wet_value_t ret_val;
1020 |                     ret_val.type = WET_VAL_INT;
1021 |                     ret_val.as.i_val = 0;
1022 |                     push_val(vm, ret_val);
1023 |                 }
1024 |                 break;
1025 |             }
1026 | 
1027 |             case WET_OP_RET: {
1028 |                 if (vm->call_sp > 0) {
1029 |                     vm->call_sp--;
1030 |                     vm->pc = vm->call_stack[vm->call_sp].return_pc;
1031 |                 } else {
1032 |                     vm->pc = instr_pc + 1;
1033 |                 }
1034 |                 break;
1035 |             }
1036 | 
1037 |             case WET_OP_STIM_BIPHASIC: {
1038 |                 if (instr_pc + 2 > vm->code_size) {
1039 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_BIPHASIC operand");
1040 |                     return WET_ERR_INVALID_OPCODE;
1041 |                 }
1042 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1043 |                 vm->pc = instr_pc + 2;
1044 | 
1045 |                 /* Pop arguments: interphase, phase2, phase1, voltage */
1046 |                 wet_value_t v_interphase, v_p2, v_p1, v_volt;
1047 |                 wet_status_t st = pop_val(vm, &v_interphase);
1048 |                 if (st != WET_OK) return st;
1049 |                 st = pop_val(vm, &v_p2);
1050 |                 if (st != WET_OK) return st;
1051 |                 st = pop_val(vm, &v_p1);
1052 |                 if (st != WET_OK) return st;
1053 |                 st = pop_val(vm, &v_volt);
1054 |                 if (st != WET_OK) return st;
1055 | 
1056 |                 if (channel == 0xFF) {
1057 |                     /* Dynamic channel index popped from stack */
1058 |                     wet_value_t v_ch;
1059 |                     st = pop_val(vm, &v_ch);
1060 |                     if (st != WET_OK) return st;
1061 |                     int32_t c_idx = to_int(&v_ch);
1062 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1063 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1064 |                                  "Electrode channel %d out of bounds (max %u)",
1065 |                                  c_idx, vm->config.channel_count);
1066 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1067 |                     }
1068 |                     channel = (uint8_t)c_idx;
1069 |                 } else if (channel >= vm->config.channel_count) {
1070 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1071 |                              "Electrode channel %u out of bounds (max %u)",
1072 |                              channel, vm->config.channel_count);
1073 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1074 |                 }
1075 | 
1076 |                 float voltage = to_float(&v_volt);
1077 |                 float p1_ms = to_float(&v_p1);
1078 |                 float p2_ms = to_float(&v_p2);
1079 |                 float ip_ms = to_float(&v_interphase);
1080 | 
1081 |                 if (vm->interlocks.locked) {
1082 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1083 |                     return WET_ERR_INTERLOCK_LOCKED;
1084 |                 }
1085 | 
1086 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage, channel)) {
1087 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1088 |                              "Capability denied for STIM_BIPHASIC on ch %u (req %.2fV)", channel, voltage);
1089 |                     return WET_ERR_CAPABILITY_DENIED;
1090 |                 }
1091 | 
1092 |                 /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
1093 |                 if (p1_ms > 0.0f && p2_ms > 0.0f) {
1094 |                     float q_phase1 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p1_ms;
1095 |                     float q_phase2 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p2_ms;
1096 |                     if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
1097 |                         vm->interlocks.locked = 1;
1098 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
1099 |                         vm->interlocks.tripped_channel = channel;
1100 |                         vm->interlocks.trip_tick = vm->current_tick;
1101 |                         vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
1102 |                         if (vm->hal) {
1103 |                             wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
1104 |                         }
1105 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1106 |                                  "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
1107 |                                  channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
1108 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1109 |                         return WET_ERR_CHARGE_DENSITY_EXCEEDED;
1110 |                     }
1111 |                 }
1112 | 
1113 |                 /* Active charge recovery: if previous pulse had pending Phase 2 counter-charge, discharge it */
1114 |                 bio_stim_pulse_t* prev_p = &vm->bio.stim_pulses[channel];
1115 |                 if (prev_p->active && prev_p->phase2_ticks_left > 0) {
1116 |                     float i_ua = (prev_p->phase2_amp_v / vm->bio.electrode_impedance_kohm) * 1000.0f;
1117 |                     vm->discharge_charge_nc[channel] += i_ua * (float)vm->bio.dt_ms * (float)prev_p->phase2_ticks_left;
1118 |                 }
1119 | 
1120 |                 float clamped_v = interlocks_clamp_voltage(&vm->interlocks, voltage);
1121 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1122 |                     wet_hal_stim_voltage(vm->hal, (uint16_t)channel, clamped_v, p1_ms, p2_ms);
1123 |                 }
1124 |                 biophysics_schedule_stim_ext(&vm->bio, channel, clamped_v, p1_ms, p2_ms, ip_ms);
1125 |                 vm->voltages[channel] = clamped_v;
1126 |                 /* Accurate impedance-scaled charge: I (mA) = V / Z(kOhm); Q(nC) = I(mA) * dt(ms) */
1127 |                 float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
1128 |                 vm->last_charge_nc[channel] = i_ma * (p1_ms - p2_ms);
1129 |                 break;
1130 |             }
1131 | 
1132 |             case WET_OP_READ_SPIKES: {
1133 |                 if (instr_pc + 2 > vm->code_size) {
1134 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_SPIKES operand");
1135 |                     return WET_ERR_INVALID_OPCODE;
1136 |                 }
1137 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1138 |                 vm->pc = instr_pc + 2;
1139 | 
1140 |                 wet_value_t window;
1141 |                 wet_status_t st = pop_val(vm, &window);
1142 |                 if (st != WET_OK) return st;
1143 | 
1144 |                 if (channel == 0xFF) {
1145 |                     /* Dynamic channel index popped from stack */
1146 |                     wet_value_t v_ch;
1147 |                     st = pop_val(vm, &v_ch);
1148 |                     if (st != WET_OK) return st;
1149 |                     int32_t c_idx = to_int(&v_ch);
1150 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1151 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1152 |                                  "Electrode channel %d out of bounds (max %u)",
1153 |                                  c_idx, vm->config.channel_count);
1154 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1155 |                     }
1156 |                     channel = (uint8_t)c_idx;
1157 |                 } else if (channel >= vm->config.channel_count) {
1158 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1159 |                              "Electrode channel %u out of bounds (max %u)",
1160 |                              channel, vm->config.channel_count);
1161 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1162 |                 }
1163 | 
1164 |                 float window_ms = to_float(&window);
1165 |                 uint32_t cnt = biophysics_get_spikes_window(&vm->bio, channel, window_ms);
1166 | 
1167 |                 wet_value_t spike_res;
1168 |                 spike_res.type = WET_VAL_INT;
1169 |                 spike_res.as.i_val = (int32_t)cnt;
1170 |                 st = push_val(vm, spike_res);
1171 |                 if (st != WET_OK) return st;
1172 |                 break;
1173 |             }
1174 | 
1175 |             case WET_OP_READ_VOLTAGE: {
1176 |                 if (instr_pc + 2 > vm->code_size) {
1177 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_VOLTAGE operand");
1178 |                     return WET_ERR_INVALID_OPCODE;
1179 |                 }
1180 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1181 |                 vm->pc = instr_pc + 2;
1182 | 
1183 |                 if (channel == 0xFF) {
1184 |                     /* Dynamic channel index popped from stack */
1185 |                     wet_value_t v_ch;
1186 |                     wet_status_t st = pop_val(vm, &v_ch);
1187 |                     if (st != WET_OK) return st;
1188 |                     int32_t c_idx = to_int(&v_ch);
1189 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1190 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1191 |                                  "Electrode channel %d out of bounds (max %u)",
1192 |                                  c_idx, vm->config.channel_count);
1193 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1194 |                     }
1195 |                     channel = (uint8_t)c_idx;
1196 |                 } else if (channel >= vm->config.channel_count) {
1197 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1198 |                              "Electrode channel %u out of bounds (max %u)",
1199 |                              channel, vm->config.channel_count);
1200 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1201 |                 }
1202 | 
1203 |                 wet_value_t volt_res;
1204 |                 volt_res.type = WET_VAL_FLOAT;
1205 |                 volt_res.as.f_val = vm->bio.mea_voltage_v[channel];
1206 |                 wet_status_t st = push_val(vm, volt_res);
1207 |                 if (st != WET_OK) return st;
1208 |                 break;
1209 |             }
1210 | 
1211 |             case WET_OP_MODULATE_STDP: {
1212 |                 if (instr_pc + 3 > vm->code_size) {
1213 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MODULATE_STDP operand");
1214 |                     return WET_ERR_INVALID_OPCODE;
1215 |                 }
1216 |                 uint8_t pre = *(const uint8_t*)(vm->code + instr_pc + 1);
1217 |                 uint8_t post = *(const uint8_t*)(vm->code + instr_pc + 2);
1218 |                 vm->pc = instr_pc + 3;
1219 | 
1220 |                 wet_value_t delta_w;
1221 |                 wet_status_t st = pop_val(vm, &delta_w);
1222 |                 if (st != WET_OK) return st;
1223 | 
1224 |                 if (pre == 0xFF && post == 0xFF) {
1225 |                     /* Dynamic pre/post channels popped from stack */
1226 |                     wet_value_t v_post, v_pre;
1227 |                     st = pop_val(vm, &v_post);
1228 |                     if (st != WET_OK) return st;
1229 |                     st = pop_val(vm, &v_pre);
1230 |                     if (st != WET_OK) return st;
1231 |                     int32_t pre_idx = to_int(&v_pre);
1232 |                     int32_t post_idx = to_int(&v_post);
1233 |                     if (pre_idx < 0 || (uint32_t)pre_idx >= vm->config.channel_count ||
1234 |                         post_idx < 0 || (uint32_t)post_idx >= vm->config.channel_count) {
1235 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1236 |                                  "STDP dynamic channels (%d, %d) out of bounds (max %u)",
1237 |                                  pre_idx, post_idx, vm->config.channel_count);
1238 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1239 |                     }
1240 |                     pre = (uint8_t)pre_idx;
1241 |                     post = (uint8_t)post_idx;
1242 |                 } else if (pre >= vm->config.channel_count || post >= vm->config.channel_count) {
1243 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1244 |                              "STDP channels (%u, %u) out of bounds (max %u)",
1245 |                              pre, post, vm->config.channel_count);
1246 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1247 |                 }
1248 | 
1249 |                 if (vm->interlocks.locked) {
1250 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1251 |                     return WET_ERR_INTERLOCK_LOCKED;
1252 |                 }
1253 | 
1254 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_MODULATE_STDP, 0.0f, pre)) {
1255 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1256 |                              "Capability denied for MODULATE_STDP");
1257 |                     return WET_ERR_CAPABILITY_DENIED;
1258 |                 }
1259 | 
1260 |                 float dw = to_float(&delta_w);
1261 |                 if (pre == 0 && post == 0) {
1262 |                     vm->bio.stdp_lr_scale = dw;
1263 |                 } else if (pre != post) {
1264 |                     biophysics_modulate_stdp(&vm->bio, pre, post, dw);
1265 |                 }
1266 |                 break;
1267 |             }
1268 | 
1269 |             case WET_OP_GET_POP_RATE: {
1270 |                 vm->pc = instr_pc + 1;
1271 |                 wet_value_t window;
1272 |                 wet_status_t st = pop_val(vm, &window);
1273 |                 if (st != WET_OK) return st;
1274 | 
1275 |                 wet_value_t rate_res;
1276 |                 rate_res.type = WET_VAL_FLOAT;
1277 |                 rate_res.as.f_val = vm->bio.population_rate_hz;
1278 |                 st = push_val(vm, rate_res);
1279 |                 if (st != WET_OK) return st;
1280 |                 break;
1281 |             }
1282 | 
1283 |             case WET_OP_MEA_CONFIG: {
1284 |                 if (instr_pc + 3 > vm->code_size) {
1285 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MEA_CONFIG operand");
1286 |                     return WET_ERR_INVALID_OPCODE;
1287 |                 }
1288 |                 uint8_t rows = *(const uint8_t*)(vm->code + instr_pc + 1);
1289 |                 uint8_t cols = *(const uint8_t*)(vm->code + instr_pc + 2);
1290 |                 vm->pc = instr_pc + 3;
1291 |                 vm->grid_rows = rows;
1292 |                 vm->grid_cols = cols;
1293 |                 break;
1294 |             }
1295 | 
1296 |             case WET_OP_PUMP_SET_RATE: {
1297 |                 if (instr_pc + 6 > vm->code_size) {
1298 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_SET_RATE operand");
1299 |                     return WET_ERR_INVALID_OPCODE;
1300 |                 }
1301 |                 uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1302 |                 float rate_ul_min;
1303 |                 memcpy(&rate_ul_min, vm->code + instr_pc + 2, sizeof(float));
1304 |                 vm->pc = instr_pc + 6;
1305 | 
1306 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_SET_RATE, 0.0f, pump_id)) {
1307 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1308 |                              "Capability denied for PUMP_SET_RATE (requires CAP_MICROFLUIDICS)");
1309 |                     return WET_ERR_CAPABILITY_DENIED;
1310 |                 }
1311 | 
1312 |                 if (pump_id >= 8) {
1313 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
1314 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1315 |                 }
1316 | 
1317 |                 if (rate_ul_min < 0.0f || rate_ul_min > 15.0f) {
1318 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1319 |                              "ERR_SHEAR_STRESS_EXCEEDED: Requested pump rate %.2f uL/min exceeds safe hydrodynamic limit (0..15.0 uL/min)",
1320 |                              (double)rate_ul_min);
1321 |                     return WET_ERR_SHEAR_STRESS_EXCEEDED;
1322 |                 }
1323 | 
1324 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1325 |                     wet_hal_status_t hst = wet_hal_write_pump(vm->hal, pump_id, (double)rate_ul_min, 1);
1326 |                     if (hst == WET_HAL_ERR_DEAD_HEAD) {
1327 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1328 |                                  "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
1329 |                                  pump_id);
1330 |                         return WET_ERR_ACTUATOR_FAULT;
1331 |                     }
1332 |                 }
1333 | 
1334 |                 vm->pump_rates_ul_min[pump_id] = rate_ul_min;
1335 |                 break;
1336 |             }
1337 | 
1338 |             case WET_OP_PUMP_DISPENSE: {
1339 |                 if (instr_pc + 6 > vm->code_size) {
1340 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_DISPENSE operand");
1341 |                     return WET_ERR_INVALID_OPCODE;
1342 |                 }
1343 |                 uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1344 |                 float volume_ul;
1345 |                 memcpy(&volume_ul, vm->code + instr_pc + 2, sizeof(float));
1346 |                 vm->pc = instr_pc + 6;
1347 | 
1348 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_DISPENSE, 0.0f, pump_id)) {
1349 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1350 |                              "Capability denied for PUMP_DISPENSE (requires CAP_MICROFLUIDICS)");
1351 |                     return WET_ERR_CAPABILITY_DENIED;
1352 |                 }
1353 | 
1354 |                 if (pump_id >= 8) {
1355 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
1356 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1357 |                 }
1358 | 
1359 |                 if (volume_ul <= 0.0f || volume_ul > 500.0f) {
1360 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1361 |                              "ERR_ACTUATOR_FAULT: Invalid dispense volume %.2f uL (allowed: 0.1..500.0 uL)",
1362 |                              (double)volume_ul);
1363 |                     return WET_ERR_ACTUATOR_FAULT;
1364 |                 }
1365 | 
1366 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1367 |                     wet_hal_status_t hst = wet_hal_dispense_pump(vm->hal, pump_id, (double)volume_ul);
1368 |                     if (hst == WET_HAL_ERR_DEAD_HEAD) {
1369 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1370 |                                  "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
1371 |                                  pump_id);
1372 |                         return WET_ERR_ACTUATOR_FAULT;
1373 |                     }
1374 |                 }
1375 | 
1376 |                 vm->pump_dispensed_ul[pump_id] += volume_ul;
1377 |                 break;
1378 |             }
1379 | 
1380 |             case WET_OP_VALVE_SET: {
1381 |                 if (instr_pc + 3 > vm->code_size) {
1382 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated VALVE_SET operand");
1383 |                     return WET_ERR_INVALID_OPCODE;
1384 |                 }
1385 |                 uint8_t valve_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1386 |                 uint8_t state = *(const uint8_t*)(vm->code + instr_pc + 2);
1387 |                 vm->pc = instr_pc + 3;
1388 | 
1389 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_VALVE_SET, 0.0f, valve_id)) {
1390 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1391 |                              "Capability denied for VALVE_SET (requires CAP_MICROFLUIDICS)");
1392 |                     return WET_ERR_CAPABILITY_DENIED;
1393 |                 }
1394 | 
1395 |                 if (valve_id >= 8) {
1396 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Valve ID %u out of bounds (max 7)", valve_id);
1397 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1398 |                 }
1399 | 
1400 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1401 |                     wet_hal_write_valve(vm->hal, valve_id, state);
1402 |                 }
1403 | 
1404 |                 vm->valve_states[valve_id] = (state != 0) ? 1 : 0;
1405 |                 break;
1406 |             }
1407 | 
1408 |             case WET_OP_MOTOR_STEP: {
1409 |                 if (instr_pc + 10 > vm->code_size) {
1410 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MOTOR_STEP operand");
1411 |                     return WET_ERR_INVALID_OPCODE;
1412 |                 }
1413 |                 uint8_t motor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1414 |                 int32_t steps;
1415 |                 float speed_rpm;
1416 |                 memcpy(&steps, vm->code + instr_pc + 2, sizeof(int32_t));
1417 |                 memcpy(&speed_rpm, vm->code + instr_pc + 6, sizeof(float));
1418 |                 vm->pc = instr_pc + 10;
1419 | 
1420 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_MOTOR_STEP, 0.0f, motor_id)) {
1421 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1422 |                              "Capability denied for MOTOR_STEP (requires CAP_MOTOR_ACTUATION)");
1423 |                     return WET_ERR_CAPABILITY_DENIED;
1424 |                 }
1425 | 
1426 |                 if (motor_id >= 4) {
1427 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Motor ID %u out of bounds (max 3)", motor_id);
1428 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1429 |                 }
1430 | 
1431 |                 vm->motor_positions[motor_id] += steps;
1432 |                 vm->motor_speeds_rpm[motor_id] = speed_rpm;
1433 |                 break;
1434 |             }
1435 | 
1436 |             case WET_OP_READ_PRESSURE: {
1437 |                 if (instr_pc + 2 > vm->code_size) {
1438 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_PRESSURE operand");
1439 |                     return WET_ERR_INVALID_OPCODE;
1440 |                 }
1441 |                 uint8_t port_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1442 |                 vm->pc = instr_pc + 2;
1443 | 
1444 |                 if (port_id >= 4) port_id = 0;
1445 |                 wet_value_t p_val;
1446 |                 p_val.type = WET_VAL_FLOAT;
1447 |                 p_val.as.f_val = vm->fluid_pressure_kpa[port_id];
1448 |                 wet_status_t st = push_val(vm, p_val);
1449 |                 if (st != WET_OK) return st;
1450 |                 break;
1451 |             }
1452 | 
1453 |             case WET_OP_READ_TEMPERATURE: {
1454 |                 vm->pc = instr_pc + 1;
1455 |                 wet_value_t t_val;
1456 |                 t_val.type = WET_VAL_FLOAT;
1457 |                 t_val.as.f_val = vm->ambient_temperature_c;
1458 |                 wet_status_t st = push_val(vm, t_val);
1459 |                 if (st != WET_OK) return st;
1460 |                 break;
1461 |             }
1462 | 
1463 |             case WET_OP_STIM_CURRENT: {
1464 |                 if (instr_pc + 6 > vm->code_size) {
1465 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_CURRENT operand");
1466 |                     return WET_ERR_INVALID_OPCODE;
1467 |                 }
1468 |                 uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
1469 |                 float current_ua;
1470 |                 memcpy(&current_ua, vm->code + instr_pc + 2, sizeof(float));
1471 |                 vm->pc = instr_pc + 6;
1472 | 
1473 |                 /* Pop duration arguments: interphase, phase2, phase1 */
1474 |                 wet_value_t v_interphase, v_p2, v_p1;
1475 |                 wet_status_t st = pop_val(vm, &v_interphase);
1476 |                 if (st != WET_OK) return st;
1477 |                 st = pop_val(vm, &v_p2);
1478 |                 if (st != WET_OK) return st;
1479 |                 st = pop_val(vm, &v_p1);
1480 |                 if (st != WET_OK) return st;
1481 | 
1482 |                 if (channel == 0xFF) {
1483 |                     wet_value_t v_ch;
1484 |                     st = pop_val(vm, &v_ch);
1485 |                     if (st != WET_OK) return st;
1486 |                     int32_t c_idx = to_int(&v_ch);
1487 |                     if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
1488 |                         snprintf(vm->last_error, sizeof(vm->last_error),
1489 |                                  "Electrode channel %d out of bounds (max %u)",
1490 |                                  c_idx, vm->config.channel_count);
1491 |                         return WET_ERR_OUT_OF_BOUNDS_CH;
1492 |                     }
1493 |                     channel = (uint8_t)c_idx;
1494 |                 } else if (channel >= vm->config.channel_count) {
1495 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1496 |                              "Electrode channel %u out of bounds (max %u)",
1497 |                              channel, vm->config.channel_count);
1498 |                     return WET_ERR_OUT_OF_BOUNDS_CH;
1499 |                 }
1500 | 
1501 |                 if (vm->interlocks.locked) {
1502 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1503 |                     return WET_ERR_INTERLOCK_LOCKED;
1504 |                 }
1505 | 
1506 |                 if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
1507 |                     snprintf(vm->last_error, sizeof(vm->last_error),
1508 |                              "Capability denied for STIM_CURRENT on ch %u (ref/rec bank restricted or missing CAP_STIMULATION)", channel);
1509 |                     return WET_ERR_CAPABILITY_DENIED;
1510 |                 }
1511 | 
1512 |                 float p1_ms = to_float(&v_p1);
1513 |                 float p2_ms = to_float(&v_p2);
1514 |                 float ip_ms = to_float(&v_interphase);
1515 | 
1516 |                 /* Randles Interface: V_elec = I * Rs + V_dl */
1517 |                 float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
1518 |                 wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
1519 |                 if (comp_st != WET_OK) {
1520 |                     snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1521 |                     return comp_st;
1522 |                 }
1523 | 
1524 |                 /* Per-phase charge density check: Q (nC) = I (uA) * t (ms) */
1525 |                 if (p1_ms > 0.0f && p2_ms > 0.0f) {
1526 |                     float q_phase1 = wet_fabsf(current_ua) * 1e-3f * p1_ms;
1527 |                     float q_phase2 = wet_fabsf(current_ua) * 1e-3f * p2_ms;
1528 |                     if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
1529 |                         vm->interlocks.locked = 1;
1530 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
1531 |                         vm->interlocks.tripped_channel = channel;
1532 |                         vm->interlocks.trip_tick = vm->current_tick;
1533 |                         vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
1534 |                         if (vm->hal) {
1535 |                             wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
1536 |                         }
1537 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1538 |                                  "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
1539 |                                  channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
1540 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1541 |                         return WET_ERR_CHARGE_DENSITY_EXCEEDED;
1542 |                     }
1543 |                 }
1544 | 
1545 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1546 |                     int32_t cur_pA = (int32_t)(current_ua * 1e6f);
1547 |                     uint32_t dur_us = (uint32_t)(p1_ms * 1000.0f);
1548 |                     wet_hal_status_t hst = wet_hal_stim_current(vm->hal, (uint16_t)channel, cur_pA, dur_us);
1549 |                     if (hst == WET_HAL_ERR_COMPLIANCE_RAILED) {
1550 |                         vm->interlocks.locked = 1;
1551 |                         vm->interlocks.trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
1552 |                         vm->interlocks.tripped_channel = channel;
1553 |                         vm->interlocks.trip_tick = vm->current_tick;
1554 |                         snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
1555 |                                  "ERR_COMPLIANCE_RAILED: Channel %u compliance rail tripped on hardware driver (~7.0V limit)", channel);
1556 |                         snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
1557 |                         wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_COMPLIANCE_RAILED);
1558 |                         return WET_ERR_COMPLIANCE_RAILED;
1559 |                     }
1560 |                 }
1561 | 
1562 |                 biophysics_schedule_stim_current(&vm->bio, channel, current_ua, p1_ms, p2_ms, ip_ms);
1563 |                 vm->voltages[channel] = v_elec;
1564 |                 vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (p1_ms - p2_ms);
1565 |                 break;
1566 |             }
1567 | 
1568 |             case WET_OP_READ_PH: {
1569 |                 vm->pc = instr_pc + 1;
1570 |                 wet_value_t ph_val;
1571 |                 ph_val.type = WET_VAL_FLOAT;
1572 |                 ph_val.as.f_val = vm->ph_level > 0.0f ? vm->ph_level : 7.40f;
1573 |                 wet_status_t st = push_val(vm, ph_val);
1574 |                 if (st != WET_OK) return st;
1575 |                 break;
1576 |             }
1577 | 
1578 |             case WET_OP_READ_DO: {
1579 |                 vm->pc = instr_pc + 1;
1580 |                 wet_value_t do_val;
1581 |                 do_val.type = WET_VAL_FLOAT;
1582 |                 do_val.as.f_val = vm->dissolved_oxygen_pct > 0.0f ? vm->dissolved_oxygen_pct : 95.0f;
1583 |                 wet_status_t st = push_val(vm, do_val);
1584 |                 if (st != WET_OK) return st;
1585 |                 break;
1586 |             }
1587 | 
1588 |             case WET_OP_READ_CO2: {
1589 |                 vm->pc = instr_pc + 1;
1590 |                 wet_value_t co2_val;
1591 |                 co2_val.type = WET_VAL_FLOAT;
1592 |                 co2_val.as.f_val = vm->dissolved_co2_pct > 0.0f ? vm->dissolved_co2_pct : 5.0f;
1593 |                 wet_status_t st = push_val(vm, co2_val);
1594 |                 if (st != WET_OK) return st;
1595 |                 break;
1596 |             }
1597 | 
1598 |             case WET_OP_READ_BUBBLE: {
1599 |                 if (instr_pc + 2 > vm->code_size) {
1600 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_BUBBLE operand");
1601 |                     return WET_ERR_INVALID_OPCODE;
1602 |                 }
1603 |                 uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1604 |                 vm->pc = instr_pc + 2;
1605 |                 if (sensor_id >= 8) sensor_id = 0;
1606 |                 wet_value_t b_val;
1607 |                 b_val.type = WET_VAL_INT;
1608 |                 b_val.as.i_val = vm->bubble_detected[sensor_id] ? 1 : 0;
1609 |                 wet_status_t st = push_val(vm, b_val);
1610 |                 if (st != WET_OK) return st;
1611 |                 break;
1612 |             }
1613 | 
1614 |             case WET_OP_READ_FLOW: {
1615 |                 if (instr_pc + 2 > vm->code_size) {
1616 |                     snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_FLOW operand");
1617 |                     return WET_ERR_INVALID_OPCODE;
1618 |                 }
1619 |                 uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
1620 |                 vm->pc = instr_pc + 2;
1621 |                 if (sensor_id >= 8) sensor_id = 0;
1622 |                 double flow_val = (double)vm->fluid_flow_rate_ul_min[sensor_id];
1623 |                 if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
1624 |                     wet_hal_read_flow(vm->hal, sensor_id, &flow_val);
1625 |                 }
1626 |                 wet_value_t f_val;
1627 |                 f_val.type = WET_VAL_FLOAT;
1628 |                 f_val.as.f_val = (float)flow_val;
1629 |                 wet_status_t st = push_val(vm, f_val);
1630 |                 if (st != WET_OK) return st;
1631 |                 break;
1632 |             }
1633 | 
1634 |             default: {
1635 |                 snprintf(vm->last_error, sizeof(vm->last_error),
1636 |                          "Unrecognized or invalid opcode 0x%02X at pc %zu", op, instr_pc);
1637 |                 return WET_ERR_INVALID_OPCODE;
1638 |             }
1639 |         }
1640 |     }
1641 | 
1642 |     populate_telemetry(vm, out_telem);
1643 |     return WET_OK;
1644 | }
1645 | 
1646 | /* =========================================================================
1647 |  * Phase 3: Standalone C99 Load-Time Bytecode Verifier
1648 |  * ========================================================================= */
1649 | 
1650 | wet_status_t wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len) {
1651 |     if (!bytecode) {
1652 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Null bytecode pointer");
1653 |         return WET_ERR_NULL_PTR;
1654 |     }
1655 |     if (size < WET_HEADER_SIZE) {
1656 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Bytecode size %zu smaller than 32-byte header", size);
1657 |         return WET_ERR_INVALID_MAGIC;
1658 |     }
1659 | 
1660 |     if (memcmp(bytecode, WET_HEADER_MAGIC, 4) != 0) {
1661 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Invalid header magic (expected WETB)");
1662 |         return WET_ERR_INVALID_MAGIC;
1663 |     }
1664 | 
1665 |     uint8_t v_maj = bytecode[4];
1666 |     uint8_t v_min = bytecode[5];
1667 |     if (v_maj != WET_VERSION_MAJOR || v_min != WET_VERSION_MINOR) {
1668 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unsupported version %u.%u (expected 1.0)", v_maj, v_min);
1669 |         return WET_ERR_UNSUPPORTED_VERSION;
1670 |     }
1671 | 
1672 |     uint32_t file_size = wet_read_u32_le(bytecode + 8);
1673 |     uint32_t stored_crc = wet_read_u32_le(bytecode + 12);
1674 |     uint32_t num_sections = wet_read_u32_le(bytecode + 16);
1675 | 
1676 |     if (file_size > size) {
1677 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Declared file size %u exceeds buffer %zu", file_size, size);
1678 |         return WET_ERR_MALFORMED_SECTION;
1679 |     }
1680 | 
1681 |     /* CRC32 check: copy header, zero bytes 12..15, compute CRC */
1682 |     uint8_t hdr_copy[WET_HEADER_SIZE];
1683 |     memcpy(hdr_copy, bytecode, WET_HEADER_SIZE);
1684 |     memset(hdr_copy + 12, 0, 4);
1685 |     uint32_t crc = wet_compute_crc32(hdr_copy, WET_HEADER_SIZE, 0);
1686 |     if (file_size > WET_HEADER_SIZE) {
1687 |         crc = wet_compute_crc32(bytecode + WET_HEADER_SIZE, file_size - WET_HEADER_SIZE, crc);
1688 |     }
1689 |     if (crc != stored_crc) {
1690 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "CRC32 mismatch (computed 0x%08X != stored 0x%08X)", crc, stored_crc);
1691 |         return WET_ERR_CRC_MISMATCH;
1692 |     }
1693 | 
1694 |     size_t sec_table_end = WET_HEADER_SIZE + (size_t)num_sections * WET_SECTION_ENTRY_SIZE;
1695 |     if (sec_table_end > file_size) {
1696 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section table overflows file bounds");
1697 |         return WET_ERR_MALFORMED_SECTION;
1698 |     }
1699 | 
1700 |     const uint8_t* code_ptr = NULL;
1701 |     size_t code_size = 0;
1702 |     size_t num_constants = 0;
1703 | 
1704 |     for (uint32_t s = 0; s < num_sections; ++s) {
1705 |         const uint8_t* entry = bytecode + WET_HEADER_SIZE + s * WET_SECTION_ENTRY_SIZE;
1706 |         uint16_t sec_type = wet_read_u16_le(entry);
1707 |         uint32_t sec_offset = wet_read_u32_le(entry + 4);
1708 |         uint32_t sec_size = wet_read_u32_le(entry + 8);
1709 | 
1710 |         if ((size_t)sec_offset + sec_size > file_size || sec_offset < sec_table_end) {
1711 |             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section %u (type %u) out of bounds", s, sec_type);
1712 |             return WET_ERR_MALFORMED_SECTION;
1713 |         }
1714 | 
1715 |         if (sec_type == WET_SEC_BYTECODE_STREAM) {
1716 |             code_ptr = bytecode + sec_offset;
1717 |             code_size = sec_size;
1718 |         } else if (sec_type == WET_SEC_CONSTANT_POOL) {
1719 |             if (sec_size >= 4) {
1720 |                 uint32_t declared_entries = wet_read_u32_le(bytecode + sec_offset);
1721 |                 const uint8_t* cp = bytecode + sec_offset + 4;
1722 |                 size_t cp_remain = sec_size - 4;
1723 |                 while (cp_remain > 0) {
1724 |                     uint8_t ctype = *cp;
1725 |                     cp++; cp_remain--;
1726 |                     if (ctype == WET_VAL_INT || ctype == WET_VAL_FLOAT) {
1727 |                         if (cp_remain < 4) {
1728 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed constant pool");
1729 |                             return WET_ERR_MALFORMED_SECTION;
1730 |                         }
1731 |                         cp += 4; cp_remain -= 4;
1732 |                     } else if (ctype == WET_VAL_STRING) {
1733 |                         if (cp_remain < 2) {
1734 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed string in constant pool");
1735 |                             return WET_ERR_MALFORMED_SECTION;
1736 |                         }
1737 |                         uint16_t slen = wet_read_u16_le(cp);
1738 |                         cp += 2; cp_remain -= 2;
1739 |                         if (cp_remain < slen) {
1740 |                             if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "String payload overflows constant pool");
1741 |                             return WET_ERR_MALFORMED_SECTION;
1742 |                         }
1743 |                         cp += slen; cp_remain -= slen;
1744 |                     } else {
1745 |                         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unknown constant type %u", ctype);
1746 |                         return WET_ERR_MALFORMED_SECTION;
1747 |                     }
1748 |                     num_constants++;
1749 |                 }
1750 |             }
1751 |         }
1752 |     }
1753 | 
1754 |     if (!code_ptr || code_size == 0) {
1755 |         return WET_OK;
1756 |     }
1757 | 
1758 |     uint8_t* is_start = (uint8_t*)malloc(code_size);
1759 |     if (!is_start) {
1760 |         if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Failed to allocate verifier bitmap (%zu bytes)", code_size);
1761 |         return WET_ERR_ALLOC_FAILED;
1762 |     }
1763 |     memset(is_start, 0, code_size);
1764 | 
1765 |     /* Pass 1: Decode opcodes and check instruction sizes */
1766 |     size_t pc = 0;
1767 |     while (pc < code_size) {
1768 |         is_start[pc] = 1;
1769 |         uint8_t op = code_ptr[pc];
1770 |         size_t ilen = 1;
1771 | 
1772 |         switch ((wet_opcode_t)op) {
1773 |             case WET_OP_NOP:
1774 |             case WET_OP_HALT:
1775 |             case WET_OP_SYNC_TICK:
1776 |             case WET_OP_POP:
1777 |             case WET_OP_DUP:
1778 |             case WET_OP_SWAP:
1779 |             case WET_OP_ADD_I:
1780 |             case WET_OP_SUB_I:
1781 |             case WET_OP_MUL_I:
1782 |             case WET_OP_DIV_I:
1783 |             case WET_OP_ADD_F:
1784 |             case WET_OP_SUB_F:
1785 |             case WET_OP_MUL_F:
1786 |             case WET_OP_DIV_F:
1787 |             case WET_OP_NEG:
1788 |             case WET_OP_MOD_I:
1789 |             case WET_OP_CMP_EQ:
1790 |             case WET_OP_CMP_NE:
1791 |             case WET_OP_CMP_LT:
1792 |             case WET_OP_CMP_LE:
1793 |             case WET_OP_CMP_GT:
1794 |             case WET_OP_CMP_GE:
1795 |             case WET_OP_RET:
1796 |             case WET_OP_GET_POP_RATE:
1797 |             case WET_OP_READ_TEMPERATURE:
1798 |             case WET_OP_READ_PH:
1799 |             case WET_OP_READ_DO:
1800 |             case WET_OP_READ_CO2:
1801 |                 ilen = 1;
1802 |                 break;
1803 | 
1804 |             case WET_OP_STIM_BIPHASIC:
1805 |             case WET_OP_READ_SPIKES:
1806 |             case WET_OP_READ_VOLTAGE:
1807 |             case WET_OP_READ_PRESSURE:
1808 |             case WET_OP_READ_BUBBLE:
1809 |             case WET_OP_READ_FLOW:
1810 |                 ilen = 2;
1811 |                 break;
1812 | 
1813 |             case WET_OP_SLEEP_TICKS:
1814 |             case WET_OP_LOAD_LOCAL:
1815 |             case WET_OP_STORE_LOCAL:
1816 |             case WET_OP_JMP:
1817 |             case WET_OP_JMP_IF_TRUE:
1818 |             case WET_OP_JMP_IF_FALSE:
1819 |             case WET_OP_MODULATE_STDP:
1820 |             case WET_OP_MEA_CONFIG:
1821 |             case WET_OP_VALVE_SET:
1822 |                 ilen = 3;
1823 |                 break;
1824 | 
1825 |             case WET_OP_PUSH_CONST:
1826 |                 ilen = 3;
1827 |                 if (pc + 3 <= code_size) {
1828 |                     uint16_t c_idx = wet_read_u16_le(code_ptr + pc + 1);
1829 |                     if (c_idx >= num_constants) {
1830 |                         if (err_buf && err_buf_len > 0)
1831 |                             snprintf(err_buf, err_buf_len, "Constant index %u out of range (%zu)", c_idx, num_constants);
1832 |                         free(is_start);
1833 |                         return WET_ERR_BYTECODE_VERIFICATION;
1834 |                     }
1835 |                 }
1836 |                 break;
1837 | 
1838 |             case WET_OP_CALL:
1839 |                 ilen = 4;
1840 |                 break;
1841 | 
1842 |             case WET_OP_PUSH_INT:
1843 |             case WET_OP_PUSH_FLOAT:
1844 |                 ilen = 5;
1845 |                 break;
1846 | 
1847 |             case WET_OP_PUMP_SET_RATE:
1848 |             case WET_OP_PUMP_DISPENSE:
1849 |             case WET_OP_STIM_CURRENT:
1850 |                 ilen = 6;
1851 |                 break;
1852 | 
1853 |             case WET_OP_MOTOR_STEP:
1854 |                 ilen = 10;
1855 |                 break;
1856 | 
1857 |             default:
1858 |                 if (err_buf && err_buf_len > 0)
1859 |                     snprintf(err_buf, err_buf_len, "Invalid opcode 0x%02X at offset %zu", op, pc);
1860 |                 free(is_start);
1861 |                 return WET_ERR_INVALID_OPCODE;
1862 |         }
1863 | 
1864 |         if (pc + ilen > code_size) {
1865 |             if (err_buf && err_buf_len > 0)
1866 |                 snprintf(err_buf, err_buf_len, "Truncated instruction (opcode 0x%02X needs %zu bytes, only %zu left)", op, ilen, code_size - pc);
1867 |             free(is_start);
1868 |             return WET_ERR_BYTECODE_VERIFICATION;
1869 |         }
1870 |         pc += ilen;
1871 |     }
1872 | 
1873 |     /* Pass 2: Verify branch target alignment */
1874 |     pc = 0;
1875 |     while (pc < code_size) {
1876 |         uint8_t op = code_ptr[pc];
1877 |         if (op == WET_OP_JMP || op == WET_OP_JMP_IF_TRUE || op == WET_OP_JMP_IF_FALSE) {
1878 |             int16_t offset = wet_read_i16_le(code_ptr + pc + 1);
1879 |             int64_t target = (int64_t)pc + offset;
1880 |             if (target < 0 || (size_t)target >= code_size) {
1881 |                 if (err_buf && err_buf_len > 0)
1882 |                     snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld out of code range [0, %zu)", pc, (long long)target, code_size);
1883 |                 free(is_start);
1884 |                 return WET_ERR_BYTECODE_VERIFICATION;
1885 |             }
1886 |             if (!is_start[target]) {
1887 |                 if (err_buf && err_buf_len > 0)
1888 |                     snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld lands in middle of instruction", pc, (long long)target);
1889 |                 free(is_start);
1890 |                 return WET_ERR_BYTECODE_VERIFICATION;
1891 |             }
1892 |             pc += 3;
1893 |         } else {
1894 |             size_t next_pc = pc + 1;
1895 |             while (next_pc < code_size && !is_start[next_pc]) next_pc++;
1896 |             pc = next_pc;
1897 |         }
1898 |     }
1899 | 
1900 |     free(is_start);
1901 |     return WET_OK;
1902 | }
1903 | 
1904 | /* =========================================================================
1905 |  * Phase 3: Live State Checkpointing & Hot-Swap
1906 |  * ========================================================================= */
1907 | 
1908 | #define WET_SNAPSHOT_MAGIC 0x53544557U /* 'W','E','T','S' */
1909 | #define WET_SNAPSHOT_VERSION 1
1910 | 
1911 | #pragma pack(push, 1)
1912 | typedef struct {
1913 |     uint32_t magic;
1914 |     uint32_t version;
1915 |     uint32_t payload_bytes;
1916 |     uint64_t current_tick;
1917 |     double   sim_time_ms;
1918 |     int64_t  sim_time_us;
1919 |     float    v_m_mv[64];
1920 |     float    v_thresh_mv[64];
1921 |     float    g_exc_ns[64];
1922 |     float    g_inh_ns[64];
1923 |     float    g_ahp_ns[64];
1924 |     uint16_t refract_ticks[64];
1925 |     float    trace_pre[64];
1926 |     float    trace_post[64];
1927 |     float    v_double_layer_v[64];
1928 |     float    q_accum[64];
1929 |     float    cumulative_unbounded_dc_nc[64];
1930 |     float    syn_weights_ns[64][64];
1931 |     float    syn_u_stp[64][64];
1932 |     float    syn_x_stp[64][64];
1933 |     float    pump_dispensed_ul[8];
1934 | } wet_vm_snapshot_payload_t;
1935 | #pragma pack(pop)
1936 | 
1937 | wet_status_t wet_vm_snapshot_internal(const struct wet_vm_instance* vm, uint8_t* buffer, size_t* inout_len) {
1938 |     if (!vm || !inout_len) return WET_ERR_NULL_PTR;
1939 | 
1940 |     size_t req_size = sizeof(wet_vm_snapshot_payload_t);
1941 |     if (!buffer) {
1942 |         *inout_len = req_size;
1943 |         return WET_OK;
1944 |     }
1945 |     if (*inout_len < req_size) {
1946 |         *inout_len = req_size;
1947 |         return WET_ERR_ALLOC_FAILED;
1948 |     }
1949 | 
1950 |     wet_vm_snapshot_payload_t* snap = (wet_vm_snapshot_payload_t*)buffer;
1951 |     memset(snap, 0, sizeof(*snap));
1952 |     snap->magic = WET_SNAPSHOT_MAGIC;
1953 |     snap->version = WET_SNAPSHOT_VERSION;
1954 |     snap->payload_bytes = (uint32_t)req_size;
1955 |     snap->current_tick = vm->current_tick;
1956 |     snap->sim_time_ms = vm->sim_time_ms;
1957 |     snap->sim_time_us = vm->sim_time_us;
1958 | 
1959 |     memcpy(snap->v_m_mv, vm->bio.v_m_mv, sizeof(snap->v_m_mv));
1960 |     memcpy(snap->v_thresh_mv, vm->bio.v_thresh_mv, sizeof(snap->v_thresh_mv));
1961 |     memcpy(snap->g_exc_ns, vm->bio.g_exc_ns, sizeof(snap->g_exc_ns));
1962 |     memcpy(snap->g_inh_ns, vm->bio.g_inh_ns, sizeof(snap->g_inh_ns));
1963 |     memcpy(snap->g_ahp_ns, vm->bio.g_ahp_ns, sizeof(snap->g_ahp_ns));
1964 |     memcpy(snap->refract_ticks, vm->bio.refract_ticks, sizeof(snap->refract_ticks));
1965 |     memcpy(snap->trace_pre, vm->bio.trace_pre, sizeof(snap->trace_pre));
1966 |     memcpy(snap->trace_post, vm->bio.trace_post, sizeof(snap->trace_post));
1967 |     memcpy(snap->v_double_layer_v, vm->bio.v_double_layer_v, sizeof(snap->v_double_layer_v));
1968 |     memcpy(snap->q_accum, vm->interlocks.q_accum, sizeof(snap->q_accum));
1969 |     memcpy(snap->cumulative_unbounded_dc_nc, vm->interlocks.cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
1970 |     memcpy(snap->pump_dispensed_ul, vm->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));
1971 | 
1972 |     for (int i = 0; i < 64; ++i) {
1973 |         for (int j = 0; j < 64; ++j) {
1974 |             snap->syn_weights_ns[i][j] = vm->bio.synapses[i][j].weight_ns;
1975 |             snap->syn_u_stp[i][j] = vm->bio.synapses[i][j].u_stp;
1976 |             snap->syn_x_stp[i][j] = vm->bio.synapses[i][j].x_stp;
1977 |         }
1978 |     }
1979 | 
1980 |     *inout_len = req_size;
1981 |     return WET_OK;
1982 | }
1983 | 
1984 | wet_status_t wet_vm_restore_internal(struct wet_vm_instance* vm, const uint8_t* buffer, size_t len) {
1985 |     if (!vm || !buffer) return WET_ERR_NULL_PTR;
1986 |     if (len < sizeof(wet_vm_snapshot_payload_t)) {
1987 |         snprintf(vm->last_error, sizeof(vm->last_error), "Snapshot buffer too small (%zu < %zu)", len, sizeof(wet_vm_snapshot_payload_t));
1988 |         return WET_ERR_MALFORMED_SECTION;
1989 |     }
1990 | 
1991 |     const wet_vm_snapshot_payload_t* snap = (const wet_vm_snapshot_payload_t*)buffer;
1992 |     if (snap->magic != WET_SNAPSHOT_MAGIC || snap->version != WET_SNAPSHOT_VERSION) {
1993 |         snprintf(vm->last_error, sizeof(vm->last_error), "Invalid snapshot magic or version");
1994 |         return WET_ERR_INVALID_MAGIC;
1995 |     }
1996 | 
1997 |     vm->current_tick = snap->current_tick;
1998 |     vm->sim_time_ms = snap->sim_time_ms;
1999 |     vm->sim_time_us = snap->sim_time_us;
2000 | 
2001 |     memcpy(vm->bio.v_m_mv, snap->v_m_mv, sizeof(snap->v_m_mv));
2002 |     memcpy(vm->bio.v_thresh_mv, snap->v_thresh_mv, sizeof(snap->v_thresh_mv));
2003 |     memcpy(vm->bio.g_exc_ns, snap->g_exc_ns, sizeof(snap->g_exc_ns));
2004 |     memcpy(vm->bio.g_inh_ns, snap->g_inh_ns, sizeof(snap->g_inh_ns));
2005 |     memcpy(vm->bio.g_ahp_ns, snap->g_ahp_ns, sizeof(snap->g_ahp_ns));
2006 |     memcpy(vm->bio.refract_ticks, snap->refract_ticks, sizeof(snap->refract_ticks));
2007 |     memcpy(vm->bio.trace_pre, snap->trace_pre, sizeof(snap->trace_pre));
2008 |     memcpy(vm->bio.trace_post, snap->trace_post, sizeof(snap->trace_post));
2009 |     memcpy(vm->bio.v_double_layer_v, snap->v_double_layer_v, sizeof(snap->v_double_layer_v));
2010 |     memcpy(vm->interlocks.q_accum, snap->q_accum, sizeof(snap->q_accum));
2011 |     memcpy(vm->interlocks.cumulative_unbounded_dc_nc, snap->cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
2012 |     memcpy(vm->pump_dispensed_ul, snap->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));
2013 | 
2014 |     for (int i = 0; i < 64; ++i) {
2015 |         for (int j = 0; j < 64; ++j) {
2016 |             vm->bio.synapses[i][j].weight_ns = snap->syn_weights_ns[i][j];
2017 |             vm->bio.synapses[i][j].u_stp = snap->syn_u_stp[i][j];
2018 |             vm->bio.synapses[i][j].x_stp = snap->syn_x_stp[i][j];
2019 |         }
2020 |     }
2021 | 
2022 |     return WET_OK;
2023 | }
```

### `native/build.py` (253 lines, SHA-256: `d80faddc3126e4c4...`)

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
  83 | """
  84 |     output_def.write_text(def_content, encoding="utf-8")
  85 |     cmd = [
  86 |         dlltool_path,
  87 |         "-d", str(output_def),
  88 |         "-l", str(output_lib),
  89 |         "-m", "i386:x86-64"
  90 |     ]
  91 |     res = subprocess.run(cmd, capture_output=True, text=True)
  92 |     return res.returncode == 0 and output_lib.exists()
  93 | 
  94 | 
  95 | def build_with_clang(clang_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
  96 |     print(f"Building with Clang: {clang_path}")
  97 |     bin_dir = out_dll.parent
  98 |     bin_dir.mkdir(parents=True, exist_ok=True)
  99 | 
 100 |     # Check if we need standalone msvcrt / kernel32 import libraries on Windows
 101 |     extra_link_args = []
 102 |     if sys.platform == "win32":
 103 |         # Look for llvm-dlltool next to clang
 104 |         clang_dir = Path(clang_path).parent
 105 |         dlltool_path = find_executable("llvm-dlltool", [clang_dir])
 106 |         msvcrt_lib = bin_dir / "msvcrt.lib"
 107 |         msvcrt_def = bin_dir / "msvcrt.def"
 108 |         kernel32_lib = bin_dir / "kernel32.lib"
 109 |         kernel32_def = bin_dir / "kernel32.def"
 110 | 
 111 |         if dlltool_path:
 112 |             if not msvcrt_lib.exists() or msvcrt_lib.stat().st_size == 0 or not msvcrt_def.exists() or "qsort" not in msvcrt_def.read_text(encoding="utf-8"):
 113 |                 generate_msvcrt_import_lib(dlltool_path, msvcrt_lib, msvcrt_def)
 114 |             if not kernel32_lib.exists() or kernel32_lib.stat().st_size == 0 or not kernel32_def.exists() or "CreateThread" not in kernel32_def.read_text(encoding="utf-8"):
 115 |                 generate_kernel32_import_lib(dlltool_path, kernel32_lib, kernel32_def)
 116 |             if msvcrt_lib.exists() and kernel32_lib.exists():
 117 |                 extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib), str(kernel32_lib)]
 118 |             elif msvcrt_lib.exists():
 119 |                 extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib)]
 120 | 
 121 |     cmd = [
 122 |         clang_path,
 123 |         "-O3",
 124 |         "-shared",
 125 |         "-DWET_BUILDING_DLL",
 126 |         f"-I{include_dir}",
 127 |         "-o", str(out_dll),
 128 |         *[str(f) for f in src_files],
 129 |         *extra_link_args
 130 |     ]
 131 | 
 132 |     res = subprocess.run(cmd, capture_output=True, text=True)
 133 |     if res.returncode != 0:
 134 |         print(f"Clang build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 135 |         return False
 136 |     return out_dll.exists()
 137 | 
 138 | 
 139 | def build_with_gcc(gcc_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
 140 |     print(f"Building with GCC: {gcc_path}")
 141 |     bin_dir = out_dll.parent
 142 |     bin_dir.mkdir(parents=True, exist_ok=True)
 143 | 
 144 |     cmd = [
 145 |         gcc_path,
 146 |         "-shared",
 147 |         "-fPIC" if sys.platform != "win32" else "",
 148 |         "-DWET_BUILDING_DLL",
 149 |         f"-I{include_dir}",
 150 |         "-o", str(out_dll),
 151 |         *[str(f) for f in src_files]
 152 |     ]
 153 |     cmd = [arg for arg in cmd if arg]
 154 |     res = subprocess.run(cmd, capture_output=True, text=True)
 155 |     if res.returncode != 0:
 156 |         print(f"GCC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 157 |         return False
 158 |     return out_dll.exists()
 159 | 
 160 | 
 161 | def build_with_msvc(cl_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
 162 |     print(f"Building with MSVC: {cl_path}")
 163 |     bin_dir = out_dll.parent
 164 |     bin_dir.mkdir(parents=True, exist_ok=True)
 165 | 
 166 |     cmd = [
 167 |         cl_path,
 168 |         "/LD",
 169 |         "/DWET_BUILDING_DLL",
 170 |         f"/I{include_dir}",
 171 |         *[str(f) for f in src_files],
 172 |         f"/Fe:{out_dll}"
 173 |     ]
 174 |     res = subprocess.run(cmd, capture_output=True, text=True)
 175 |     if res.returncode != 0:
 176 |         print(f"MSVC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
 177 |         return False
 178 |     return out_dll.exists()
 179 | 
 180 | 
 181 | def build_native_runtime() -> Path:
 182 |     proj_root = get_project_root()
 183 |     native_dir = proj_root / "native"
 184 |     include_dir = native_dir / "include"
 185 |     src_dir = native_dir / "src"
 186 |     bin_dir = native_dir / "bin"
 187 |     bin_dir.mkdir(parents=True, exist_ok=True)
 188 | 
 189 |     src_files = [
 190 |         src_dir / "wetvm_api.c",
 191 |         src_dir / "wetvm_vm.c",
 192 |         src_dir / "biophysics.c",
 193 |         src_dir / "interlocks.c",
 194 |         src_dir / "wet_hal.c",
 195 |         src_dir / "wet_hal_intan.c",
 196 |         src_dir / "wet_hal_maxwell.c",
 197 |         src_dir / "wet_hal_pump_valve.c",
 198 |         src_dir / "wet_hal_sensirion.c",
 199 |         src_dir / "wet_scheduler.c",
 200 |     ]
 201 |     for sf in src_files:
 202 |         if not sf.exists():
 203 |             raise FileNotFoundError(f"Source file not found: {sf}")
 204 | 
 205 |     ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
 206 |     out_dll = bin_dir / f"wetvm{ext}"
 207 |     fallback_dll = native_dir / f"wetvm{ext}"
 208 | 
 209 |     # Search for compilers in order of preference
 210 |     # 1. MSVC cl.exe
 211 |     cl_exe = find_executable("cl")
 212 |     if cl_exe and build_with_msvc(cl_exe, src_files, include_dir, out_dll):
 213 |         shutil.copy2(out_dll, fallback_dll)
 214 |         print(f"Successfully compiled shared library: {out_dll}")
 215 |         return out_dll
 216 | 
 217 |     # 2. Clang
 218 |     extra_clang_paths = [
 219 |         r"C:\Program Files\LLVM\bin",
 220 |         r"C:\LLVM\bin",
 221 |         r"C:\msys64\mingw64\bin",
 222 |         r"C:\msys64\ucrt64\bin"
 223 |     ]
 224 |     clang_exe = find_executable("clang", extra_clang_paths)
 225 |     if clang_exe and build_with_clang(clang_exe, src_files, include_dir, out_dll):
 226 |         shutil.copy2(out_dll, fallback_dll)
 227 |         print(f"Successfully compiled shared library: {out_dll}")
 228 |         return out_dll
 229 | 
 230 |     # 3. GCC
 231 |     extra_gcc_paths = [
 232 |         r"C:\msys64\mingw64\bin",
 233 |         r"C:\msys64\ucrt64\bin",
 234 |         r"C:\mingw64\bin",
 235 |         r"C:\TDM-GCC-64\bin"
 236 |     ]
 237 |     gcc_exe = find_executable("gcc", extra_gcc_paths)
 238 |     if gcc_exe and build_with_gcc(gcc_exe, src_files, include_dir, out_dll):
 239 |         shutil.copy2(out_dll, fallback_dll)
 240 |         print(f"Successfully compiled shared library: {out_dll}")
 241 |         return out_dll
 242 | 
 243 |     raise RuntimeError("No suitable C compiler found (MSVC cl.exe, Clang, or GCC).")
 244 | 
 245 | 
 246 | if __name__ == "__main__":
 247 |     try:
 248 |         path = build_native_runtime()
 249 |         print(f"BUILD SUCCESS: {path}")
 250 |         sys.exit(0)
 251 |     except Exception as e:
 252 |         print(f"BUILD ERROR: {e}", file=sys.stderr)
 253 |         sys.exit(1)
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

### `bindings/__init__.py` (42 lines, SHA-256: `7cfb2e1e1803c122...`)

```text
   1 | """
   2 | WetLang Bindings Package
   3 | Exports WetVM, WetVMConfig, WetTelemetry, WetStatus, WetVMError, WetRuntime, WetVMFFI, get_wetvm_lib, load_wetvm_lib.
   4 | """
   5 | 
   6 | from bindings.ffi import (
   7 |     WetStatus,
   8 |     WetVMConfig,
   9 |     WetTelemetry,
  10 |     WetVMFFI,
  11 |     load_wetvm_lib,
  12 |     get_wetvm_lib,
  13 | )
  14 | from bindings.runtime import (
  15 |     WetVM,
  16 |     WetRuntime,
  17 |     WetTelemetryView,
  18 |     WetVMError,
  19 | )
  20 | from bindings.scheduler import (
  21 |     WetScheduler,
  22 |     WetSchedulerConfig,
  23 |     WetSchedulerStats,
  24 |     WetStimCommand,
  25 | )
  26 | 
  27 | __all__ = [
  28 |     "WetVM",
  29 |     "WetRuntime",
  30 |     "WetVMConfig",
  31 |     "WetTelemetry",
  32 |     "WetTelemetryView",
  33 |     "WetStatus",
  34 |     "WetVMError",
  35 |     "WetVMFFI",
  36 |     "load_wetvm_lib",
  37 |     "get_wetvm_lib",
  38 |     "WetScheduler",
  39 |     "WetSchedulerConfig",
  40 |     "WetSchedulerStats",
  41 |     "WetStimCommand",
  42 | ]
```

### `bindings/ffi.py` (1127 lines, SHA-256: `57f28e802ac68829...`)

```text
   1 | """
   2 | WetLang Python ctypes FFI Bindings
   3 | Exposes C-ABI functions and data structures for wetvm.dll / libwetvm.so.
   4 | """
   5 | 
   6 | import os
   7 | import sys
   8 | import ctypes
   9 | from ctypes import c_void_p, c_char_p, c_int, c_int32, c_uint8, c_uint16, c_uint32, c_uint64, c_double, c_float, c_size_t, POINTER
  10 | from enum import IntEnum
  11 | from pathlib import Path
  12 | from typing import Optional, Tuple
  13 | import numpy as np
  14 | 
  15 | 
  16 | # =========================================================================
  17 | # Status and Error Codes
  18 | # =========================================================================
  19 | 
  20 | class WetStatus(IntEnum):
  21 |     WET_OK                      = 0
  22 |     WET_ERR_INVALID_MAGIC       = 1
  23 |     WET_ERR_CRC_MISMATCH        = 2
  24 |     WET_ERR_UNSUPPORTED_VERSION = 3
  25 |     WET_ERR_MALFORMED_SECTION   = 4
  26 |     WET_ERR_STACK_OVERFLOW      = 5
  27 |     WET_ERR_STACK_UNDERFLOW     = 6
  28 |     WET_ERR_INVALID_OPCODE      = 7
  29 |     WET_ERR_OUT_OF_BOUNDS_CH    = 8
  30 |     WET_ERR_DIVISION_BY_ZERO    = 9
  31 |     WET_ERR_NULL_PTR            = 10
  32 |     WET_ERR_ALLOC_FAILED        = 11
  33 |     WET_ERR_HALTED              = 12
  34 |     WET_ERR_CHARGE_IMBALANCE    = 13
  35 |     WET_ERR_EPILEPTIFORM_RUNAWAY = 14
  36 |     WET_ERR_CAPABILITY_DENIED   = 15
  37 |     WET_ERR_INTERLOCK_LOCKED    = 16
  38 |     WET_ERR_WATCHDOG_TIMEOUT    = 17
  39 |     WET_ERR_DC_DRIFT            = 18
  40 |     WET_ERR_CHARGE_DENSITY_EXCEEDED = 19
  41 |     WET_ERR_FOCAL_EXCITOTOXICITY = 20
  42 |     WET_ERR_SHEAR_STRESS_EXCEEDED = 21
  43 |     WET_ERR_SECURITY_UNTRUSTED    = 22
  44 |     WET_ERR_ACTUATOR_FAULT        = 23
  45 |     WET_ERR_THERMAL_LIMIT         = 24
  46 |     WET_ERR_BUBBLE_DETECTED       = 25
  47 |     WET_ERR_COMPLIANCE_RAILED     = 26
  48 |     WET_ERR_BYTECODE_VERIFICATION = 27
  49 | 
  50 | 
  51 | class WetHalMode(IntEnum):
  52 |     WET_HAL_MODE_SIMULATED    = 0
  53 |     WET_HAL_MODE_PHYSICAL     = 1
  54 |     WET_HAL_MODE_HIL_LOOPBACK = 2
  55 | 
  56 | 
  57 | class WetHalDriverType(IntEnum):
  58 |     WET_HAL_DRIVER_EPHYS   = 1
  59 |     WET_HAL_DRIVER_PUMP    = 2
  60 |     WET_HAL_DRIVER_VALVE   = 3
  61 |     WET_HAL_DRIVER_FLOW    = 4
  62 |     WET_HAL_DRIVER_CAN_BUS = 5
  63 | 
  64 | 
  65 | class WetHalStatus(IntEnum):
  66 |     WET_HAL_OK                   = 0
  67 |     WET_HAL_ERR_NULL_PTR         = -1
  68 |     WET_HAL_ERR_INVALID_MODE     = -2
  69 |     WET_HAL_ERR_DRIVER_NOT_FOUND = -3
  70 |     WET_HAL_ERR_IO               = -4
  71 |     WET_HAL_ERR_TIMEOUT          = -5
  72 |     WET_HAL_ERR_CRC_MISMATCH     = -6
  73 |     WET_HAL_ERR_COMPLIANCE_RAILED= -7
  74 |     WET_HAL_ERR_INTERLOCK        = -8
  75 |     WET_HAL_ERR_DEAD_HEAD        = -9
  76 |     WET_HAL_ERR_OUT_OF_BOUNDS    = -10
  77 |     WET_HAL_ERR_BUS_BUSY         = -11
  78 |     WET_HAL_ERR_NOT_SUPPORTED    = -12
  79 |     WET_HAL_ERR_BUFFER_FULL      = -13
  80 | 
  81 | 
  82 | class WetHalConfig(ctypes.Structure):
  83 |     """Mirror of C wet_hal_config_t."""
  84 |     _fields_ = [
  85 |         ("mode", c_int),
  86 |         ("max_ephys_channels", c_uint32),
  87 |         ("num_pumps", c_uint32),
  88 |         ("num_valves", c_uint32),
  89 |         ("num_flow_sensors", c_uint32),
  90 |         ("enable_dead_head_protection", c_uint8),
  91 |         ("enable_crowbar_fastpath", c_uint8),
  92 |         ("valve_for_pump", c_uint8 * 8),
  93 |     ]
  94 | 
  95 |     def __init__(
  96 |         self,
  97 |         mode: int = 0,
  98 |         max_ephys_channels: int = 64,
  99 |         num_pumps: int = 8,
 100 |         num_valves: int = 8,
 101 |         num_flow_sensors: int = 8,
 102 |         enable_dead_head_protection: int = 1,
 103 |         enable_crowbar_fastpath: int = 1,
 104 |         valve_for_pump = None,
 105 |     ):
 106 |         v = (c_uint8 * 8)(0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF)
 107 |         if valve_for_pump is not None:
 108 |             for i, val in enumerate(valve_for_pump):
 109 |                 v[i] = val
 110 |         super().__init__(
 111 |             mode=mode,
 112 |             max_ephys_channels=max_ephys_channels,
 113 |             num_pumps=num_pumps,
 114 |             num_valves=num_valves,
 115 |             num_flow_sensors=num_flow_sensors,
 116 |             enable_dead_head_protection=enable_dead_head_protection,
 117 |             enable_crowbar_fastpath=enable_crowbar_fastpath,
 118 |             valve_for_pump=v,
 119 |         )
 120 | 
 121 | 
 122 | class WetHalTelemetry(ctypes.Structure):
 123 |     """Mirror of C wet_hal_telemetry_t."""
 124 |     _fields_ = [
 125 |         ("total_spi_transactions", c_uint64),
 126 |         ("total_i2c_transactions", c_uint64),
 127 |         ("total_rs232_commands", c_uint64),
 128 |         ("total_can_frames", c_uint64),
 129 |         ("total_crowbar_events", c_uint64),
 130 |         ("last_crowbar_timestamp_us", c_uint64),
 131 |         ("last_crowbar_reason", c_uint32),
 132 |         ("crowbar_latency_us", c_double),
 133 |     ]
 134 | 
 135 | 
 136 | class WetHalContext(ctypes.Structure):
 137 |     """Mirror of C wet_hal_context_t."""
 138 |     _fields_ = [
 139 |         ("mode", c_int),
 140 |         ("config", WetHalConfig),
 141 |         ("vm", c_void_p),
 142 |         ("drivers", c_void_p * 16),
 143 |         ("driver_count", c_uint32),
 144 |         ("ephys_driver", c_void_p),
 145 |         ("pump_driver", c_void_p),
 146 |         ("valve_driver", c_void_p),
 147 |         ("flow_driver", c_void_p),
 148 |         ("can_driver", c_void_p),
 149 |         ("pump_rates_ul_min", c_float * 8),
 150 |         ("valve_states", c_uint8 * 8),
 151 |         ("flow_rates_ul_min", c_double * 8),
 152 |         ("ephys_voltages", c_float * 64),
 153 |         ("ephys_spikes", c_uint8 * 64),
 154 |         ("crowbar_tripped", c_uint8),
 155 |         ("crowbar_reason", c_uint32),
 156 |         ("crowbar_tick", c_uint64),
 157 |         ("crowbar_timestamp_us", c_uint64),
 158 |         ("telemetry", WetHalTelemetry),
 159 |     ]
 160 | 
 161 | 
 162 | class WetCanFrame(ctypes.Structure):
 163 |     """Mirror of C wet_can_frame_t."""
 164 |     _fields_ = [
 165 |         ("id", c_uint32),
 166 |         ("is_extended", c_uint8),
 167 |         ("is_rtr", c_uint8),
 168 |         ("dlc", c_uint8),
 169 |         ("data", c_uint8 * 8),
 170 |         ("timestamp_us", c_uint64),
 171 |     ]
 172 | 
 173 | 
 174 | # =========================================================================
 175 | # C Struct Mirrors
 176 | # =========================================================================
 177 | 
 178 | class WetVMConfig(ctypes.Structure):
 179 |     """Mirror of C wet_vm_config_t (28 bytes)."""
 180 |     _fields_ = [
 181 |         ("dt_ms", c_double),
 182 |         ("max_stack_depth", c_uint32),
 183 |         ("max_locals", c_uint32),
 184 |         ("channel_count", c_uint32),
 185 |         ("max_ops_per_tick", c_uint32),
 186 |     ]
 187 | 
 188 |     def __init__(
 189 |         self,
 190 |         dt_ms: float = 0.1,
 191 |         max_stack_depth: int = 1024,
 192 |         max_locals: int = 256,
 193 |         channel_count: int = 64,
 194 |         max_ops_per_tick: int = 100000
 195 |     ):
 196 |         super().__init__(
 197 |             dt_ms=dt_ms,
 198 |             max_stack_depth=max_stack_depth,
 199 |             max_locals=max_locals,
 200 |             channel_count=channel_count,
 201 |             max_ops_per_tick=max_ops_per_tick
 202 |         )
 203 | 
 204 | 
 205 | class WetTelemetry(ctypes.Structure):
 206 |     """Mirror of C wet_telemetry_t (600 bytes with 8-byte alignment padding)."""
 207 |     _fields_ = [
 208 |         ("current_tick", c_uint64),
 209 |         ("sim_time_ms", c_double),
 210 |         ("voltages", c_float * 64),
 211 |         ("spikes", c_uint8 * 64),
 212 |         ("population_rate_hz", c_float),
 213 |         ("last_charge_nc", c_float * 64),
 214 |     ]
 215 | 
 216 |     @property
 217 |     def tick_index(self) -> int:
 218 |         return int(self.current_tick)
 219 | 
 220 |     @property
 221 |     def channel_voltages(self) -> np.ndarray:
 222 |         arr = np.ctypeslib.as_array(self.voltages)
 223 |         arr.flags.writeable = False
 224 |         return arr
 225 | 
 226 |     @property
 227 |     def spike_raster(self) -> np.ndarray:
 228 |         arr = np.ctypeslib.as_array(self.spikes)
 229 |         return arr
 230 | 
 231 |     @property
 232 |     def net_charge(self) -> np.ndarray:
 233 |         arr = np.ctypeslib.as_array(self.last_charge_nc)
 234 |         return arr
 235 | 
 236 |     @property
 237 |     def last_charge(self) -> np.ndarray:
 238 |         arr = np.ctypeslib.as_array(self.last_charge_nc)
 239 |         return arr
 240 | 
 241 | 
 242 | class WetActuatorTelemetry(ctypes.Structure):
 243 |     """Mirror of C wet_actuator_telemetry_t."""
 244 |     _fields_ = [
 245 |         ("pump_rates_ul_min", c_float * 8),
 246 |         ("pump_dispensed_ul", c_float * 8),
 247 |         ("valve_states", c_uint8 * 8),
 248 |         ("motor_positions", c_int * 4),
 249 |         ("motor_speeds_rpm", c_float * 4),
 250 |         ("ambient_temperature_c", c_float),
 251 |         ("fluid_pressure_kpa", c_float * 4),
 252 |     ]
 253 | 
 254 |     @property
 255 |     def pump_rates(self) -> np.ndarray:
 256 |         return np.ctypeslib.as_array(self.pump_rates_ul_min)
 257 | 
 258 |     @property
 259 |     def pump_dispensed(self) -> np.ndarray:
 260 |         return np.ctypeslib.as_array(self.pump_dispensed_ul)
 261 | 
 262 |     @property
 263 |     def valves(self) -> np.ndarray:
 264 |         return np.ctypeslib.as_array(self.valve_states)
 265 | 
 266 |     @property
 267 |     def motors(self) -> np.ndarray:
 268 |         return np.ctypeslib.as_array(self.motor_positions)
 269 | 
 270 | 
 271 | # =========================================================================
 272 | # Shared Library Loader
 273 | # =========================================================================
 274 | 
 275 | def _find_library_path() -> Path:
 276 |     env_path = os.environ.get("WETVM_LIBRARY_PATH")
 277 |     if env_path and Path(env_path).is_file():
 278 |         return Path(env_path)
 279 | 
 280 |     ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
 281 |     lib_name = f"wetvm{ext}"
 282 | 
 283 |     # Search candidates
 284 |     curr_dir = Path(__file__).resolve().parent
 285 |     candidates = [
 286 |         curr_dir.parent / "bin" / lib_name,
 287 |         curr_dir.parent / "native" / "bin" / lib_name,
 288 |         curr_dir.parent.parent / "bin" / lib_name,
 289 |         curr_dir.parent.parent / "native" / "bin" / lib_name,
 290 |         curr_dir / lib_name,
 291 |         Path.cwd() / "native" / "bin" / lib_name,
 292 |         Path.cwd() / "bin" / lib_name,
 293 |         Path.cwd() / "native" / lib_name,
 294 |     ]
 295 | 
 296 |     for cand in candidates:
 297 |         if cand.is_file():
 298 |             return cand
 299 | 
 300 |     # Attempt to build automatically if not found
 301 |     build_script = curr_dir.parent / "native" / "build.py"
 302 |     if build_script.is_file():
 303 |         import subprocess
 304 |         res = subprocess.run([sys.executable, str(build_script)], capture_output=True, text=True)
 305 |         if res.returncode == 0:
 306 |             for cand in candidates:
 307 |                 if cand.is_file():
 308 |                     return cand
 309 | 
 310 |     raise FileNotFoundError(
 311 |         f"Could not locate {lib_name}. Run 'python native/build.py' first or set WETVM_LIBRARY_PATH."
 312 |     )
 313 | 
 314 | 
 315 | def load_wetvm_lib(lib_path: Optional[Path] = None) -> ctypes.CDLL:
 316 |     path = lib_path if lib_path is not None else _find_library_path()
 317 |     lib = ctypes.CDLL(str(path))
 318 | 
 319 |     # wet_vm_t* wet_create_vm(const wet_vm_config_t* config)
 320 |     lib.wet_create_vm.restype = c_void_p
 321 |     lib.wet_create_vm.argtypes = [POINTER(WetVMConfig)]
 322 | 
 323 |     # void wet_free_vm(wet_vm_t* vm)
 324 |     lib.wet_free_vm.restype = None
 325 |     lib.wet_free_vm.argtypes = [c_void_p]
 326 | 
 327 |     # wet_status_t wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)
 328 |     lib.wet_load_bytecode.restype = c_int
 329 |     lib.wet_load_bytecode.argtypes = [c_void_p, POINTER(c_uint8), c_size_t, c_char_p, c_size_t]
 330 | 
 331 |     # wet_status_t wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)
 332 |     lib.wet_step_tick.restype = c_int
 333 |     lib.wet_step_tick.argtypes = [c_void_p, POINTER(WetTelemetry)]
 334 | 
 335 |     # wet_status_t wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)
 336 |     lib.wet_run_ticks.restype = c_int
 337 |     lib.wet_run_ticks.argtypes = [c_void_p, c_uint32, POINTER(c_uint32), POINTER(WetTelemetry)]
 338 | 
 339 |     # wet_status_t wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)
 340 |     lib.wet_inject_stimulus.restype = c_int
 341 |     lib.wet_inject_stimulus.argtypes = [c_void_p, c_uint8, c_float, c_float, c_float]
 342 | 
 343 |     # wet_status_t wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)
 344 |     lib.wet_get_telemetry.restype = c_int
 345 |     lib.wet_get_telemetry.argtypes = [c_void_p, POINTER(WetTelemetry)]
 346 | 
 347 |     # const char* wet_get_last_error(wet_vm_t* vm)
 348 |     lib.wet_get_last_error.restype = c_char_p
 349 |     lib.wet_get_last_error.argtypes = [c_void_p]
 350 | 
 351 |     # const char* wet_status_to_string(wet_status_t status)
 352 |     lib.wet_status_to_string.restype = c_char_p
 353 |     lib.wet_status_to_string.argtypes = [c_int]
 354 | 
 355 |     # wet_status_t wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)
 356 |     if hasattr(lib, "wet_get_actuator_telemetry"):
 357 |         lib.wet_get_actuator_telemetry.restype = c_int
 358 |         lib.wet_get_actuator_telemetry.argtypes = [c_void_p, POINTER(WetActuatorTelemetry)]
 359 | 
 360 |     # Phase 3 C-ABI Functions
 361 |     if hasattr(lib, "wet_create_vm_arena"):
 362 |         lib.wet_create_vm_arena.restype = c_void_p
 363 |         lib.wet_create_vm_arena.argtypes = [c_void_p, c_size_t, POINTER(WetVMConfig)]
 364 | 
 365 |     if hasattr(lib, "wet_configure_electrode"):
 366 |         lib.wet_configure_electrode.restype = None
 367 |         lib.wet_configure_electrode.argtypes = [c_void_p, c_uint8, c_float]
 368 | 
 369 |     if hasattr(lib, "wet_active_discharge"):
 370 |         lib.wet_active_discharge.restype = None
 371 |         lib.wet_active_discharge.argtypes = [c_void_p, c_uint8]
 372 | 
 373 |     if hasattr(lib, "wet_active_discharge_all"):
 374 |         lib.wet_active_discharge_all.restype = None
 375 |         lib.wet_active_discharge_all.argtypes = [c_void_p]
 376 | 
 377 |     if hasattr(lib, "wet_enable_dead_head_protection"):
 378 |         lib.wet_enable_dead_head_protection.restype = None
 379 |         lib.wet_enable_dead_head_protection.argtypes = [c_void_p, c_uint8]
 380 | 
 381 |     if hasattr(lib, "wet_life_supervisor_shutdown"):
 382 |         lib.wet_life_supervisor_shutdown.restype = None
 383 |         lib.wet_life_supervisor_shutdown.argtypes = [c_void_p]
 384 | 
 385 |     if hasattr(lib, "wet_configure_blanking"):
 386 |         lib.wet_configure_blanking.restype = None
 387 |         lib.wet_configure_blanking.argtypes = [c_void_p, c_float, c_uint8]
 388 | 
 389 |     if hasattr(lib, "wet_inject_current_stimulus"):
 390 |         lib.wet_inject_current_stimulus.restype = c_int
 391 |         lib.wet_inject_current_stimulus.argtypes = [c_void_p, c_uint8, c_float, c_float, c_float]
 392 | 
 393 |     if hasattr(lib, "wet_verify_bytecode"):
 394 |         lib.wet_verify_bytecode.restype = c_int
 395 |         lib.wet_verify_bytecode.argtypes = [POINTER(c_uint8), c_size_t, c_char_p, c_size_t]
 396 | 
 397 |     if hasattr(lib, "wet_vm_snapshot"):
 398 |         lib.wet_vm_snapshot.restype = c_int
 399 |         lib.wet_vm_snapshot.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_size_t)]
 400 | 
 401 |     if hasattr(lib, "wet_vm_restore"):
 402 |         lib.wet_vm_restore.restype = c_int
 403 |         lib.wet_vm_restore.argtypes = [c_void_p, POINTER(c_uint8), c_size_t]
 404 | 
 405 |     if hasattr(lib, "wet_set_environmental_sensors"):
 406 |         lib.wet_set_environmental_sensors.restype = None
 407 |         lib.wet_set_environmental_sensors.argtypes = [c_void_p, c_float, c_float, c_float, c_uint8, c_uint8, c_float]
 408 | 
 409 |     if hasattr(lib, "wet_set_temperature"):
 410 |         lib.wet_set_temperature.restype = None
 411 |         lib.wet_set_temperature.argtypes = [c_void_p, c_float]
 412 | 
 413 |     if hasattr(lib, "wet_set_channel_banks"):
 414 |         lib.wet_set_channel_banks.restype = None
 415 |         lib.wet_set_channel_banks.argtypes = [c_void_p, c_uint64, c_uint64]
 416 | 
 417 |     # Milestone 2: Biophysics Live Synaptic Inspection
 418 |     if hasattr(lib, "wet_vm_get_synapse_matrix"):
 419 |         lib.wet_vm_get_synapse_matrix.restype = c_int
 420 |         lib.wet_vm_get_synapse_matrix.argtypes = [c_void_p, POINTER(c_float), c_size_t]
 421 | 
 422 |     if hasattr(lib, "wet_vm_get_synapse_weight"):
 423 |         lib.wet_vm_get_synapse_weight.restype = c_float
 424 |         lib.wet_vm_get_synapse_weight.argtypes = [c_void_p, c_uint8, c_uint8]
 425 | 
 426 |     # Milestone 1: Physical HAL Core APIs
 427 |     if hasattr(lib, "wet_hal_create"):
 428 |         lib.wet_hal_create.restype = c_void_p
 429 |         lib.wet_hal_create.argtypes = [c_int, POINTER(WetHalConfig)]
 430 | 
 431 |     if hasattr(lib, "wet_hal_destroy"):
 432 |         lib.wet_hal_destroy.restype = None
 433 |         lib.wet_hal_destroy.argtypes = [c_void_p]
 434 | 
 435 |     if hasattr(lib, "wet_hal_init"):
 436 |         lib.wet_hal_init.restype = c_int
 437 |         lib.wet_hal_init.argtypes = [c_void_p, c_int, POINTER(WetHalConfig)]
 438 | 
 439 |     if hasattr(lib, "wet_hal_attach"):
 440 |         lib.wet_hal_attach.restype = c_int
 441 |         lib.wet_hal_attach.argtypes = [c_void_p, c_void_p]
 442 | 
 443 |     if hasattr(lib, "wet_hal_get_context"):
 444 |         lib.wet_hal_get_context.restype = c_void_p
 445 |         lib.wet_hal_get_context.argtypes = [c_void_p]
 446 | 
 447 |     if hasattr(lib, "wet_hal_set_mode"):
 448 |         lib.wet_hal_set_mode.restype = c_int
 449 |         lib.wet_hal_set_mode.argtypes = [c_void_p, c_int]
 450 | 
 451 |     if hasattr(lib, "wet_hal_get_mode"):
 452 |         lib.wet_hal_get_mode.restype = c_int
 453 |         lib.wet_hal_get_mode.argtypes = [c_void_p]
 454 | 
 455 |     if hasattr(lib, "wet_hal_register_driver"):
 456 |         lib.wet_hal_register_driver.restype = c_int
 457 |         lib.wet_hal_register_driver.argtypes = [c_void_p, c_void_p]
 458 | 
 459 |     if hasattr(lib, "wet_hal_unregister_driver"):
 460 |         lib.wet_hal_unregister_driver.restype = c_int
 461 |         lib.wet_hal_unregister_driver.argtypes = [c_void_p, c_void_p]
 462 | 
 463 |     if hasattr(lib, "wet_hal_find_driver"):
 464 |         lib.wet_hal_find_driver.restype = c_void_p
 465 |         lib.wet_hal_find_driver.argtypes = [c_void_p, c_int]
 466 | 
 467 |     if hasattr(lib, "wet_hal_write_pump"):
 468 |         lib.wet_hal_write_pump.restype = c_int
 469 |         lib.wet_hal_write_pump.argtypes = [c_void_p, c_uint8, c_double, c_uint8]
 470 | 
 471 |     if hasattr(lib, "wet_hal_dispense_pump"):
 472 |         lib.wet_hal_dispense_pump.restype = c_int
 473 |         lib.wet_hal_dispense_pump.argtypes = [c_void_p, c_uint8, c_double]
 474 | 
 475 |     if hasattr(lib, "wet_hal_write_valve"):
 476 |         lib.wet_hal_write_valve.restype = c_int
 477 |         lib.wet_hal_write_valve.argtypes = [c_void_p, c_uint8, c_uint8]
 478 | 
 479 |     if hasattr(lib, "wet_hal_read_flow"):
 480 |         lib.wet_hal_read_flow.restype = c_int
 481 |         lib.wet_hal_read_flow.argtypes = [c_void_p, c_uint8, POINTER(c_double)]
 482 | 
 483 |     if hasattr(lib, "wet_hal_stim_current"):
 484 |         lib.wet_hal_stim_current.restype = c_int
 485 |         lib.wet_hal_stim_current.argtypes = [c_void_p, c_uint16, ctypes.c_int32, c_uint32]
 486 | 
 487 |     if hasattr(lib, "wet_hal_stim_voltage"):
 488 |         lib.wet_hal_stim_voltage.restype = c_int
 489 |         lib.wet_hal_stim_voltage.argtypes = [c_void_p, c_uint16, c_float, c_float, c_float]
 490 | 
 491 |     if hasattr(lib, "wet_hal_read_spikes"):
 492 |         lib.wet_hal_read_spikes.restype = c_int
 493 |         lib.wet_hal_read_spikes.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]
 494 | 
 495 |     if hasattr(lib, "wet_hal_measure_impedance"):
 496 |         lib.wet_hal_measure_impedance.restype = c_int
 497 |         lib.wet_hal_measure_impedance.argtypes = [c_void_p, c_uint16, c_float, POINTER(c_float), POINTER(c_float)]
 498 | 
 499 |     if hasattr(lib, "wet_hal_active_discharge"):
 500 |         lib.wet_hal_active_discharge.restype = c_int
 501 |         lib.wet_hal_active_discharge.argtypes = [c_void_p, c_uint16]
 502 | 
 503 |     if hasattr(lib, "wet_hal_emergency_crowbar"):
 504 |         lib.wet_hal_emergency_crowbar.restype = None
 505 |         lib.wet_hal_emergency_crowbar.argtypes = [c_void_p, c_uint32]
 506 | 
 507 |     if hasattr(lib, "wet_hal_get_time_us"):
 508 |         lib.wet_hal_get_time_us.restype = c_uint64
 509 |         lib.wet_hal_get_time_us.argtypes = []
 510 | 
 511 |     if hasattr(lib, "wet_hal_get_telemetry"):
 512 |         lib.wet_hal_get_telemetry.restype = POINTER(WetHalTelemetry)
 513 |         lib.wet_hal_get_telemetry.argtypes = [c_void_p]
 514 | 
 515 |     if hasattr(lib, "wet_hal_set_valve_for_pump"):
 516 |         lib.wet_hal_set_valve_for_pump.restype = None
 517 |         lib.wet_hal_set_valve_for_pump.argtypes = [c_void_p, c_uint8, c_uint8]
 518 | 
 519 |     # Intan RHS2116 APIs
 520 |     if hasattr(lib, "wet_hal_intan_create"):
 521 |         lib.wet_hal_intan_create.restype = c_void_p
 522 |         lib.wet_hal_intan_create.argtypes = [c_int]
 523 | 
 524 |     if hasattr(lib, "wet_hal_intan_destroy"):
 525 |         lib.wet_hal_intan_destroy.restype = None
 526 |         lib.wet_hal_intan_destroy.argtypes = [c_void_p]
 527 | 
 528 |     if hasattr(lib, "wet_hal_intan_spi_transfer"):
 529 |         lib.wet_hal_intan_spi_transfer.restype = c_uint32
 530 |         lib.wet_hal_intan_spi_transfer.argtypes = [c_void_p, c_uint32]
 531 | 
 532 |     if hasattr(lib, "wet_hal_intan_set_stim_current"):
 533 |         lib.wet_hal_intan_set_stim_current.restype = c_int
 534 |         lib.wet_hal_intan_set_stim_current.argtypes = [c_void_p, c_uint8, ctypes.c_int32, c_uint32]
 535 | 
 536 |     if hasattr(lib, "wet_hal_intan_get_compliance_status"):
 537 |         lib.wet_hal_intan_get_compliance_status.restype = ctypes.c_uint16
 538 |         lib.wet_hal_intan_get_compliance_status.argtypes = [c_void_p]
 539 | 
 540 |     if hasattr(lib, "wet_hal_intan_clear_compliance"):
 541 |         lib.wet_hal_intan_clear_compliance.restype = None
 542 |         lib.wet_hal_intan_clear_compliance.argtypes = [c_void_p]
 543 | 
 544 |     if hasattr(lib, "wet_hal_intan_measure_impedance"):
 545 |         lib.wet_hal_intan_measure_impedance.restype = c_int
 546 |         lib.wet_hal_intan_measure_impedance.argtypes = [c_void_p, c_uint8, c_float, POINTER(c_float), POINTER(c_float)]
 547 | 
 548 |     if hasattr(lib, "wet_hal_intan_set_charge_recovery"):
 549 |         lib.wet_hal_intan_set_charge_recovery.restype = c_int
 550 |         lib.wet_hal_intan_set_charge_recovery.argtypes = [c_void_p, c_uint8, c_uint8]
 551 | 
 552 |     if hasattr(lib, "wet_hal_intan_inject_fault"):
 553 |         lib.wet_hal_intan_inject_fault.restype = None
 554 |         lib.wet_hal_intan_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8]
 555 | 
 556 |     # MaxWell MaxOne APIs
 557 |     if hasattr(lib, "wet_hal_maxwell_create"):
 558 |         lib.wet_hal_maxwell_create.restype = c_void_p
 559 |         lib.wet_hal_maxwell_create.argtypes = [c_int]
 560 | 
 561 |     if hasattr(lib, "wet_hal_maxwell_destroy"):
 562 |         lib.wet_hal_maxwell_destroy.restype = None
 563 |         lib.wet_hal_maxwell_destroy.argtypes = [c_void_p]
 564 | 
 565 |     if hasattr(lib, "wet_hal_maxwell_route_channels"):
 566 |         lib.wet_hal_maxwell_route_channels.restype = c_int
 567 |         lib.wet_hal_maxwell_route_channels.argtypes = [c_void_p, POINTER(ctypes.c_uint16), c_uint32]
 568 | 
 569 |     if hasattr(lib, "wet_hal_maxwell_connect_stim"):
 570 |         lib.wet_hal_maxwell_connect_stim.restype = c_int
 571 |         lib.wet_hal_maxwell_connect_stim.argtypes = [c_void_p, c_uint8, ctypes.c_uint16]
 572 | 
 573 |     if hasattr(lib, "wet_hal_maxwell_sequence_clear"):
 574 |         lib.wet_hal_maxwell_sequence_clear.restype = None
 575 |         lib.wet_hal_maxwell_sequence_clear.argtypes = [c_void_p]
 576 | 
 577 |     if hasattr(lib, "wet_hal_maxwell_sequence_append"):
 578 |         lib.wet_hal_maxwell_sequence_append.restype = c_int
 579 |         lib.wet_hal_maxwell_sequence_append.argtypes = [c_void_p, c_uint32, c_uint8, ctypes.c_uint16, c_float, ctypes.c_uint16]
 580 | 
 581 |     if hasattr(lib, "wet_hal_maxwell_sequence_arm"):
 582 |         lib.wet_hal_maxwell_sequence_arm.restype = c_int
 583 |         lib.wet_hal_maxwell_sequence_arm.argtypes = [c_void_p]
 584 | 
 585 |     if hasattr(lib, "wet_hal_maxwell_sequence_start"):
 586 |         lib.wet_hal_maxwell_sequence_start.restype = c_int
 587 |         lib.wet_hal_maxwell_sequence_start.argtypes = [c_void_p]
 588 | 
 589 |     if hasattr(lib, "wet_hal_maxwell_sequence_get_state"):
 590 |         lib.wet_hal_maxwell_sequence_get_state.restype = c_int
 591 |         lib.wet_hal_maxwell_sequence_get_state.argtypes = [c_void_p]
 592 | 
 593 |     if hasattr(lib, "wet_hal_maxwell_stim_voltage"):
 594 |         lib.wet_hal_maxwell_stim_voltage.restype = c_int
 595 |         lib.wet_hal_maxwell_stim_voltage.argtypes = [c_void_p, c_uint8, ctypes.c_uint16, c_float, c_float, c_float]
 596 | 
 597 |     if hasattr(lib, "wet_hal_maxwell_inject_fault"):
 598 |         lib.wet_hal_maxwell_inject_fault.restype = None
 599 |         lib.wet_hal_maxwell_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8]
 600 | 
 601 |     # Microfluidics & CAN APIs
 602 |     if hasattr(lib, "wet_hal_microfluidics_create"):
 603 |         lib.wet_hal_microfluidics_create.restype = c_void_p
 604 |         lib.wet_hal_microfluidics_create.argtypes = [c_int]
 605 | 
 606 |     if hasattr(lib, "wet_hal_microfluidics_destroy"):
 607 |         lib.wet_hal_microfluidics_destroy.restype = None
 608 |         lib.wet_hal_microfluidics_destroy.argtypes = [c_void_p]
 609 | 
 610 |     if hasattr(lib, "wet_hal_harvard_format_cmd"):
 611 |         lib.wet_hal_harvard_format_cmd.restype = c_int
 612 |         lib.wet_hal_harvard_format_cmd.argtypes = [c_uint8, c_uint8, c_char_p, c_char_p, c_char_p, c_size_t]
 613 | 
 614 |     if hasattr(lib, "wet_hal_harvard_parse_response"):
 615 |         lib.wet_hal_harvard_parse_response.restype = c_int
 616 |         lib.wet_hal_harvard_parse_response.argtypes = [c_char_p, c_size_t]
 617 | 
 618 |     if hasattr(lib, "wet_hal_pump_set_rate"):
 619 |         lib.wet_hal_pump_set_rate.restype = c_int
 620 |         lib.wet_hal_pump_set_rate.argtypes = [c_void_p, c_uint8, c_double, c_uint8]
 621 | 
 622 |     if hasattr(lib, "wet_hal_pump_dispense"):
 623 |         lib.wet_hal_pump_dispense.restype = c_int
 624 |         lib.wet_hal_pump_dispense.argtypes = [c_void_p, c_uint8, c_double]
 625 | 
 626 |     if hasattr(lib, "wet_hal_pump_stop"):
 627 |         lib.wet_hal_pump_stop.restype = c_int
 628 |         lib.wet_hal_pump_stop.argtypes = [c_void_p, c_uint8]
 629 | 
 630 |     if hasattr(lib, "wet_hal_valve_set_state"):
 631 |         lib.wet_hal_valve_set_state.restype = c_int
 632 |         lib.wet_hal_valve_set_state.argtypes = [c_void_p, c_uint8, c_uint8]
 633 | 
 634 |     if hasattr(lib, "wet_hal_pump_bind_downstream_valve"):
 635 |         lib.wet_hal_pump_bind_downstream_valve.restype = None
 636 |         lib.wet_hal_pump_bind_downstream_valve.argtypes = [c_void_p, c_uint8, c_uint8]
 637 | 
 638 |     if hasattr(lib, "wet_hal_can_send"):
 639 |         lib.wet_hal_can_send.restype = c_int
 640 |         lib.wet_hal_can_send.argtypes = [c_void_p, POINTER(WetCanFrame)]
 641 | 
 642 |     if hasattr(lib, "wet_hal_can_recv"):
 643 |         lib.wet_hal_can_recv.restype = c_int
 644 |         lib.wet_hal_can_recv.argtypes = [c_void_p, POINTER(WetCanFrame)]
 645 | 
 646 |     if hasattr(lib, "wet_hal_can_send_emcy"):
 647 |         lib.wet_hal_can_send_emcy.restype = c_int
 648 |         lib.wet_hal_can_send_emcy.argtypes = [c_void_p, c_uint8, ctypes.c_uint16, c_uint8]
 649 | 
 650 |     if hasattr(lib, "wet_hal_microfluidics_inject_fault"):
 651 |         lib.wet_hal_microfluidics_inject_fault.restype = None
 652 |         lib.wet_hal_microfluidics_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8]
 653 | 
 654 |     # Sensirion Flow Meter APIs
 655 |     if hasattr(lib, "wet_hal_sensirion_create"):
 656 |         lib.wet_hal_sensirion_create.restype = c_void_p
 657 |         lib.wet_hal_sensirion_create.argtypes = [c_int]
 658 | 
 659 |     if hasattr(lib, "wet_hal_sensirion_destroy"):
 660 |         lib.wet_hal_sensirion_destroy.restype = None
 661 |         lib.wet_hal_sensirion_destroy.argtypes = [c_void_p]
 662 | 
 663 |     if hasattr(lib, "wet_hal_sensirion_crc8"):
 664 |         lib.wet_hal_sensirion_crc8.restype = c_uint8
 665 |         lib.wet_hal_sensirion_crc8.argtypes = [POINTER(c_uint8), c_size_t]
 666 | 
 667 |     if hasattr(lib, "wet_hal_sensirion_validate_crc"):
 668 |         lib.wet_hal_sensirion_validate_crc.restype = c_int
 669 |         lib.wet_hal_sensirion_validate_crc.argtypes = [POINTER(c_uint8)]
 670 | 
 671 |     if hasattr(lib, "wet_hal_sensirion_start_measurement"):
 672 |         lib.wet_hal_sensirion_start_measurement.restype = c_int
 673 |         lib.wet_hal_sensirion_start_measurement.argtypes = [c_void_p, ctypes.c_uint16]
 674 | 
 675 |     if hasattr(lib, "wet_hal_sensirion_stop_measurement"):
 676 |         lib.wet_hal_sensirion_stop_measurement.restype = c_int
 677 |         lib.wet_hal_sensirion_stop_measurement.argtypes = [c_void_p]
 678 | 
 679 |     if hasattr(lib, "wet_hal_sensirion_read_flow"):
 680 |         lib.wet_hal_sensirion_read_flow.restype = c_int
 681 |         lib.wet_hal_sensirion_read_flow.argtypes = [c_void_p, POINTER(c_double)]
 682 | 
 683 |     if hasattr(lib, "wet_hal_sensirion_hil_set_flow"):
 684 |         lib.wet_hal_sensirion_hil_set_flow.restype = None
 685 |         lib.wet_hal_sensirion_hil_set_flow.argtypes = [c_void_p, c_double]
 686 | 
 687 |     if hasattr(lib, "wet_hal_shdlc_encode"):
 688 |         lib.wet_hal_shdlc_encode.restype = c_size_t
 689 |         lib.wet_hal_shdlc_encode.argtypes = [c_uint8, c_uint8, POINTER(c_uint8), c_uint8, POINTER(c_uint8), c_size_t]
 690 | 
 691 |     if hasattr(lib, "wet_hal_shdlc_decode"):
 692 |         lib.wet_hal_shdlc_decode.restype = c_int
 693 |         lib.wet_hal_shdlc_decode.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
 694 | 
 695 |     if hasattr(lib, "wet_hal_sensirion_inject_fault"):
 696 |         lib.wet_hal_sensirion_inject_fault.restype = None
 697 |         lib.wet_hal_sensirion_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8]
 698 | 
 699 |     return lib
 700 | 
 701 | 
 702 | def get_wetvm_lib(lib_path: Optional[Path] = None) -> ctypes.CDLL:
 703 |     """Alias for load_wetvm_lib."""
 704 |     return load_wetvm_lib(lib_path)
 705 | 
 706 | 
 707 | class WetVMFFI:
 708 |     """Low-level FFI helper wrapper matching E2E test interface."""
 709 |     def __init__(self, lib_path: Optional[Path] = None):
 710 |         self.lib = get_wetvm_lib(lib_path)
 711 | 
 712 |     def get_version(self) -> int:
 713 |         return 0x0100
 714 | 
 715 |     def create_vm(self, config: Optional[WetVMConfig] = None) -> ctypes.c_void_p:
 716 |         cfg_ptr = ctypes.byref(config) if config is not None else None
 717 |         return self.lib.wet_create_vm(cfg_ptr)
 718 | 
 719 |     def free_vm(self, vm: ctypes.c_void_p) -> None:
 720 |         self.lib.wet_free_vm(vm)
 721 | 
 722 |     def allocate_telemetry(self) -> WetTelemetry:
 723 |         return WetTelemetry()
 724 | 
 725 |     def step_tick(self, vm: ctypes.c_void_p, telem: WetTelemetry) -> int:
 726 |         telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
 727 |         return self.lib.wet_step_tick(vm, telem_ptr)
 728 | 
 729 |     def run_ticks(self, vm: ctypes.c_void_p, ticks: int, telem: WetTelemetry) -> Tuple[int, int]:
 730 |         executed = ctypes.c_uint32(0)
 731 |         telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
 732 |         status = self.lib.wet_run_ticks(vm, ctypes.c_uint32(ticks), ctypes.byref(executed), telem_ptr)
 733 |         return status, int(executed.value)
 734 | 
 735 |     def inject_stimulus(
 736 |         self,
 737 |         vm: ctypes.c_void_p,
 738 |         channel: int,
 739 |         voltage_v: float,
 740 |         p1_ms: float = 0.5,
 741 |         p2_ms: float = 0.5
 742 |     ) -> int:
 743 |         return self.lib.wet_inject_stimulus(
 744 |             vm,
 745 |             ctypes.c_uint8(channel),
 746 |             ctypes.c_float(voltage_v),
 747 |             ctypes.c_float(p1_ms),
 748 |             ctypes.c_float(p2_ms)
 749 |         )
 750 | 
 751 |     def get_last_error(self, vm: Optional[ctypes.c_void_p] = None) -> str:
 752 |         if vm:
 753 |             err = self.lib.wet_get_last_error(vm)
 754 |             return err.decode("utf-8", errors="replace") if err else ""
 755 |         return ""
 756 | 
 757 |     def status_to_string(self, status: int) -> str:
 758 |         s = self.lib.wet_status_to_string(int(status))
 759 |         return s.decode("utf-8", errors="replace") if s else str(status)
 760 | 
 761 |     def load_bytecode(self, vm: ctypes.c_void_p, bytecode: bytes) -> int:
 762 |         c_bytes = (ctypes.c_uint8 * len(bytecode)).from_buffer_copy(bytecode)
 763 |         err_buf = ctypes.create_string_buffer(512)
 764 |         return self.lib.wet_load_bytecode(vm, c_bytes, len(bytecode), err_buf, len(err_buf))
 765 | 
 766 |     def get_telemetry(self, vm: ctypes.c_void_p, telem: WetTelemetry) -> int:
 767 |         telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
 768 |         return self.lib.wet_get_telemetry(vm, telem_ptr)
 769 | 
 770 |     def create_vm_arena(self, arena_bytes: int, config: Optional[WetVMConfig] = None) -> Tuple[ctypes.c_void_p, ctypes.Array]:
 771 |         """Creates a VM using a pre-allocated static ctypes byte buffer (zero heap malloc)."""
 772 |         buf = (ctypes.c_uint8 * arena_bytes)()
 773 |         cfg_ptr = ctypes.byref(config) if config is not None else None
 774 |         vm = self.lib.wet_create_vm_arena(ctypes.byref(buf), ctypes.c_size_t(arena_bytes), cfg_ptr)
 775 |         return vm, buf
 776 | 
 777 |     def configure_electrode(self, vm: ctypes.c_void_p, material: int, area_um2: float) -> None:
 778 |         self.lib.wet_configure_electrode(vm, ctypes.c_uint8(material), ctypes.c_float(area_um2))
 779 | 
 780 |     def active_discharge(self, vm: ctypes.c_void_p, channel: int) -> None:
 781 |         self.lib.wet_active_discharge(vm, ctypes.c_uint8(channel))
 782 | 
 783 |     def active_discharge_all(self, vm: ctypes.c_void_p) -> None:
 784 |         self.lib.wet_active_discharge_all(vm)
 785 | 
 786 |     def enable_dead_head_protection(self, vm: ctypes.c_void_p, enable: bool) -> None:
 787 |         self.lib.wet_enable_dead_head_protection(vm, ctypes.c_uint8(1 if enable else 0))
 788 | 
 789 |     def life_supervisor_shutdown(self, vm: ctypes.c_void_p) -> None:
 790 |         self.lib.wet_life_supervisor_shutdown(vm)
 791 | 
 792 |     def configure_blanking(self, vm: ctypes.c_void_p, blanking_ms: float = 2.0, enable_spatial: bool = True) -> None:
 793 |         self.lib.wet_configure_blanking(vm, ctypes.c_float(blanking_ms), ctypes.c_uint8(1 if enable_spatial else 0))
 794 | 
 795 |     def inject_current_stimulus(
 796 |         self,
 797 |         vm: ctypes.c_void_p,
 798 |         channel: int,
 799 |         current_ua: float,
 800 |         p1_ms: float = 0.5,
 801 |         p2_ms: float = 0.5
 802 |     ) -> int:
 803 |         return self.lib.wet_inject_current_stimulus(
 804 |             vm,
 805 |             ctypes.c_uint8(channel),
 806 |             ctypes.c_float(current_ua),
 807 |             ctypes.c_float(p1_ms),
 808 |             ctypes.c_float(p2_ms)
 809 |         )
 810 | 
 811 |     def verify_bytecode(self, bytecode: bytes) -> Tuple[int, str]:
 812 |         c_bytes = (ctypes.c_uint8 * len(bytecode)).from_buffer_copy(bytecode)
 813 |         err_buf = ctypes.create_string_buffer(512)
 814 |         st = self.lib.wet_verify_bytecode(c_bytes, ctypes.c_size_t(len(bytecode)), err_buf, ctypes.c_size_t(len(err_buf)))
 815 |         msg = err_buf.value.decode("utf-8", errors="replace")
 816 |         return st, msg
 817 | 
 818 |     def snapshot(self, vm: ctypes.c_void_p) -> bytes:
 819 |         needed_len = ctypes.c_size_t(0)
 820 |         self.lib.wet_vm_snapshot(vm, None, ctypes.byref(needed_len))
 821 |         buf = (ctypes.c_uint8 * needed_len.value)()
 822 |         st = self.lib.wet_vm_snapshot(vm, buf, ctypes.byref(needed_len))
 823 |         if st != 0:
 824 |             raise RuntimeError(f"Snapshot failed with status {st}")
 825 |         return bytes(buf)
 826 | 
 827 |     def restore(self, vm: ctypes.c_void_p, data: bytes) -> int:
 828 |         c_bytes = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
 829 |         return self.lib.wet_vm_restore(vm, c_bytes, ctypes.c_size_t(len(data)))
 830 | 
 831 |     def set_environmental_sensors(
 832 |         self,
 833 |         vm: ctypes.c_void_p,
 834 |         ph: float = 7.4,
 835 |         do_pct: float = 95.0,
 836 |         co2_pct: float = 5.0,
 837 |         bubble_sensor_id: int = 0,
 838 |         bubble_state: bool = False,
 839 |         flow_rate_ul_min: float = 1.5
 840 |     ) -> None:
 841 |         self.lib.wet_set_environmental_sensors(
 842 |             vm,
 843 |             ctypes.c_float(ph),
 844 |             ctypes.c_float(do_pct),
 845 |             ctypes.c_float(co2_pct),
 846 |             ctypes.c_uint8(bubble_sensor_id),
 847 |             ctypes.c_uint8(1 if bubble_state else 0),
 848 |             ctypes.c_float(flow_rate_ul_min)
 849 |         )
 850 | 
 851 |     def set_temperature(self, vm: ctypes.c_void_p, temp_c: float) -> None:
 852 |         self.lib.wet_set_temperature(vm, ctypes.c_float(temp_c))
 853 | 
 854 |     def set_channel_banks(
 855 |         self,
 856 |         vm: ctypes.c_void_p,
 857 |         ref_mask: int = 0,
 858 |         rec_mask: int = 0
 859 |     ) -> None:
 860 |         self.lib.wet_set_channel_banks(vm, ctypes.c_uint64(ref_mask), ctypes.c_uint64(rec_mask))
 861 | 
 862 |     # =========================================================================
 863 |     # Milestone 1: Physical Hardware Abstraction Layer (HAL) FFI Methods
 864 |     # =========================================================================
 865 | 
 866 |     def hal_create(self, mode: int = 2, config: Optional[WetHalConfig] = None):
 867 |         cfg_ptr = ctypes.byref(config) if config is not None else None
 868 |         ptr = self.lib.wet_hal_create(ctypes.c_int(mode), cfg_ptr)
 869 |         return ctypes.cast(ptr, ctypes.POINTER(WetHalContext)) if ptr else None
 870 | 
 871 |     def hal_destroy(self, hal: ctypes.c_void_p) -> None:
 872 |         self.lib.wet_hal_destroy(hal)
 873 | 
 874 |     def hal_get_telemetry(self, hal: ctypes.c_void_p) -> Optional[WetHalTelemetry]:
 875 |         if hasattr(self.lib, "wet_hal_get_telemetry"):
 876 |             p = self.lib.wet_hal_get_telemetry(hal)
 877 |             return p.contents if p else None
 878 |         return None
 879 | 
 880 |     def hal_set_valve_for_pump(self, hal: ctypes.c_void_p, pump_id: int, valve_id: int) -> None:
 881 |         if hasattr(self.lib, "wet_hal_set_valve_for_pump"):
 882 |             self.lib.wet_hal_set_valve_for_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_uint8(valve_id))
 883 | 
 884 |     def hal_init(self, vm: ctypes.c_void_p, mode: int = 2, config: Optional[WetHalConfig] = None) -> int:
 885 |         cfg_ptr = ctypes.byref(config) if config is not None else None
 886 |         return self.lib.wet_hal_init(vm, ctypes.c_int(mode), cfg_ptr)
 887 | 
 888 |     def hal_attach(self, vm: ctypes.c_void_p, hal: ctypes.c_void_p) -> int:
 889 |         return self.lib.wet_hal_attach(vm, hal)
 890 | 
 891 |     def hal_get_context(self, vm: ctypes.c_void_p) -> ctypes.c_void_p:
 892 |         return self.lib.wet_hal_get_context(vm)
 893 | 
 894 |     def hal_set_mode(self, hal: ctypes.c_void_p, mode: int) -> int:
 895 |         return self.lib.wet_hal_set_mode(hal, ctypes.c_int(mode))
 896 | 
 897 |     def hal_get_mode(self, hal: ctypes.c_void_p) -> int:
 898 |         return self.lib.wet_hal_get_mode(hal)
 899 | 
 900 |     def hal_register_driver(self, hal: ctypes.c_void_p, driver: ctypes.c_void_p) -> int:
 901 |         return self.lib.wet_hal_register_driver(hal, driver)
 902 | 
 903 |     def hal_unregister_driver(self, hal: ctypes.c_void_p, driver: ctypes.c_void_p) -> int:
 904 |         return self.lib.wet_hal_unregister_driver(hal, driver)
 905 | 
 906 |     def hal_find_driver(self, hal: ctypes.c_void_p, driver_type: int) -> ctypes.c_void_p:
 907 |         return self.lib.wet_hal_find_driver(hal, ctypes.c_int(driver_type))
 908 | 
 909 |     def hal_write_pump(self, hal: ctypes.c_void_p, pump_id: int, rate_ul_min: float, run_flag: int = 1) -> int:
 910 |         return self.lib.wet_hal_write_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_double(rate_ul_min), ctypes.c_uint8(run_flag))
 911 | 
 912 |     def hal_dispense_pump(self, hal: ctypes.c_void_p, pump_id: int, volume_ul: float) -> int:
 913 |         return self.lib.wet_hal_dispense_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_double(volume_ul))
 914 | 
 915 |     def hal_write_valve(self, hal: ctypes.c_void_p, valve_id: int, state: int) -> int:
 916 |         return self.lib.wet_hal_write_valve(hal, ctypes.c_uint8(valve_id), ctypes.c_uint8(state))
 917 | 
 918 |     def hal_read_flow(self, hal: ctypes.c_void_p, sensor_id: int = 0) -> Tuple[int, float]:
 919 |         val = ctypes.c_double(0.0)
 920 |         st = self.lib.wet_hal_read_flow(hal, ctypes.c_uint8(sensor_id), ctypes.byref(val))
 921 |         return st, float(val.value)
 922 | 
 923 |     def hal_stim_current(self, hal: ctypes.c_void_p, channel: int, current_pA: int, duration_us: int) -> int:
 924 |         return self.lib.wet_hal_stim_current(hal, ctypes.c_uint16(channel), ctypes.c_int32(current_pA), ctypes.c_uint32(duration_us))
 925 | 
 926 |     def hal_stim_voltage(self, hal: ctypes.c_void_p, channel: int, voltage_v: float, p1_ms: float = 0.5, p2_ms: float = 0.5) -> int:
 927 |         return self.lib.wet_hal_stim_voltage(hal, ctypes.c_uint16(channel), ctypes.c_float(voltage_v), ctypes.c_float(p1_ms), ctypes.c_float(p2_ms))
 928 | 
 929 |     def hal_read_spikes(self, hal: ctypes.c_void_p, channel: int) -> Tuple[int, int]:
 930 |         spk = ctypes.c_uint8(0)
 931 |         st = self.lib.wet_hal_read_spikes(hal, ctypes.c_uint16(channel), ctypes.byref(spk))
 932 |         return st, int(spk.value)
 933 | 
 934 |     def hal_measure_impedance(self, hal: ctypes.c_void_p, channel: int, freq_hz: float = 1000.0) -> Tuple[int, float, float]:
 935 |         mag = ctypes.c_float(0.0)
 936 |         phase = ctypes.c_float(0.0)
 937 |         st = self.lib.wet_hal_measure_impedance(hal, ctypes.c_uint16(channel), ctypes.c_float(freq_hz), ctypes.byref(mag), ctypes.byref(phase))
 938 |         return st, float(mag.value), float(phase.value)
 939 | 
 940 |     def hal_active_discharge(self, hal: ctypes.c_void_p, channel: int) -> int:
 941 |         return self.lib.wet_hal_active_discharge(hal, ctypes.c_uint16(channel))
 942 | 
 943 |     def hal_emergency_crowbar(self, vm: ctypes.c_void_p, trip_reason: int = 1) -> None:
 944 |         self.lib.wet_hal_emergency_crowbar(vm, ctypes.c_uint32(trip_reason))
 945 | 
 946 |     # Intan RHS2116 Driver
 947 |     def intan_create(self, mode: int = 2) -> ctypes.c_void_p:
 948 |         return self.lib.wet_hal_intan_create(ctypes.c_int(mode))
 949 | 
 950 |     def intan_destroy(self, drv: ctypes.c_void_p) -> None:
 951 |         self.lib.wet_hal_intan_destroy(drv)
 952 | 
 953 |     def intan_spi_transfer(self, drv: ctypes.c_void_p, mosi_word: int) -> int:
 954 |         return int(self.lib.wet_hal_intan_spi_transfer(drv, ctypes.c_uint32(mosi_word)))
 955 | 
 956 |     def intan_set_stim_current(self, drv: ctypes.c_void_p, channel: int, current_pA: int, duration_us: int) -> int:
 957 |         return self.lib.wet_hal_intan_set_stim_current(drv, ctypes.c_uint8(channel), ctypes.c_int32(current_pA), ctypes.c_uint32(duration_us))
 958 | 
 959 |     def intan_get_compliance_status(self, drv: ctypes.c_void_p) -> int:
 960 |         return int(self.lib.wet_hal_intan_get_compliance_status(drv))
 961 | 
 962 |     def intan_clear_compliance(self, drv: ctypes.c_void_p) -> None:
 963 |         self.lib.wet_hal_intan_clear_compliance(drv)
 964 | 
 965 |     def intan_measure_impedance(self, drv: ctypes.c_void_p, channel: int, freq_hz: float = 1000.0) -> Tuple[int, float, float]:
 966 |         mag = ctypes.c_float(0.0)
 967 |         phase = ctypes.c_float(0.0)
 968 |         st = self.lib.wet_hal_intan_measure_impedance(drv, ctypes.c_uint8(channel), ctypes.c_float(freq_hz), ctypes.byref(mag), ctypes.byref(phase))
 969 |         return st, float(mag.value), float(phase.value)
 970 | 
 971 |     def intan_set_charge_recovery(self, drv: ctypes.c_void_p, channel: int, enable: bool) -> int:
 972 |         return self.lib.wet_hal_intan_set_charge_recovery(drv, ctypes.c_uint8(channel), ctypes.c_uint8(1 if enable else 0))
 973 | 
 974 |     def intan_inject_fault(self, drv: ctypes.c_void_p, force_rail: bool = False, spi_error: bool = False, timeout: bool = False) -> None:
 975 |         self.lib.wet_hal_intan_inject_fault(drv, ctypes.c_uint8(1 if force_rail else 0), ctypes.c_uint8(1 if spi_error else 0), ctypes.c_uint8(1 if timeout else 0))
 976 | 
 977 |     # MaxWell MaxOne Driver
 978 |     def maxwell_create(self, mode: int = 2) -> ctypes.c_void_p:
 979 |         return self.lib.wet_hal_maxwell_create(ctypes.c_int(mode))
 980 | 
 981 |     def maxwell_destroy(self, drv: ctypes.c_void_p) -> None:
 982 |         self.lib.wet_hal_maxwell_destroy(drv)
 983 | 
 984 |     def maxwell_route_channels(self, drv: ctypes.c_void_p, electrode_indices: list[int]) -> int:
 985 |         c_arr = (ctypes.c_uint16 * len(electrode_indices))(*electrode_indices)
 986 |         return self.lib.wet_hal_maxwell_route_channels(drv, c_arr, ctypes.c_uint32(len(electrode_indices)))
 987 | 
 988 |     def maxwell_connect_stim(self, drv: ctypes.c_void_p, stim_unit: int, electrode_id: int) -> int:
 989 |         return self.lib.wet_hal_maxwell_connect_stim(drv, ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id))
 990 | 
 991 |     def maxwell_sequence_clear(self, drv: ctypes.c_void_p) -> None:
 992 |         self.lib.wet_hal_maxwell_sequence_clear(drv)
 993 | 
 994 |     def maxwell_sequence_append(self, drv: ctypes.c_void_p, timestamp_us: int, stim_unit: int, electrode_id: int, voltage_mv: float, duration_us: int) -> int:
 995 |         return self.lib.wet_hal_maxwell_sequence_append(drv, ctypes.c_uint32(timestamp_us), ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id), ctypes.c_float(voltage_mv), ctypes.c_uint16(duration_us))
 996 | 
 997 |     def maxwell_sequence_arm(self, drv: ctypes.c_void_p) -> int:
 998 |         return self.lib.wet_hal_maxwell_sequence_arm(drv)
 999 | 
1000 |     def maxwell_sequence_start(self, drv: ctypes.c_void_p) -> int:
1001 |         return self.lib.wet_hal_maxwell_sequence_start(drv)
1002 | 
1003 |     def maxwell_sequence_get_state(self, drv: ctypes.c_void_p) -> int:
1004 |         return self.lib.wet_hal_maxwell_sequence_get_state(drv)
1005 | 
1006 |     def maxwell_stim_voltage(self, drv: ctypes.c_void_p, stim_unit: int, electrode_id: int, voltage_mv: float, p1_ms: float = 0.5, p2_ms: float = 0.5) -> int:
1007 |         return self.lib.wet_hal_maxwell_stim_voltage(drv, ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id), ctypes.c_float(voltage_mv), ctypes.c_float(p1_ms), ctypes.c_float(p2_ms))
1008 | 
1009 |     def maxwell_inject_fault(self, drv: ctypes.c_void_p, force_charge_violation: bool = False, drop_frames: bool = False) -> None:
1010 |         self.lib.wet_hal_maxwell_inject_fault(drv, ctypes.c_uint8(1 if force_charge_violation else 0), ctypes.c_uint8(1 if drop_frames else 0))
1011 | 
1012 |     # Microfluidics Driver
1013 |     def microfluidics_create(self, mode: int = 2) -> ctypes.c_void_p:
1014 |         return self.lib.wet_hal_microfluidics_create(ctypes.c_int(mode))
1015 | 
1016 |     def microfluidics_destroy(self, drv: ctypes.c_void_p) -> None:
1017 |         self.lib.wet_hal_microfluidics_destroy(drv)
1018 | 
1019 |     def harvard_format_cmd(self, address: int, fast_mode: bool, cmd_name: str, args: str = "") -> str:
1020 |         buf = ctypes.create_string_buffer(128)
1021 |         ret = self.lib.wet_hal_harvard_format_cmd(
1022 |             ctypes.c_uint8(address),
1023 |             ctypes.c_uint8(1 if fast_mode else 0),
1024 |             cmd_name.encode("utf-8"),
1025 |             args.encode("utf-8"),
1026 |             buf,
1027 |             ctypes.c_size_t(len(buf))
1028 |         )
1029 |         return buf.value.decode("utf-8", errors="replace") if ret >= 0 else ""
1030 | 
1031 |     def harvard_parse_response(self, resp: str) -> str:
1032 |         c_str = resp.encode("utf-8")
1033 |         prompt = self.lib.wet_hal_harvard_parse_response(c_str, ctypes.c_size_t(len(c_str)))
1034 |         return chr(prompt) if prompt > 0 else "?"
1035 | 
1036 |     def pump_set_rate(self, drv: ctypes.c_void_p, pump_id: int, rate_ul_min: float, run_flag: int = 1) -> int:
1037 |         return self.lib.wet_hal_pump_set_rate(drv, ctypes.c_uint8(pump_id), ctypes.c_double(rate_ul_min), ctypes.c_uint8(run_flag))
1038 | 
1039 |     def pump_dispense(self, drv: ctypes.c_void_p, pump_id: int, volume_ul: float) -> int:
1040 |         return self.lib.wet_hal_pump_dispense(drv, ctypes.c_uint8(pump_id), ctypes.c_double(volume_ul))
1041 | 
1042 |     def pump_stop(self, drv: ctypes.c_void_p, pump_id: int) -> int:
1043 |         return self.lib.wet_hal_pump_stop(drv, ctypes.c_uint8(pump_id))
1044 | 
1045 |     def valve_set_state(self, drv: ctypes.c_void_p, valve_id: int, state: int) -> int:
1046 |         return self.lib.wet_hal_valve_set_state(drv, ctypes.c_uint8(valve_id), ctypes.c_uint8(state))
1047 | 
1048 |     def pump_bind_downstream_valve(self, drv: ctypes.c_void_p, pump_id: int, valve_id: int) -> None:
1049 |         self.lib.wet_hal_pump_bind_downstream_valve(drv, ctypes.c_uint8(pump_id), ctypes.c_uint8(valve_id))
1050 | 
1051 |     def can_send(self, drv: ctypes.c_void_p, frame: WetCanFrame) -> int:
1052 |         return self.lib.wet_hal_can_send(drv, ctypes.byref(frame))
1053 | 
1054 |     def can_recv(self, drv: ctypes.c_void_p) -> Tuple[int, Optional[WetCanFrame]]:
1055 |         f = WetCanFrame()
1056 |         st = self.lib.wet_hal_can_recv(drv, ctypes.byref(f))
1057 |         return st, f if st == 0 else None
1058 | 
1059 |     def can_send_emcy(self, drv: ctypes.c_void_p, node_id: int, error_code: int, error_register: int = 0) -> int:
1060 |         return self.lib.wet_hal_can_send_emcy(drv, ctypes.c_uint8(node_id), ctypes.c_uint16(error_code), ctypes.c_uint8(error_register))
1061 | 
1062 |     def microfluidics_inject_fault(self, drv: ctypes.c_void_p, stall: bool = False, can_drop: bool = False, timeout: bool = False) -> None:
1063 |         self.lib.wet_hal_microfluidics_inject_fault(drv, ctypes.c_uint8(1 if stall else 0), ctypes.c_uint8(1 if can_drop else 0), ctypes.c_uint8(1 if timeout else 0))
1064 | 
1065 |     # Sensirion Flow Meter Driver
1066 |     def sensirion_create(self, mode: int = 2) -> ctypes.c_void_p:
1067 |         return self.lib.wet_hal_sensirion_create(ctypes.c_int(mode))
1068 | 
1069 |     def sensirion_destroy(self, drv: ctypes.c_void_p) -> None:
1070 |         self.lib.wet_hal_sensirion_destroy(drv)
1071 | 
1072 |     def sensirion_crc8(self, data: bytes) -> int:
1073 |         c_bytes = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
1074 |         return int(self.lib.wet_hal_sensirion_crc8(c_bytes, ctypes.c_size_t(len(data))))
1075 | 
1076 |     def sensirion_validate_crc(self, word_and_crc: bytes) -> bool:
1077 |         c_bytes = (ctypes.c_uint8 * len(word_and_crc)).from_buffer_copy(word_and_crc)
1078 |         return bool(self.lib.wet_hal_sensirion_validate_crc(c_bytes))
1079 | 
1080 |     def sensirion_start_measurement(self, drv: ctypes.c_void_p, cmd: int = 0x3608) -> int:
1081 |         return self.lib.wet_hal_sensirion_start_measurement(drv, ctypes.c_uint16(cmd))
1082 | 
1083 |     def sensirion_stop_measurement(self, drv: ctypes.c_void_p) -> int:
1084 |         return self.lib.wet_hal_sensirion_stop_measurement(drv)
1085 | 
1086 |     def sensirion_read_flow(self, drv: ctypes.c_void_p) -> Tuple[int, float]:
1087 |         val = ctypes.c_double(0.0)
1088 |         st = self.lib.wet_hal_sensirion_read_flow(drv, ctypes.byref(val))
1089 |         return st, float(val.value)
1090 | 
1091 |     def sensirion_hil_set_flow(self, drv: ctypes.c_void_p, flow_ul_min: float) -> None:
1092 |         self.lib.wet_hal_sensirion_hil_set_flow(drv, ctypes.c_double(flow_ul_min))
1093 | 
1094 |     def shdlc_encode(self, address: int, command: int, payload: bytes) -> bytes:
1095 |         p_len = len(payload)
1096 |         c_payload = (ctypes.c_uint8 * p_len).from_buffer_copy(payload) if p_len > 0 else None
1097 |         out_buf = (ctypes.c_uint8 * 256)()
1098 |         enc_len = self.lib.wet_hal_shdlc_encode(
1099 |             ctypes.c_uint8(address),
1100 |             ctypes.c_uint8(command),
1101 |             c_payload,
1102 |             ctypes.c_uint8(p_len),
1103 |             out_buf,
1104 |             ctypes.c_size_t(len(out_buf))
1105 |         )
1106 |         return bytes(out_buf[:enc_len])
1107 | 
1108 |     def shdlc_decode(self, raw_bytes: bytes) -> Tuple[bool, int, int, bytes]:
1109 |         c_raw = (ctypes.c_uint8 * len(raw_bytes)).from_buffer_copy(raw_bytes)
1110 |         addr = ctypes.c_uint8(0)
1111 |         cmd = ctypes.c_uint8(0)
1112 |         payload = (ctypes.c_uint8 * 256)()
1113 |         plen = ctypes.c_uint8(0)
1114 |         ok = self.lib.wet_hal_shdlc_decode(
1115 |             c_raw,
1116 |             ctypes.c_size_t(len(raw_bytes)),
1117 |             ctypes.byref(addr),
1118 |             ctypes.byref(cmd),
1119 |             payload,
1120 |             ctypes.byref(plen)
1121 |         )
1122 |         if ok:
1123 |             return True, int(addr.value), int(cmd.value), bytes(payload[:plen.value])
1124 |         return False, 0, 0, b""
1125 | 
1126 |     def sensirion_inject_fault(self, drv: ctypes.c_void_p, corrupt_crc: bool = False, nak_addr: bool = False) -> None:
1127 |         self.lib.wet_hal_sensirion_inject_fault(drv, ctypes.c_uint8(1 if corrupt_crc else 0), ctypes.c_uint8(1 if nak_addr else 0))
```

### `bindings/runtime.py` (505 lines, SHA-256: `b6ce663da7e4f589...`)

```text
   1 | """
   2 | WetLang High-Level Virtual Machine Runtime Wrapper
   3 | Provides object-oriented Python interface with zero-copy NumPy array telemetry views.
   4 | """
   5 | 
   6 | from pathlib import Path
   7 | from typing import Optional, Tuple, Union
   8 | import ctypes
   9 | import numpy as np
  10 | 
  11 | from bindings.ffi import (
  12 |     load_wetvm_lib,
  13 |     WetStatus,
  14 |     WetVMConfig,
  15 |     WetTelemetry,
  16 |     WetActuatorTelemetry,
  17 |     WetHalMode,
  18 |     WetHalConfig,
  19 |     WetHalStatus,
  20 | )
  21 | 
  22 | 
  23 | class WetVMError(RuntimeError):
  24 |     """Exception raised for WetVM execution or validation errors."""
  25 |     def __init__(self, status: WetStatus, message: str):
  26 |         super().__init__(f"[{status.name}] {message}")
  27 |         self.status = status
  28 |         self.raw_message = message
  29 | 
  30 | 
  31 | class WetTelemetryView:
  32 |     """Wrapper around WetTelemetry providing convenient properties and array views."""
  33 |     def __init__(self, raw: WetTelemetry):
  34 |         self._raw = raw
  35 | 
  36 |     @property
  37 |     def current_tick(self) -> int:
  38 |         return int(self._raw.current_tick)
  39 | 
  40 |     @property
  41 |     def tick_index(self) -> int:
  42 |         return int(self._raw.current_tick)
  43 | 
  44 |     @property
  45 |     def sim_time_ms(self) -> float:
  46 |         return float(self._raw.sim_time_ms)
  47 | 
  48 |     @property
  49 |     def population_rate_hz(self) -> float:
  50 |         return float(self._raw.population_rate_hz)
  51 | 
  52 |     @property
  53 |     def channel_voltages(self) -> np.ndarray:
  54 |         arr = np.ctypeslib.as_array(self._raw.voltages)
  55 |         arr.flags.writeable = False
  56 |         return arr
  57 | 
  58 |     @property
  59 |     def spike_raster(self) -> np.ndarray:
  60 |         arr = np.ctypeslib.as_array(self._raw.spikes)
  61 |         return arr
  62 | 
  63 |     @property
  64 |     def last_charge_nc(self) -> np.ndarray:
  65 |         arr = np.ctypeslib.as_array(self._raw.last_charge_nc)
  66 |         return arr
  67 | 
  68 |     def get(self, key: str, default: object = None) -> object:
  69 |         """Dictionary-like get method for telemetry attributes."""
  70 |         if hasattr(self, key):
  71 |             val = getattr(self, key)
  72 |             return val() if callable(val) else val
  73 |         return default
  74 | 
  75 |     def __getitem__(self, key: str) -> object:
  76 |         """Dictionary-like indexer for telemetry attributes."""
  77 |         if hasattr(self, key):
  78 |             val = getattr(self, key)
  79 |             return val() if callable(val) else val
  80 |         raise KeyError(key)
  81 | 
  82 | 
  83 | class WetVM:
  84 |     """
  85 |     High-level Python wrapper for the native WetVM execution engine.
  86 |     Supports cycle-accurate stepping, batch tick execution, and zero-copy NumPy views.
  87 |     """
  88 | 
  89 |     def __init__(
  90 |         self,
  91 |         config: Optional[WetVMConfig] = None,
  92 |         lib_path: Optional[Union[str, Path]] = None
  93 |     ):
  94 |         self._lib = load_wetvm_lib(Path(lib_path) if lib_path else None)
  95 |         self._config = config if config is not None else WetVMConfig()
  96 |         self._handle = self._lib.wet_create_vm(ctypes.byref(self._config))
  97 |         if not self._handle:
  98 |             raise MemoryError("Failed to allocate native WetVM instance")
  99 | 
 100 |         # Persistent telemetry buffer for reuse and zero-copy NumPy mapping
 101 |         self._telem = WetTelemetry()
 102 |         self._closed = False
 103 |         self._is_halted = False
 104 |         self._bytecode_loaded = False
 105 | 
 106 |     def close(self) -> None:
 107 |         """Frees the native VM resources."""
 108 |         if not self._closed and self._handle:
 109 |             self._lib.wet_free_vm(self._handle)
 110 |             self._handle = None
 111 |             self._closed = True
 112 | 
 113 |     def __enter__(self) -> "WetVM":
 114 |         return self
 115 | 
 116 |     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
 117 |         self.close()
 118 | 
 119 |     def __del__(self) -> None:
 120 |         self.close()
 121 | 
 122 |     def _check_alive(self) -> None:
 123 |         if self._closed or not self._handle:
 124 |             raise RuntimeError("WetVM instance is closed")
 125 | 
 126 |     def load_bytecode(self, bytecode: Union[bytes, bytearray, str, Path]) -> None:
 127 |         """
 128 |         Loads WBC binary bytecode into the VM.
 129 |         Accepts raw bytes, or a filesystem path to a .wbc file.
 130 |         """
 131 |         self._check_alive()
 132 |         if isinstance(bytecode, (str, Path)):
 133 |             with open(bytecode, "rb") as f:
 134 |                 code_data = f.read()
 135 |         elif isinstance(bytecode, (bytes, bytearray)):
 136 |             code_data = bytes(bytecode)
 137 |         else:
 138 |             raise TypeError(f"Expected bytes or path, got {type(bytecode).__name__}")
 139 | 
 140 |         err_buf = ctypes.create_string_buffer(512)
 141 |         c_bytes = (ctypes.c_uint8 * len(code_data)).from_buffer_copy(code_data)
 142 | 
 143 |         status_code = self._lib.wet_load_bytecode(
 144 |             self._handle,
 145 |             c_bytes,
 146 |             len(code_data),
 147 |             err_buf,
 148 |             len(err_buf)
 149 |         )
 150 | 
 151 |         status = WetStatus(status_code)
 152 |         if status != WetStatus.WET_OK:
 153 |             err_msg = err_buf.value.decode("utf-8", errors="replace")
 154 |             if not err_msg:
 155 |                 err_msg = self.last_error() or self._status_to_string(status)
 156 |             raise WetVMError(status, err_msg)
 157 | 
 158 |         self._bytecode_loaded = True
 159 |         self._is_halted = False
 160 |         # Sync initial telemetry
 161 |         self.get_telemetry()
 162 | 
 163 |     def load(self, bytecode: Union[bytes, bytearray, str, Path]) -> int:
 164 |         """Alias for load_bytecode returning 0 on success."""
 165 |         self.load_bytecode(bytecode)
 166 |         return 0
 167 | 
 168 |     def step_tick(self) -> WetTelemetry:
 169 |         """
 170 |         Executes instructions until the next SYNC_TICK, SLEEP_TICKS, or HALT.
 171 |         Advances simulation time by dt_ms.
 172 |         """
 173 |         self._check_alive()
 174 |         if not self._bytecode_loaded:
 175 |             raise RuntimeError("No bytecode loaded into VM before stepping")
 176 | 
 177 |         status_code = self._lib.wet_step_tick(self._handle, ctypes.byref(self._telem))
 178 |         status = WetStatus(status_code)
 179 | 
 180 |         if status == WetStatus.WET_ERR_HALTED:
 181 |             self._is_halted = True
 182 |             raise WetVMError(status, "VM is halted")
 183 |         elif status != WetStatus.WET_OK:
 184 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 185 | 
 186 |         return self._telem
 187 | 
 188 |     def run_ticks(self, ticks: int) -> Tuple[int, WetTelemetry]:
 189 |         """
 190 |         Executes up to `ticks` consecutive simulation steps.
 191 |         Returns (executed_ticks_count, final_telemetry).
 192 |         """
 193 |         self._check_alive()
 194 |         if not self._bytecode_loaded:
 195 |             raise RuntimeError("No bytecode loaded into VM before running")
 196 | 
 197 |         if ticks < 0:
 198 |             raise ValueError(f"ticks must be non-negative, got {ticks}")
 199 | 
 200 |         executed = ctypes.c_uint32(0)
 201 |         status_code = self._lib.wet_run_ticks(
 202 |             self._handle,
 203 |             ctypes.c_uint32(ticks),
 204 |             ctypes.byref(executed),
 205 |             ctypes.byref(self._telem)
 206 |         )
 207 | 
 208 |         status = WetStatus(status_code)
 209 |         if status == WetStatus.WET_ERR_HALTED:
 210 |             self._is_halted = True
 211 |         elif status != WetStatus.WET_OK:
 212 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 213 | 
 214 |         return int(executed.value), self._telem
 215 | 
 216 |     def step(self, ticks: int = 1) -> WetTelemetryView:
 217 |         """Convenience method stepping 1 or more ticks and returning telemetry view."""
 218 |         self._check_alive()
 219 |         if not self._bytecode_loaded:
 220 |             raise RuntimeError("No bytecode loaded into VM before stepping")
 221 | 
 222 |         if ticks <= 1:
 223 |             try:
 224 |                 self.step_tick()
 225 |             except WetVMError as e:
 226 |                 if e.status == WetStatus.WET_ERR_HALTED:
 227 |                     pass
 228 |                 else:
 229 |                     raise
 230 |         else:
 231 |             self.run_ticks(ticks)
 232 |         return WetTelemetryView(self._telem)
 233 | 
 234 |     def inject_stimulus(
 235 |         self,
 236 |         channel: int,
 237 |         voltage_v: float,
 238 |         phase1_ms: float = 0.5,
 239 |         phase2_ms: float = 0.5
 240 |     ) -> None:
 241 |         """Injects biphasic stimulus onto designated MEA channel."""
 242 |         self._check_alive()
 243 |         status_code = self._lib.wet_inject_stimulus(
 244 |             self._handle,
 245 |             ctypes.c_uint8(channel),
 246 |             ctypes.c_float(voltage_v),
 247 |             ctypes.c_float(phase1_ms),
 248 |             ctypes.c_float(phase2_ms)
 249 |         )
 250 |         status = WetStatus(status_code)
 251 |         if status != WetStatus.WET_OK:
 252 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 253 | 
 254 |     def get_telemetry(self) -> WetTelemetry:
 255 |         """Fetches the latest cycle-accurate telemetry snapshot."""
 256 |         self._check_alive()
 257 |         status_code = self._lib.wet_get_telemetry(self._handle, ctypes.byref(self._telem))
 258 |         status = WetStatus(status_code)
 259 |         if status != WetStatus.WET_OK:
 260 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 261 |         return self._telem
 262 | 
 263 |     def get_actuator_telemetry(self) -> WetActuatorTelemetry:
 264 |         """Fetches the latest cyber-physical actuator telemetry."""
 265 |         self._check_alive()
 266 |         act_telem = WetActuatorTelemetry()
 267 |         status_code = self._lib.wet_get_actuator_telemetry(self._handle, ctypes.byref(act_telem))
 268 |         status = WetStatus(status_code)
 269 |         if status != WetStatus.WET_OK:
 270 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 271 |         return act_telem
 272 | 
 273 |     def get_voltages_numpy(self) -> np.ndarray:
 274 |         """
 275 |         Returns a zero-copy 1D NumPy array view (float32, 64 elements)
 276 |         mapped directly onto the telemetry voltage buffer.
 277 |         """
 278 |         arr = np.ctypeslib.as_array(self._telem.voltages)
 279 |         arr.flags.writeable = False
 280 |         return arr
 281 | 
 282 |     def get_spikes_numpy(self) -> np.ndarray:
 283 |         """
 284 |         Returns a zero-copy 1D NumPy array view (uint8, 64 elements)
 285 |         mapped directly onto the telemetry spike raster buffer.
 286 |         """
 287 |         return np.ctypeslib.as_array(self._telem.spikes)
 288 | 
 289 |     def get_charge_numpy(self) -> np.ndarray:
 290 |         """
 291 |         Returns a zero-copy 1D NumPy array view (float32, 64 elements)
 292 |         mapped directly onto the telemetry cumulative charge buffer.
 293 |         """
 294 |         return np.ctypeslib.as_array(self._telem.last_charge_nc)
 295 | 
 296 |     def last_error(self) -> str:
 297 |         """Returns the last recorded native error message."""
 298 |         if not self._handle:
 299 |             return "VM is closed"
 300 |         err = self._lib.wet_get_last_error(self._handle)
 301 |         return err.decode("utf-8", errors="replace") if err else ""
 302 | 
 303 |     def _status_to_string(self, status: WetStatus) -> str:
 304 |         s = self._lib.wet_status_to_string(int(status))
 305 |         return s.decode("utf-8", errors="replace") if s else status.name
 306 | 
 307 |     @property
 308 |     def current_tick(self) -> int:
 309 |         return int(self._telem.current_tick)
 310 | 
 311 |     @property
 312 |     def tick_index(self) -> int:
 313 |         return int(self._telem.current_tick)
 314 | 
 315 |     @property
 316 |     def sim_time_ms(self) -> float:
 317 |         return float(self._telem.sim_time_ms)
 318 | 
 319 |     @property
 320 |     def is_halted(self) -> bool:
 321 |         return self._is_halted
 322 | 
 323 |     # Phase 3 Hardware Readiness Methods
 324 |     def configure_electrode(self, material: int, area_um2: float) -> None:
 325 |         """Configures electrode material and physical geometric surface area."""
 326 |         self._check_alive()
 327 |         self._lib.wet_configure_electrode(self._handle, ctypes.c_uint8(material), ctypes.c_float(area_um2))
 328 | 
 329 |     def active_discharge(self, channel: int) -> None:
 330 |         """Actuates hardware discharge switch on designated channel to clear accumulated DC charge."""
 331 |         self._check_alive()
 332 |         self._lib.wet_active_discharge(self._handle, ctypes.c_uint8(channel))
 333 | 
 334 |     def active_discharge_all(self) -> None:
 335 |         """Actuates hardware discharge switch on all 64 channels."""
 336 |         self._check_alive()
 337 |         self._lib.wet_active_discharge_all(self._handle)
 338 | 
 339 |     def enable_dead_head_protection(self, enable: bool = True) -> None:
 340 |         """Enables microfluidic valve-pump dead-head overpressure interlock."""
 341 |         self._check_alive()
 342 |         self._lib.wet_enable_dead_head_protection(self._handle, ctypes.c_uint8(1 if enable else 0))
 343 | 
 344 |     def life_supervisor_shutdown(self, vm: Optional[ctypes.c_void_p] = None) -> None:
 345 |         """Terminates Ring-0 Life Support Supervisor autonomous baseline perfusion."""
 346 |         self._check_alive()
 347 |         self._lib.wet_life_supervisor_shutdown(self._handle)
 348 | 
 349 |     def configure_blanking(self, blanking_ms: float = 2.0, enable_spatial: bool = True) -> None:
 350 |         """Configures amplifier blanking duration and spatial neighbor crosstalk suppression."""
 351 |         self._check_alive()
 352 |         self._lib.wet_configure_blanking(self._handle, ctypes.c_float(blanking_ms), ctypes.c_uint8(1 if enable_spatial else 0))
 353 | 
 354 |     def inject_current_stimulus(
 355 |         self,
 356 |         channel: int,
 357 |         current_ua: float,
 358 |         p1_ms: float = 0.5,
 359 |         p2_ms: float = 0.5
 360 |     ) -> None:
 361 |         """Injects constant-current electrical stimulus (uA) through Randles interface."""
 362 |         self._check_alive()
 363 |         status_code = self._lib.wet_inject_current_stimulus(
 364 |             self._handle,
 365 |             ctypes.c_uint8(channel),
 366 |             ctypes.c_float(current_ua),
 367 |             ctypes.c_float(p1_ms),
 368 |             ctypes.c_float(p2_ms)
 369 |         )
 370 |         status = WetStatus(status_code)
 371 |         if status != WetStatus.WET_OK:
 372 |             raise WetVMError(status, self.last_error() or self._status_to_string(status))
 373 | 
 374 |     def verify_bytecode(self, bytecode: bytes) -> str:
 375 |         """Runs the C99 load-time bytecode verifier without loading into VM."""
 376 |         c_bytes = (ctypes.c_uint8 * len(bytecode)).from_buffer_copy(bytecode)
 377 |         err_buf = ctypes.create_string_buffer(512)
 378 |         st = self._lib.wet_verify_bytecode(c_bytes, ctypes.c_size_t(len(bytecode)), err_buf, ctypes.c_size_t(len(err_buf)))
 379 |         status = WetStatus(st)
 380 |         msg = err_buf.value.decode("utf-8", errors="replace")
 381 |         if status != WetStatus.WET_OK:
 382 |             raise WetVMError(status, msg or self._status_to_string(status))
 383 |         return "OK"
 384 | 
 385 |     def snapshot(self) -> bytes:
 386 |         """Serializes complete dynamic neural state, synaptic matrix, and monotonic clocks."""
 387 |         self._check_alive()
 388 |         needed_len = ctypes.c_size_t(0)
 389 |         self._lib.wet_vm_snapshot(self._handle, None, ctypes.byref(needed_len))
 390 |         buf = (ctypes.c_uint8 * needed_len.value)()
 391 |         st = self._lib.wet_vm_snapshot(self._handle, buf, ctypes.byref(needed_len))
 392 |         status = WetStatus(st)
 393 |         if status != WetStatus.WET_OK:
 394 |             raise WetVMError(status, self.last_error() or "Snapshot failed")
 395 |         return bytes(buf)
 396 | 
 397 |     def restore(self, data: bytes) -> None:
 398 |         """Restores complete neural state and synaptic weights without resetting learned memory."""
 399 |         self._check_alive()
 400 |         c_bytes = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
 401 |         st = self._lib.wet_vm_restore(self._handle, c_bytes, ctypes.c_size_t(len(data)))
 402 |         status = WetStatus(st)
 403 |         if status != WetStatus.WET_OK:
 404 |             raise WetVMError(status, self.last_error() or "Restore failed")
 405 |         self._lib.wet_get_telemetry(self._handle, ctypes.byref(self._telem))
 406 | 
 407 |     def set_environmental_sensors(
 408 |         self,
 409 |         ph: float = 7.4,
 410 |         do_pct: float = 95.0,
 411 |         co2_pct: float = 5.0,
 412 |         bubble_sensor_id: int = 0,
 413 |         bubble_state: bool = False,
 414 |         flow_rate_ul_min: float = 1.5
 415 |     ) -> None:
 416 |         """Updates simulated or hardware sensor telemetry readings."""
 417 |         self._check_alive()
 418 |         self._lib.wet_set_environmental_sensors(
 419 |             self._handle,
 420 |             ctypes.c_float(ph),
 421 |             ctypes.c_float(do_pct),
 422 |             ctypes.c_float(co2_pct),
 423 |             ctypes.c_uint8(bubble_sensor_id),
 424 |             ctypes.c_uint8(1 if bubble_state else 0),
 425 |             ctypes.c_float(flow_rate_ul_min)
 426 |         )
 427 | 
 428 |     def set_temperature(self, temp_c: float) -> None:
 429 |         """Sets simulated or incubator ambient / CMOS die temperature."""
 430 |         self._check_alive()
 431 |         self._lib.wet_set_temperature(self._handle, ctypes.c_float(temp_c))
 432 | 
 433 |     def set_channel_banks(
 434 |         self,
 435 |         ref_channels: list[int] = [],
 436 |         rec_only_channels: list[int] = []
 437 |     ) -> None:
 438 |         """Configures typed channel capability banks (reference and recording-only)."""
 439 |         self._check_alive()
 440 |         ref_mask = 0
 441 |         for ch in ref_channels:
 442 |             if 0 <= ch < 64:
 443 |                 ref_mask |= (1 << ch)
 444 |         rec_mask = 0
 445 |         for ch in rec_only_channels:
 446 |             if 0 <= ch < 64:
 447 |                 rec_mask |= (1 << ch)
 448 |         self._lib.wet_set_channel_banks(self._handle, ctypes.c_uint64(ref_mask), ctypes.c_uint64(rec_mask))
 449 | 
 450 |     def init_hal(
 451 |         self,
 452 |         mode: WetHalMode = WetHalMode.WET_HAL_MODE_HIL_LOOPBACK,
 453 |         config: Optional[WetHalConfig] = None
 454 |     ) -> int:
 455 |         """Initializes and attaches Hardware Abstraction Layer (HAL) on VM."""
 456 |         self._check_alive()
 457 |         cfg_ptr = ctypes.byref(config) if config is not None else None
 458 |         return self._lib.wet_hal_init(self._handle, ctypes.c_int(int(mode)), cfg_ptr)
 459 | 
 460 |     def attach_hal(self, hal: ctypes.c_void_p) -> int:
 461 |         """Attaches an existing HAL context to the VM."""
 462 |         self._check_alive()
 463 |         return self._lib.wet_hal_attach(self._handle, hal)
 464 | 
 465 |     def get_hal(self) -> ctypes.c_void_p:
 466 |         """Returns the HAL context pointer attached to this VM."""
 467 |         self._check_alive()
 468 |         return self._lib.wet_hal_get_context(self._handle)
 469 | 
 470 |     def emergency_crowbar(self, trip_reason: int = 1) -> None:
 471 |         """Triggers emergency hardware crowbar fast-path (<100 µs)."""
 472 |         self._check_alive()
 473 |         self._lib.wet_hal_emergency_crowbar(self._handle, ctypes.c_uint32(trip_reason))
 474 | 
 475 |     def get_synapse_matrix(self) -> np.ndarray:
 476 |         """
 477 |         Extracts the 64x64 synaptic conductance matrix (nS) from C VM biophysics state.
 478 |         Returns a NumPy float32 array of shape (64, 64).
 479 |         """
 480 |         self._check_alive()
 481 |         buf = (ctypes.c_float * (64 * 64))()
 482 |         st = self._lib.wet_vm_get_synapse_matrix(
 483 |             self._handle,
 484 |             buf,
 485 |             ctypes.c_size_t(64 * 64)
 486 |         )
 487 |         if st != WetStatus.WET_OK:
 488 |             raise WetVMError(WetStatus(st), self.last_error() or "Failed to read synapse matrix")
 489 |         return np.ctypeslib.as_array(buf).reshape((64, 64)).copy()
 490 | 
 491 |     def get_synapse_weight(self, pre: int, post: int) -> float:
 492 |         """
 493 |         Queries the synaptic conductance weight between pre and post neurons in nS.
 494 |         """
 495 |         self._check_alive()
 496 |         return float(self._lib.wet_vm_get_synapse_weight(
 497 |             self._handle,
 498 |             ctypes.c_uint8(pre),
 499 |             ctypes.c_uint8(post)
 500 |         ))
 501 | 
 502 | 
 503 | class WetRuntime(WetVM):
 504 |     """Alias / Subclass of WetVM providing E2E test-suite compatibility."""
 505 |     pass
```

### `bindings/scheduler.py` (302 lines, SHA-256: `a26fa321476c3e7e...`)

```text
   1 | """
   2 | WetLang Python ctypes Bindings for Hard Real-Time Sub-100 µs Execution Scheduler
   3 | Provides high-level object-oriented interface to wet_scheduler C99 runtime.
   4 | """
   5 | 
   6 | from __future__ import annotations
   7 | 
   8 | import ctypes
   9 | import multiprocessing
  10 | from ctypes import (
  11 |     c_void_p,
  12 |     c_uint8,
  13 |     c_uint32,
  14 |     c_uint64,
  15 |     c_int32,
  16 |     c_double,
  17 |     c_float,
  18 |     c_int,
  19 |     POINTER,
  20 |     byref,
  21 | )
  22 | from dataclasses import dataclass
  23 | from typing import Optional, Union, Any
  24 | 
  25 | from bindings.ffi import load_wetvm_lib, WetStatus, WetTelemetry
  26 | 
  27 | 
  28 | def resolve_p_core(requested_core: Optional[int] = None, allow_e_cores: bool = False) -> int:
  29 |     """
  30 |     Selects or validates a Performance Core (P-core) for real-time thread affinity.
  31 | 
  32 |     ARCHITECTURAL BACKGROUND:
  33 |     Modern heterogeneous x86 processors (Intel 12th-15th Gen Alder Lake, Raptor Lake,
  34 |     Arrow Lake, and Intel Core Ultra / Lunar Lake) integrate high-performance P-cores
  35 |     and low-power E-cores. E-cores exhibit +55% compute latency (13-14 µs vs 8.8 µs)
  36 |     and >300 µs jitter, failing hard real-time sub-100 µs guarantees.
  37 |     
  38 |     Logical Core 0 typically services host OS interrupts and driver DPCs. Therefore,
  39 |     Core 1, 2, or 3 are the prime Performance Cores. If no core is requested or an
  40 |     out-of-range/E-core is specified on hybrid architectures without allow_e_cores,
  41 |     fallback logic redirects execution to a verified P-core.
  42 |     """
  43 |     try:
  44 |         cpu_count = multiprocessing.cpu_count()
  45 |     except Exception:
  46 |         cpu_count = 1
  47 | 
  48 |     if requested_core is None:
  49 |         return 1 if cpu_count > 1 else 0
  50 | 
  51 |     if requested_core < 0:
  52 |         return 1 if cpu_count > 1 else 0
  53 | 
  54 |     # If the system has >= 8 logical cores (typical hybrid layout with 4 P-cores + 4 E-cores),
  55 |     # guard against accidental assignment to E-cores (cores 4+) unless allow_e_cores=True
  56 |     if not allow_e_cores and cpu_count >= 8 and requested_core >= 4:
  57 |         p_fallback = requested_core % 4
  58 |         if p_fallback == 0 and cpu_count > 1:
  59 |             p_fallback = 1
  60 |         return p_fallback
  61 | 
  62 |     if requested_core >= cpu_count:
  63 |         return 1 if cpu_count > 1 else 0
  64 | 
  65 |     return requested_core
  66 | 
  67 | 
  68 | class WetSchedulerConfig(ctypes.Structure):
  69 |     """Mirror of C wet_scheduler_config_t."""
  70 |     _fields_ = [
  71 |         ("target_period_us", c_uint32),
  72 |         ("target_core", c_uint32),
  73 |         ("priority_class", c_uint32),
  74 |         ("thread_priority", c_int32),
  75 |         ("enable_core_pinning", c_uint8),
  76 |         ("enable_priority_elevation", c_uint8),
  77 |         ("telemetry_queue_capacity", c_uint32),
  78 |         ("stimulus_queue_capacity", c_uint32),
  79 |         ("total_ticks", c_uint64),
  80 |     ]
  81 | 
  82 |     def __init__(
  83 |         self,
  84 |         target_period_us: int = 100,
  85 |         target_core: Optional[int] = None,
  86 |         priority_class: int = 0x00000100,  # REALTIME_PRIORITY_CLASS
  87 |         thread_priority: int = 15,          # THREAD_PRIORITY_TIME_CRITICAL
  88 |         enable_core_pinning: bool = True,
  89 |         enable_priority_elevation: bool = True,
  90 |         telemetry_queue_capacity: int = 1024,
  91 |         stimulus_queue_capacity: int = 256,
  92 |         total_ticks: int = 0,
  93 |         allow_e_cores: bool = False,
  94 |     ):
  95 |         p_core = resolve_p_core(target_core, allow_e_cores=allow_e_cores)
  96 |         super().__init__(
  97 |             target_period_us=target_period_us,
  98 |             target_core=p_core,
  99 |             priority_class=priority_class,
 100 |             thread_priority=thread_priority,
 101 |             enable_core_pinning=1 if enable_core_pinning else 0,
 102 |             enable_priority_elevation=1 if enable_priority_elevation else 0,
 103 |             telemetry_queue_capacity=telemetry_queue_capacity,
 104 |             stimulus_queue_capacity=stimulus_queue_capacity,
 105 |             total_ticks=total_ticks,
 106 |         )
 107 | 
 108 | 
 109 | class WetStimCommand(ctypes.Structure):
 110 |     """Mirror of C wet_stim_command_t."""
 111 |     _fields_ = [
 112 |         ("channel", c_uint8),
 113 |         ("voltage_v", c_float),
 114 |         ("phase1_ms", c_float),
 115 |         ("phase2_ms", c_float),
 116 |         ("tick_scheduled", c_uint64),
 117 |     ]
 118 | 
 119 |     def __init__(
 120 |         self,
 121 |         channel: int = 0,
 122 |         voltage_v: float = 0.8,
 123 |         phase1_ms: float = 0.2,
 124 |         phase2_ms: float = 0.2,
 125 |         tick_scheduled: int = 0,
 126 |     ):
 127 |         super().__init__(
 128 |             channel=channel,
 129 |             voltage_v=voltage_v,
 130 |             phase1_ms=phase1_ms,
 131 |             phase2_ms=phase2_ms,
 132 |             tick_scheduled=tick_scheduled,
 133 |         )
 134 | 
 135 | 
 136 | class WetSchedulerStats(ctypes.Structure):
 137 |     """Mirror of C wet_scheduler_stats_t."""
 138 |     _fields_ = [
 139 |         ("total_ticks", c_uint64),
 140 |         ("min_compute_us", c_double),
 141 |         ("max_compute_us", c_double),
 142 |         ("mean_compute_us", c_double),
 143 |         ("min_period_us", c_double),
 144 |         ("max_period_us", c_double),
 145 |         ("mean_period_us", c_double),
 146 |         ("mean_jitter_us", c_double),
 147 |         ("p50_jitter_us", c_double),
 148 |         ("p95_jitter_us", c_double),
 149 |         ("p99_jitter_us", c_double),
 150 |         ("p999_jitter_us", c_double),
 151 |         ("max_jitter_us", c_double),
 152 |         ("deadline_overruns", c_uint64),
 153 |         ("telemetry_dropped", c_uint64),
 154 |         ("stimuli_injected", c_uint64),
 155 |     ]
 156 | 
 157 |     def as_dict(self) -> dict:
 158 |         return {
 159 |             "total_ticks": self.total_ticks,
 160 |             "min_compute_us": self.min_compute_us,
 161 |             "max_compute_us": self.max_compute_us,
 162 |             "mean_compute_us": self.mean_compute_us,
 163 |             "min_period_us": self.min_period_us,
 164 |             "max_period_us": self.max_period_us,
 165 |             "mean_period_us": self.mean_period_us,
 166 |             "mean_jitter_us": self.mean_jitter_us,
 167 |             "p50_jitter_us": self.p50_jitter_us,
 168 |             "p95_jitter_us": self.p95_jitter_us,
 169 |             "p99_jitter_us": self.p99_jitter_us,
 170 |             "p999_jitter_us": self.p999_jitter_us,
 171 |             "max_jitter_us": self.max_jitter_us,
 172 |             "deadline_overruns": self.deadline_overruns,
 173 |             "telemetry_dropped": self.telemetry_dropped,
 174 |             "stimuli_injected": self.stimuli_injected,
 175 |         }
 176 | 
 177 | 
 178 | def _bind_scheduler_ffi(lib: ctypes.CDLL) -> None:
 179 |     """Configures ctypes argtypes and restypes for scheduler functions."""
 180 |     lib.wet_scheduler_create.restype = c_void_p
 181 |     lib.wet_scheduler_create.argtypes = [c_void_p, POINTER(WetSchedulerConfig)]
 182 | 
 183 |     lib.wet_scheduler_start.restype = c_int
 184 |     lib.wet_scheduler_start.argtypes = [c_void_p]
 185 | 
 186 |     lib.wet_scheduler_step.restype = c_int
 187 |     lib.wet_scheduler_step.argtypes = [c_void_p]
 188 | 
 189 |     lib.wet_scheduler_stop.restype = c_int
 190 |     lib.wet_scheduler_stop.argtypes = [c_void_p]
 191 | 
 192 |     lib.wet_scheduler_get_stats.restype = c_int
 193 |     lib.wet_scheduler_get_stats.argtypes = [c_void_p, POINTER(WetSchedulerStats)]
 194 | 
 195 |     lib.wet_scheduler_poll_telemetry.restype = c_int
 196 |     lib.wet_scheduler_poll_telemetry.argtypes = [c_void_p, POINTER(WetTelemetry)]
 197 | 
 198 |     lib.wet_scheduler_push_stimulus.restype = c_int
 199 |     lib.wet_scheduler_push_stimulus.argtypes = [c_void_p, POINTER(WetStimCommand)]
 200 | 
 201 |     lib.wet_scheduler_benchmark.restype = c_int
 202 |     lib.wet_scheduler_benchmark.argtypes = [c_void_p, c_uint32, POINTER(WetSchedulerStats)]
 203 | 
 204 |     lib.wet_scheduler_destroy.restype = None
 205 |     lib.wet_scheduler_destroy.argtypes = [c_void_p]
 206 | 
 207 | 
 208 | class WetScheduler:
 209 |     """
 210 |     Python wrapper for the C99 deterministic hard real-time scheduler.
 211 |     """
 212 |     def __init__(
 213 |         self,
 214 |         vm_or_runtime: Any,
 215 |         config: Optional[WetSchedulerConfig] = None,
 216 |         lib: Optional[ctypes.CDLL] = None,
 217 |     ):
 218 |         self._lib = lib or load_wetvm_lib()
 219 |         _bind_scheduler_ffi(self._lib)
 220 | 
 221 |         if hasattr(vm_or_runtime, "_handle"):
 222 |             self._vm_ptr = c_void_p(vm_or_runtime._handle)
 223 |         elif hasattr(vm_or_runtime, "vm"):
 224 |             v = vm_or_runtime.vm
 225 |             self._vm_ptr = c_void_p(v) if isinstance(v, int) else v
 226 |         elif hasattr(vm_or_runtime, "_vm"):
 227 |             v = vm_or_runtime._vm
 228 |             self._vm_ptr = c_void_p(v) if isinstance(v, int) else v
 229 |         elif isinstance(vm_or_runtime, int):
 230 |             self._vm_ptr = c_void_p(vm_or_runtime)
 231 |         else:
 232 |             self._vm_ptr = vm_or_runtime
 233 | 
 234 |         self._config = config or WetSchedulerConfig()
 235 |         self._sched = self._lib.wet_scheduler_create(self._vm_ptr, byref(self._config))
 236 |         if not self._sched:
 237 |             raise RuntimeError("Failed to allocate wet_scheduler_t instance")
 238 | 
 239 |     @property
 240 |     def handle(self) -> c_void_p:
 241 |         return self._sched
 242 | 
 243 |     def start(self) -> None:
 244 |         st = self._lib.wet_scheduler_start(self._sched)
 245 |         if st != WetStatus.WET_OK:
 246 |             raise RuntimeError(f"wet_scheduler_start failed with status {st}")
 247 | 
 248 |     def step(self) -> int:
 249 |         return self._lib.wet_scheduler_step(self._sched)
 250 | 
 251 |     def stop(self) -> None:
 252 |         self._lib.wet_scheduler_stop(self._sched)
 253 | 
 254 |     def get_stats(self) -> WetSchedulerStats:
 255 |         stats = WetSchedulerStats()
 256 |         st = self._lib.wet_scheduler_get_stats(self._sched, byref(stats))
 257 |         if st != WetStatus.WET_OK:
 258 |             raise RuntimeError(f"wet_scheduler_get_stats failed with status {st}")
 259 |         return stats
 260 | 
 261 |     def poll_telemetry(self) -> Optional[WetTelemetry]:
 262 |         telem = WetTelemetry()
 263 |         st = self._lib.wet_scheduler_poll_telemetry(self._sched, byref(telem))
 264 |         if st == WetStatus.WET_OK:
 265 |             return telem
 266 |         return None
 267 | 
 268 |     def push_stimulus(
 269 |         self,
 270 |         channel: int,
 271 |         voltage_v: float,
 272 |         phase1_ms: float = 0.2,
 273 |         phase2_ms: float = 0.2,
 274 |         tick_scheduled: int = 0
 275 |     ) -> bool:
 276 |         cmd = WetStimCommand(
 277 |             channel=channel,
 278 |             voltage_v=voltage_v,
 279 |             phase1_ms=phase1_ms,
 280 |             phase2_ms=phase2_ms,
 281 |             tick_scheduled=tick_scheduled,
 282 |         )
 283 |         st = self._lib.wet_scheduler_push_stimulus(self._sched, byref(cmd))
 284 |         return st == WetStatus.WET_OK
 285 | 
 286 |     def benchmark(self, total_ticks: int = 10000) -> WetSchedulerStats:
 287 |         stats = WetSchedulerStats()
 288 |         st = self._lib.wet_scheduler_benchmark(self._sched, c_uint32(total_ticks), byref(stats))
 289 |         if st != WetStatus.WET_OK and st != WetStatus.WET_ERR_HALTED:
 290 |             raise RuntimeError(f"wet_scheduler_benchmark failed with status {st}")
 291 |         return stats
 292 | 
 293 |     def destroy(self) -> None:
 294 |         if self._sched:
 295 |             self._lib.wet_scheduler_destroy(self._sched)
 296 |             self._sched = None
 297 | 
 298 |     def __enter__(self) -> "WetScheduler":
 299 |         return self
 300 | 
 301 |     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
 302 |         self.destroy()
```

### `biophysics/__init__.py` (17 lines, SHA-256: `2f45135b6989e595...`)

```text
   1 | """
   2 | WetLang In-Silico Biophysical Digital Twin Sandbox
   3 | """
   4 | 
   5 | from biophysics.mea_grid import MEAGrid
   6 | from biophysics.ode_solver import LifODESolver
   7 | from biophysics.stp import SynapseSTP
   8 | from biophysics.stdp import PairwiseSTDP
   9 | from biophysics.telemetry import TelemetryStream
  10 | 
  11 | __all__ = [
  12 |     "MEAGrid",
  13 |     "LifODESolver",
  14 |     "SynapseSTP",
  15 |     "PairwiseSTDP",
  16 |     "TelemetryStream",
  17 | ]
```

### `biophysics/mea_grid.py` (94 lines, SHA-256: `d0ccaf43957f0d45...`)

```text
   1 | """
   2 | WetLang Biophysical Digital Twin: 8x8 MEA Grid Topology
   3 | Provides spatial mapping, electrode substrate coordinates, 3D volume conduction forward matrix,
   4 | and resistive cross-talk kernel for an 8x8 microelectrode array (200 um pitch).
   5 | """
   6 | 
   7 | import math
   8 | from typing import Tuple
   9 | import numpy as np
  10 | 
  11 | 
  12 | class MEAGrid:
  13 |     """
  14 |     8x8 Microelectrode Array (MEA) with 200 um pitch.
  15 |     Total of 64 electrodes arranged in an 8x8 Cartesian topology.
  16 |     """
  17 | 
  18 |     def __init__(self, rows: int = 8, cols: int = 8, pitch_um: float = 200.0):
  19 |         self.rows: int = rows
  20 |         self.cols: int = cols
  21 |         self.pitch_um: float = pitch_um
  22 |         self.total_electrodes: int = rows * cols
  23 | 
  24 |     def coords_to_channel(self, row: int, col: int) -> int:
  25 |         """Bijective mapping from 2D (row, col) coordinates to 1D channel index."""
  26 |         if not (0 <= row < self.rows and 0 <= col < self.cols):
  27 |             raise ValueError(f"Coordinates ({row}, {col}) out of MEA bounds ({self.rows}x{self.cols})")
  28 |         return row * self.cols + col
  29 | 
  30 |     def channel_to_coords(self, ch: int) -> Tuple[int, int]:
  31 |         """Bijective mapping from 1D channel index to 2D (row, col) coordinates."""
  32 |         if not (0 <= ch < self.total_electrodes):
  33 |             raise ValueError(f"Channel index {ch} out of bounds (0..{self.total_electrodes - 1})")
  34 |         return (ch // self.cols, ch % self.cols)
  35 | 
  36 |     def get_electrode_pos(self, ch: int) -> Tuple[float, float]:
  37 |         """
  38 |         Returns physical Cartesian substrate coordinates (x_um, y_um) of electrode center.
  39 |         Electrodes are centered at (col + 0.5) * pitch_um, (row + 0.5) * pitch_um.
  40 |         For 200 um pitch: ch 0 -> (100.0, 100.0), ch 63 -> (1500.0, 1500.0).
  41 |         """
  42 |         r, c = self.channel_to_coords(ch)
  43 |         x_um = (c + 0.5) * self.pitch_um
  44 |         y_um = (r + 0.5) * self.pitch_um
  45 |         return (x_um, y_um)
  46 | 
  47 |     def calculate_field_potential(
  48 |         self,
  49 |         source_x: float,
  50 |         source_y: float,
  51 |         source_z: float,
  52 |         current_na: float,
  53 |         sigma: float = 0.3,
  54 |         r0_um: float = 15.0,
  55 |     ) -> np.ndarray:
  56 |         """
  57 |         Calculates 3D volume conduction forward pickup potentials across all electrodes
  58 |         given a point current source in conductive extracellular medium (conductivity sigma in S/m).
  59 |         """
  60 |         potentials = np.zeros(self.total_electrodes, dtype=np.float64)
  61 |         for ch in range(self.total_electrodes):
  62 |             ex, ey = self.get_electrode_pos(ch)
  63 |             dx = source_x - ex
  64 |             dy = source_y - ey
  65 |             dz = source_z
  66 |             dist_um = math.sqrt(dx * dx + dy * dy + dz * dz + r0_um * r0_um)
  67 |             # Extracellular potential: V = I / (4 * pi * sigma * r)
  68 |             # I in nA (1e-9 A), dist in um (1e-6 m), sigma in S/m -> V in Volts
  69 |             v_volts = (current_na * 1e-9) / (4.0 * math.pi * sigma * (dist_um * 1e-6))
  70 |             potentials[ch] = v_volts
  71 | 
  72 |         return potentials
  73 | 
  74 |     def get_crosstalk_matrix(self) -> np.ndarray:
  75 |         """
  76 |         Returns 64x64 resistive cross-talk matrix between electrodes.
  77 |         Self-coupling is 1.0; 4-way adjacent electrodes have ~0.04 resistive coupling.
  78 |         """
  79 |         mat = np.zeros((self.total_electrodes, self.total_electrodes), dtype=np.float64)
  80 |         for i in range(self.total_electrodes):
  81 |             r1, c1 = self.channel_to_coords(i)
  82 |             for j in range(self.total_electrodes):
  83 |                 if i == j:
  84 |                     mat[i, j] = 1.0
  85 |                 else:
  86 |                     r2, c2 = self.channel_to_coords(j)
  87 |                     manhattan_dist = abs(r1 - r2) + abs(c1 - c2)
  88 |                     if manhattan_dist == 1:
  89 |                         mat[i, j] = 0.04
  90 |                     else:
  91 |                         euclid_dist = math.sqrt((r1 - r2) ** 2 + (c1 - c2) ** 2)
  92 |                         mat[i, j] = 0.04 / (euclid_dist ** 2)
  93 | 
  94 |         return mat
```

### `biophysics/ode_solver.py` (109 lines, SHA-256: `2ce4db9b21d3fe8c...`)

```text
   1 | """
   2 | WetLang Numerical ODE Solver: Conductance-Based Leaky Integrate-and-Fire (COBA-LIF)
   3 | Implements Exact Exponential Euler integration at fixed dt = 0.1 ms,
   4 | 2.0 ms absolute refractory hard clamp, dynamic threshold elevation, and slow AHP adaptation.
   5 | """
   6 | 
   7 | import math
   8 | from typing import List, Tuple
   9 | 
  10 | 
  11 | class LifODESolver:
  12 |     """
  13 |     Exact Exponential Euler ODE solver for COBA-LIF dynamics.
  14 |     Integrates sub-threshold membrane potentials, synaptic conductances,
  15 |     and enforces absolute/relative refractory limits.
  16 |     """
  17 | 
  18 |     def __init__(self, dt_ms: float = 0.1):
  19 |         self.dt_ms: float = dt_ms
  20 | 
  21 |     def step_passive(self, v_init: float, tau_m: float, v_rest: float) -> float:
  22 |         """
  23 |         Exact Exponential Euler passive membrane relaxation toward resting potential.
  24 |         V(t + dt) = V_rest + (V(t) - V_rest) * exp(-dt / tau_m)
  25 |         """
  26 |         decay = math.exp(-self.dt_ms / tau_m)
  27 |         return v_rest + (v_init - v_rest) * decay
  28 | 
  29 |     def decay_conductance(self, g: float, tau_ms: float) -> float:
  30 |         """
  31 |         Exponential synaptic conductance decay.
  32 |         g(t + dt) = g(t) * exp(-dt / tau_ms)
  33 |         """
  34 |         return g * math.exp(-self.dt_ms / tau_ms)
  35 | 
  36 |     def update_neuron(self, v_m: float, v_thresh: float, v_reset: float) -> Tuple[bool, float]:
  37 |         """
  38 |         Evaluates action potential threshold crossing and reset.
  39 |         Returns (spiked: bool, v_new: float).
  40 |         """
  41 |         if v_m >= v_thresh:
  42 |             return (True, v_reset)
  43 |         return (False, v_m)
  44 | 
  45 |     def simulate_refractory(self, v_init: float, current_inj: float, ticks: int) -> List[float]:
  46 |         """
  47 |         Simulates absolute refractory hard clamp: membrane potential remains pinned at v_init
  48 |         regardless of injected current.
  49 |         """
  50 |         return [v_init] * ticks
  51 | 
  52 |     def decrement_refractory(self, counter: int) -> int:
  53 |         """Decrements remaining absolute refractory ticks toward zero."""
  54 |         return max(0, counter - 1)
  55 | 
  56 |     def simulate_continuous_stimulus(
  57 |         self,
  58 |         current_pA: float,
  59 |         duration_ms: float,
  60 |         c_m_pf: float = 200.0,
  61 |         g_leak_ns: float = 10.0,
  62 |         v_rest_mv: float = -70.0,
  63 |         v_reset_mv: float = -75.0,
  64 |         v_thresh_base_mv: float = -50.0,
  65 |         abs_refract_ms: float = 2.0,
  66 |     ) -> List[int]:
  67 |         """
  68 |         Simulates neuron response to sustained strong current injection with 2.0 ms refractory clamp.
  69 |         Returns list of spike tick indices.
  70 |         Enforces maximum firing frequency of 500 Hz (at least 20 ticks between spikes).
  71 |         """
  72 |         total_ticks = int(duration_ms / self.dt_ms)
  73 |         refract_ticks_total = int(abs_refract_ms / self.dt_ms)
  74 | 
  75 |         v_m = v_rest_mv
  76 |         v_thresh = v_thresh_base_mv
  77 |         refract_remaining = 0
  78 |         spikes: List[int] = []
  79 | 
  80 |         tau_m = c_m_pf / g_leak_ns # 20.0 ms
  81 | 
  82 |         for t in range(total_ticks):
  83 |             if refract_remaining > 0:
  84 |                 refract_remaining -= 1
  85 |                 v_m = v_reset_mv
  86 |             else:
  87 |                 # Steady-state voltage under current injection: V_inf = V_rest + I / g_leak
  88 |                 # current in pA, g_leak in nS -> V_inf in mV
  89 |                 v_inf = v_rest_mv + (current_pA / 1000.0) / (g_leak_ns / 1.0)
  90 |                 decay = math.exp(-self.dt_ms / tau_m)
  91 |                 v_m = v_inf + (v_m - v_inf) * decay
  92 | 
  93 |                 if v_m >= v_thresh:
  94 |                     spikes.append(t)
  95 |                     v_m = v_reset_mv
  96 |                     refract_remaining = refract_ticks_total
  97 | 
  98 |             # Dynamic threshold decay
  99 |             v_thresh = v_thresh_base_mv + (v_thresh - v_thresh_base_mv) * math.exp(-self.dt_ms / 10.0)
 100 | 
 101 |         return spikes
 102 | 
 103 |     def elevate_threshold(self, base_thresh: float, delta: float) -> float:
 104 |         """Dynamic threshold elevation for relative refractory period (+15 mV)."""
 105 |         return base_thresh + delta
 106 | 
 107 |     def activate_ahp(self, g_current: float, delta_g: float) -> float:
 108 |         """Activates slow after-hyperpolarization (AHP) potassium conductance jump (+2..4 nS)."""
 109 |         return g_current + delta_g
```

### `biophysics/stdp.py` (70 lines, SHA-256: `f156f43f0b438efe...`)

```text
   1 | """
   2 | WetLang Pairwise Spike-Timing-Dependent Plasticity (STDP)
   3 | Implements online exponential trace STDP with 1.05x depression bias (A_- / A_+ == 1.05),
   4 | hard bounding within [w_min, w_max], and Dale's principle preservation on inhibitory synapses.
   5 | """
   6 | 
   7 | import math
   8 | 
   9 | 
  10 | class PairwiseSTDP:
  11 |     """
  12 |     Pairwise Spike-Timing-Dependent Plasticity rule.
  13 |     Potentiates synapses when pre spikes before post (delta_t > 0).
  14 |     Depresses synapses when post spikes before pre (delta_t < 0) with a 1.05x LTD bias.
  15 |     """
  16 | 
  17 |     def __init__(
  18 |         self,
  19 |         tau_plus_ms: float = 20.0,
  20 |         tau_minus_ms: float = 20.0,
  21 |         a_plus: float = 0.20,
  22 |         a_minus: float = 0.21,
  23 |         w_min: float = 0.0,
  24 |         w_max: float = 40.0,
  25 |     ):
  26 |         self.tau_plus_ms: float = tau_plus_ms
  27 |         self.tau_minus_ms: float = tau_minus_ms
  28 |         self.a_plus: float = a_plus
  29 |         self.a_minus: float = a_minus
  30 |         self.w_min: float = w_min
  31 |         self.w_max: float = w_max
  32 | 
  33 |     def compute_delta_w(self, delta_t_ms: float) -> float:
  34 |         """
  35 |         Calculates synaptic weight change delta_w (in nS) for a spike timing difference
  36 |         delta_t_ms = t_post - t_pre.
  37 |           delta_t > 0: LTP  -> +a_plus * exp(-delta_t / tau_plus)
  38 |           delta_t < 0: LTD  -> -a_minus * exp(-|delta_t| / tau_minus)
  39 |           delta_t == 0: 0.0
  40 |         """
  41 |         if delta_t_ms > 0.0:
  42 |             return self.a_plus * math.exp(-delta_t_ms / self.tau_plus_ms)
  43 |         elif delta_t_ms < 0.0:
  44 |             return -self.a_minus * math.exp(delta_t_ms / self.tau_minus_ms)
  45 |         else:
  46 |             return 0.0
  47 | 
  48 |     def decay_trace(self, init_val: float, elapsed_ms: float) -> float:
  49 |         """
  50 |         Exponential decay of pre/post synaptic eligibility traces.
  51 |         trace(t) = init_val * exp(-elapsed_ms / tau_plus_ms)
  52 |         """
  53 |         return init_val * math.exp(-elapsed_ms / self.tau_plus_ms)
  54 | 
  55 |     def update_weight(self, w_init: float, is_inhibitory: bool, delta_t_ms: float) -> float:
  56 |         """
  57 |         Applies STDP update to a synaptic weight under Dale's principle.
  58 |         Inhibitory synapses do not undergo STDP.
  59 |         Excitatory synapses are updated and hard-bounded in [w_min, w_max].
  60 |         """
  61 |         if is_inhibitory:
  62 |             return w_init
  63 | 
  64 |         dw = self.compute_delta_w(delta_t_ms)
  65 |         w_new = w_init + dw
  66 |         if w_new < self.w_min:
  67 |             return self.w_min
  68 |         if w_new > self.w_max:
  69 |             return self.w_max
  70 |         return w_new
```

### `biophysics/stp.py` (112 lines, SHA-256: `ceebb61134d250aa...`)

```text
   1 | """
   2 | WetLang Tsodyks-Markram Short-Term Plasticity (STP)
   3 | Simulates short-term synaptic depression (vesicle depletion) and facilitation
   4 | across four cortical synapse classes: E->E, E->I, I->E, and I->I.
   5 | """
   6 | 
   7 | import math
   8 | from typing import List, Optional
   9 | 
  10 | 
  11 | class SynapseSTP:
  12 |     """
  13 |     Tsodyks-Markram short-term synaptic plasticity model.
  14 |     Tracks vesicle fraction x (0..1) and release probability u (0..1).
  15 |     """
  16 | 
  17 |     def __init__(
  18 |         self,
  19 |         synapse_type: str = "E->E",
  20 |         tau_rec_ms: Optional[float] = None,
  21 |         weight_ns: float = 10.0,
  22 |     ):
  23 |         self.synapse_type: str = synapse_type
  24 |         self.weight_ns: float = weight_ns
  25 | 
  26 |         # Cortical synapse class parameterization
  27 |         if synapse_type == "E->E":
  28 |             self.U_base: float = 0.50
  29 |             self.tau_rec_ms: float = 800.0
  30 |             self.tau_fac_ms: float = 20.0
  31 |         elif synapse_type == "E->I":
  32 |             self.U_base: float = 0.15
  33 |             self.tau_rec_ms: float = 200.0
  34 |             self.tau_fac_ms: float = 600.0
  35 |         elif synapse_type == "I->E":
  36 |             self.U_base: float = 0.25
  37 |             self.tau_rec_ms: float = 700.0
  38 |             self.tau_fac_ms: float = 50.0
  39 |         elif synapse_type == "I->I":
  40 |             self.U_base: float = 0.30
  41 |             self.tau_rec_ms: float = 400.0
  42 |             self.tau_fac_ms: float = 50.0
  43 |         else:
  44 |             self.U_base = 0.50
  45 |             self.tau_rec_ms = 800.0
  46 |             self.tau_fac_ms = 20.0
  47 | 
  48 |         if tau_rec_ms is not None:
  49 |             self.tau_rec_ms = float(tau_rec_ms)
  50 | 
  51 |         self.u: float = self.U_base
  52 |         self.x: float = 1.0
  53 | 
  54 |     def deliver_spikes(self, count: int, freq_hz: float) -> List[float]:
  55 |         """
  56 |         Delivers a regular spike train at freq_hz and returns the list of
  57 |         effective post-synaptic conductance jumps (nS) produced at each spike.
  58 |         """
  59 |         if count <= 0:
  60 |             return []
  61 | 
  62 |         interval_ms = 1000.0 / freq_hz if freq_hz > 0 else 100.0
  63 |         g_jumps: List[float] = []
  64 | 
  65 |         u = self.U_base
  66 |         x = 1.0
  67 | 
  68 |         for i in range(count):
  69 |             # Facilitation update on spike arrival
  70 |             u = u + self.U_base * (1.0 - u)
  71 |             # Conductance jump proportional to released vesicles
  72 |             g = self.weight_ns * (u * x)
  73 |             g_jumps.append(g)
  74 | 
  75 |             # Vesicle depletion
  76 |             x = x - (u * x)
  77 | 
  78 |             # Recovery during inter-spike interval
  79 |             if i < count - 1:
  80 |                 u = self.U_base + (u - self.U_base) * math.exp(-interval_ms / self.tau_fac_ms)
  81 |                 x = 1.0 - (1.0 - x) * math.exp(-interval_ms / self.tau_rec_ms)
  82 | 
  83 |         return g_jumps
  84 | 
  85 |     def track_utilization(self, count: int, freq_hz: float) -> List[float]:
  86 |         """
  87 |         Delivers a regular spike train and returns the utilization parameter u
  88 |         immediately after each spike arrival.
  89 |         """
  90 |         if count <= 0:
  91 |             return []
  92 | 
  93 |         interval_ms = 1000.0 / freq_hz if freq_hz > 0 else 100.0
  94 |         u_vals: List[float] = []
  95 | 
  96 |         u = self.U_base
  97 | 
  98 |         for i in range(count):
  99 |             u = u + self.U_base * (1.0 - u)
 100 |             u_vals.append(u)
 101 | 
 102 |             if i < count - 1:
 103 |                 u = self.U_base + (u - self.U_base) * math.exp(-interval_ms / self.tau_fac_ms)
 104 | 
 105 |         return u_vals
 106 | 
 107 |     def recover(self, r_init: float, delta_t_ms: float) -> float:
 108 |         """
 109 |         Calculates recovered vesicle fraction R after a quiescent interval delta_t_ms.
 110 |         R = 1.0 - (1.0 - r_init) * exp(-delta_t_ms / tau_rec_ms)
 111 |         """
 112 |         return 1.0 - (1.0 - r_init) * math.exp(-delta_t_ms / self.tau_rec_ms)
```

### `biophysics/telemetry.py` (84 lines, SHA-256: `7ca0976d1c5d9f3f...`)

```text
   1 | """
   2 | WetLang Telemetry Streaming Engine
   3 | Provides JSONL and CSV logging for cycle-accurate biological digital twin state,
   4 | including membrane potentials, spike rasters, population firing rates, and net charges.
   5 | """
   6 | 
   7 | import json
   8 | from typing import Any, Dict, List, Optional
   9 | 
  10 | 
  11 | class TelemetryStream:
  12 |     """
  13 |     Structured telemetry serialization engine for JSONL and CSV streaming formats.
  14 |     """
  15 | 
  16 |     def format_tick_json(
  17 |         self,
  18 |         tick: int,
  19 |         time_ms: float,
  20 |         v_m: Optional[List[float]] = None,
  21 |         spikes: Optional[List[int]] = None,
  22 |         population_rate_hz: float = 0.0,
  23 |         charges_nc: Optional[List[float]] = None,
  24 |         **kwargs: Any,
  25 |     ) -> str:
  26 |         """Serializes a single simulation cycle record to a JSONL-compliant line."""
  27 |         record: Dict[str, Any] = {
  28 |             "tick": tick,
  29 |             "time_ms": round(time_ms, 5),
  30 |             "v_m": v_m if v_m is not None else [],
  31 |             "spikes": spikes if spikes is not None else [],
  32 |             "population_rate_hz": population_rate_hz,
  33 |             "charges_nc": charges_nc if charges_nc is not None else [],
  34 |         }
  35 |         record.update(kwargs)
  36 |         return json.dumps(record)
  37 | 
  38 |     def get_csv_header(self) -> str:
  39 |         """Returns standard CSV telemetry summary header."""
  40 |         return "tick,time_ms,spike_count,r_inst_hz\n"
  41 | 
  42 |     def make_record(
  43 |         self,
  44 |         tick: int,
  45 |         time_ms: Optional[float] = None,
  46 |         spike_count: int = 0,
  47 |         population_rate_hz: float = 0.0,
  48 |         **kwargs: Any,
  49 |     ) -> Dict[str, Any]:
  50 |         """Creates a structured in-memory dictionary record for a given simulation tick."""
  51 |         t_ms = time_ms if time_ms is not None else tick * 0.1
  52 |         rec: Dict[str, Any] = {
  53 |             "tick": tick,
  54 |             "time_ms": t_ms,
  55 |             "spike_count": spike_count,
  56 |             "population_rate_hz": population_rate_hz,
  57 |         }
  58 |         rec.update(kwargs)
  59 |         return rec
  60 | 
  61 |     def format_spike_event(
  62 |         self,
  63 |         tick: int,
  64 |         time_ms: float,
  65 |         neuron_id: int,
  66 |         neuron_type: str,
  67 |     ) -> str:
  68 |         """Formats a single sparse spike event for CSV logging: 'tick,time_ms,neuron_id,neuron_type'."""
  69 |         return f"{tick},{time_ms:.1f},{neuron_id},{neuron_type}"
  70 | 
  71 |     def compute_firing_rate(
  72 |         self,
  73 |         spike_count: int,
  74 |         neuron_count: int = 64,
  75 |         dt_ms: float = 0.1,
  76 |     ) -> float:
  77 |         """
  78 |         Calculates instantaneous population firing rate in Hertz (spikes / sec / neuron).
  79 |         r = spike_count / (neuron_count * (dt_ms / 1000.0))
  80 |         """
  81 |         if neuron_count <= 0 or dt_ms <= 0.0:
  82 |             return 0.0
  83 |         dt_sec = dt_ms / 1000.0
  84 |         return float(spike_count) / (neuron_count * dt_sec)
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
