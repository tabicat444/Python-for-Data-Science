#!/usr/bin/env python
# coding: utf-8

# # Assignment 3: Dictionaries 
# Tabitha Belshee

# 1. What does this code do?
# The dictionary temperatures contain four Fahrenheit samples for each of five days. What does the “for” statement do?

# As can be seen in the output below, the code produces the average temperature for each day of the week. The names of the days are the keys, represented in the for loop as 'k' and the values for each key are represented as 'v'. The print statement inside the for loop performs the average calulculation (sum of items divded by number of items) and prints the result as a formatted string literal. 

# In[1]:


temperatures = {
'Monday': [67, 71, 74, 77],
'Tuesday': [52, 56, 66 , 50],
'Wednesday': [77, 80, 87 , 95],
'Thursday': [67, 77, 81 , 77],
'Friday': [54 , 60 , 67, 60],
}
for k, v in temperatures.items():
     print(f'{k}: {sum(v)/len(v):.0f}')


# 2. Following the instructions, write a script that counts duplicate words.
# Techniques like word frequency counting are often used to analyze published work. Other document analysis techniques are in natural language processing. Write a script that uses a dictionary to determine and print the number of duplicate words in a sentence. Treat uppercase and lowercase letters the same and assume there is no punctuation in the sentence. Words with counts larger than one have duplicates.

# In[4]:


import string 

def double_double_toil_and_trouble(text):
    #text = line.translate(line.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    counts = dict()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    for k, v in list(counts.items()):
        if v < 2:
            del counts[k]
    
    return counts
    
def main():
    text = input('What text would you like to analyze? \n')
    counts = double_double_toil_and_trouble(text)
    print()
    print(f"WORD" + '\t' + "COUNT")
    for k,v in counts.items():
        print(f'{k}\t{v:.0f}')
    
    
if __name__ == '__main__':
    main()


# 3. The Python list stores a collection of objects in an ordered sequence. In contrast, the dictionary stores objects in an unordered collection. Give three examples of real-world objects that can be stored in a dictionary.

# Three real life examples of dictionary situations are: 
# + Storing counrties and capitals
# + Olympians and each person's scoring records
# + Girl scout cookie types and sales 

# 4. Which of the following are immutable data structures? Why? Please explain.

# __Dictionaries & Lists__ \
# The elements of dictionaries and lists can be changed; therefore, these data types are mutable. \
# __Strings & Tuples__ \
# Strings and tuples cannot be changed after being created. Their names can be overwritten with changed versions of the content, but operations can't change information stored in strings or tuples. Therefore, these data types are immutable. 
