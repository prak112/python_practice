#%%
"""
DCP
---
20Jan2021-[HARD]
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i, i.e., if input is [2, 3, 5, 6], output is [90, 60, 36, 30]
"""

#%%
#import neccesary libraries
from functools import reduce

#%%
arr = [10, 2, 4, 5] #input array
prod_arr = [] #initialize output array

#calculating by skipping each element
for i in range(len(arr)):
    skip_element = arr.pop(0)
    prod =  reduce(lambda x, y: x*y, arr)
    
    #appending skipped element
    arr.append(skip_element)
    prod_arr.append(prod)

print(prod_arr)

# %%
