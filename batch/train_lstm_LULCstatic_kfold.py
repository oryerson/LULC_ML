import os
import subprocess as sp
import glob
import numpy as np


yaml_files = glob.glob(f'/work/pi_casey_umass_edu/Owen/lulc_lstm/configs/config_file_LSTM_basins_test_LULCstatic_*')

#get slurm job array index for parallel

slurm_idx = int(os.environ['SLURM_ARRAY_TASK_ID'])

sp.run(['/home/oryerson_umass_edu/.conda/envs/neuralhydrology/bin/nh-run',
        'train', '--config-file', 
        yaml_files[slurm_idx-1]])
    
print(yaml_files[slurm_idx-1])
