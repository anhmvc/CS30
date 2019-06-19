'''
Description: A program that implements the Python turtle library to draw a tree.
(I did not discuss this assignment with anyone.)
Written By: Anh Mac
Date: 11/6/2018
'''

from turtle import *

# I've implemented this function for you; do not edit it.
def tree( trunkLength, angle, levels ):
    left(90)
    sidewaysTree(trunkLength, angle, levels)

# This is the function you have to implement.
def sidewaysTree( trunkLength, angle, levels ):
    """ draws a sideways tree
        trunklength = the length of the first line drawn ("the trunk")
        angle = the angle to turn before drawing a branch
        levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        forward(trunkLength)
        left(angle)
        sidewaysTree(trunkLength*0.5, angle, levels-1)
        right(angle*2)
        sidewaysTree(trunkLength*0.5, angle, levels-1)
        left(angle)
        backward(trunkLength)
    
# tree(128,30,6)

