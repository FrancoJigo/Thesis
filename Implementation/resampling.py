import math
import sys
import types
import Image # python imaging library (PIL)
try:
from Hexint import Hexint
from Hexarray import Hexarray
import Hexdisp
except:
print ’ERROR:Hexlibsarenotinstalled ’
sys.exit( )
# different sampling techniques
BLINEAR = 1
BCUBIC = 2
# the sampling kernel
def kernel( x,y, tech ):
xabs ,yabs = abs(x), abs(y)
if tech == BLINEAR:
if xabs >=0 and xabs <1:
xf = 1-xabs
else:
xf = 0.0
if yabs >=0 and yabs <1:
yf = 1-yabs
else:
yf = 0.0
else: # BCUBIC
a = 0
if xabs >=0 and xabs <1:
xf = (a+2)*( xabs **3) - (a+3)*( xabs **2) +
1
elif xabs >=1 and xabs <2:
xf = a*( xabs **3) - 5*a*( xabs **2) + 8*a*
xabs - 4*a
else:
xf = 0.0
if yabs >=0 and yabs <1:
yf = (a+2)*( yabs **3) - (a+3)*( yabs **2) +
1
elif yabs >=1 and yabs <2:
    yf = a*( yabs **3) - 5*a*( yabs **2) + 8*a*
