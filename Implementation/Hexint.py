# coding: utf-8
import math
class Hexint:
    # class constructor , provides conversion from a
    # normal integer if required
    def __init__( self , value =0, base7=True ):
        # error is less than zero
        if value <0:
            raise 'BadHexintError_must_be_greater_than_or_equal_to_0'
        if base7 == True:
            # any non 0-6 digit will raise error
            temp = '%d'%value
            for i in range(len(temp)):
                if int(temp[i]) >6:
                    raise 'BadHexintError_cant_have_digit_greater_than_6'
            self.numval = value
        else:
            temp = 0
            mul = 1
            while value >0:
                temp += (value %7)*mul
                
                value /= 7
                
                mul *= 10
            self.numval = temp
        self.numstr = '%d'%self.numval
        self.ndigits = len( self.numstr )
        
    # convert to a string for displaying result
    def __str__( self ):
        return '('+self.numstr+')'
    __repr__ = __str__
    # comparison ==
    def __eq__( self , object ):
        if isinstance(object ,Hexint):
            return self.numval == object.numval
        else:
            return False
    # Hexint addition
    def __add__( self , object ):
        # lookup table
        A = [ [ 0, 1, 2, 3, 4, 5, 6 ] ,
              [ 1,63,15, 2, 0, 6,64 ] ,
              [ 2,15,14,26, 3, 0, 1 ] ,
              [ 3, 2,26,25,31, 4, 0 ] ,
              [ 4, 0, 3,31,36,42, 5 ] ,
              [ 5, 6, 0, 4 ,42 ,41 ,53 ] ,
              [ 6,64, 1, 0, 5,53,52 ] ]
    # pad out with zeros to make strs same length
        slen = self.ndigits-object.ndigits
        if slen >0:
            numa = '0'+self.numstr
            numb = '0'+('0'*slen)+object.numstr
        else:
            numa = '0'+('0'*(-slen))+self.numstr
            numb = '0'+object.numstr
        maxlen = len(numa)
        total = 0
        mul = 1
        for i in range(maxlen):
            ii = maxlen -i-1
            t = A[ int(numa[ii]) ][ int(numb[ii]) ]
            total += (t%10)*mul
            carry = t/10
            for j in range(i+1,maxlen):
                jj = maxlen-j-1
                if carry >0:
                    t = A[int(numa[jj])][carry]
                    numa = numa [:jj]+str(t%10)+numa[jj +1:]
                    carry = t/10

            mul *=10
        return Hexint( total )
       
    # Hexint multiplication works for another Hexint
    # or a scalar
    def __mul__( self , object ):
        if isinstance(object ,Hexint):
            # lookup table
            M = [ [ 0,0,0,0,0,0,0 ] ,
                  [ 0,1,2,3,4,5,6 ] ,
                  [ 0,2,3,4,5,6,1 ] ,
                  [ 0,3,4,5,6,1,2 ] ,
                  [ 0,4,5,6,1,2,3 ] ,
                  [ 0,5,6,1,2,3,4 ] ,
                  [ 0,6,1,2,3,4,5 ] ]
                # pad out with zeros to make strs
                # same length
            slen = self.ndigits-object.ndigits
            if slen >0:
                numa = '0'+self.numstr
                numb = '0'+('0'*s.len)+object.numstr
            else:
                numa = '0'+('0'*(-slen))+self.numstr
                numb = '0'+object.numstr
            maxlen = len(numa)
            powers = [10**i for i in range(maxlen)]
            sum = Hexint( 0 )
            for i in range(maxlen):
                ii = maxlen -i-1
                partial = long(0)
                mul = powers[i]
                for j in range(maxlen):
                    jj = maxlen -j-1
                    if numa[ii ]!=0:
                        partial += M[ int(numa[ii]) ][ int(numb[jj]) ]*mul
                    mul *= 10
                sum += Hexint(partial)
            return sum
        # scalar multiplication
        elif isinstance(object ,int):
            if object >0:
                num = Hexint(self.numval)
            else:
                num = -Hexint(self.numval)
            total = Hexint (0)
            for i in range(abs(object)):
                total += num
            return total
    __rmul__ = __mul__
    # negate a Hexint
    def __neg__( self ):
        total = 0
        mul = 1
        for i in range(self.ndigits -1,-1,-1):
            if self.numstr[i]=='1':
                total += (4* mul)
            elif self.numstr[i]=='2':
                total += (5* mul)
            elif self.numstr[i]=='3':
                total += (6* mul)
            elif self.numstr[i]=='4':
                total += (1* mul)
            elif self.numstr[i]=='5':
                total += (2* mul)
            elif self.numstr[i]=='6':
                total += (3* mul)
            mul *= 10
        return Hexint( total )
    # Hexint subtraction
    def __sub__( self , object ):
        return self + (-object)
    # get the digit of the Hexint at position pos
    def __getitem__( self , pos ):
        if pos >= self.ndigits:
            raise 'HexIndexError_not_that_many_layers'
        else:
            return int( self.numstr[self.ndigits -pos-1] )
    # get a Hexint that is some part of the original
    def __getslice__( self , low ,high ):
        return Hexint( int(self.numstr[low:high ]) )
    # number of digits in the Hexint
    def __len__( self ):
        return self.ndigits
    # return spatial integer coord pair
    def getSpatial( self ):
        xi ,yi ,zi = self.getHer( )
        # return result
        return ( (xi + yi - 2*zi)/3, (-xi + 2*yi - zi)/3 )
    # return fequency integer coord pair
    def getFrequency( self ):
        xi ,yi ,zi = self.getHer( )
        # return result
        return ( (-xi + 2*yi - zi)/3, (2*xi - yi - zi)/3 )
    # return integer coord of skewed 60 degree axis
    def getSkew( self ):
        xi ,yi ,zi = self.getHer( )
        # return result
        return ( (2*xi -yi -zi)/3, (-xi+2*yi -zi)/3 )
    # return polar coords for a hexint
    def getPolar( self ):
        if self.numval ==0:
            return (0,0)
        (x,y) = self.getReal( )
        r = math.sqrt(x*x+y*y)
        t = math.atan2(y,x)
        return (r,t)
    # return cartesian coords of hexint
    def getReal( self ):
        xc ,yc = 1.0 ,0.0
        x,y = 0.0 ,0.0
        sqrt3 = math.sqrt (3)
        for i in range(self.ndigits -1,-1,-1):
            if i<self.ndigits -1: # compute key points
                xc ,yc = 2*xc - sqrt3*yc , sqrt3*xc + 2*yc
            # compute rotation
            if self.numstr[i]=='1':
                x += xc
                y += yc
            elif self.numstr[i]=='2':
                x += (xc/2) - (sqrt3*yc/2)
                y += (sqrt3*xc/2) + (yc/2)
            elif self.numstr[i]=='3':
                x += -(xc/2) - (sqrt3*yc/2)
                y += (sqrt3*xc/2) - (yc/2)
            elif self.numstr[i]=='4':
                x -= xc
                y -= yc
            elif self.numstr[i]=='5':
                x += -(xc/2) + (sqrt3*yc/2)
                y += -(sqrt3*xc/2) - (yc/2)
            elif self.numstr[i]=='6':
                x += (xc/2) + (sqrt3*yc/2)
                y += -(sqrt3*xc/2) + (yc/2)
        return (x,y)
    # returns a 3-tuple using Her’s coord system
    def getHer( self ):
        xc,yc,zc = 1,0,-1
        x,y,z = 0,0,0
        for i in range(self.ndigits -1,-1,-1):
            if i<self.ndigits -1: # compute key points
                xc ,yc ,zc = (4* xc - 5*yc + zc)/3, (xc+ 4*yc - 5*zc)/3,(-5*xc + yc + 4*zc)/3
            # compute the rotation
            if self.numstr[i]=='1':
                x += xc
                y += yc
                z += zc
            elif self.numstr[i]=='2':
                x -= yc
                y -= zc
                z -= xc
            elif self.numstr[i]=='3':
                x += zc
                y += xc
                z += yc
            elif self.numstr[i]=='4':
                x -= xc
                y -= yc
                z -= zc
            elif self.numstr[i]=='5':
                x += yc
                y += zc
                z += xc
            elif self.numstr[i]=='6':
                x -= zc
                y -= xc
                z -= yc
    # return result
        return (x,y,z)
    # returns a base 10 integer corresponding
    # to a Hexint
    def getInt( self ):
        total = 0
        mul = 1
        for i in range(self.ndigits -1,-1,-1):
            total += int(self.numstr[i])*mul
            mul *= 7
        return total
    # find the nearest Hexint to Cartesian coords
    def getNearest( self , x,y ):
        sqrt3 = math.sqrt (3)
        o1 = Hexint (1)
        o2 = Hexint (2)
        h = Hexint (0)
        r1 = x -y/sqrt3
        r2 = 2*y/sqrt3
        if r1 <0:
            o1 = Hexint (4)
            if r1+math.floor(r1) >0.5:
                h += o1
        elif r1 -math.floor(r1) >0.5:
            h += o1
        if r2 <0:
            o2 = Hexint (5)
            if r2+math.floor(r2) >0.5:
                h += o2
        elif r2 -math.floor(r2) >0.5:
            h += o2
        h += abs(int(r1))*o1
        h += abs(int(r2))*o2
        return h