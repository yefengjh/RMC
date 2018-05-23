import sys
import numpy as np
from mantid.simpleapi import *
from mantid.geometry import SpaceGroupFactory, SymmetryOperationFactory

symOp = SymmetryOperationFactory.createSymOp("x,y,-z")

symOps = SymmetryOperationFactory.createSymOps("x,y,-z; -x,-y,-z; z,x,y")