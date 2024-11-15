import pandas as pd
import numpy as np


# Define number of trials
n_trials = 100

# Generate random stimulus values for each trial
data = {
    "Trial": np.arange(1, n_trials + 1),
    "Stimulus 1 value": np.random.uniform(0, 1, n_trials),  # Random mean values for Stimulus 1
    "Stimulus 1 std": np.random.uniform(0.1, 0.5, n_trials),  # Random std deviations for Stimulus 1
    "Stimulus 2 value": np.random.uniform(0, 1, n_trials),  # Random mean values for Stimulus 2
    "Stimulus 2 std": np.random.uniform(0.1, 0.5, n_trials)  # Random std deviations for Stimulus 2
}

# Create DataFrame
stim_pairs_df = pd.DataFrame(data)

# Save to CSV
stim_pairs_df.to_csv("experiment_stim_pairs.csv", index=False)
print("Stimulus pairs file created: experiment_stim_pairs.csv")