# Program to validate login credentials

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Output: Login successful.")
else:
    print("Output: Invalid username or password.")
