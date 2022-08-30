#%%
"""
DCP
---
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""
# %%
# User Input
nums = []
#[1,2,-4,0,4]
total_nums = int(input(prompt='How many numbers do you want to insert'))

for i in range(total_nums):
    num = int(input())
    nums.append(num)

#Filter, sort & verify list
pos_ints = [x for x in nums if x >= 0]
sort_nums = sorted(pos_ints)
verify_list = range(sort_nums[0], sort_nums[-1]+1)

# Implementing Sets to remove redundant numbers
user_set = set(sort_nums)
verify_set = set(verify_list)

# Filtering output
if user_set == verify_set:
    if min(user_set) == 0:
        missing_int = max(user_set)+1
    else:
        missing_int = min(user_set)-1
else:
    missing_int = min(verify_set - user_set)

print(f"User input values are: \n{nums}\n Lowest positive integer missing in the input: \n{missing_int}")
# %%
