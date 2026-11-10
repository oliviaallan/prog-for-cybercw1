# imports the security tools module
import task_05_security_tools

# asks the user for a password and IP address
password = input("Enter a password: ")
ip_address = input("Enter an IP address: ")

# validates the password
if task_05_security_tools.validate_password(password):
    print("Password is valid.")
else:
    print("Password is not strong enough.")
    print("Suggested password: ", task_05_security_tools.generate_password())

# validates the IP address
if task_05_security_tools.validate_ip(ip_address):
    print("Valid IP address.")
else:
    print("Invalid IP address.")