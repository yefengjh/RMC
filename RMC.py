# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

NQx = np.linspace(-5,5,5)
NQy = np.linspace(-4,4,5)
NQz = np.linspace(-3,3,5)
xx, yy, zz=np.meshgrid(NQx, NQy, NQz, indexing='xy')
newx=xx.reshape(1,-1)
newy=yy.reshape(1,-1)
newz=zz.reshape(1,-1)
newx=newx.flatten()
newy=newy.flatten()
newz=newz.flatten()
#newx=np.arange(10)
#newy=np.arange(10)
newcord=np.concatenate(newx,newy)

#xx = np.arange(-5, 5, 0.1)
#y = np.arange(-5, 5, 0.1)
#xx, yy = np.meshgrid(x, y, sparse=True)
#z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
#h = plt.contourf(x,y,z)  


#a=np.random.rand(1,100)

NQx = np.linspace(0,1,2)
NQy = np.linspace(0,1,3)
NQz = np.linspace(0,1,4)
xx, yy, zz=np.meshgrid(NQx, NQy, NQz, indexing='xy')