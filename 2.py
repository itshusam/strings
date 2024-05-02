import re


def check_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: names should be at least 2 characters long.")
    else:
        print("First name and last name are valid.")


def check(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return False

    if not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter.")
        return False

    if not any(char.islower() for char in password):
        print("Error: Password must contain at least one lowercase letter.")
        return False

    if not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one number.")
        return False

    print("Password meets requirements.")
    return True



def validate_email(email):
    # Regular expression pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        print("Email is in standard format.")
        return True
    else:
        print("Error: Email address is not in the right format.")
        return False


password=input("please enter a new password!")
check(password)

email=input("enter your email!")
validate_email(email)
