from functools import reduce
# lisp programming

''' LAMBDA '''
def add(x,y):
    return x+y
print(add(2,4))

# lambda arguments: expressions
addUsingLambda=lambda x,y: x+y
print(addUsingLambda(2,4))

def compare(x,y):
    if x>y:
        return x
    else:
        return y
print(compare(5, 10))

compareUsingLambda = lambda x,y: x if x>y else y
print(compareUsingLambda(5,10))

''' MAP '''
l=[-1, 2, 9, 5, 4]
def doubleAll(l):
    if l==[]:
        return []
    else:
        return [2*l[0] + doubleAll(l[1:])]
        
double = lambda x: 2*x
print(double(l))

# map(function, list)

print(list(map(double, l)))
print(list(map(lambda x: pow(x,2), l)))

''' FILTER '''
l=[3,8,7,12,18,4,22]
def even(x):
    return x%2==0
print(even(66))

# filter(function that returns boolean statement, list)
print(list(filter(even, l)))
print("list of even numbers filtered out: ", list(filter(lambda x: x%2==0, l)))

''' REDUCE '''
# reduce(function that takes two arguments, list)
print(reduce(lambda x,y: x+y,l))
print(reduce(lambda x,y: x if x>y else y,l))
