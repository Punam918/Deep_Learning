def calculate_in_hand_salary(gross_salary):
    # Deduction percentages
    HRA = 0.10  # 10% HRA
    DA = 0.05   # 5% DA
    PF = 0.03   # 3% PF
    
    # Calculate deductions
    hra_deduction = gross_salary * HRA
    da_deduction = gross_salary * DA
    pf_deduction = gross_salary * PF
    total_deductions = hra_deduction + da_deduction + pf_deduction

    # Calculate taxable income
    taxable_income = gross_salary - total_deductions
    
    # Calculate tax based on income slabs
    if taxable_income <= 100000:
        tax = 0
        print("Salary is below 1 lakh. In-hand salary is 'K'")
        return 'K'
    elif 500000 <= taxable_income <= 1000000:
        tax = taxable_income * 0.10  # 10% tax
    elif 1000001 <= taxable_income <= 2000000:
        tax = taxable_income * 0.20  # 20% tax
    elif taxable_income > 2000000:
        tax = taxable_income * 0.30  # 30% tax
    else:
        tax = 0  # No tax for income below 5 lakhs

    # Calculate final in-hand salary
    in_hand_salary = taxable_income - tax
    return in_hand_salary

# Input: Taking the gross salary from the user
gross_salary = float(input("Enter your gross salary: "))

# Calculate and display the in-hand salary
in_hand_salary = calculate_in_hand_salary(gross_salary)
if in_hand_salary != 'K':
    print(f"Your in-hand salary after deductions is: {in_hand_salary}")
