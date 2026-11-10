# IP address validator

# function to check if an IP address is valid
def validate_ip(ip):
    ip = ip.strip()

    # removes unneccessary spaces from the IP address
    if "." not in ip:
        return False

    # checks if the IP address contains exactly 3 periods
    if ip.count(".") != 3:
        return False

    # splits the IP address  into separate parts using periods
    parts = ip.split(".")

    # checks if the IP address contains 4 numbers
    if len(parts) != 4:
        return False

    # checks each part of the IP address is valid
    for part in parts:

        # checks if each part contains only digits
        if not part.isdigit():
            return False

        # converts each part into an integer
        number = int(part)

        # checks if each number is between 0 and 255
        if number < 0 or number > 255:
            return False

    return True

# asks the user to enter an IP address
ip_address = input("Enter IP address: ")

# checks the IP address and displays the result
if validate_ip(ip_address):
    print("Valid IP address.")
else:
    print("Invalid IP address.")