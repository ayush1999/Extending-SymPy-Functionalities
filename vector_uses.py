try:
    from sympy.vector import *
    from sympy import *
    from sympy.geometry import *
except ImportError:
    print ("Module not found: Sympy now depends on mpmath as an external library.")
from math import *

def distance(arg1, arg2):
    if isinstance(arg1, Point2D) and isinstance(arg2, Point2D):                                                            # Two Points (2-D)
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2)

    if isinstance(arg1, Point3D) and isinstance(arg2, Point3D):                                                             # Two Points(3-D)
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2 + (arg1[2]-arg2[2])**2 )

    if (isinstance(arg1, Line2D) and isinstance(arg2, Point2D)) or (isinstance(arg1, Point2D) and isinstance(arg2, Line2D)): # A Line and a Point(2-D)
        if  isinstance(arg1, Line2D):
            temp, arg1, arg2=arg1, arg2, temp

        # Now, arg1 is the point and arg2 is the Linear Entity

        return arg2.perpendicular_segment(arg1).length
    if (isinstance(arg1, Line3D) and isinstance(arg2, Point3D)) or (isinstance(arg1, Point3D) and isinstance(arg2, Line3D)):  # A Line and a point(3-D)
        if  isinstance(arg1, Line3D):
            temp, arg1, arg2=arg1, arg2, temp

        # Now, arg1 is the point and arg2 is the Linear Entity

        return arg2.perpendicular_segment(arg1).length
    if isinstance(arg1, Point2D) and isinstance(arg2, Point2D):
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2)

    if isinstance(arg1, Point3D) and isinstance(arg2, Point3D):
        return sqrt((arg1[0]-arg2[0])**2 + (arg1[1]-arg2[1])**2 + (arg1[2]-arg2[2])**2 )

    if (isinstance(arg1, Line2D) and isinstance(arg2, Point2D)) or (isinstance(arg1, Point2D) and isinstance(arg2, Line2D)):
        

