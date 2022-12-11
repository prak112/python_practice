#%%
"""
Ex 10. Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
num = int(input("Enter an integer between 1-9 : "))
result = num + num*11 + num*111
print(f"\nGiven value : {num}\nOutput value : {result}")

# %%
"""
Ex 11. Write a Python program to print the documents (syntax, description etc.) 
of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
import time
print("\n\n",time.__doc__)

# %%
"""
Ex 12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
year = int(input("Enter year : "))
month = int(input("Enter month (in numbers) : "))
result = calendar.month(year, month)
print(result)

# %%
