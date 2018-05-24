import sys
import numpy as np
from mantid.simpleapi import *
from mantid.geometry import SpaceGroupFactory, SymmetryOperationFactory

# symOp = SymmetryOperationFactory.createSymOp("x,y,-z")
#symOps = SymmetryOperationFactory.createSymOps("x,y,-z; -x,-y,-z; z,x,y")
#print "Number of operations:", len(symOps)
#print "Operations:"
#for op in symOps:
#        print op.getIdentifier()


#  three different symmetry operation expressions
#symOps='206'
#symOps='x,y,z; -y,x-y,z+1/3; -x+y,-x,z+2/3; y,x,-z; x-y,-y,-z+2/3; -x,-x+y,-z+1/3'
symOps='I a -3'

try:
    symOps = SpaceGroupFactory.subscribedSpaceGroupSymbols(int(symOps))[0]
except ValueError:
    pass
if SpaceGroupFactory.isSubscribedSymbol(symOps):
    symOps = SpaceGroupFactory.createSpaceGroup(symOps).getSymmetryOperations()
else:
    symOps = SymmetryOperationFactory.createSymOps(symOps)

#print "Number of operations:", len(symOps)
#print "Operations:"
#for op in symOps:
#    print op.getIdentifier()

totcoordinate=[]
coordinates = [0, 0, 0]
for op in symOps:
    coordinatesPrime = op.transformCoordinates(coordinates)
    print('{:<20s},{:10s}').format(op.getIdentifier(),coordinatesPrime)
    if coordinatesPrime not in totcoordinate:
        totcoordinate.append(coordinatesPrime)
        
unique_coordinate=np.unique(totcoordinate,axis=0)
print unique_coordinate

