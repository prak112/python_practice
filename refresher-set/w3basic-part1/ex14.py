"""
W3 Resources
------------
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

import datetime
import time
from datetime import *


def time_diff(old_date, new_date):
    """
    Arguments:
    date format - (yyyy, mm, dd)
    
    Returns:
    diff_date - (yyyy, mm, dd)
    """
    time_diff = new_date - old_date

    return time_diff


if __name__ == '__main__':
    # assign variables
    old_date = datetime.strptime( input("Enter older date in yyyy, mm, dd format :\n"), "%Y, %m, %d")
    new_date = datetime.strptime( input("Enter older date in yyyy, mm, dd format :\n"), "%Y, %m, %d")
    
    time_diff = time_diff(old_date, new_date)
    print(f"Difference between {old_date} and {new_date} in days :\n{time_diff}")