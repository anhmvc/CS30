'''
Description:
Written by :
Date:
'''
firstName = "Anh "
lastName = "Mac"
# concatenation
fullName = firstName + lastName
print(fullName)
# print(len(firstName))
print(firstName[1:])
print(firstName*3)

#lists
mixList = ['computer science 30', 1999, format( 56.90, '.1f'), 'Anna', 'physics', 'c']
numberList = [89, 787, 78.6, 32.90, 788.67]
concatenateLists = mixList + numberList
#print(concatenateLists)
print(concatenateLists[2:8])

'''print(mixList)
print(mixList[0])
print(len(mixList))
print(mixList[1:5])
print(format(56.900000, '.0f'))
print(int(format(56.900000, '.0f'))+ 34)
print(float(87))'''

num1 = 90
num2 = 37
num3 = -39

if (num1 < num3):
    print("num1 is greater than num2")
else:
    print("num1 is less than num2")
    
print("*******program ending******")