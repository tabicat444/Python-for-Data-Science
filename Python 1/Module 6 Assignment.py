#!/usr/bin/env python
# coding: utf-8

# # Module 6 Assignment 
# Tabitha Belshee

# ## Question 1
# ord()

# ## Question 2

# In[2]:


str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

str = str[str.find(':'):]

str.rstrip()


# ## Question 3

# In[3]:


#a.
str =     '''
    inet addr :127.0.0.1 Mask:255.0.0.0
    inet addr :127.0.0.2 Mask:255.0.0.0

    inet addr :127.0.0.3 Mask:255.0.0.0
    inet addr :127.0.0.4 Mask:255.0.0.0
    '''
strings = str.split("\n")
count = 0 
for line in strings:
    if "inet addr" in line:
        count += 1
    
print(count)


# In[4]:


#b.
# Out of a loop for one substring
line = strings[2]
print(line.count("inet addr :"))

# Within a loop for the whole string
count = 0
for line in strings: 
    count += (line.count("inet addr :"))
print(count)


# ## Question 4

# In[5]:


def add_html_tags(size, words):
    return ('<' + size + '>' + words + '<' + size + '>')

print(add_html_tags('h1', 'My First Page'))  
print(add_html_tags('p', 'This is my first page.'))  
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))


# ## Question 5

# In[6]:


first = input("What is your first name?")
last = input("What is your last name?")
print('Hi ' + first.capitalize() + ' ' + last.capitalize() + ', welcome to my Python greet application!')


# ## Question 6

# In[7]:


name = input("What is your full name?")
names = name.split()
print(names[0].capitalize() + ' ' + names[1][0].upper() + '. ' + names[2].capitalize())


# ## Question 7

# In[8]:


famous_list = ''' 
Marilyn Monroe (1926 – 1962) American actress, singer, model

Abraham Lincoln (1809 – 1865) US President during American civil war

Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner

John F. Kennedy (1917 – 1963) US President 1961 – 1963

Martin Luther King (1929 – 1968)  American civil rights campaigner

Queen Elizabeth II (1926 – ) British monarch since 1954

Winston Churchill (1874 – 1965) British Prime Minister during WWII

Donald Trump (1946 – ) Businessman, US President.

Bill Gates (1955 – ) American businessman, founder of Microsoft

Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner

Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement

Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990

Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun

Christopher Columbus (1451 – 1506) Italian explorer

Charles Darwin (1809 – 1882) British scientist, theory of evolution

Elvis Presley (1935 – 1977) American musician

Albert Einstein (1879 – 1955) German scientist, theory of relativity

Paul McCartney (1942 – ) British musician, member of Beatles

Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901

Pope Francis (1936 – ) First pope from the Americas

'''


# In[9]:


famous = input("Please enter the name of the famous individual.")

total = " ".join(name.capitalize() for name in famous.split())

if total in famous_list:
    print("Yup, " + total + " did make the Top 20 cut!")
else:
    print("Sorry, " + total + " did not make the Top 20 cut!")
    
    


# In[10]:


famous = input("Please enter the name of the famous individual.")

total = " ".join(name.capitalize() for name in famous.split())

if total in famous_list:
    print("Yup, " + total + " did make the Top 20 cut!")
else:
    print("Sorry, " + total + " did not make the Top 20 cut!")
    

