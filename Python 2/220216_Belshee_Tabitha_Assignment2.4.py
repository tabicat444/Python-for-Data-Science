#!/usr/bin/env python
# coding: utf-8

# # 2.4 Module 2 Assignment 
# Tabitha Belshee

# Q1. To sort a list in descending order, call list method sort with the optional keyword argument ____ set to True.

# reverse

# Q2. Insert 10 random letters in the range ‘a’ through ‘z’ into a list. Perform the following tasks and display your results
# 
# a. Sort the list in ascending order
# 
# b. Sort the list in descending order
# 
# c. Get the unique values sort them in ascending order

# In[1]:


import random

ord_alphabet = list(chr(i) for i in range(ord('a'), ord('z') + 1, 1))
alphabet = random.choices(ord_alphabet, k=10)
print("Random Letters:")
print(alphabet)

print("Sort the list in ascending order.")
alphabet.sort()
print(alphabet)

print("Sort the list in descending order.")
alphabet.sort(reverse = True)
print(alphabet)

print("Unique values sorted in as ascending order.")
alphabet.sort()
alphabet = list(set(alphabet))
print(alphabet)


# Q3. Create a program that a user can use to manage the primary email address and phone number for a contact.
# 
# a. Use a multi-dimensional list to store the data for the contacts. Provide starting data for two or more contacts.
# 
# b.  For the view and del commands, display an error message if the user enters an invalid contact number.
# 
# c. When you exit the program, all changes that you made to the contact list are lost.

# In[6]:


def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list    - Display all contacts")
    print("view    - View a contact")
    print("add     - Add a contact")
    print("del     - Delete a contact")
    print("exit    - Exit program")
    print()
    
def display(employee_list):
    i = 1
    for x in employee_list:
        print(str(i) + "." + x[0])
        i += 1
    print()
    
def view(employee_list):
    number = int(input('Which number to view: '))
    if number < 1 or number > len(employee_list):
        print('Invalid employee number.\n')
    else:
        print('Name: ' + employee_list[number - 1][0])
        print('Email: ' + employee_list[number - 1][1])
        print('Number: ' + employee_list[number - 1][2])
        print()
    
def add(employee_list):
    employee = input('Name: ')
    email = input('Email: ')
    num = input('Number: ')
    emp_total = [employee, email, num]
    employee_list.append(emp_total)
    print(employee + ' was added.')
    print()
    
    
def delete(employee_list):
    number = int(input('Which number to delete: '))
    if number < 1 or number > len(employee_list):
        print('Invalid employee number.\n')
    else:
        employee = employee_list.pop(number-1)
        print(employee[0] + ' was deleted.')
    print()
    
def main(): 
    employee_list = [['Tabitha Belshee', 'tbelshee@gmail.com', '4444444'],
                    ['Justin Calimlim', 'jlimlim@gmail.com', '4564564']]
    display_menu()
    
    while True:
        command = input('Enter command: ')
        if command.lower() == 'list':
            display(employee_list)
        elif command.lower() == 'view':
            view(employee_list)
        elif command.lower() == 'add':
            add(employee_list)
        elif command.lower() == 'del':
            delete(employee_list)
        elif command.lower() == 'exit':
            print('Bye!')
            break
        else: 
            print('That\'s not an option. Please try again.')
    
if __name__ == '__main__':
    main()

