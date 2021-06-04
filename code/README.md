# Code for preprocessing on JASMIN using the LOTUS batch service

File 'batch_process.py' collects, regrids, and finds the anomaly of all CMIP6 models for a specified scenario calling anom_regrid.py

File MMM_processing performs a multi model mean, grouping multiple realisations from the same model together first, therefore avoiding biasing the ensemble output towards models that run lots of realisations
