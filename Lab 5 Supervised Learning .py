#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[63]:


# import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as sm

# load nbaallelo.csv into a dataframe
df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\nbaallelo.csv")

# Converts the feature "game_result" to a binary feature and adds as new column "wins"
wins = df.game_result == "W"
bool_val = np.multiply(wins, 1)
wins = pd.DataFrame(bool_val, columns = ["game_result"])
wins_new = wins.rename(columns = {"game_result": "wins"})
df_final = pd.concat([df, wins_new], axis=1) 

# split the data df_final into training and test sets with a test size of 0.3 and random_state = 0
train, test = train_test_split(df_final, test_size=0.3, random_state=0)

# construct a logistic model with wins and the target and elo_i as the predictor, using the training set
lm = sm.logit(formula = 'wins ~ elo_i', data=train).fit()

# print coefficients for the model
print(lm.params)


# ## Question 2

# In[64]:


# import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# load nbaallelo.csv into a dataframe
df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\nbaallelo.csv")

# Converts the feature "game_result" to a binary feature and adds as new column "wins"
wins = df.game_result == "W"
bool_val = np.multiply(wins, 1)
wins = pd.DataFrame(bool_val, columns = ["game_result"])
wins_new = wins.rename(columns = {"game_result": "wins"})
df_final = pd.concat([df, wins_new], axis=1) 

# split the data df_final into training and test sets with a test size of 0.3 and random_state = 0
train, test = train_test_split(df_final, test_size=0.3, random_state=0)

# build the logistic model using the LogisticRegression function with wins as the target variable and elo_i as the predictor. 
model = LogisticRegression(solver = 'lbfgs')
model.fit(train[['elo_i']], train[['wins']].values.ravel())

# use the test set to predict the wins from the elo_i score
predictions = model.predict(test[['elo_i']])

# generate confusion matrix
conf = confusion_matrix(test[['wins']], predictions)

print("confusion matrix is \n", conf)

# calculate the sensitivity
sens = conf[0,0]/(conf[0,0]+conf[0,1])
print("Sensitivity is ", sens)

# calculate the specificity
spec = conf[1,1]/(conf[1,0]+conf[1,1])
print ("Specificity is ", spec)

