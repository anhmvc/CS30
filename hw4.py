'''
Description: A program that implements functions using list comprehension with map, filter, and reduce.
(I consulted https://www.python-course.eu/lambda.php and the textbook for more examples on list comprehension functions and 
how to implement the lambda operator.)
Written By: Anh Mac
Date: 11/12/2018
'''

from functools import reduce

'''
IMPORTANT:  The only function below that is allowed to use recursion is map2.
All other functions (including any helper functions you write) must not be recursive.  Instead, they should make calls to one or more of map, 
filter, and reduce to perform the necessary list traversals.
'''

def inRange(lo, hi, l):
    '''
    Returns all numbers in the list l that are between lo and hi (inclusive).
    >>> inRange(5, 15, [3, 15, 7, 21, 12, 34])
    [15, 7, 12]
    '''
    return list(filter(lambda x: x >= lo and x <= hi, l))
    
# print(inRange(5, 15, [3, 15, 7, 21, 12, 34]))

def zeroNegatives(l):
    '''
    Replaces all negative numbers in list l with 0,
    leaving all other numbers unchanged.
    >>> zeroNegatives([1,3,-4,-6,5,-5])
    [1, 3, 0, 0, 5, 0]
    '''
    return list(map(lambda x: 0 if x<0 else x, l))

# print(zeroNegatives([1,3,-4,-6,5,-5]))

def flatten(l):
    '''
    Flattens a list of lists into a single list.
    >>> flatten([[1,2], [3], [], [4,5,6]])
    [1, 2, 3, 4, 5, 6]
    '''
    def combine(x,y):
        return x+y
    return list(reduce(combine, l))

# print(flatten([[1,2], [3], [], [4,5,6]]))

def halveEvens(l):
    '''
    Removes all odd integers from l and divides each even number in half.
    The list l is assumed to be a list of integers, and the function returns
    a list of integers.
    >>> halveEvens([10,21,32,42,55])
    [5, 16, 21]
    '''
    removeOdd = list(filter(lambda x: x%2 == 0, l)) # create list with odd numbers removed 
    return list(map(lambda x: x//2, removeOdd)) # half all remaining values in filtered list

# print(halveEvens([10,21,32,42,55]))

def map2(f, l1, l2):
    '''
    Behaves like the map function, but it traverses two lists simultaneously.
    Specifically, map(f, [x1,...,xn], [y1,...,yn]) returns [f(x1,y1), ..., f(xn,yn)].
    You may assume that l1 and l2 have the same length.
    >>> map2(lambda x,y: [x,y], [1,2,3], [4,5,6])
    [[1, 4], [2, 5], [3, 6]]
    '''
    if l1 == []:
        return []
    if l2 == []:
        return []
    else:
        return [f(l1[0], l2[0])] + map2(f, l1[1:], l2[1:])

# print(map2(lambda x,y: [x,y], [1,2,3], [4,5,6]))

def dotProduct(v1, v2):
    '''
    Computes the dot product of the vectors v1 and v2, each of which is a list
    of numbers.  The dot product of [x1,...,xn] and [y1,...,yn] is
    x1*y1 + ... + xn*yn.
    You may assume that v1 and v2 have the same length.
    NOTE: You will want to make use of the map2 function that you defined above.
    >>> dotProduct([1,2,3],[4,5,6])
    32    
    '''
    def product(x, y):
        return map2(lambda x,y: x*y, v1, v2)
    return reduce(lambda x,y: x+y, product(v1, v2))

# print(dotProduct([1,2,3],[4,5,6]))
