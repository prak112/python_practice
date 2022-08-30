#%%
# concept learnt from freeCodeCamp (https://www.freecodecamp.org/news/binary-search-in-python-visual-introduction/)

from typing import List
def binary_search(data: List[float], to_find: int) -> int:
    """
    Arguments:
        data - sorted data to be scanned through for an element
        to_find - element to be found in the dataset
    Returns:
        mid_point - index of the element found
        -1 - if not found
    Examples:
        >>> bindef binary_search([1,5,6,7,8,10], 4)
            -1
    """

    # define lower_bound and upper_bound of the data
    lower_bound = 0
    upper_bound = len(data)-1

    # loop through the data (assuming data is sorted) between lower and upper bounds
    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound)//2    #floor division to avoid float type for index value
        if data[mid_point] == to_find:
            return mid_point
        elif data[mid_point] < to_find:
            lower_bound = mid_point   #lower_bound is reset to the mid_point
        else:
            return -1 #element not found
# %%
unsorted_data = [20, 4, 67, 53, 21, 44, 9, 11]
data = sorted(unsorted_data)
to_find = 20
bst_index = binary_search(data, to_find)
print(data[bst_index])
# %%
# pytest to run