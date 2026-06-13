# Login Validation


stored_username = "admin"
stored_password = "1234"


username = input("Username: ")
password = input("Password: ")

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Login Failed")
