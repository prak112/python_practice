#%%
# Binary Search (source: freeCodeCamp)
# (https://www.freecodecamp.org/news/binary-search-in-python-visual-introduction/)

from typing import List
def binary_search(array: List[int], search_item: int, lower_bound: int, upper_bound: int) -> int:
    """
    Arguments:
        array           
        - sorted array to be scanned through for an element
        search_item     
        - element to be found in the arrayset
        lower_bound     
        - lower index value to search from
        upper_bound     
        - higher index value to search till
    
    Returns:
        mid_point       
        - index of the element found
        - -1, if not found
    
    Example:
        >>> binary_search([1,5,6,7,8,10], 4)
            -1
        >>> binary_search([1,5,6,7,8,10], 5)
            1
    """

    # define lower_bound and upper_bound of the array
    lower_bound = lower_bound
    upper_bound = upper_bound

    # loop through the array (assuming array is sorted) between lower and upper bounds
    while lower_bound < upper_bound:
        mid_point = (lower_bound + upper_bound)//2    #floor division to avoid float type for index value
        if array[mid_point] == search_item:
            return mid_point
        elif array[mid_point] < search_item:
            lower_bound = mid_point   #lower_bound is reset to the mid_point
        else:
            return -1 #element not found
        
#%%
# Insertion Sort algorithm (source: GeeksForGeeks)
# (https://www.geeksforgeeks.org/binary-insertion-sort/)

def insertion_sort(unsorted_array):
    """
    Arguments:
    unsorted_array  
    - part of list elements given by user

    Returns:
    sorted_array    
    - list of sorted elements from the unsorted_array

    Example:
        >>> insertion_sort([23, 12, 1])
            [1, 12, 23] 
    """
    # iterate through the given input array
    for current_index in range(1, len(unsorted_array)):
        key = unsorted_array[current_index]
        searched_index = binary_search(unsorted_array, key, 0, current_index-1)
        sorted_array = unsorted_array[ : searched_index] + unsorted_array[searched_index : current_index] + unsorted_array[current_index+1 : ]

    return sorted_array

# %%

# Main Method

print("\n---Welcome to Binary Search---\n")
unsorted_array = input("Enter a list of numbers to be sorted (separate numbers with a ' ') : ").split(' ')
int_unsorted_array = list(map(int, unsorted_array))
sorted_array = insertion_sort(int_unsorted_array)
#search_item = int(input("Enter the number to found : "))
#item_index = binary_search(sorted_array, search_item)

# finding a specific array index
#if item_index == -1:
#    print("Element not found")
#else:
#    print(f"The number {search_item} is at index {item_index}\n\n---End Binary Search---\n")

print(f"Given array : {unsorted_array}\nSorted array : {sorted_array}")
# %%
# pytest to run