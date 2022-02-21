import numpy as np

from math import *
import matplotlib.pyplot as plt
a=np.linspace(0, 2, num=20)
def calcx(a,x):
    prevx=x
    x=atan((1.2*a) / ((0.6+((1.8*sin(prevx))))+ (0.4*tan(prevx))))
    return x



def main():
    
    xvals=[]
    for aval in a:
        x=.01
        prevx=(calcx(aval,x))
        while abs(prevx-x)>.00000001 :
            prevx=x
            x=calcx(aval,prevx)

        finalx=atan((1.2*aval) / ((0.6+((1.8*sin(x))))+(0.4*tan(x))))
        xvals.append(finalx)

    plt.plot(a,xvals)
    plt.xlabel('a')
    plt.ylabel('x')
    plt.show()
if __name__=="__main__":
    main()
