# Program to check college admission eligibility based on marks and age

marks = int(input("Enter your marks: "))
age = int(input("Enter your age: "))

if age >= 18:
    if marks >= 60:
        print("Output: Eligible for college admission.")
    else:
        print("Output: Not eligible - insufficient marks.")
else:
    print("Output: Not eligible - age requirement not met.")
