import os
import subprocess as sp
import glob
import numpy as np


yaml_files = glob.glob(f'/work/pi_casey_umass_edu/Owen/lulc_lstm/GRU_configs/*')

#get slurm job array index for parallel
#just change "fold" values into slurm array IDs, "slurm_idx"
slurm_idx = int(os.environ['SLURM_ARRAY_TASK_ID'])

sp.run(['/home/oryerson_umass_edu/.conda/envs/neuralhydrology/bin/nh-run',
        'train', '--config-file', 
        yaml_files[slurm_idx-1]])
    
print(yaml_files[slurm_idx-1])
