
# 🏦 Bank Account Management System

A simple **Bank Account Management System built with Python** using **Object-Oriented Programming (OOP)** concepts.

The project allows users to log in using their account name and perform basic banking operations such as depositing money, withdrawing money, checking their balance, and viewing the updated bank account dictionary.

## 📌 Features

* 🔐 Account holder verification
* 💰 Deposit money
* 💸 Withdraw money
* 📊 Display current balance
* 📖 Display all bank accounts
* 🔄 Automatically update the dictionary after deposit/withdrawal
* ⚠️ Validate invalid deposit and withdrawal amounts
* 🚫 Prevent withdrawal when the balance is insufficient
* 🧱 Uses Python classes and encapsulation

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Dictionary
* Classes and Objects
* Encapsulation
* Private variables
* Conditional statements
* Loops
* Functions/Methods

## 📂 Project Structure

```text
Bank-Account-Management/
│
├── bank_account.py
└── README.md
```

## ⚙️ How It Works

The program starts with a dictionary containing account holders and their balances:

```python
bank_Account_list = {
    "Ahmad": 1000,
    "Ali": 2000,
    "Waleed": 3000,
    "Hassan": 4000,
    "Zeeshan": 5000
}
```

The user enters their name. If the name exists in the dictionary, a `BankAccount` object is created.

```python
account = BankAccount(name, balance)
```

The program then displays a banking menu.

### Main Menu

```text
----- BANK MENU -----
1. Deposit
2. Withdraw
3. Display Balance
4. Show Dictionary
5. Exit
```

## 💰 Deposit

The user can deposit money into their account.

Example:

```text
Enter deposit amount: 500

Deposited: 500
Your new balance is: 1500
Dictionary updated!
```

The dictionary is also updated:

```python
{
    "Ahmad": 1500,
    "Ali": 2000,
    "Waleed": 3000,
    "Hassan": 4000,
    "Zeeshan": 5000
}
```

## 💸 Withdraw

The user can withdraw money if they have enough balance.

Example:

```text
Enter withdrawal amount: 500

Withdrawn: 500
Your new balance is: 500
Dictionary updated!
```

The dictionary is updated automatically.

If the withdrawal amount is greater than the balance:

```text
Insufficient balance
```

## 📊 Display Balance

The user can check their current account information:

```text
Account Holder: Ahmad
Your balance is: 1000
```

## 📖 Show Dictionary

Option 4 displays all accounts and their latest balances.

Example:

```text
Updated Bank Accounts:
{
    'Ahmad': 1500,
    'Ali': 2000,
    'Waleed': 3000,
    'Hassan': 4000,
    'Zeeshan': 5000
}
```

## 🔒 OOP Concepts Used

### 1. Class

The project uses a `BankAccount` class:

```python
class BankAccount:
```

### 2. Constructor

The `__init__()` method initializes the account holder and balance:

```python
def __init__(self, account_holder, balance):
    self.__account_holder = account_holder
    self.__balance = balance
```

### 3. Encapsulation

The account holder and balance are private variables:

```python
self.__account_holder
self.__balance
```

The double underscore `__` makes them private by name mangling.

### 4. Methods

The class contains several methods:

```text
deposit()
withdraw()
display_balance()
get_balance()
```

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Open the Project

```bash
cd Bank-Account-Management
```

### Step 3: Run the Python File

```bash
python bank_account.py
```

## 🧪 Example

```text
Enter your name: Ahmad

Account found!
Account Holder: Ahmad
Your balance is: 1000

----- BANK MENU -----
1. Deposit
2. Withdraw
3. Display Balance
4. Show Dictionary
5. Exit

Enter your choice: 1
Enter deposit amount: 500

Deposited: 500
Your new balance is: 1500
Dictionary updated!
```

## 🎯 Learning Objectives

This project was created to practice:

* Python fundamentals
* Dictionaries
* Classes and objects
* Constructors
* Encapsulation
* Private variables
* Methods
* `if/elif/else`
* `while` loops
* User input
* Updating data dynamically
* Basic banking logic

## 🚀 Future Improvements

Possible improvements for future versions:

* Add account numbers
* Add PIN/password authentication
* Add transaction history
* Add transfer-money functionality
* Add multiple account types
* Store account data in a file or database
* Add a graphical user interface (GUI)
* Add exception handling for invalid input
* Add an option to create new accounts

## 👨‍💻 Author

**Muhammad Ahmad**

This project was created as a Python OOP practice project.
