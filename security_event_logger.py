# security event logger

import random
from datetime import datetime
import socket

# sets correct login details
correct_username = "admin"
correct_password = "password123"

# displays heading
print("Security Event Log")
print("-------------------")

# loop continues until correct login details are entered
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # generates random event ID for each login attempt
    event_id = random.randint(1000, 9999)

    # records the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # creates a socket to find the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    # checks if the username and password are correct
    if username == correct_username and password == correct_password:
        # diplays the successful login event info
        print("Event ID:", event_id)
        print("Username: ", username)
        print("IP Address: ", ip_address)
        print("Event: Successful login")
        print("Timestamp: ", timestamp)
        break
    else:
        # displays the failed login event info
        print("Event ID:", event_id)
        print("Username: ", username)
        print("IP Address: ", ip_address)
        print("Event: Failed login")
        print("Timestamp: ", timestamp)
        print()