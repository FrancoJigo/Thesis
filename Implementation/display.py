# coding: utf-8
import math
import sys
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print 'ERROR: PyOpenGL not installed properly'
    sys.exit ()
try:
    from Hexint import Hexint
    from Hexarray import Hexarray
except:
    print 'ERROR: Hex libs are not installed'
    sys.exit( )
# default rotation and scale
xrot ,yrot ,zrot = 0.0 ,0.0 ,0.0
scale = -7.5
max = -9.99 e99
scf = 1.0
# initialise the open GL context
def initGL( hdata , domain ):
    glClearColor (0.0, 1.0, 1.0, 0.0)
    glShadeModel( GL_SMOOTH )
    glPolygonMode( GL_FRONT , GL_FILL )
    glPolygonMode( GL_BACK , GL_LINE )
    glEnable( GL_DEPTH_TEST )
    # be efficient --make display list
    global hexList
    hexList = glGenLists (1)
    glNewList( hexList , GL_COMPILE )
    compute2DDisplayList( hdata ,domain )
    glEndList ()
# what to do when window is resized
def reshapeGL( w,h ):
    if w>h:
        w=h
    elif h>w:
        h=w
    glViewport( 0,0, w,h )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity( )
    glFrustum (-1.0, 1.0, -1.0, 1.0, 5.0, 10.0)
    glMatrixMode( GL_MODELVIEW )
# the display function
# uses a display list to store current
# HIP image
def displayGL ():
    global scf
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity( )
    glTranslatef( 0.0,0.0, scale )
    glScalef( scf ,scf ,scf )
    glRotatef( xrot , 1.0, 0.0, 0.0 )
    glRotatef( yrot , 0.0, 1.0, 0.0 )
    glRotatef( zrot , 0.0, 0.0, 1.0 )
    glCallList(hexList)
    glFlush ()
# keyboard controls
# escape : exit
# x/X,y/Y,z/Z : rotate about x,y,z axis
# s/S : scale the image
def keyboardGL(key , x, y):
    global xrot ,yrot ,zrot
    global scale
    # quit
    if key == chr (27):
        sys.exit (0)
    # change rotation
    if key==chr (88): # X
        xrot += 0.5
    if key==chr(120): # x
        xrot -= 0.5
    if key==chr (89): # Y
        yrot += 0.5
    if key==chr(121): # y
        yrot -= 0.5
    if key==chr (90): # Z
        zrot += 0.5
    if key==chr(122): # z
        zrot -= 0.5
    # change scale
    if key==chr (83): # S
        scale -= 0.1
    if key==chr(115): # s
        scale += 0.1
    # reset all vals
    if key==chr (82) or key==chr (114):
        scale = -10
        xrot ,yrot ,zrot = 0.0 ,0.0 ,0.0
    xrot ,yrot ,zrot = xrot %360, yrot %360, zrot %360
    if scale > -5.0: scale = -5.0
    if scale < -10.0: scale = -10.0
    displayGL( )
# find the basis for plotting
def findBasis( domain ,order):
sqrt3 = math.sqrt (3.0)
if domain: # spatial
N = [ [1.0 , -0.5] ,[0.0 , sqrt3 /2.0] ]
else: # frequency
if order ==1:
N = [ [1.0/7.0 , -2.0/7.0] ,
[5.0/(7* sqrt3), 4.0/(7* sqrt3) ] ]
elif order ==2:
N = [ [ -3.0/49.0 , -8.0/49.0] ,
[13.0/(49.0* sqrt3), 2.0/(49.0* sqrt3
)] ]
elif order ==3:
N = [ [ -19.0/343.0 , -18.0/343.0] ,
[17.0/(343.0* sqrt3), -20.0/(343.0*
sqrt3)] ]
elif order ==4:
N = [ [ -55.0/2401.0 , -16.0/2401.0] ,
[ -23.0/(2401.0* sqrt3),
-94.0/(2401.0* sqrt3)] ]
elif order ==5:
N = [ [ -87.0/16807.0 , 62.0/16807.0] ,
[ -211.0/(16807.0* sqrt3),
-236.0/(16807.0* sqrt3)] ]
elif order ==6:
N = [ [37.0/117649.0 , 360.0/117649.0] ,
[ -683.0/(117649.0* sqrt3),
-286.0/(117649.0* sqrt3)] ]
elif order ==7:
    N = [ [757.0/823543.0 , 1006/823543.0] ,
[ -1225.0/(823543* sqrt3),
508/(823543* sqrt3)] ]
else:
N = [ [ 1.0, 0.0] , [0.0, 1.0] ]
return N
# compute the coords for a single hexagon
def doHex( ox ,oy , r,o ):
glBegin( GL_POLYGON )
for i in range (7):
x = r*math.cos( i*math.pi /3.0 + math.pi /2.0 +
o )
y = r*math.sin( i*math.pi /3.0 + math.pi /2.0 +
o )
glVertex3f(ox+x,oy+y ,0.0)
glEnd( )
# compute the display list
def compute2DDisplayList( hdata ,domain ):
global max ,scf
N = findBasis( domain ,hdata.layers )
if domain: # spatial
radius = 1/ math.sqrt (3.0)
offset = 0
else: # frequency
radius = math.sqrt( N[0][1]*N[0][1] + N
[1][1]*N[1][1] )/math.sqrt (3.0)
offset = math.atan2( (N[1][0] -N[1][1]) ,(N
[0][0] -N[0][1]) )
max = -9.99 e99
for i in range( len(hdata) ):
if domain:
xa ,ya = Hexint(i,False).getSpatial ()
else:
xa ,ya = Hexint(i,False).getFrequency ()
hx = xa*N[0][0] + ya*N[0][1]
hy = xa*N[1][0] + ya*N[1][1]
if hx >max: max = hx
if hy >max: max = hy
if not isinstance( hdata[i],tuple ):
glColor3f( hdata[i]/255.0 , hdata[i
]/255.0 , hdata[i]/255.0 )
else:
    glColor3f( hdata[i][0]/255.0 , hdata[i
][1]/255.0 , hdata[i][2]/255.0 )
doHex( hx ,hy , radius , offset )
scf = 1.0/( max *(1+0.8/ hdata.layers))
# display the image
def display( hdata , domain=True , ang=0,sc= -7.5 ):
global zrot ,scale
zrot = ang
scale = sc
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB |
GLUT_DEPTH)
glutInitWindowSize (500, 500)
glutInitWindowPosition (50 ,50)
glutCreateWindow("heximagelayers =%d" % hdata.
layers )
initGL( hdata , domain )
glutReshapeFunc(reshapeGL)
glutDisplayFunc(displayGL)
glutKeyboardFunc(keyboardGL)
glutMainLoop ()

#To use the code presented here, issue the command Hexdisp.display(hipimage)
# from the Python interpreter or your code.