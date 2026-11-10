# imports modules needed for random password generation
import random
import string

# function to validate a password
def validate_password(password):
    has_letter = False
    has_digit = False
    has_symbol = False
    allowed_symbols = "!@#$%"

    if len(password) < 10:
        return False

    for character in password:
        if character.isalpha():
            has_letter = True
        elif character.isdigit():
            has_digit = True
        elif character in allowed_symbols:
            has_symbol = True

    return bool(has_letter and has_digit and has_symbol)

# function to validate an IP address
def validate_ip(ip):
    ip = ip.strip()

    if ip.count(".") != 3:
        return False
    
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True

# function to generate a random password
def generate_password():
    length = random.randint(10, 16)

    characters = string.ascii_letters + string.digits + "!@#$%"
    password = " "

    for i in range(length):
        password += random.choice(characters)

    return password