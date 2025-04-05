#Variables
#Variable holding initial value
balance = 1000
#Variable to hold deposit amount
deposit = 0
#Variable to hold menuOption
menuOption = 0
#Program Title
print("ATM MENU")
#While loop executing menu until user select 4
while menuOption != 4:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    #Coverts to int and stores the value of user input
    menuOption = int(input("Choose an option: "))
    #Conditional logic to execute menu
    if menuOption == 1:
        #Display the balance amount
        print(f"Your balance is: {balance}")
    if menuOption == 2:
        #Converst to float and stores the value of deposit by the user
        deposit = float(input("Enter deposit ammount: "))
        #Update the balenace value
        balance += deposit
        #Prinbts deposit confirmation Message
        print("Deposit successful.")
    if menuOption == 3:
        #Convert and store the withdraw value by the user.
        withdraw = float(input("Enter withdrawal ammount: "))
        #Check if there is enough money to withdraw
        if withdraw > balance:
            #Display error message
            print("Not enough balance!")
        else:
            #Update the balance value
            balance -= withdraw
#End of the program
print("Thanks for using the ATM!\n")

#Pushed to GitHub Wk11Ex4 repo.