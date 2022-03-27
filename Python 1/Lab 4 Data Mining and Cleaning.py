#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[23]:


# Import the necessary modules
import pandas as pd

hmeq = pd.read_csv(r"C:\Users\tbels\Downloads\hmeq_small.csv")

# Create a new data frame with the rows with missing values dropped
df1 = hmeq.dropna()

# Create a new data frame with the missing values filled in by the mean of the column
df2 = hmeq.fillna(hmeq.mean())

# Print the means of the columns for each new data frame
print("Means for df1 are ", df1.mean())

print("Means for df2 are ", df2.mean())


# ## Question 2

# In[24]:


# Import the necessary modules
import pandas as pd
from sklearn import preprocessing

hmeq = pd.read_csv(r"C:\Users\tbels\Downloads\hmeq_lab412.csv")

# Standardize the data
standardized = preprocessing.scale(hmeq)

# Output the standardized data as a data frame
df1 = pd.DataFrame(standardized, columns = ['LOAN', 'MORTDUE', 'VALUE', 'YOJ', 'CLAGE', 'CLNO', 'DEBTINC'])

# Normalize the data
normalized = preprocessing.MinMaxScaler().fit_transform(hmeq)

# Output the standardized data as a data frame
df2 = pd.DataFrame(normalized, columns = ['LOAN', 'MORTDUE', 'VALUE', 'YOJ', 'CLAGE', 'CLNO', 'DEBTINC'])

# Print the means and standard deviations of df1 and df2
print("The means of df1 are ", df1.mean())
print("The standard deviations of df1 are ", df1.std())
print("The means of df2 are ", df2.mean())
print("The standard deviations of df2 are ", df2.std())

