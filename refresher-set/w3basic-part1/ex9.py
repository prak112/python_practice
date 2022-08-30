"""
Basic Exercise 2, 3 & 9/150
2. Write a Python program to get the Python version you are using.
3. Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
9. [WOW!] Write a Python program to display the examination schedule. (extract the date from exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
"""

# %% ex 2
import sys
print("\nPython version : ", sys.version)
print("System version : ", sys.version_info)

# %% ex 3
import datetime
now = datetime.datetime.now()
print("\nCurrent Date and Time : ", now.strftime("%Y-%m-%d %H:%M:%S"),"\n")

# %% ex 9
exam_st_date = (11, 12, 2014)
print("Exam starts on : %i / %i / %i\n"%exam_st_date)
