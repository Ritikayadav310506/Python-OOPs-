# Program to check loan eligibility

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 21 and income >= 25000:
    print("Output: Eligible for loan.")
else:
    print("Output: Not eligible for loan.")
