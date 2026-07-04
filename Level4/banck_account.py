from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

class BankAccount:
    def __init__(self, name, password):
        self.account_holder_name = name
        self.password = password

        data = f"{name}:{password}".encode()
        self.account_number = cipher.encrypt(data).decode()

        print("Your account number is:")
        print(self.account_number)

        self.account_balance = 0

    def authenticate(self, name, password, account_number):
        try:
            decrypted = cipher.decrypt(account_number.encode()).decode()
            stored_name, stored_password = decrypted.split(":")

            return (
                stored_name == name
                and stored_password == password
                and account_number == self.account_number
            )
        except:
            return False

    def get_statement(self, name, password, account_number):
        if self.authenticate(name, password, account_number):
            print("\n----- Statement -----")
            print("Name:", self.account_holder_name)
            print("Account Number:", self.account_number)
            print("Balance:", self.account_balance)
        else:
            print("Incorrect Credentials....")

    def update_balance(self, name, password, account_number, amount):
        if self.authenticate(name, password, account_number):
            self.account_balance += amount
            print("Deposit Successful")
            print("Balance:", self.account_balance)
        else:
            print("Incorrect Credentials....")

    def withdraw_amount(self, name, password, account_number, amount):
        if self.authenticate(name, password, account_number):
            if self.account_balance >= amount:
                self.account_balance -= amount
                print("Withdrawal Successful")
                print("Balance:", self.account_balance)
            else:
                print("Insufficient Balance....")
        else:
            print("Incorrect Credentials....")


bank_xyz = None

while True:
    choice = int(input("""
Welcome to XYZ Bank

1. Create account
2. Deposit
3. Withdraw
4. Get statement
5. Exit

Enter your choice: """))

    if choice == 5:
        print("Thank you...")
        break

    if choice == 1:
        name = input("Enter your name: ")
        passwd = input("Enter your password: ")
        bank_xyz = BankAccount(name, passwd)

    elif bank_xyz is None:
        print("Please create an account first.")

    else:
        name = input("Enter your name: ")
        passwd = input("Enter your password: ")
        account_number = input("Enter account number: ")

        if choice == 2:
            amount = int(input("Enter amount to deposit: "))
            bank_xyz.update_balance(name, passwd, account_number, amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            bank_xyz.withdraw_amount(name, passwd, account_number, amount)

        elif choice == 4:
            bank_xyz.get_statement(name, passwd, account_number)