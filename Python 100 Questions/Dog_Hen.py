def solve_animals(heads, legs):
    # Check for invalid input (if legs or heads are impossible)
    if legs % 2 != 0 or heads > legs // 2:
        return "No solution possible."
    
    # Using the two equations:
    # x + y = heads (equation for heads)
    # 2x + 4y = legs (equation for legs)
    
    # Rearranging the equations:
    # x = total_heads - y
    # 2*(total_heads - y) + 4y = total_legs
    chickens = (4 * heads - legs) // 2
    dogs = heads - chickens

    # Check if the solution makes sense (no negative number of animals)
    if chickens < 0 or dogs < 0:
        return "No solution possible."
    
    return chickens, dogs

# Input: Taking the total heads and legs from the user
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

# Solve and display the result
result = solve_animals(total_heads, total_legs)
if isinstance(result, str):
    print(result)
else:
    chickens, dogs = result
    print(f"There are {chickens} chickens and {dogs} dogs.")
