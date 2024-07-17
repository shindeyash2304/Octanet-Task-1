class ATMMachine:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")
    
    def menu(self):
        while True:
            print("\n===== ATM Machine =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

# Create an instance of ATMMachine and call the menu method to start the simulation
atm = ATMMachine()
atm.menu()
