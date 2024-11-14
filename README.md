### ANACONDA ###

Install miniconda, see : https://docs.anaconda.com/miniconda/

From a terminal, move to an appropriate folder of your choice.

Run the following command:
    conda env create -f environment.yml
    conda activate bmcb
    python run_simple.pyc
    
A window called Agent Simulation Interface should open.
Try if everything works well:
- Click on Start Learning (2000 Trials) => This should save a file called training_history.csv
- Click on Load Stimuli Pairs CSV and select the experiment_stim_pairs_csv file then click on Run Experiment => This should save a file called experiment_results.csv


Agent is eating apple depending on the color which is the value of the stimuli.

We want to have an agent that is trained which is adapted to its environment

### What do we wat
Learn the distribution of the posterior: Given that the apple is a certain color how will his health be affected.
We want it to learn the prior

### Stimuls files
Controling the color of the apple with a real number
tells us wether stimulus is more "redish" than stimulus two for example
Pair of stimuli we want the agent to compare as stim1 > stim2
These are priod definitions as normal distributions

**idea**: analyze the behaviour of the agent

#### Experiment results
same columns of the stimuls
last column is the comparison results made by the agent that stimulus 1 > stimulus 2

### Training history files
The measured value of the stimulus by the agent

###
with pair of stimuli we can check if it is bigger

If we change the stimuli so that they are close 


#### Psychometric 
we need to simulate the code multiple times to 