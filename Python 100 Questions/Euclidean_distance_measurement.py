import math

# Function to calculate the Euclidean distance between two coordinates
def euclidean_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


# Example input
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Output the Euclidean distance
distance = euclidean_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between the two points is: {distance:.2f}")
