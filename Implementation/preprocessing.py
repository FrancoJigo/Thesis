# coding: utf-8
try:
    from Hexint import Hexint
    import math
    from hexarray import Hexarray
    import sys
    import types
    from PIL import Image
    import Hexdisp
except:
    print 'Not all files are imported'

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except: 
    print 'Open GL is not installed inyou system'

