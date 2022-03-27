#!/usr/bin/env python
# coding: utf-8

# # Assignment 4: OS Concepts
# Tabitha Belshee

# 1. Write a code segment that opens a file named file.txt for input and prints the number of lines in that file.

# In[3]:


#import os
#os.getcwd()
text = open("file.txt", "r")
print("Number of lines: " + str(len(text.readlines())))
text.close()


# 2. Write a code segment that opens a file for input and prints the number of five-letter words in the file.

# In[2]:


text = open("file.txt", "r")
text = text.read()
words = text.split()
counter = 0
for word in words:
    if len(word) == 5:
        counter += 1

print("Number of 5-letter words: " + str(counter))


# 3. Write a code segment that prints the names of all the items in the current working directory.

# In[3]:


import os 

os.listdir(os.curdir)


# 4. Write a code segment that prompts the user for a file. If the file does not exist then the program should print an error. Otherwise, the program should print its contents.

# In[16]:


text = input('Enter the file name: ')
print()
try:
    text = open(text)
    print(text.read())
except:
    print('File cannot be opened:', text)
    exit()


# 5. Create a file called accounts.txt and enter the following information in the file

# In[14]:


with open('accounts.txt', 'w') as f:
    f.write('100 Mary 34.58 \n200 Alison 345.67 \n300 Marc 3.00 \n400 Zoltar -32.16 \n500 Kathleen 24.32')
f.close()


# 6. In the accounts.txt file:

# - update the name 'Zoltar' to 'Robert' 
# - create a tempfile with the new data
# - remove accounts.txt file from the directory
# - rename the tempfile to a new file called myaccounts.txt

# In[15]:


#Open file and check it out
file = open('accounts.txt', 'r')
text = file.read()
print("Original file:")
print(text)
file.close()
#Replace Zoltar with Robert
text = text.replace('Zoltar', 'Robert')

#Create tempfile
file2 = open('tempfile.txt', 'w')
file2.write(text)
file2.close()

#Remove accounts.txt
os.remove("accounts.txt")

#Rename tempfile
os.rename("tempfile.txt", "accounts.txt")

#prove it worked
file = open('accounts.txt', 'r')
text = file.read()
print()
print("New file:")
print(text)

