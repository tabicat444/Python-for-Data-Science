#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[71]:


import pandas as pd
import statsmodels.api as sms
from statsmodels.formula.api import ols


# create a new column of the difference in points
df['y'] = df['pts'] - df['opp_pts']

# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\nbaallelo_slr.csv")

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] =  nba['pts'] - nba['opp_pts']

# Perform simple linear regression on y and elo_i
results = ols('y~elo_i', data=nba).fit()

# Create an analysis of variance table
aov_table = sms.stats.anova_lm(results)

# Print the analysis of variance table
print(aov_table)


# In[72]:


## Question 2


# In[73]:


import numpy as np
import pandas as pd
import statsmodels.formula.api as sms

# load the file internetusage.csv
internet = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\internetusage.csv")

internet.columns
# fit a linear model using the sms.ols function and the internet dataframe
model = sms.ols('internet_usage~bachelors_degree', data=internet).fit()

bach_percent = float(input())

# use the model.predict function to find the predicted value for internet_usage using 
# the bach_percent value for the predictor
d = {"bachelors_degree": [bach_percent]}
test = pd.DataFrame(d)
test
prediction = model.predict(test)

print(prediction)


# In[74]:


## Question 3


# In[75]:


#Import the necessary modules
import pandas as pd

# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\nbaallelo_slr.csv")

# Display the correlation matrix for the columns elo_i, pts, and opp_pts
print(nba[['elo_i', 'pts', 'opp_pts']].corr())

# Create a new column in the data frame that is the difference between pts and opp_pts
# Code to find the difference between the columns pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts']
    
# Display the correlation matrix for elo_i and y
print(nba[['elo_i', 'y']].corr())


# In[76]:


## Question 4


# In[77]:


#Import the necessary modules
import pandas as pd
import statsmodels.api as sms
from statsmodels.formula.api import ols

# Code to read in nbaallelo_slr.csv
nba = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\nbaallelo_slr.csv")

# Perform multiple linear regression on pts, elo_i, and opp_pts
results = ols('pts~elo_i + opp_pts', data=nba).fit()

# Create an analysis of variance table
aov_table = sms.stats.anova_lm(results)

# Print the analysis of variance table
print(aov_table)

