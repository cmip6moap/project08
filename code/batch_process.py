
import glob
import numpy as np
import subprocess

# Load SSP directories
realisation = 'ssp126'
ssp_files = glob.glob('/badc/cmip6/data/CMIP6/ScenarioMIP/*/*/{}/*/Amon/tas/*/latest/*.nc'.format(realisation))
ssp_model_reals = ['/'.join(file.split('/')[:-1]) for file in ssp_files]
id_ssp = np.unique(['/'.join(np.asarray(file.split('/'))[np.array([6,7,9])]) for file in ssp_files])

# Load hist directories
hist_files = glob.glob('/badc/cmip6/data/CMIP6/CMIP/*/*/historical/*/Amon/tas/*/latest/*.nc')
hist_model_reals = ['/'.join(file.split('/')[:-1]) for file in hist_files]
id_hist = np.unique(['/'.join(np.asarray(file.split('/'))[np.array([6,7,9])]) for file in hist_files])

# Find which model runs are in both
models_to_load = np.intersect1d(id_ssp, id_hist)

# Confirm which ssp dirs to load
ssp_dirs_to_load = []
for ssp_dir in ssp_model_reals:
    if '/'.join(np.asarray(ssp_dir.split('/'))[np.array([6,7,9])]) in models_to_load:
        ssp_dirs_to_load.append(ssp_dir)
ssp_dirs_to_load = np.unique(ssp_dirs_to_load)
assert len(ssp_dirs_to_load) == len(models_to_load)

#Confirm which hist dirs to load
hist_dirs_to_load = []
for hist_dir in hist_model_reals:
    if '/'.join(np.asarray(hist_dir.split('/'))[np.array([6,7,9])]) in models_to_load:
        hist_dirs_to_load.append(hist_dir)
hist_dirs_to_load = np.unique(hist_dirs_to_load)
assert len(hist_dirs_to_load) == len(ssp_dirs_to_load)

# Fire this to a batch command
for i in range(len(hist_dirs_to_load)): #len(hist_dirs_to_load)
    hist_dir = hist_dirs_to_load[i]
    ssp_dir = ssp_dirs_to_load[i]

    job_name = "_".join(np.array(ssp_dir.split('/'))[[6,7,9]])
    subprocess.call(["sbatch",
                        "-p", "short-serial-4hr",#short-serial-4hr
                        "--time=00:05:00",
                        "--time-min=00:05:00",
                        "--job-name= " + job_name,
                        "--output= " + job_name + ".out",
                        "--error= " + job_name + ".err",
                        "anom_regrid.py",
                        hist_dir,
                        ssp_dir
                        ])
                                                                                                                                                                           1,1           Top
