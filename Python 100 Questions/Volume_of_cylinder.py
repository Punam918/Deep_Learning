import math

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

# Function to calculate the cost of milk
def calculate_cost(volume, cost_per_litre):
    cost = volume * cost_per_litre
    return cost

# Example input
radius = float(input("Enter the radius of the cylinder (in meters): "))
height = float(input("Enter the height of the cylinder (in meters): "))

# Cost per liter of milk
cost_per_litre = 40  # Rs per liter

# Calculate the volume of the cylinder (in cubic meters)
volume = calculate_cylinder_volume(radius, height)

# Convert the volume from cubic meters to liters (1 cubic meter = 1000 liters)
volume_litres = volume * 1000

# Calculate the cost of the milk
cost = calculate_cost(volume_litres, cost_per_litre)

# Output the results
print(f"The volume of the cylinder is: {volume:.2f} cubic meters")
print(f"The volume in liters is: {volume_litres:.2f} liters")
print(f"The cost of the milk is: {cost:.2f} Rs")
