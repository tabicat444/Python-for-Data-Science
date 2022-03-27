#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1 - Importing Modules
import numpy as np
import scipy.stats as st

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

x = np.array([x1, x2, x3, x4])
y = np.array([0, 10, 7, 25])

print(st.linregress(x,y))


# In[2]:


# Question 2 - Data Frames
import pandas as pd

cars_df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\Cars.csv")

userNum = int(input())
cars_sub = cars_df[0:userNum]
print("Quality", cars_sub["Quality"].max())
print("Speed", cars_sub["Speed"].max())
print("Angle", cars_sub["Angle"].max())


# In[3]:


# Question 3 - Subsetting Data Frames
import pandas as pd

cylinders = int(input())
df = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\mtcars.csv")
df_cyl = df[df.cyl == cylinders]
print(df_cyl.shape)


# In[4]:


# Question 4 - Bar Charts
import seaborn as sns 

titanic = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\titanic.csv")

first_south = titanic[(titanic.pclass == 1) & (titanic.embarked == "S")]

second_third = titanic[(titanic.pclass == 2) | (titanic.pclass == 3)]

print(first_south.head())
print(second_third.head())



# In[5]:


fs = sns.countplot(x = "pclass", hue = "sex", data = first_south)
fs.set_xlabel("Passenger Class")
fs.set_ylabel("Count")


# In[6]:


st = sns.countplot(x = "pclass", hue = "survived", data = second_third)
st.set_xlabel("Passenger Class")
st.set_ylabel("Count")


# In[7]:


# Question 5 - Line Chart
import pandas as pd

tgt = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\target.csv")

tgt_march = tgt.tail(19)

tgt_vol = tgt_march[["Date", "Volume"]]

tgt_close = tgt_march[["Date", "Close"]]

day = int(input()) - 1

volume_row = tgt_vol.iloc[[day]]
volume = volume_row.iloc[0][1] # gets the volume for the given day

close_row = tgt_close.iloc[[day]]
close = close_row.iloc[0][1] # gets the closing stock price for the given day

date = tgt_march.iloc[[day]].iloc[0][0] # gets the date


print("The volume of TGT on", date, "is", str(int(volume)) + ".")
print("The closing stock price of TGT on", date, "is", "$" + str(close) + ".")


# In[8]:


import matplotlib.pyplot as plt

# title
plt.title('March 2018 Trading Volume for Target Stock', fontsize = 20)

# x and y axis labels
plt.xlabel('Date')
plt.ylabel('Number of Trades')

plt.xticks(np.arange(0,30,5))

# plot
plt.plot(tgt_vol["Date"], tgt_vol["Volume"])

# saves the image
plt.savefig("linechart.png")

# shows the image
plt.show()


# In[9]:


# title
plt.title('March 2018 Market Closing Prices for Target Stock', fontsize = 20)

# x and y axis labels
plt.xlabel('Date')
plt.ylabel('Price')

plt.xticks(np.arange(0,30,5))

# plot
plt.plot(tgt_close["Date"], tgt_close["Close"], 'r')

# saves the image
plt.savefig("linechart.png")

# shows the image
plt.show()


# In[10]:


# Question 6 - Strip Plots
import pandas as pd

titanic = pd.read_csv(r"C:\Users\tbels\OneDrive\Documents\csvfiles\csvfiles\titanic.csv")

df = titanic[(titanic.sex == 'male') & (titanic.pclass == 1) & (titanic.age > 18)]
# subset titanic to include male passengers in first class over 18 years old

print(df.head())

sp = sns.stripplot(x="embark_town", y="age", hue = "survived", jitter= True, data=df)
sp.set_xlabel("Embark Town")
sp.set_ylabel("Age")

