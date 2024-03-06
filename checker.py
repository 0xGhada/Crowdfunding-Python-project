import re
# import getpass  # masking  password 
import maskpass

def checkString(msg="Enter String "):
    while True:
        St = input(msg)
        if St.isalpha():
            return St
        else:
            print("Please enter a string.")

def checkInt(msg="Please enter an integer"):
    while True:
        num = input(msg)
        if num.isdigit():
            return num
        else:
            print("Please enter an integer.")

def checkEmailValidation():
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        Email = input("Enter your valid email: ")
        if re.fullmatch(email_regex, Email):
            return Email
        else:
            print("Please enter a correct email.")

def checkPasswrd(msg="Enter a complex password: "):
    pass_reg = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    while True:
        passwd = maskpass.askpass(msg)
        if re.search(pass_reg, passwd):
            return passwd
        else:
            print("Enter a valid password. Make it more complex.")

def Checkphone():
    phone_regex = r'^01[0-2]\d{8}$'  
    while True:
        phone = input("Enter your  phone number : ")
        if re.fullmatch(phone_regex, phone):
            return phone
        else:
            print("Invalid mobile number format.")



