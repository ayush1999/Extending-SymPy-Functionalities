try:
    from sympy.vector import *
    from sympy import *
except ImportError:
    print ("Module not found: Sympy now depends on mpmath as an external library.")
from math import *

def distance(arg1, arg2):
    if isinstance(arg1, Point2D) and isinstance(arg2, Point2D):
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2)

    if isinstance(arg1, Point3D) and isinstance(arg2, Point3D):
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2 + (arg1[2]-arg2[2])**2 )

    if (isinstance(arg1, Line2D) and isinstance(arg2, Point2D)) or (isinstance(arg1, Point2D) and isinstance(arg2, Line2D)):
        