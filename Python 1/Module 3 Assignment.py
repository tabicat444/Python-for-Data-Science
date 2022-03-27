#!/usr/bin/env python
# coding: utf-8

# # Assignment 3
# Tabitha Belshee

# ## Question 1
# 
# Pass is a bit of a placeholder. It does not do anything necessarily but is an indicator that there's no code currently available to run BUT that won't always be the case. Continue has a very active role, and indicates that the loop should be redirected to begin the next iteration of the loop.

# ## Question 2
# 
# The output of the code is "Hi there, This is how a pass statement works!" 
# 
# For each letter within "letter", the code checks whether it's "mn". Clearly, it'll never be "mn" so this is a perfect use of a pass statement. Syntactically, something needs to go after the if statement but that code will never run. Then the code moved on to check if the current letter is a "z", which is printed as a space. If it wasn't a "z", then the else statement indicates the letter should just be printed as itself. 

# In[4]:


## Question 3


# In[8]:


print("What shall I wear today?")

name = input("Please Enter Your First Name: ")
temp = float(input("What is Today's Temperature: "))

if temp < 70:
    choice = "You should probably bring a sweater"
else: 
    choice = "It will be a warm day, T-shirt time!"

print("Hi " + name + ", " + choice)


# In[9]:


print("What shall I wear today?")

name = input("Please Enter Your First Name: ")
temp = float(input("What is Today's Temperature: "))

if temp < 70:
    choice = "You should probably bring a sweater"
else: 
    choice = "It will be a warm day, T-shirt time!"

print("Hi " + name + ", " + choice)

