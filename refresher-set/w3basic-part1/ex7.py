"""
Basic Exercise 7/150
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""

file = input("\nEnter file name with extension : ")
print("Filename without extension : ", str.split(file, '.')[0])