# Instructions for MC/DC's ICSBEP validation suite

This continuous energy criticality validation test suite is taken from OpenMC's benchmark repository: https://github.com/mit-crpg/benchmarks/tree/master/icsbep

It contains several hundred criticality problems from the international criticality safety benchmark evaluation project (ICSBEP). Currently only 118 of them translate and run with the current state of the translator.


## Running problems:

Inside the icsbep directory, the icsbep_translator.ipynb file is a slightly modified version of the OpenMC to MC/DC xml translator found in the CEMeNT organization's repositories (may be private).

There is also an openmc directory which houses all the folders for the input decks and the bash scripts to run them. Inside each problem directory, an openmc directory has subdirectories for each case, and an mcdc directory places all the translated input files in a single place.

Inside the base icsbeb/openmc directory, there are two bash scripts: run_mcdc.sh and run_openmc.sh. These should scan all subdirectories, create slurm submission scripts for each input deck, and submit those decks to the pbatch partition. Please note that this has been set up for LLNL's Dane machine, and each of these input scripts will need to be customized to the user.

The python script collect_results.py will scan those subdirectories and scrape the keff results for both codes.

Also note that OpenMC's default submission scripts have been left in, but they will not work for MC/DC or on LLNL's systems.
