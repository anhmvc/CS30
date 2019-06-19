'''
Description: A program that implements recursive functions to draw shapes using the Python turtle library.
(I discussed the last problem with Sally Seok and Miles Kang and got help from the other classmates' questions on Piazza.)
Written By: Anh Mac
Date: 10/23/2018
'''

from turtle import *

def regularNGon(n, sideLength):
    """Draws a regular polygon.

    Arguments:
    n - the number of sides
    sideLength - the length of each side
    """
    helperNGon(n, sideLength, 360/n)

def helperNGon(n, sideLength, angle):
    if n == 0:
        return
    else:
        forward(sideLength)
        left(angle)
        helperNGon(n-1, sideLength, angle)
        
# regularNGon(8, 100)

def archSpiral(initialLen, increment, angle, n):
    """Draws an Archimedean spiral.

    Arguments:
    initialLen - the length of the first line segment
    increment - the amount to increment the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw
    """
    if n == 0:
        return
    else:
        forward(initialLen)
        left(angle)
        archSpiral(initialLen+increment, increment, angle, n-1)

# archSpiral(1, 0.5, 30, 100)

def logSpiral(initialLen, percentIncrease, angle, n):
    """Draws an logarithmic spiral.

    Arguments:
    initialLen - the length of the first line segment
    percentIncrease - the percentage to increase the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw
    """
    if n == 0:
        return
    else:
        forward(initialLen)
        left(angle)
        logSpiral(initialLen*(1+percentIncrease/100.0), percentIncrease, angle, n-1)
        
# logSpiral(1, 4, 30, 120)
