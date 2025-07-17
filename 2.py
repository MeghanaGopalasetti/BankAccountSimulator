import time
from logging import exception
class BankAccount:
    def __init__(self, owner, account_number, ifsc_code, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.ifsc_code = ifsc_code
        self.balance = balance

    def log_transaction(self, message):
        """Log transaction details to a file."""
        with open("abc.txt", "a") as f:               #abc.txt--file name,a--append mode
            f.write(f"{time.ctime()} - {message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            time.sleep(4)
            print(f"Deposited: ${amount:.2f}")
            self.log_transaction(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            time.sleep(4)
            print("Invalid deposit amount.")
            self.log_transaction("Failed deposit attempt: Invalid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                time.sleep(4)
                print(f"Withdrew: ${amount:.2f}")
                self.log_transaction(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}.")
            else:
                time.sleep(4)
                print("Insufficient balance.")
                self.log_transaction("Failed withdrawal attempt: Insufficient balance.")
        else:
            time.sleep(4)
            print("Invalid withdrawal amount.")
            self.log_transaction("Failed withdrawal attempt: Invalid amount.")

    def check_balance(self):
        time.sleep(3)
        print("...processing")
        time.sleep(4)
        print(f"Current Balance: ${self.balance:.2f}")
        self.log_transaction(f"Checked balance: ${self.balance:.2f}.")

    def account_details(self):
        print("\n--- Account Details ---")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"IFSC Code: {self.ifsc_code}")
        print(f"Current Balance: ${self.balance:.2f}")
        self.log_transaction("Viewed account details.")

def main():
    print("Welcome to the Bank Account Simulator!")
    while True:
        name = input("Enter account owner's Full Name (alphabets only): ")
        if all(part.isalpha() for part in name.split()):
            break
        else:
            print("Invalid input. Please enter a name with alphabets only (no digits or special characters).")

 #   name = input("Enter account owner's Full_Name: ")
    try:
        account_number = int(input("Enter Account Number: "))
    except:
        print("Account Number can't contain characters")
        account_number = int(input("Enter Valid Account Number: "))

    ifsc_code = input("Enter IFSC Code: ")

    # Initialize the BankAccount
    account = BankAccount(name, account_number, ifsc_code)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.account_details()
        elif choice == "5":
            time.sleep(3)
            print("Thank you for using the Bank Account Simulator.")
            break
        else:
            time.sleep(2)
            print("Invalid choice. Please try again.")

main()
