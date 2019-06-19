from functools import reduce

#l = [0,1,2,3,4,5,-2,3,-5,5]

def doubleAll(l):
    return list(map(lambda x: x*2, l))
    
#print(doubleAll(l))

def allPositive(l):
    return list(filter(lambda x: x > 0, l))
    
##print(allPositive(l))

def average(l):
    return reduce(lambda x, y: x+y, l) / len(l)
    
#print(average(l))

# l = [[1,2], [0,2], [2, 0], [4, 2]]

def switchList(l):
    return list(map(lambda x: [x[1],x[0]], l))

# print(switchList(l))

def noZeroLists(l):
    return list(filter(lambda x: 0 not in x, l))
    
print(noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]]))

def intersect(l1,l2):
    return(list(map(lambda x,y: x if x not in y else not x, l1, l2)))
    
print(intersect([1,2,3], [2,4,6]))