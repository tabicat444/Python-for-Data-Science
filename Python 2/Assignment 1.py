#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime, timedelta
import math


# 1. Create a program that calculates the estimated duration of a trip in hours and minutes (same time zone). This should include an estimated date/time of departure and an estimated date/time of arrival:

# In[39]:


def get_departure_date():
    dep_date_str = input('Estimated date of departure (YYYY-MM-DD): ')
    dep_date = datetime.strptime(dep_date_str, '%Y-%m-%d')
    return dep_date
    
def get_departure_tme():
    dep_time_str = input('Estimated time of departure (HH:MM AM/PM): ')
    dep_time = datetime.strptime(dep_time_str, '%I:%M %p').time()
    return dep_time
    
def get_miles():
    dep_miles = int(input('Enter miles: '))
    return dep_miles

def get_speed():
    dep_speed = int(input('Enter miles per hour: '))
    return dep_speed

def main(): 
    print("Arrival Time Estimator")
    while True: 
        
        # get all the inputs
        dep_date = get_departure_date()
        dep_time = get_departure_tme()
        dep_miles = get_miles()
        dep_speed = get_speed()
        print(" ")

        #how long will the trip take?
        print("Estimated travel time")
        trip_hours = math.floor(dep_miles/dep_speed)
        print('Hours: ' + str(trip_hours))
        trip_minutes = math.floor((dep_miles % dep_speed) / dep_speed * 60)
        print('Minutes: ' + str(trip_minutes))
        departure = datetime.combine(dep_date, dep_time)
        arrival = departure + timedelta(hours = dep_miles/dep_speed)
        
        arr_date = arrival.strftime('%Y-%m-%d')
        arr_time = arrival.strftime('%I:%M %p')
        print('Estimated date of arrival: ' + str(arr_date))
        print('Estimated time of arrival: ' + str(arr_time))

        #ask if they want to continue
        print()
        result = input('Continue? (y/n): ')
        print()
        if result.lower() != 'y':
            print('Bye!')
            break
    
    
if __name__ == '__main__':
    main()


# 2. Create a program that accepts a name and a birth date and displays the person’s birthday,the current day, the person’s age, and the number of days until the person’s next birthday.

# In[40]:


def get_name(): 
    name = str(input('Enter name: '))
    return name 

def get_birthday():
    birthday_str = input('Enter birthday (MM/DD/YY): ')
    birthday = datetime.strptime(birthday_str, '%m/%d/%y')
    return birthday

def main():
    print("Birthday Calculator")
    while True:
        #get the inputs
        name = get_name()
        birthday = get_birthday() 
        #present known info
        long_birthday = birthday.strftime('%A, %B %d, %Y')
        print('Birthday:  ' + long_birthday)
        today = datetime.now()
        today_long = today.strftime('%A, %B %d, %Y')
        print('Today:     ' + today_long)
        
        #find age
        age_days = (today - birthday).days
        age_years = math.floor(age_days / 365)
        if age_years > 2:
            print(name + ' is ' + str(age_years) + ' years old.')
        else:    
            print(name + ' is ' + str(age_days) + ' days old.')
            
        #find days to birthday 
        this_birthday = datetime(datetime.now().year, birthday.month, birthday.day)
        days_until = (this_birthday - today).days
        if days_until == -1:
            print(name + '\'s birthday is today!')
        elif days_until == -2:
            print(name + '\'s birthday was yesterday!')
        elif days_until == 0:
            print(name + '\'s birthday is tomorrow!')
        elif days_until < 0:
            this_birthday = datetime(datetime.now().year + 1, birthday.month, birthday.day)
            days_until = (this_birthday - today).days
            print(name + '\'s birthday is in ' +  str(days_until) + ' days.')
        else: 
            print(name + '\'s birthday is in ' +  str(days_until) + ' days.')
        
        
        #ask if they want to continue
        print()
        result = input('Continue? (y/n): ')
        print()
        if result.lower() != 'y':
            print('Bye!')
            break        
        
if __name__ == '__main__':
    main()


# 3. Measure the time cost (efficiency) of an algorithm to use the computer’s clock to obtain an actual runtime. Via benchmarking/profiling implement an algorithm that counts from 1 to a million, time the algorithm and output the running time to the terminal window. Triple the problem size of this number and repeat this process. After four such increases, output the results of your program. For simplicity, measure the efficiency of the algorithm below.

# I wasn't sure if the problem was asking us to mimic the results, but here's my take:

# In[38]:


print('Problem Size         Seconds')
problemSize = 1000000
while problemSize < 27000001:
    now = datetime.now()
    work = 1
    for x in range(problemSize):
           work += 5
           work -= 5
    then = datetime.now()
    elapsed = (then-now).microseconds/1000000
    print(str(problemSize) + '             ' + str(elapsed))
    problemSize = problemSize*3
    

