#def delete(e,l):
   # if l==[]:
    #    return[]
  #  else:
       # if l[0]==e:
        #    return l[1:]
        #else:
        #    return [l[0]] + delete(e,l[1:])
            
from turtle import *
import time

'''
'''
def triangle(n, d):
    helperTriangle(n, d, 360/n)
    
def helperTriangle(n, d, angle):
    if n == 0:
        return
    else:
        forward(d)
        time.sleep(2)
        left(angle)
        time.sleep(2)
        helperTriangle(n-1, d, angle)
        time.sleep(4)
    
# triangle(3, 100)


