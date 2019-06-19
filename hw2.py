'''
Description: A program that implements recursive functions to solve problems involving manipulating lists.
(I did not discuss this assignment with anyone.)
Written By: Anh Mac
Date: 10/22/2018
''' 

from doctest import testmod

def doubleAll(l):
    """Returns a list that is identical to l but with each value doubled.

    Arguments:
    l -- a list of integers
    """
    if l==[]:
        return []
    else:
        doubleValue = 2*l[0]
        return [doubleValue] + doubleAll(l[1:])
        

def countPos(l):
    """Returns the number of elements in l that are positive.

    Arguments:
    l -- a list of integers
    """
    if l==[]:
        return 0
    elif l[0] <= 0:
        return 0 + countPos(l[1:])
    else:
        return 1 + countPos(l[1:])


def intRange(low, high):
    """Returns a list of integers in the range low to high, inclusive.

    Arguments:
    low -- the lower bound (an integer)
    high -- the upper bound (an integer)
    """
    if low > high:
        return []
    else:
        return [low] + intRange(low+1, high)
    

def merge(l1, l2):
    """Merge two sorted integer lists to produce a new sorted list of their elements.

    Arguments:
    l1 -- the first list
    l2 -- the second list
    """
    if l1==[] and l2==[]:
        return []
    elif l1==[]:
        return l2
    elif l2==[]:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2[0:])
    elif l1[0] > l2[0]:
        return [l2[0]] + merge(l1[0:], l2[1:])


# run all doctests whenever this file is run (via the Run menu in IDLE)
if __name__ == '__main__':
    testmod()