yabs - 4*a
else:
yf = 0.0
return xf*yf
# resample from a square image into a hip image for
# gray scale images
# order : the size of the hip image
# scale : the spacing between points in the hex
# lattice
def hipsampleGray( image , order , sc , technique ):
(w,h) = image.size
ox ,oy = w/2.0,h/2.0
scale = sc
himage = Hexarray( order )
for i in range(len(himage)):
x,y = Hexint(i,False).getReal( )
y = -y # y direction for PIL is inverted
xa ,ya = ox+scale*x, oy+scale*y
out = 0.0
for m in range( int(round(xa -3)),int(round(xa
+4)) ):
for n in range( int(round(ya -3)),int(
round(ya+4)) ):
if m>=0 and m<w and n>=0 and n<h:
pixel = image.getpixel( (m,n) )
out += pixel*kernel(xa -m,ya -n,
technique)
himage[i] = round(out)
return himage
# resample from a square image into a hip image for
# colour images
# order : the size of the hip image
# scale : the spacing between points in the hex
# lattice
def hipsampleColour ( image , order , sc , technique ):
(w,h) = image.size
ox ,oy = w/2.0,h/2.0
himage = Hexarray( order )
for i in range(len(himage)):
x,y = Hexint(i,False).getReal( )
y = -y # y direction for PIL is inverted
xa,ya = ox+sc*x, oy+sc*y
out = [0.0 ,0.0 ,0.0]
for m in range( int(round(xa -3)),int(round(xa
+4)) ):
for n in range( int(round(ya -3)),int(
round(ya+4)) ):
if m>=0 and m<w and n>=0 and n<h:
pixel = image.getpixel( (m,n) )
out [0] += pixel [0]* kernel(xa -m,ya
-n,technique)
out [1] += pixel [1]* kernel(xa -m,ya
-n,technique)
out [2] += pixel [2]* kernel(xa -m,ya
-n,technique)
himage[i] = ( out[0],out[1],out [2] )
return himage
# resample from a hip image to a square image
# this version is for grayscale images
# rge : radius to resample from
# sc : the spacing between points in the hex lattice
def sqsampleGray( himage , rge ,sc , technique ):
# find size of image
mh = Hexint(len(himage) -1,False)
xvs = [Hexint(i,False).getReal ()[0] for i in
range(len(himage))]
yvs = [Hexint(i,False).getReal ()[1] for i in
range(len(himage))]
mxx ,mnx = round(max(xvs)),round(min(xvs))
mxy ,mny = round(max(yvs)),round(min(yvs))
rx = int( round ((mxx -mnx)/sc) )+1
ry = int( round ((mxy -mny)/sc) )+1
# create a square image of the right size
image = Image.new( ’L’,(rx ,ry) )
# offset table
sizes = [ Hexint (7**o-1,False) for o in range (8)
]
order = [ o for o in range(len(sizes)) if sizes[o
]. getPolar ()[0]>rge ]
offsets = [ Hexint(h,False) for h in range (7**
order [0]) if Hexint(h,False).getPolar ()[0]<=
rge ]
for i in range(ry):
for j in range(rx): # for the points in the
image
xa ,ya = mnx+j*sc , mny+i*sc
# find hex lattice points near the point
(xa ,ya)
list = []
hn = Hexint ().getNearest(xa ,ya)
for h in offsets:
hi = hn + h
(x,y) = hi.getReal ()
if abs(x-xa) <=1 and abs(y-ya) <=1:
list.append( hi )
# compute the colour of the square pixel
out = 0.0
for h in list:
if h.getInt () <=mh.getInt ():
(x,y) = h.getReal ()
pixel = himage[h]
out += pixel*kernel(xa -x,ya -y,
technique)
image.putpixel ((j,ry -i-1),int(
round(out)) )
return image
# resample from a hip image to a square image.
# this version is for colour images
# rge : radius to resample from
# sc : the spacing between points in the hex lattice
def sqsampleColour( himage , rge ,sc , technique ):
# find size of image
mh = Hexint(len(himage) -1,False)
xvs = [Hexint(i,False).getReal ()[0] for i in
range(len(himage))]
yvs = [Hexint(i,False).getReal ()[1] for i in
range(len(himage))]
mxx ,mnx = round(max(xvs)),round(min(xvs))
mxy ,mny = round(max(yvs)),round(min(yvs))
rx = int( round ((mxx -mnx)/sc) )+1
ry = int( round ((mxy -mny)/sc) )+1
# create a square image
image = Image.new( ’RGB’,(rx ,ry) )
# offset table
sizes = [ Hexint (7**o-1,False) for o in range (8)
]
order = [ o for o in range(len(sizes)) if sizes[o
]. getPolar ()[0]>rge ]
offsets = [ Hexint(h,False) for h in range (7**
order [0]) if Hexint(h,False).getPolar ()[0]<=
rge ]
for i in range(ry):
for j in range(rx): # for the points in the
image
xa ,ya = mnx+j*sc , mny+i*sc
# find hex lattice points near the point
(xa ,ya)
list = []
hn = Hexint ().getNearest(xa ,ya)
for h in offsets:
hi = hn + h
(x,y) = hi.getReal ()
if abs(x-xa) <=1 and abs(y-ya) <=1:
list.append( hi )
# compute the colour of the square pixel
out = [0.0 ,0.0 ,0.0]
for h in list:
if h.getInt () <=mh.getInt ():
(x,y) = h.getReal ()
pixel = himage[h]
out [0] += pixel [0]* kernel(xa -x,ya
-y,technique)
out [1] += pixel [1]* kernel(xa -x,ya
-y,technique)
out [2] += pixel [2]* kernel(xa -x,ya
-y,technique)
image.putpixel ((j,ry -i-1),
(int(round(out [0])
),
int(round(out [1]))
,
int(round(out [2]))
) )
return image
# perform sampling from a square sampled image to a
# HIP image
# image : a valid PIL image
# order : how many layers in the HIP image
# sc : spacing between points in the hex lattice
# technique : which kernel to use
def hipsample( image , order =5, sc=1.0, technique=
BLINEAR ):
if image.mode ==’L’:
    return hipsampleGray( image , order , sc ,
technique )
elif image.mode ==’RGB’:
return hipsampleColour( image , order , sc ,
technique )
else:
raise Exception(’hexsample:donotsupport
thiscolourmodel ’)
# perform sampling from a HIP image to a
# square image
# image : a valid PIL image
# rad : range on which to perform interpolation
# sc : spacing between points in the hex lattice
# technique : which kernel to use
def sqsample( himage , rad =1.0, sc=1.0, technique=
BLINEAR):
if type(himage [0]) == types.FloatType or type(
himage [0]) == types.IntType:
return sqsampleGray( himage , rad ,sc ,
technique )
elif type(himage [0]) == types.TupleType or type(
himage [0]) == types.ListType:
return sqsampleColour( himage , rad ,sc ,
technique )
else:
raise Exception(’squaresample:donot
suportthiscolourmodel ’)