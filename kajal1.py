#Name : Kajal Pathak
# Date : 08/10/2025
# Lab Title : Expense Tracker Tool

# Task 1: Setup & Introduction
print("Welcome to the Expense Tracker!")
print("This tool helps you record and analyze your expenses.")

# Task 2: Input & Data Collection
categories = []
amounts = []

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    categories.append(category)
    amounts.append(amount)

    more = input("Do you want to add more? (yes/no): ").lower()
    if more == "no":
        break

# Task 3: Expense Calculations
total_expense = sum(amounts)
average_expense = total_expense / len(amounts)

# Task 4: Neatly Formatted Output
print("Your Expenses:")
for i in range(len(categories)):
    print(f"{categories[i]} - {amounts[i]:.1f}")



print("Expenses Record")
print("---------------")
for i in range(len(categories)):
    print(f"{categories[i]} - {amounts[i]:.1f}")

print("Total Expense:", total_expense)
print("Average Expense: ", average_expense)