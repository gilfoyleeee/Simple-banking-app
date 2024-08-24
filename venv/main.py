def show_balance(current_balance):
    print(f"Your current balance is: ${current_balance}")

def deposit_balance(current_balance):
    try:
        print("")
        amount = float(input("Enter amount to deposit: $"))
        if amount < 0:
            print("Deposit amount must be positive!")
            return current_balance
        current_balance += amount
        print(f"${amount} deposited successfully.")
        print("")
        print(f"$Your new balance is {current_balance}.")
    except ValueError:
        print("Invalid amount entered!")
    return current_balance

def withdraw_balance(current_balance):
    try:
        print("")
        amount = float(input("Enter amount to withdraw: $"))
        if amount < 0:
            print("Withdrawal amount must be positive!")
            return current_balance
        if amount > current_balance:
            print("Insufficient funds!")
            return current_balance
        current_balance -= amount
        print(f"${amount} withdrawn successfully.")
        print(f"$Your new balance is {current_balance}.")
    except ValueError:
        print("Invalid amount entered!")
    return current_balance

balance = 0
is_running = True

while is_running:
    print("\n************** Banking Program ************\n")
    print("1. Show Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Balance")
    print("4. Exit Program\n")
    
    user_choice = input("Enter your choice from 1-4: ")
    
    if user_choice == '1':
        show_balance(balance)
        
    elif user_choice == '2':
        balance = deposit_balance(balance)
        
    elif user_choice == '3':
        balance = withdraw_balance(balance)
        
    elif user_choice == '4':
        is_running = False  # Corrected assignment
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

print("\nThank you! Have a good day!\n")
