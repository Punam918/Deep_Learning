def find_duplicates(arr):
    # Initialize a dictionary to keep track of element frequencies
    frequency = {}
    
    # Populate the dictionary with element frequencies
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Collect elements that occur more than once
    duplicates = [num for num, count in frequency.items() if count > 1]
    
    # Sort the list of duplicates in ascending order
    duplicates.sort()
    
    return duplicates

# Example usage
n = 5
arr = [2, 3, 1, 2, 3]
print(find_duplicates(arr))  # Output will be [2, 3]
