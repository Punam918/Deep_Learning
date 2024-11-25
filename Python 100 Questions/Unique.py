import itertools

# List of numbers
numbers = [1, 2, 3, 4]

# Get all unique combinations of the numbers (permutations)
combinations = itertools.permutations(numbers, len(numbers))

# Print each combination
print("Unique combinations of 1, 2, 3, and 4:")
for combo in combinations:
    print(combo)
