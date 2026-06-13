# Program to classify student grades

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Output: Grade A+")
elif marks >= 75:
    print("Output: Grade A")
elif marks >= 60:
    print("Output: Grade B")
elif marks >= 40:
    print("Output: Grade C")
else:
    print("Output: Fail")
