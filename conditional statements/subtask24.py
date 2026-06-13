# Program to validate ATM withdrawal

balance = 5000
pin = int(input("Enter your PIN: "))

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        print("Output: Withdrawal successful.")
    else:
        print("Output: Insufficient balance.")
else:
    print("Output: Invalid PIN.")
