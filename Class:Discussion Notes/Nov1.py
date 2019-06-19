
#in
#range(Start, Stop, Step)
#l=[-9, -5, 10, 4, 5, 2, 1, 10, 8]

#list(filter(lambda x: range(-5, 5), l))
#range (-5,5)

# start, stop step have to be integers, positive or negative

# lambda
# map
# filter
# reduce
# in
l=[-3,-90,8,7,34,23,12,15,10,9,-2,-1]

print(list(range(-5,5,2)))
print(list(range(5,-5,-1)))

def intRange(l):
    f= lambda x: x in range(-2,10)
    return list(filter(f,l))
    
print(intRange(l))

'''
Write a function noZeroLists that takes a list of lists and removes any inner lists 
that contain at least one 0 in them. For example, noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]]) 
returns [[1,2,3], [], [1,1,1]]. Python's "in" operator for checking whether a value is in a list will be useful.
'''

def noZeroLists(l):
    return list(filter(lambda x: not(0 in x),l))
    # return list(filter(lambda x: 0 not in x,l))
    
print(noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]]))

'''
Write a function intersect that takes two lists l1 and l2 and returns a list identical to l1 but with all 
elements of l2 removed. THAT IS NOT WHAT INTERSECTION SHOULD DO! RENAME AS SET DIFFERENCE AND MAKE SURE THE IMPL IS CORRECT 
For example, intersect([1,2,3], [2,4,6]) is [1,3]. Python's "in" operator for checking whether a value is in a list will be useful.
'''
def

'''
Write a function innerMultiply that multiplies all elements of a list of lists by a given number. For example, 
innerMultiply([[1,2,3], [4,5]], 10) returns [[10,20,30], [40,50]].
'''