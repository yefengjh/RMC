import sys
import numpy as np
from mantid.simpleapi import *
from mantid.geometry import SpaceGroupFactory, SymmetryOperationFactory

# symOp = SymmetryOperationFactory.createSymOp("x,y,-z")

symOps = SymmetryOperationFactory.createSymOps("x,y,-z; -x,-y,-z; z,x,y")
print "Number of operations:", len(symOps)
print "Operations:"

for op in symOps:
        print op.getIdentifier()

symOp = SymmetryOperationFactory.createSymOp("x-y,x,z")

coordinates = [0.3, 0.4, 0.5]
coordinatesPrime = symOp.transformCoordinates(coordinates)

print "Transformed coordinates:", coordinatesPrime


symOps = SpaceGroupFactory.subscribedSpaceGroupSymbols(206).getSymmetryOperations()

print "Number of operations:", len(symOps)
print "Operations:"

for op in symOps:
        print op.getIdentifier()
