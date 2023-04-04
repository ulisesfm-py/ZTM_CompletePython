import re


def is_valid_email(email):
    """Return True if the email is valid, False otherwise."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_password(password):
    '''return True if the password is valid, False otherwise'''
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$%])[a-zA-Z0-9$%#@]{8,16}\d'
    pattern_comp = re.compile(pattern)
    check = pattern_comp.fullmatch(password)
    # print(check)
    return bool(re.fullmatch(pattern, password))


e = True
p = True
while e is True:
    email = input('Introduce your email: ')
    if is_valid_email(email):
        while p is True:
            password = input('Introduce your password: ')
            if is_valid_password(password):
                print('You are registered correctly.')
                p = False
            else:
                print('The password is not correct')
            e = False
    else:
        print('The email is not correct.')
