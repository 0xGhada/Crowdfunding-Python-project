import checker
import json
import uuid  # Library to generate unique IDs
# import getpass
import maskpass


def Registeration():
    users = []
    Fname = checker.checkString("Enter your First name: ")
    Lname = checker.checkString("Enter your last name: ")

    while True:
        password = checker.checkPasswrd()
        confirm_password = checker.checkPasswrd("Confirm your password: ")

        if password == confirm_password:
            break
        else:
            print("incorecct password")

    email = checker.checkEmailValidation()
    phone_number = checker.Checkphone()
  # Generate a unique  ID
    user_id = str(uuid.uuid4())
    user_data = {
        "User ID": user_id,
        "First name": Fname,
        "Last name": Lname,
        "Password": password,
        "Email": email,
        "Phone number": phone_number,
    }
    
    users.append(user_data)
    print("Register  successful!")
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


# # -------------------
# login()
# Create a Login Fun
# Load  user data
# Check Login
def login():
    with open("users.json", "r") as file:
        users = json.load(file)
    email = input("Enter your email: ")
    password = maskpass.askpass("Enter your password: ")

    for user in users:
        if user["Email"] == email and user["Password"] == password:
            print("Login successful!")
            return user['User ID'] 

    print("Invalid email or password")


# if __name__=='__main__':
#         # Registeration()
#         # login()

#       pass
