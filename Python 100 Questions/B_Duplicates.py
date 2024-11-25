def has_duplicate(nums):
    # Create a set from the list
    num_set = set(nums)
    
    # Return True if the set size is less than the list length, indicating duplicates
    return len(num_set) != len(nums)

# Example usage:
nums = [1, 2, 3, 4, 5, 1]
print(has_duplicate(nums))  # Output: True
