#!/usr/bin/env python
# coding: utf-8

# # Module 7 Assignment
# Tabitha Belshee

# ## Question 1

# In[6]:


tau = int(input())
print("The value of Tau is ", '{:^8}'.format(tau), ", which is two times ", '{:^8}'.format(tau/2), ".")


# ## Question 2

# In[17]:


bytes = int(input("Enter number of Bytes you would like to determine the signed range of: "))
bits = bytes * 8
nums = 2**bits

print(bytes, " Byte(s) integral type with 8 bits can encode " + "{:,}".format(nums), "numbers. The signed range will be from -" + "{:,}".format(int(nums/2)), " to", "{:,}".format(int(nums/2)))


# ## Question 3

# In[16]:


from decimal import *
def rms(tempC):
    R = 8.3145
    T = tempC + 273
    M = 0.032
    temp = Decimal((3 * R * T)/M)
    temp = temp.sqrt()
    return temp.quantize(Decimal('1.000'))

temperatureC = 100

print('The average velocity or root mean square velocity of a molecule in a sample of oxygen at ' +
      str(temperatureC) + ' degrees Celsius is ' + str(rms(temperatureC)) + ' m/sec.')
    

