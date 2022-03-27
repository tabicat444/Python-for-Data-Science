#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1 - Measures of Center
import pandas as pd
import statistics

df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\mtcars.csv")

mean = statistics.mean(df.wt)
median = statistics.median(df.wt)
mode = statistics.mode(df.wt)

print("mean = ", mean, ", median = ", median, ", mode = ", mode)


# In[2]:


# Question 2 - Standard Deviation

import pandas as pd

import scipy.stats as st

NBA2019_df = pd.read_csv(r"C:\Users\tbels\Downloads\NBA2019.csv")

# Input desired column. Ex: AGE, 2P%, or PointsPerGame.
chosen_column = str(input())

# Create subset of NBA2019_df based on input.
NBA2019_df_column = NBA2019_df[[chosen_column]]

# Find standard deviation and round to two decimal places. 
sample_s = st.tstd(NBA2019_df_column)
sample_s_rounded = round(sample_s, 2) #The student has incorrectly used the round() function.

# Output
print('The standard deviation for', chosen_column, 'is', sample_s_rounded)


# In[3]:


# Question 3 - 5 Number Summary

import pandas as pd
import numpy as np 

df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\internetusage.csv")
internet = df[['internet_usage']]
internet["internet_usage"]


table = {'mean': round(statistics.mean(internet["internet_usage"]),6), 
         'std': round(statistics.stdev(internet["internet_usage"]),6), 
         'min': round(np.min(internet["internet_usage"]),6), 
         '25%': round(np.quantile(internet["internet_usage"], 0.25),6),
         '50%': round(np.quantile(internet["internet_usage"], 0.50),6), 
         '75%': round(np.quantile(internet["internet_usage"], 0.75),6), 
         'max': round(np.max(internet["internet_usage"]),6)}
print('internet_usage')
for key, value in table.items():
     print(f'{key:10}    {value:10}')


# In[6]:


# Question 4 - Box Plots

import pandas as pd
df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\internetusage.csv")
population = df[['State', 'Population']]

state_index = int(input())
state = population.iloc[[state_index]]
state_name = state.iloc[0][0]
state_pop = state.iloc[0][1]
print("The population of " + str(state_name) + " is " + str(state_pop)+ ".")


# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt

bp = sns.boxplot(y= 'Population', data=population, orient = 'v')
 
ylabels = ['{:,.1f}'.format(x) + 'M' for x in bp.get_yticks()/1000000]
bp.set_yticklabels(ylabels)
bp = sns.swarmplot(y='Population', data=population, color="grey")

bp.set_title('Box Plot for State Populations in the US (Millions Excluding Territories)')
bp.set_ylabel(' ')
bp.set_xlabel('Population')

plt.show()

