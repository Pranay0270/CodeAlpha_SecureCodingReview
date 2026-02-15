import hashlib

# hashed password for "admin123"
stored_user = "admin"
stored_pass = hashlib.sha256("admin123".encode()).hexdigest()

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_user and hashed == stored_pass:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Invalid Login. Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")
    