# Personal Finance Calculator
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
Savings = savings * 12 + (savings * 12 * 0.05)
print("Your monthly savings are ${savings}.")
print("Projected savings after one year, with interest, is: ${Savings}")


