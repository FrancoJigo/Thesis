# coding: utf-8
from Hexint import Hexint
import math

class Hexarray:
    # class constructor , creates a list which has
    # 7^{ size} elements
    def __init__( self , size ):
        self.nhexs = 7** size
        self.hexdata = [ 0 ]* self.nhexs
        self.layers = size
    # provided to print out a Hexarray in the form
    # <0,0,...0>
    def __str__( self ):
        output = '<'
        for i in self.hexdata:
            output += str(i)+ ','
        output += '>'
        return output
    __repr__ = __str__
    # return the number of elements in the hexarray
    def __len__( self ):
        return self.nhexs
    # return the value of the Hexarray at pos.
    # pos can be either a Hexint or an integer
    def __getitem__( self , pos ):
        if isinstance( pos , Hexint ):
            p = pos.getInt ()
        else:
            p = pos
        return self.hexdata[p]
    # set the value of the Hexarray at pos.
    # pos can be either a Hexint or an integer
    def __setitem__( self , pos , value ):
        if isinstance( pos , Hexint ):
            p = pos.getInt ()
        else:
            p = pos
        self.hexdata[p] = value
    # get a list of data from within a Hexarray
    # low ,high can be either a Hexint or a int
    def __getslice__( self , low ,high ):
        if isinstance( low , Hexint ) and isinstance(high ,Hexint):
            p1 ,p2 = low.getInt (), high.getInt ()
        else:
            p1 ,p2 = low ,high
        return self.hexdata[low:high]
    # assign a list of data to the Hexarray
    def __setslice__( self , low ,high , values ):
        if isinstance( low , Hexint ) and isinstance(high ,Hexint):
            p1 ,p2 = low.getInt (), high.getInt ()
        else:
            p1 ,p2 = low ,high
        self.hexdata[low:high] = values
    # return the number of layers in the HIP
    # structure
    # represented by this Hexarray
    def getLayers( self ):
        return self.layers
    # save the current Hexarray in an XML file
    # which is called filename
    def save( self , filename ):
        data = open( filename , 'w' )
        output = self.getXML( )
        data.write( output )
        data.close( )
    # generate XML that represents the Hexarray
    def getXML( self ):
        data = ''
        cmplxflag = False
        tupleflag = False
        if isinstance (self.hexdata [0],int):
            dname = 'int'
        elif isinstance(self.hexdata [0], float):
            dname = 'double'
        elif isinstance(self.hexdata [0], complex):
            dname = 'complex'
            cmplxflag = True
        elif isinstance(self.hexdata [0], tuple):
            dname = 'rgb'
            tupleflag = True
        data += '<struct >\n'
        data += '<member >\n'
        data += '<name >layers </name >\n'
        data += '<value ><int >%d</int ></value >\n'%self.layers
        data += '</member >\n'
        data += '<member >\n'
        data += '<name >datatype </name >\n'
        data += '<value ><string >%s</string ></value >\n'%dname
        data += '</member >\n'
        data += '</struct >\n'
        data += '<array >\n'
        data += '<data >\n'
        for i in self.hexdata:
            if cmplxflag == True:
                data += '<value ><%s>%d,%d</%s></value>\n'% (dname ,i.real ,i.imag ,dname)
            else:
                if tupleflag == True:
                    data += '<value ><%s>%d,%d,%d</%s></value >\n' % (dname ,i[0],i[1],i[2], dname)
                else:
                    data += '<value ><%s>%d</%s></value >\n'%(dname ,i,dname)
        data += '</data >\n'
        data += '</array >\n'
        return data
