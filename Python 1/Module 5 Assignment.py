#!/usr/bin/env python
# coding: utf-8

# # Module 5 Assignment
# Tabitha Belshee

# ## Question 1
# The Base Case is how the action knows to stop. Once this Case is reached, the function/loop does not continue and instead returns the value or otherwise stops running. 

# ## Question 2

# In[5]:


def FactorialFortress(num):
    '''Returns the value of the factorial of a number'''
    if num < 0:
        print("Here, let me flip the sign for you.")
        num = -num
        
    if num == 0: 
        return 1
    else: 
        return num * FactorialFortress(num - 1)
        
print(FactorialFortress(4))
print(FactorialFortress(-4))


# ## Question 3

# In[7]:


def SumSum(num):
    '''Returns the sum of 1-input'''
    if num < 0:
        print("Here, let me flip the sign for you.")
        num = -num
        
    if num == 0: 
        return 0
    else: 
        return num + SumSum(num - 1)
    
print(SumSum(3))
print(SumSum(4))


# ## Question 4
# The semordnilap function (aka palindrome function) takes the indexed letter and prints it, while also increasing the iterator to the next value. The function effectively prints the input word backwards.

# ## Question 5

# In[13]:


(lambda x: x**x)(4)


# ## Question 6

# In[15]:


import math 

def area_circle(rad):
    area = math.pi * rad**2
    return area

area_circle(3)


# ## Question 7

# In[17]:


import math 

(lambda rad: math.pi * (rad**2))(3)


# ## Question 8

# In[44]:


#a. 
import math
def DoubleTime(apr):
    if apr > 1: 
        apr = apr/100
    return round(math.log10(2)/math.log10(1 + (apr/12)), 1)

print(str(DoubleTime(1.85)), "months")

#b. 
print(str((lambda apr: round(math.log10(2)/math.log10(1 + (apr/100/12)), 1))(1.85)), "months")

#c
print(str(round(DoubleTime(3)/12, 1)), "years")

