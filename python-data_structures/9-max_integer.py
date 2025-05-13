#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_val = my_list[0]  # Assume the first element is the largest
    for num in my_list:  # Iterate through the list
        if num > max_val:  # Update max_val if a larger number is found
            max_val = num
    return max_val
