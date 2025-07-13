# Personal Finance Calculator
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
savings = income - expenses
ASavings = savings * 12
interest = ASavings * 0.05
Psavings = ASavings + interest
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${Psavings}.")


