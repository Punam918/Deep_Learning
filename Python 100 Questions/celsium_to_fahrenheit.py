def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius+9/5)+32
    return fahrenheit

#input
celsius = float(input("Enter the value of Celsius"))

#output
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")