# Program to check scholarship eligibility

marks = int(input("Enter your marks: "))
income = int(input("Enter your family income: "))

if marks >= 85 or income <= 20000:
    print("Output: Eligible for scholarship.")
else:
    print("Output: Not eligible for scholarship.")
