#%%
"""
DCP
---
19Jan2021-[EASY]
Problem was asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""

l1 = [10, 5, 22, 8, 6, 9] #list of numbers
k = 30 #given value K

#checking if sum of any pair of numbers == K
for i in l1:
    for j in l1:
        if i+j == k:
            print(True)
        else:
            continue


# %%
