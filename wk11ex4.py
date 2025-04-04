balance = 1000
deposit = 0
menuOption = 0

print("ATM MENU")

while menuOption != 4:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    menuOption = int(input("Choose an option: "))

    if menuOption == 1:
        print(f"Your balance is: {balance}")
        #break
    if menuOption == 2:
        deposit = float(input("Enter deposit ammount: "))
        balance += deposit
        print("Deposit successful.")
        #break
    if menuOption == 3:
        withdraw = float(input("Enter withdrawal ammount: "))
        if withdraw > balance:
            print("Not enough balance!")
        else:
            balance -= withdraw
        #break
    
print("Thanks for using the ATM!\n")