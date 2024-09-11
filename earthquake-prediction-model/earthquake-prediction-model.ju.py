# %% [markdown]
"""
# Earthquake Prediction Model with Machine Learning

Followed via [this](https://thecleverprogrammer.com/2020/11/12/earthquake-prediction-model-with-machine-learning/) link.
"""

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("./data.csv")
df

# %%
df.columns

# %% [markdown]
"""
counting the number of Earthquakes
"""

# %%
df['Type'].unique()
df['Type'].value_counts()

