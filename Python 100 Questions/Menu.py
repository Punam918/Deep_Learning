def cm_to_ft(cm):
    return cm / 30.48  # 1 foot = 30.48 cm

def km_to_miles(km):
    return km * 0.621371  # 1 kilometer = 0.621371 miles

def usd_to_inr(usd, exchange_rate=83.0):  # Default exchange rate is set to 83.0 INR/USD (adjustable)
    return usd * exchange_rate

# Menu-driven program
def main():
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Convert cm to ft")
        print("2. Convert km to miles")
        print("3. Convert USD to INR")
        print("4. Exit")

        # Take user input for the option
        choice = int(input("Enter your choice (1-4): "))

        # Perform the corresponding conversion based on user input
        if choice == 1:
            cm = float(input("Enter the length in centimeters: "))
            feet = cm_to_ft(cm)
            print(f"{cm} cm is equal to {feet:.2f} feet.")
        
        elif choice == 2:
            km = float(input("Enter the distance in kilometers: "))
            miles = km_to_miles(km)
            print(f"{km} km is equal to {miles:.2f} miles.")
        
        elif choice == 3:
            usd = float(input("Enter the amount in USD: "))
            exchange_rate = float(input("Enter the exchange rate (USD to INR): "))  # Option to input exchange rate
            inr = usd_to_inr(usd, exchange_rate)
            print(f"{usd} USD is equal to {inr:.2f} INR.")
        
        elif choice == 4:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Call the main function to run the program
main()
