# clone takes an item e and a nonnegative integer n# and returns a list containing n copies of e

def clone(e, n):
    if n == 0:
        return []
    else:
        return [e] + clone(e, n-1)
        
# count takes item e and list l and returns number of occurrences of e in l
def count(e, l):
    if l == []:
        return 0
    elif l[0] == e:number = 1
        return number + count(e, l[1:])
    else:
        return count(e, l[1:])
        
# minimum returns the smallest element in a list of integers
# may assume the list is nonempty

def minimum(l):
    if len(l) == 1:
        return l[0]
    if l[0]<=l[1]:
        return minimum([l[0]]+l[2:])
    if l[0]>l[1]:
        return minimum(l[1:])
        
# function q checks that every number in a list between 10 and 100 (inclusive) is even
def q(l):
    if l == []:
        return True
    if l[0]>=10 and l[0]<=100:
        if l[0]%2 !=0:
            return False
        else:
            return q(l[1:])
    else:
        return q(l[1:])
        
        
from random import randint

def intersection(l1,l2):
    result=[]
    for x in l1:
        if x in l2 and x not in result: # deals with duplicates
            result += [x]
        return result
        
def intersection2(l1,l2):
    answer = []
    i=0
    while i<len(l1):
        if l1[i] in l2:
            answer = answer + [l[i]]
        i = i+1
    return answer
    
def commonPrefix(s1,s2):
    answer = ''
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i]==s2[i]:
            answer += s1[i]
        i += 1
    return answer
    
def higherLower():
    playAgain = 1
    while playAgain == 1:
        secret = randint(1,100)
        guess = int(input('Guess a number between 1 and 100 '))

def mymax(l):
    result = l[0]
    for x in l:
        if x>result:
            result = x
    return result
    
def mymax1(l): # loop over actual elements of list
    maxValue = l[0]
    maxIndex = 0
    currIndex = 0
    for x in l:
        if x>maxValue:
            maxValue = x
            maxIndex = currIndez
        currIndex += 1
    return [maxValue, maxIndex]

def mymax2(l): # loop over indices of list
    maxValue = l[0]
    maxIndex = 0
    n = len(l)
    for i in range(0,n):
        if l[i] > maxValue:
            maxValue = l[i]
            maxIndex = i
    return [maxValue, maxIndex]
    
def find(x, l): # returns the lowest index i in l where l[i] == x, return, -1 otherwise
    for i in range(0, len(l)):
        if x == l[i]:
            return i # works because function ends when it reaches this return statement
    return -1
    
def indexValuePairs(l):
    result = []
    for i in range(len(l)):
        result = result + [[i,l[i]]]
    return result

def indexValuePairsMap(l):
    return list(map(lambda i: [i,l[i]], range(len)))
    
def test():
    for x in ['a', 'b', 'c']:
        print(x)
    return

def test1():
    for x in range(0,3): # should loop 3 (when x=0,1,2)
        print('hi')
        
# recursive version
def sumListRec(l):
    if l == []:
        return 0
    else:
        return l[0]+sumListRec(l[1:])
        
def sumList(l):
    result = 0 # result is called an accumulator
    for n in l:
        result += n
    return result

    
def factorial(n):
    result = 1
    for x in range(1, n+1):
        result *= n
    return result