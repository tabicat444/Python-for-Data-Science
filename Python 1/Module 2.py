#!/usr/bin/env python
# coding: utf-8

# # Module 2 Assignment 
# by Tabitha Belshee

# In[1]:


## Question 1


# In[2]:


name = str(input("Enter your first name: ")) 
print("Welcome " + name + " to Comp 600!")


# In[3]:


## Question 2


# In[4]:


length = 10.0
width = 7
print(width//2)
print(type(width//2))
print(length/2.0)
print(type(length/2.0))
print(length/2)
print(type(length/2))
print(1 + 4 * 5)
print(type(1 + 4 * 5))


# In[5]:


## Question 3


# In[6]:


pounds = float(input("Please enter the mass in lb that you would like to convert to kg: "))
kg =  pounds/2.20462
print("The converted mass in kg is: " + str(kg))
earth = kg * 9.807
print("Your weight on Earth is: " + str(earth) + " Newtons")
moon = kg * 1.62
print("Your weight on the Moon is: " + str(moon) + " Newtons")
comp = (moon/earth) * 100
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth: " + str(comp) + "%")
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is " + str(round(comp)) + "%")

