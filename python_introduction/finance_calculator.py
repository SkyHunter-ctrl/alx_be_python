# Personal Finance Calculator
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
savings = income - expenses
PSavings = savings * 12 + (savings * 12 * 0.05)
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${PSavings}.")


