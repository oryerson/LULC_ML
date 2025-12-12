#!/bin/bash 
#SBATCH --job-name=LSTM_Static
#SBATCH --open-mode=append 
#SBATCH --output=./logs_train/train.out 
#SBATCH --error=./logs_train/train-err.out 
#SBATCH --partition=gpu-preempt,gpu 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cpus-per-task=20
#SBATCH --mem=300G 
#SBATCH --time=2880
#SBATCH --gres=gpu:1
#SBATCH --array=1-5

#time stamp 
TZ='America/New_York' date 
echo "Job started on $(hostname)"

module load conda/latest
module load cuda/11.8    

#run code 
python3 -u train_lstm_LULCstatic_kfold.py 

echo "Job finished."

#time stamp 
TZ='America/New_York' date
