 ATM Machine Simulation

1. Class Definition:
    python
    class ATMMachine:
        def __init__(self):
            self.balance = 0
    
    - This defines a class named `ATMMachine`.
    - The `__init__` method initializes an instance of the class with a `balance` attribute set to 0.

2. Check Balance Method:
    python
    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
    
    - This method prints the current balance in the account formatted to two decimal places.

3. Deposit Money Method:
    python
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    
    - This method takes an `amount` as input.
    - If the amount is greater than 0, it adds the amount to the balance and prints a confirmation message.
    - If the amount is not positive, it prints an error message.

4. Withdraw Money Method:
    python
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")
    
    - This method takes an `amount` as input.
    - If the amount is greater than the current balance, it prints an insufficient funds message.
    - If the amount is not positive, it prints an error message.
    - If the amount is valid and within the balance, it deducts the amount from the balance and prints a confirmation message.

5. Menu Method:
    python
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
    
    - This method displays a menu of options to the user in a loop.
    - It prompts the user to choose an option:
        - `1` calls the `check_balance` method.
        - `2` prompts the user to enter a deposit amount and calls the `deposit` method with the entered amount.
        - `3` prompts the user to enter a withdrawal amount and calls the `withdraw` method with the entered amount.
        - `4` exits the loop and ends the simulation.
        - Any other input prints an error message.

6. Creating an Instance and Running the Menu:
    python
    atm = ATMMachine()
    atm.menu()
    
    - This creates an instance of the `ATMMachine` class.
    - The `menu` method is called on this instance to start the simulation.

 How It Works
- When the program runs, it creates an ATM machine instance with an initial balance of 0.
- The user is repeatedly presented with a menu until they choose to exit.
- Based on the user's choice, the program performs the corresponding action:
  - Checking the balance displays the current balance.
  - Depositing money updates the balance with the entered amount.
  - Withdrawing money deducts the entered amount from the balance if sufficient funds are available.
- If the user chooses to exit, the program thanks the user and terminates.

 User Interaction
1. Check Balance: 
    - User selects option `1`.
    - The program displays the current balance.
    
2. Deposit Money:
    - User selects option `2`.
    - The program prompts the user to enter a deposit amount.
    - If the amount is valid, it adds it to the balance and confirms the deposit.

3. Withdraw Money:
    - User selects option `3`.
    - The program prompts the user to enter a withdrawal amount.
    - If the amount is valid and there are sufficient funds, it deducts it from the balance and confirms the withdrawal.

4. Exit:
    - User selects option `4`.
    - The program thanks the user and exits the loop, ending the simulation.

This simulation provides a basic structure for an ATM machine, allowing for further expansion and customization as needed.
