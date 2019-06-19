'''
Description: A program that implements recursive functions to counting and sorting problems.
(I visited Upsilon Pi Epsilon for tutoring and help on problems 1a and 1b, and referenced PythonCentral for a visual of the mergeSort function.)
Written By: Anh Mac
Date: 11/6/2018
'''

def partition(v, l):
    '''
    Write a function partition that accepts a value v and a list l and partitions l into a list of elements 
    that are equal to v and a list of all other elements. For example, partition(2, [1,5,3,2,2,1,3,2]) returns 
    [[2,2,2], [1,5,3,1,3]]. Note that the result of partition should always be a list that contains exactly two lists.
    '''
    if len(l)==1:
        if l[0]==v:
            return [[l[0]],[]]
        else:
            return [[],[l[0]]]
    if l==[]:
        return [[],[]]
    else:
        equal = []
        nonequal = []
        if l[0]==v:
            equal += [l[0]]
        else:
            nonequal += [l[0]]
        equal += partition(v,l[1:])[0]
        nonequal += partition(v,l[1:])[1]
        return [equal, nonequal]


# print(partition(2, [1,5,3,2,2,1,3,2]))

def countDistinct(l):
    '''
    Write a function countDistinct that accepts a list l and returns the number of distinct elements in the list. 
    For example, countDistinct([1,5,3,2,2,1,3,2]) returns 4. The partition function you wrote above will be a useful 
    helper function for this task, since partitioning a list on its first element has the effect of removing all occurrences 
    of that element from the list.
    '''
    if l==[]:
        return 0
    if len(l)==1:
        return 1
    else:
        return countDistinct(partition(l[0],l)[1]) + 1

# print(countDistinct([1,5,3,2,2,1,3,2]))

def selectionSort(l):
    '''
    Implement a function selectionSort that takes a list and returns a list containing the same elements 
    but sorted from least to greatest. For example, selectionSort([1,5,3,2,2,1,3,2]) returns [1,1,2,2,2,3,3,5].
    '''
    # partition min elements to the front and do it recursively
    if l==[]:
        return []
    else:
        return partition(min(l),l)[0] + selectionSort(partition(min(l),l)[1])


# print(selectionSort([1,5,3,2,2,1,3,2]))

# for use in mergesort below; do not edit
def merge(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])


def mergeSort(l):
    '''
    Implement a function mergeSort that takes a list and returns a list containing the same elements 
    but sorted from least to greatest. For example, mergeSort([1,2,2,1,5,3,1,2]) returns [1,1,1,2,2,2,3,5].
    Merge sort uses the merge function from the previous homework, which I have provided in hw3.py. 
    The algorithm conceptually works as follows. First, split the list into two equal (or in the case of an 
    odd number of elements, close to equal) size lists --- in our example this produces [1,5,3,2] and [2,1,3,2]. 
    Then recursively sort each of these lists --- in our example this produces [1,2,3,5] and [1,2,2,3]. 
    Finally merge the resulting lists to obtain the full sorted list.
    '''
    if len(l)<=1:
        return l
    else:
        middle = len(l)//2
        firstHalf = l[:middle]
        lastHalf = l[middle:] # split list into 2 equal lists
        return merge(mergeSort(firstHalf),mergeSort(lastHalf))

# print(mergeSort([1,2,2,1,5,3,1,2]))