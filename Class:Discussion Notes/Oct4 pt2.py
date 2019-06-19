'''
Description : create a function that doubles any value passed as an argument
'''

num1= int(input("Enter the 1st number ? "))
num2= int(input("Enter the 2nd number ? "))

def doubleNumber(num):
    return 2*num
    
def sumOfSquares(num1, num2):
    
    #return num1**2+num2**2
    return (pow(num1,2)+pow(num2,2))


print(sumOfSquares(num1, num2))
#print(doubleNumber(77))