'''
Description: A program that simulate a banking application.
(I did not discuss this assignment with anyone.)
Written By: Anh Mac
Date: 11/30/2018
'''
customers = ['Mike','Jane','Steve']
balances = [300,400,500]

print("//////       WELCOME TO BANK APP       //////")
print("=============================================")

def userName():
    global name
    flag = False
    name = input("Please enter your username? ")
    for i in customers:
        if name == i:
            flag = True
            break
        else:
            flag = False
            continue
    if flag == True:
        print("Username is " + i + ".")
        menu()
    else:
        print('User not found.. [NOTE: First letter of username must be capitalized.]')
        userName()

def menu():
    global x
    x = customers.index(name)
    while name == customers[x]:
        print()
        print("Please choose an option:")
        print("Type D to deposit money")
        print("Type W to withdraw money")
        print("Type B to display Balance")
        print("Type C to change user")
        print("Type E to exit")
        print()
        choice = input("What would you like to do? ").upper()
        if choice == 'D':
            deposit()
        elif choice == 'W':
            displayBalance()
            withdraw()
        elif choice == 'B':
            displayBalance()
        elif choice == 'C':
            changeUser()
        elif choice == 'E':
            print()
            print('''
            /\ 
           /  \ 
          .∧＿∧ 
          ( ･ω･｡)つ━☆・*。 
          ⊂　 ノ 　　　・゜+. 
          しーＪ　　　°。+ *THANK YOU FOR BANKING WITH US TODAY!''')
            quit()
        else:
            print("INVALID OPTION")

def deposit():
    depositAmount = float(input("Enter the amount you'd like to deposit: "))
    if depositAmount >= 0:
        balances[x] += depositAmount
        displayBalance()
    else:
        print("INVALID INPUT!")
        deposit()

def withdraw():
    withdrawAmount = float(input("Enter the amount you'd like to withdraw: "))
    if withdrawAmount <= balances[x] and withdrawAmount >= 0:
        balances[x] = balances[x] - withdrawAmount
        displayBalance()
    elif withdrawAmount < 0:
        print("INVALID INPUT. Please enter a different amount.")
        withdraw()
    else:
        print("INSUFFICIENT FUNDS. Please enter a different amount.")
        withdraw()

def displayBalance():
    print('Your current balance is ' + format(balances[x], '.2f') + '.')

def changeUser():
    userName()
    
userName()