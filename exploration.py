import pandas as pd
import numpy as np

df = pd.read_csv('training_history.csv')

mean = df["Measured Stimulus"].mean()
std = df["Measured Stimulus"].std()

print(mean, std)
experiment_stimuli = []
stimuli_df = pd.DataFrame()

ex_df = pd.read_csv('experiment_results.csv')
ex_df["True Value"] = ex_df["Stim"]