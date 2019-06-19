'''
Description: A program that determines the length of bursts of zero's in a list of N numbers stored in a list.
(I did not discuss this assignment with anyone.)
Written By: Anh Mac
Date: 12/4/2018
'''
def createList():
    global burstList
    burstList = []
    N = input("Please enter desired size of list [NOTE: Input must be between 1 and 50]: ")
    while len(N) == 0 or int(N) <= 0:
        N = input("INVALID INPUT. [NOTE: Size of list must be between 1 and 50]. Please re-enter desired size of list: ")
    for i in range(1, int(N)+1):
        num = input("Enter number " + str(i) + ": ")
        while len(num) == 0:
            num = input("INVALID INPUT. Re-enter number " + str(i) + ": ")
        burstList += [int(num)]

def countBursts():
    global burstLengths
    burstLengths = []
    burstOpen = 0
    count = 0
    for i in range(len(burstList)):
        if burstList[i] == 0:
            burstOpen = 1
            count += 1
        else:
            if burstOpen == 1:
                burstLengths += [count]
                count = 0
                burstOpen = 0
            else:
                continue
    if burstOpen == 1:
        burstLengths += [count]

def printList():
    print("Burst  " + " Length")
    i = 0
    if burstLengths == []:
        print("  0       0")
    while i < len(burstLengths) and len(burstLengths) != 0:
        print("  " + str(i+1) + "        " + str(burstLengths[i]))
        i += 1

def averageBurst():
    if burstLengths == []:
        average = 0
    else:
        total = 0
        for i in range(len(burstLengths)):
            total += burstLengths[i] 
        average = total/float(len(burstLengths))
    print("Average burst length: " + format(average,'.2f'))
    
def findMax():
    if burstLengths == []:
        maximum = 0
    else:
        maximum = 0
        for i in range(len(burstLengths)):
            if burstLengths[i] > maximum:
                maximum = burstLengths[i]
            else: 
                continue
    print("Maximum burst length: " + str(maximum))

def findMin():
    if burstLengths == []:
        minimum = 0
    else:
        minimum = 99
        for i in range(len(burstLengths)):
            if burstLengths[i] < minimum:
                minimum = burstLengths[i]
            else:
                continue
    print("Minimum burst length: " + str(minimum))

def totalBurst():
    total = 0
    for i in range(len(burstLengths)):
        total += burstLengths[i]
    print("Total number of zeros: " + str(total))
    
createList()
countBursts()
printList()
averageBurst()
findMin()
findMax()
totalBurst()