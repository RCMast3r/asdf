from math import sqrt
import numpy as np

with open("test03.txt") as textFile:
        lines = [line.split() for line in textFile]


linesnp=np.asarray(lines)
linesint=linesnp.astype(int)
print("Test 03 Problem 1")
print("the maximum value is ",np.amax(linesint))

print("The maximum occurs in ")

print("row col")



for (x,y), value in np.ndenumerate(linesint):

    if linesint[x][y]==np.amax(linesint):
        print(x,"\t",y)
    
