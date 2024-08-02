import re
from PwLists import pws
def checker(pw: str):
    """
    This function checks for password complexity
    :param pw: password to be checked
    :return: Boolean True of False if  or not
    """
    pattern = r"[a-zA-Z0-9\.\\\[\]\(\)\^$\|\+\*\?]+"
    if len(pw) >= 8 and " " not in pw and re.match(pattern, pw):
        if pw not in pws:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    print("*"*7,"Welcome to password checker", "*" * 7)
    while(1):
        pw = input("Enter Your password (To exit: Ctrl + D): ")
        status = checker(pw)
        if status:
            print("Password is Valid and Strong!!!")
        else:
            print("""Error: password must follow the pattern
                  - Length must be at least 8 characters
                  - Must contain an uppercase and lowercase letter
                  - Must contain numbers and special characters
                  - and white spaces are not allowed""")
