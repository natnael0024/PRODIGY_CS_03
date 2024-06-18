SP_CHARS = '!@#$%^&*()[]?<>'

def contains_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def contains_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
    return False

def check_sp_char(password):
    for ch in SP_CHARS:
        if ch in password:
            return True
    return False

def check_password():
    password = input("Enter password:\n")
    if len(password) < 12:
        return print("\033[91m # weak, password must be 12 characters long # \033[0m")
    uppercase = contains_uppercase(password)
    if not uppercase:
        return print("\033[91m# weak, password must contain atleast one uppercase letter #\033[0m")
    lowercase = contains_lowercase(password)
    if not lowercase:
        return print("\033[91m# weak, password must contain atleast one lowercase letter #\033[0m")
    if not check_sp_char(password):
        return print("\033[91m# medium, pasword must contain atleast one special character #\033[0m")

    return print("\033[92m*** Strongest password ever created! ***\033[0m")

if __name__ == "__main__":
    while True:
        check_password()