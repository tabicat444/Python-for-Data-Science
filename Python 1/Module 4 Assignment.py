#!/usr/bin/env python
# coding: utf-8

# 
# # Module 4 Assignment 
# Tabitha Belshee

# ## Question 1
# A function in Python is an instruction that executes some code. Depending on the function's purpose, the function may take in some information, arguments, or it may not. 

# ## Question 2
# Parameters and arguments often end up referring to the same values when a funciton is being run. The difference is that parameters are the placeholders in a function that take the value of the arguments each time the function is run. The arguments are then referenced via the parameters' names inside the function.

# ## Question 3 
# The code produces: "Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution - Albert Einstein" 
# The functions run in the order they're called (aka quote(), day(), ofthe(), influencers(), famous(), and name()) and print their contents in that order.

# ## Question 4

# In[1]:


#a - build the function
import math 

def velocityFinal (vo, a, d):
    '''find the final velocity from initial velocity, acceleration, and distance'''
    v = round(math.sqrt(vo**2 + (2*a*d)), 1)
    return v
    
#b and c - call for the ball and answer
# velocityFinal(0, 9.8, 51)
print(str(velocityFinal(0, 9.8, 51)) + ' m/s')


# ## Question 5

# In[12]:


# v = u + at
# therefore t = (v - u)/a
def elapsedTime (u, v, a):
    t = round((v - u)/a ,1)
    return t

print(str(elapsedTime(0, 31.6, 9.8)) + ' s')

