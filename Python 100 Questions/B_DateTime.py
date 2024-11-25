def mainfunction(date):
    # Split the input date into year, month, and day
    year, month, day = map(int, date.split('-'))
    
    # Days in each month for a non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year and adjust February days
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    # Calculate the number of days remaining in the year
    # Total days in the year
    total_days_in_year = sum(days_in_month)
    
    # Days passed up to the given date
    days_passed = sum(days_in_month[:month-1]) + day
    
    # Days remaining in the year
    days_remaining = total_days_in_year - days_passed
    
    return days_remaining

# Example usage
date = "2024-08-20"
print(mainfunction(date))  # Output will be 133
