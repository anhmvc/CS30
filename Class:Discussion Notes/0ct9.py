def doubleValue(num):
    return 2*num
    
def sumOfSquares(num1, num2):
    return pow(doubleValue(num1),2)+pow(abs(doubleValue(num2)),2)
    
def main():
    num1 = int(input("Enter the first integer number "))
    num2 = int(input("Enter the second integer number "))
    
    result = sumOfSquares(num1, num2)
    print( result )
    
#main()

'''
Written By : Anh Mac
Description : Write a recursive function that will count down to zero
Date : 10/0/2019
'''

def countDown(num):
    if num == 0:
        return(" Blast off ")
    else:
        print(num)
        return countDown(num-1)
print(countDown(10))

'''
Description : Write a function named factorial that takes an integer number as an argument and computes the factorial and returns the result.
'''

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
        
#print(factorial(3))

'''
Description: Write a function that will count all the positive numbers occurrence in the list.
'''

listOfNumber= [7,9,-9,5,89,-98]
myList=[]
num1 = int(input("Enter an integer number"))
myList.append(num1)
print(myList)

print(count(listOfNumber))
    