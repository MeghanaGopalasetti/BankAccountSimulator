import time   # here,time is module
class BankAccount:
    def __init__(self, owner, account_number, ifsc_code, balance=0):

        self.owner = owner
        self.account_number = account_number
        self.ifsc_code = ifsc_code
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            time.sleep(2)
            print(f"Deposited: ${amount:.2f}")
        else:
            time.sleep(2)
            print("Invalid deposit amount.")

    def withdraw(self, amount):

        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                time.sleep(3)
                print(f"Withdrew: ${amount:.2f}")
            else:
                time.sleep(3)
                print("Insufficient balance.")
        else:
            time.sleep(3)
            print("Invalid withdrawal amount.")

    def check_balance(self):

        time.sleep(2)
        print("...processing")
        time.sleep(3)
        print(f"Current Balance: ${self.balance:.2f}")

    def account_details(self):

        print("\n--- Account Details ---")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"IFSC Code: {self.ifsc_code}")
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    #f = open("abc.txt", "w")
    print("Welcome to the Bank Account Simulator!")
    name = input("Enter account owner's name: ")
    account_number = int(input("Enter Account Number: "))
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
            time.sleep(5)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
            time.sleep(5)
        elif choice == "3":
            account.check_balance()
            time.sleep(5)
        elif choice == "4":
            account.account_details()
            time.sleep(5)
        elif choice == "5":
            time.sleep(3)
            print("Thank you for using the Bank Account Simulator.")
            break
        else:
            time.sleep(2)
            print("Invalid choice. Please try again.")
            time.sleep(5)

main()
