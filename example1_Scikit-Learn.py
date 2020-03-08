import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# Load the data
oecd_bli=pd.read_csv("oecd_bli_2015.csv",thousands=',')
gdp_per_capita=pd.read_csv("gdp_per_capita.csv",thousands=',',delimeter='\t',encodin='latin1',na_values="n/a")

# Prepare the data
# country_stats=prepare_country_stats(oecd_bli,gdp_per_capita)
# X=np.c_[country_stats["GDP per capita"]]
# Y=np.c_[country_stats["Life satisfaction"]]

# Visualize the data

# Select a linear model

# Train the model

# Make a prediction for Cryrus
