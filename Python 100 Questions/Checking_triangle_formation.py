# Function to check if three angles can form a triangle
def is_valid_triangle(angle1, angle2, angle3):
    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
        return True
    else:
        return False

# Example input
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Output whether the angles form a valid triangle
if is_valid_triangle(angle1, angle2, angle3):
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")
