import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ") #hides password digits
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created succesfuly.")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")  # hides password digits
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login succesfuly.")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input("Enter 1 to create an account, enter 2 to login, 0 to exit")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
            main()