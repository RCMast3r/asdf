import numpy as np

import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


x,y=np.meshgrid(np.linspace(0,2*math.pi,num=1000),np.linspace(0,2*math.pi,num=1000))
z=np.sin(x)*np.cos(y)
fig1=plt.figure(1)
plt.clf
ay=fig1.gca(projection='3d')


ay.plot_surface(x,y,z)
plt.show()