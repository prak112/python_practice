"""
W3 Resources
Exercises 14 - 20
======================
"""

#%%
"""
Ex 14 :
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
# import librariess
import datetime
import time
from datetime import *
from unittest import result

# function to calculate time difference
def time_diff(old_date, new_date):
    """
    Arguments:
    date format - (yyyy, mm, dd)
    
    Returns:
    diff_date - (yyyy, mm, dd)
    """
    time_diff = new_date - old_date

    return time_diff

# input variables
if __name__ == '__main__':
    # assign variables
    print('This program calculates number of days between two dates\n')
    old_date = datetime.strptime( input("Enter older date in yyyy, mm, dd format :\n"), "%Y, %m, %d")
    new_date = datetime.strptime( input("Enter older date in yyyy, mm, dd format :\n"), "%Y, %m, %d")
    
    time_diff = time_diff(old_date, new_date)
    print(f"Difference between {old_date} and {new_date} in days :\n{time_diff}\n")
# %%
"""
Ex 15 :
Write a Python program to get the volume of a sphere with radius as input.
"""
# import libraries
import math

# function to calculate volume of a sphere - 4/3*pi*r^3
def vol_sphere(radius):
    """
    Args:
    radius - radius of the sphere

    Returns:
    volume - volume of the sphere
    """
    from math import pi, pow
    volume = (4/3)*pi*pow(radius, 3)

    return volume

# input variables
if __name__ == '__main__':
    print('This program calculates volume of a sphere with radius as input\n')
    r = int(input("Enter radius of the sphere :\n"))
    v = vol_sphere(r)
    print (f"Volume of sphere : {round(v, 3)}\n")

# %%
"""
Ex 16 :
Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference
"""
# function to get difference or (abs difference*2)
def spec_diff(num):
    """
    Args:
    num - integer to be subtracted with 17

    Returns:
    sub     - difference or absolute difference between num & 17
    num_id  - identify number if > 17 or not
    """
    # assign standard
    threshold = 17

    # calculate difference
    if num > threshold:
        sub = abs(17 - num)*2
        num_id = "number > 17. Result = abs(diff)*2"
    else:
        sub = 17 - num
        num_id = "number < 17. Result = (diff)"

    return sub, num_id

# input variables
if __name__ == '__main__':
    print('This program calculates the difference between a given number and 17, if the number is greater than 17 return double the absolute difference\n')
    n = int(input("Enter an integer : "))
    result, num_id = spec_diff(n)
    print(f"Result :{num_id}, {result}\n")

# %%
"""
Ex 17:
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
# function to define number range
def near1000(num)-> int:
    """
    Args:
    num - number within range of 100-2000

    Returns:
    print statement
    """
    ans = ((abs(1000-num)) <= 100) or ((abs(2000-num)) <= 100)
    print('Given number is within 100 of 1000 or 2000 :', ans,'\n')

    return None

if __name__ == '__main__':
    print('This program calculates whether a given number is within 100 of 1000 or 2000\n')
    num = int(input("Enter a number :"))
    near1000(num)

# %%
