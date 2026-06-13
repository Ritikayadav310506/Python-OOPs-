# Program to check employee bonus eligibility

salary = int(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
    if salary < 50000:
        print("Output: Eligible for bonus.")
    else:
        print("Output: Not eligible - salary too high.")
else:
    print("Output: Not eligible - insufficient years of service.")
