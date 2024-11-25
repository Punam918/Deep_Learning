def sum_of_largest_and_smallest(arr):
    # Ensure the array is not empty
    if not arr:
        raise ValueError("The array is empty")
    
    # Find the smallest and largest elements in the array
    smallest = min(arr)
    largest = max(arr)
    
    # Calculate the sum of the smallest and largest elements
    result = smallest + largest
    return result

# Example usage
arr = [23, 4, 6, 3, 100]
print(sum_of_largest_and_smallest(arr))  # Output will be 103
