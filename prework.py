# Question 1:
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of code has been defined as below.


def hello_name(user_name):
    """Display 'hello_USERNAME!'"""
    print("hello_" + user_name.upper() + "!")
hello_name('username')


# Question 2:
# Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds():
    """Prints odd numbers from 1-100 and returns nothing"""
    for odd_numbers in range(1, 101, 2):
        print(odd_numbers, end=", ")
first_odds()


# Question 3:
# Please write a Python function, 
# max_num_in_list to return the max number of a given list.
# The first line of code has been defined below.


def max_num_in_list(a_list):
    """Return the max number of a given list"""
    max_num = a_list[0]
    for number in a_list:
        if number > max_num:
            max_num = number
    return max_num
print(max_num_in_list([1, 157, 10, 4, 9683, 72, 18, 43]))


# Question 4:
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, 
# but not divisible by 100 unless it is also divisible by 400.
#The return should be boolean Type (true/false).


def is_leap_year(a_year):
    """Determines if year entered is a leap year or not"""
    leap = False
    if a_year % 4 == 0:
        leap = True
    elif a_year % 100 == 0:
        leap = False
    elif a_year % 400 == 0:
        leap = True
    return leap
a_year = int(input("Enter the year: "))
print(is_leap_year(a_year))


# Question 5: 
# Write a function to check to see if all numbers in the list are 
# consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type. 


def is_consecutive(a_list):
    """Check to see if all numbers in list are consecutive numbers"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
list_1 = [2,3,4,5,6]
list_2 = [2,3,4,6,7]

print(is_consecutive(list_1))  
print(is_consecutive(list_2))



