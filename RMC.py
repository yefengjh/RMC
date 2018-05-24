# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#NQx = np.linspace(-5,5,5)
#NQy = np.linspace(-4,4,5)
#NQz = np.linspace(-3,3,5)
#xx, yy, zz=np.meshgrid(NQx, NQy, NQz, indexing='xy')
#newx=xx.reshape(1,-1)
#newy=yy.reshape(1,-1)
#newz=zz.reshape(1,-1)
#newx=newx.flatten()
#newy=newy.flatten()
#newz=newz.flatten()
#newx=np.arange(10)
#newy=np.arange(10)
#newcord=np.concatenate(newx,newy)

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

def aredat():
    return np.add.reduceat(c, np.arange(0, len(c), 5))

def reshp():
    np.reshape(c, (-1, 5)).sum(axis=-1)

c = np.random.random([10,10])

dos2 = np.random.random((1000, 19))
atom = np.random.random((2, 1000, 2))

ldata = [None, None, '100', '1.1']
maxind = int(ldata[2])
dos2_r = dos2[:maxind, 1:19].reshape(-1, 9, 2)  

aa = np.linspace(0,10,11)
bb = np.linspace(0,10,11)
c1, c2 = np.meshgrid(aa,bb)
#x=np.reshape(c1,(12,-1,4)).sum(axis=-1)
#c3=np.reshape(x,(-1,4,3)).sum(axis=1)

def summatrix(mat,binsize):
    import numpy as np
    dim0=np.shape(mat)[0]
    dim1=np.shape(mat)[1]
    Nx=np.int(dim0/binsize)*binsize
    Ny=np.int(dim1/binsize)*binsize
    newmat=mat[0:Nx,0:Ny]
    newmat=np.reshape(newmat,(np.shape(newmat)[0],-1,binsize)).sum(axis=-1)
    newmat=np.reshape(newmat,(-1,binsize,np.shape(newmat)[-1])).sum(axis=1)
    return newmat
