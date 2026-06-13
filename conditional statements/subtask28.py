# Program to simulate traffic signal

signal = input("Enter traffic signal color (Red/Yellow/Green): ").lower()

if signal == "red":
    print("Output: Stop! ")
elif signal == "yellow":
    print("Output: Get Ready! ")
elif signal == "green":
    print("Output: Go! ")
else:
    print("Output: Invalid signal color.")
