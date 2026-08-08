bank_Account_list = {
    "Ahmad": 1000,
    "Ali": 2000,
    "Waleed": 3000,
    "Hassan": 4000,
    "Zeeshan": 5000
}


class BankAccount:

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
            print("Your new balance is:", self.__balance)
            return True
        else:
            print("Invalid amount")
            return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False

        elif amount > self.__balance:
            print("Insufficient balance")
            return False

        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
            print("Your new balance is:", self.__balance)
            return True

    def display_balance(self):
        print("Account Holder:", self.__account_holder)
        print("Your balance is:", self.__balance)

    def get_balance(self):
        return self.__balance


# User enters name
name = input("Enter your name: ")

if name in bank_Account_list:

    balance = bank_Account_list[name]
    account = BankAccount(name, balance)

    print("\nAccount found!")
    account.display_balance()

    while True:

        print("\n----- BANK MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Show Dictionary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            amount = int(input("Enter deposit amount: "))

            if account.deposit(amount):
                # Update dictionary
                bank_Account_list[name] = account.get_balance()

                print("Dictionary updated!")

        elif choice == "2":

            amount = int(input("Enter withdrawal amount: "))

            if account.withdraw(amount):
                # Update dictionary
                bank_Account_list[name] = account.get_balance()

                print("Dictionary updated!")

        elif choice == "3":

            account.display_balance()

        elif choice == "4":

            print("\nUpdated Bank Accounts:")
            print(bank_Account_list)

        elif choice == "5":

            print("Thank you for using the bank.")
            break

        else:
            print("Invalid choice")

else:
    print("Please re-check your information.")
    print("Account not found.")