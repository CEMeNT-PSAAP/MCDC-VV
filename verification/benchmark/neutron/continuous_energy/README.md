# Continuous-energy verification

The continuous-energy benchmarks require a nuclear-data library generated with the same MC/DC version used to run the cases.

Set `MCDC_LIB` to the generated HDF5 library before launching a benchmark:

```bash
export MCDC_LIB=/path/to/mcdc/library
```

Generate or refresh the library with MC/DC's `tools/data_library_generator/neutron/generate.py` utility.
The source ACE data location is configured with `MCDC_ACELIB`; see the generator's README in the MC/DC repository for installation and invocation details.

The benchmark inputs perform a lightweight schema check before compiling so an outdated library produces an actionable error rather than a low-level HDF5 exception.
