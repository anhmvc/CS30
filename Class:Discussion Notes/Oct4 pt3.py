'''

children 12 and under get a discounted price of $40
anyone 65 or over only has to pay $60
everyone else has to pay $85
write a function that takes in the age of a guest and returns the correct price

'''

age = int(input("Please enter the age of the guest ? "))
if (age <= 12):
    print ("$40")
elif (age >= 65):
    print ("$60")
else:
    print ("$85")
    