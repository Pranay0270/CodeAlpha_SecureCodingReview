# Simple vulnerable login system

username = input("Enter username: ")
password = input("Enter password: ")

# fake database
db_user = "admin"
db_pass = "admin123"

if username == db_user and password == db_pass:
    print("Login Successful")
else:
    print("Invalid Login")
