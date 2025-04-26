class BankAccount:
    """Class to simulate bank account"""
    def __init__(self, password):
        self.balance = 0
        self.password = password.strip()  # ensure no extra space
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        user_password = input("Enter password to withdraw: ").strip()
        print(f"Expected: '{self.password}', Entered: '{user_password}'")  # debug
        if user_password != self.password:
            return "Incorrect password. Withdrawal denied."
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return self.balance
ac101 = BankAccount(password="1234")
while True:
    print("\n==== Bank Menu ====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        ac101.deposit(amount)
        print("Amount deposited. Current balance:", ac101.balance)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        result = ac101.withdraw(amount)
        print("Withdrawal result:", result)
        print("Balance after withdrawal:", ac101.balance)

    elif choice == "3":
        print("Current balance:", ac101.balance)
    elif choice == "4":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
