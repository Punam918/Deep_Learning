def calculate_angle(hour, minute):
    # Normalize hour to 12-hour format
    if hour >= 12:
        hour = hour - 12

    # Calculate the positions of hour and minute hands
    minute_angle = minute * 6  # Each minute represents 6 degrees
    hour_angle = (hour * 30) + (minute * 0.5)  # Each hour represents 30 degrees and each minute adds 0.5 degrees to the hour hand

    # Calculate the difference between hour and minute angles
    angle = abs(hour_angle - minute_angle)

    # The minimum angle between the hands should be <= 180 degrees
    return min(angle, 360 - angle)

# Example usage
H = 9
M = 0
angle = calculate_angle(H, M)
print(angle)  # Output: 90
