# security tool

# correct security details
correct_username = "admin"
correct_password = "password123"

# function to record correct and incorrect password attempts
def security_event_counter():
    correct_count = 0
    incorrect_count = 0

    # sets security password
    security_password = "secure123"

    print("\n--- Security Event Counter ---")

    # loop to ask for a password 10 times
    for i in range (10):
        password = input("Enter password: ")

        # checks if password is correct or not
        if password == security_password:
            correct_count += 1
        else:
            incorrect_count += 1

    # calulates percentage of incorrect password attempts
    incorrect_percentage = (incorrect_count / 10) * 100

    # displays results
    print("\nResults: ")
    print("Correct passwords: ", correct_count)
    print("Incorrect passwords = ", incorrect_count)
    print("Percentage of incorrect passwords: ", incorrect_percentage, "%")

    # checks if incorrect attempts exceeds 50% and displays alert if so
    if incorrect_percentage > 50:
        print("ALERT: More than 50% of password attempts were incorrect!")

# function to simulate a brute-force password attack
def brute_force_simulation():
    correct_password = "secret123"
    max_attempts = 5
    attempts = 0

    print("\n--- Brute-Force Simulation ---")

    # loop continues until password is correct or attempts run out
    while attempts < max_attempts:
        password_guess = input("Enter password guess: ")
        attempts += 1

        # checks if password is correct
        if password_guess == correct_password:
            print("Correct password!")
            print("Password entered after ", attempts, "x attempts.")
            break
        else:
            print("Incorrect password.")

    # checks if max number of attempts has been reached
    if attempts == max_attempts and password_guess != correct_password:
        print("Max number of attempts reached.")

# function to check login authentication
def login_authentication():
    failed_logins = 0
    max_failed_logins = 3

    print("\n--- Login Authentication ---")

    # loop allows user 3 login attempts
    while failed_logins < max_failed_logins:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # checks if username and password are correct
        if username == correct_username and password == correct_password:
            print("Authentication succeeded!")
            return
        else:
            failed_logins += 1
            print("Authentication failed.")

            # allows another attempt if max not reached
            if failed_logins < max_failed_logins:
                print("Please try again.")

    # displays message when max attempts have been reached
    print("Account frozen for 24 hours.")

# displays heading
print("--------------------")
print("     SECURITY TOOL")
print("--------------------")

# checks user authentication before allowing access to menu
authenticated = False

while not authenticated:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        authenticated = True
        print("Authentication successful!")
    else:
        print("Authentication failed. Please try again.")

# displays menu until user chooses exit
while True:
    print("\n--- Security Menu ---")
    print("1. Security Event Counter")
    print("2. Brute-Force Counter")
    print("3. Login Authentication")
    print("4. Exit")

    choice = input("Select an option: ")

    # calls the selected user function
    if choice == "1":
        security_event_counter()
    elif choice == "2":
        brute_force_simulation()
    elif choice == "3":
        login_authentication()

    # exits the program
    elif choice == "4":
        print("Thank you for using the security tool.")
        break

    # displays error message if invalid selection made
    else:
        print("Invalid option, Please enter 1, 2, 3 or 4.")