# Load users from file
users = {}

try:
    with open("users.txt", "r") as file:
        for line in file:
            account_number, name, pin, balance = line.strip().split(",")
            users[account_number] = {
                "name": name,
                "pin": pin,
                "balance": float(balance)
            }
except FileNotFoundError:
    pass


# Save users to file
def save_users():
    with open("users.txt", "w") as file:
        for account_number, details in users.items():
            file.write(
                f"{account_number},{details['name']},{details['pin']},{details['balance']}\n"
            )


# Save transaction history
def save_transaction(message):
    with open("transactions.txt", "a") as file:
        file.write(message + "\n")


# Create account
def create_account():
    account_number = input("Enter Account Number: ")

    if account_number in users:
        print("Account already exists")
        return

    name = input("Enter Name: ")
    pin = input("Set PIN: ")
    balance = float(input("Enter Initial Balance: "))

    users[account_number] = {
        "name": name,
        "pin": pin,
        "balance": balance
    }

    save_users()

    print("Account created successfully")


# Login
def login():

    account_number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account_number in users and users[account_number]["pin"] == pin:

        print("Login Successful")

        return users[account_number], account_number

    else:

        print("Invalid Account Number or PIN")

        return None, None


# Check balance
def check_balance(current_user):
    print("Current Balance =", current_user["balance"])


# Deposit
def deposit(current_user):

    amount = float(input("Enter amount to deposit: "))

    current_user["balance"] += amount

    save_users()

    save_transaction(
        current_user["name"] + " deposited " + str(amount)
    )

    print("Deposit Successful")


# Withdraw
def withdraw(current_user):

    amount = float(input("Enter amount to withdraw: "))

    if amount <= current_user["balance"]:

        current_user["balance"] -= amount

        save_users()

        save_transaction(
            current_user["name"] + " withdrew " + str(amount)
        )

        print("Withdrawal Successful")

    else:

        print("Insufficient Balance")


# Transfer money
def transfer_money(current_user):

    receiver = input("Enter receiver account number: ")

    if receiver not in users:
        print("Receiver account not found")
        return

    amount = float(input("Enter amount to transfer: "))

    if amount <= current_user["balance"]:

        current_user["balance"] -= amount

        users[receiver]["balance"] += amount

        save_users()

        print("Transfer Successful")

    else:

        print("Insufficient Balance")


# Change PIN
def change_pin(current_user):

    old_pin = input("Enter old PIN: ")

    if old_pin == current_user["pin"]:

        new_pin = input("Enter new PIN: ")

        current_user["pin"] = new_pin

        save_users()

        print("PIN changed successfully")

    else:

        print("Incorrect PIN")


# Transaction history
def transaction_history():

    try:

        with open("transactions.txt", "r") as file:

            data = file.read()

            if data:
                print(data)
            else:
                print("No transactions available")

    except FileNotFoundError:

        print("No transaction history found")


# Main program
while True:

    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        create_account()

    elif choice == "2":

        current_user, account_number = login()

        if current_user:

            while True:

                print("\n===== ATM MENU =====")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer Money")
                print("5. Change PIN")
                print("6. Transaction History")
                print("7. Logout")

                option = input("Enter choice: ")

                if option == "1":
                    check_balance(current_user)

                elif option == "2":
                    deposit(current_user)

                elif option == "3":
                    withdraw(current_user)

                elif option == "4":
                    transfer_money(current_user)

                elif option == "5":
                    change_pin(current_user)

                elif option == "6":
                    transaction_history()

                elif option == "7":
                    break

                else:
                    print("Invalid Choice")

    elif choice == "3":

        print("Thank you")

        break

    else:

        print("Invalid Choice")