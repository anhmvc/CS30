def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y
    
def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y 

print("Select a function.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit calculator.py")

userChoice = int(input("Choose your option: "))

def calculator(userChoice):
    x = int(input("Please enter the first number? "))
    y = int(input("Please enter the second number? "))
    if userChoice == 1:
        return addition(x, y)
    elif userChoice == 2:
        return subtraction(x, y)
    elif userChoice == 3:
        return multiplication(x, y)
    elif userChoice == 4:
        return division(x, y)
    elif userChoice == 5:
        return quit()
        
print(calculator(userChoice))

