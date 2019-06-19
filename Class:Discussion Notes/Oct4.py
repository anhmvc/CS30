''''
Description: Write a program that will ask the user for an integer number and your program should decide if this number is negative or positive or zero
   concatenate only happens for strings
'''
flag= True
if (flag):
    print("Flag is ", flag)
    flag= False
else:
    print("Flag is ", flag)

    
intValue = int (input("Please enter an integer number ? "))

   print("the number you entered is:",+ str(intValue +2 ))
   
#intValue = int(intValue)
if (intValue >0) :
    print("********You entered a positive number**********")
elif (intValue <0):
    print("********You entered a negative number**********")
else:
    print("You entered zero")

#from random import randint    
import random 
#import random

val = random.randint(1,4)
def magic8ball(question):
    if (val==1):
        return ("Definitely.")
    elif (val==2):
        return ("NO WAY")
    elif (val==3):
        return ("It is not Known.")
    else:
        return ("Maybe ..")
        
question = input(" tell me your question and I will ask the magic ball to answer? ")
print(magic8ball(question))

