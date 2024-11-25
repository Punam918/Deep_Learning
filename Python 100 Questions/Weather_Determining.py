def determine_weather(temperature, humidity):
    if temperature >= 30 and humidity >= 90:
        return "Hot and Humid"
    elif temperature >= 30 and humidity < 90:
        return "Hot"
    elif temperature < 30 and humidity >= 90:
        return "Cool and Humid"
    elif temperature < 30 and humidity < 90:
        return "Cool"

# Example usage
temp = float(input("Enter the temperature (in °C): "))
hum = float(input("Enter the humidity (in %): "))

weather = determine_weather(temp, hum)
print(f"The weather is: {weather}")
