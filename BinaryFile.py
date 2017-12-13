## A Wrapper class for File to handle binary data.
#  
#  
class BinaryFile:

    ## 
    #  @param   fileName    .
    #  @param   mode        .
    #  
    #  @see     https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
    #  
    def __init__(self, fileName = None, mode = "r" ):
        self.file = None
        self.bigEndian = False
       
        if fileName <> None:
            self.open( fileName, mode )
            
    ## 
    #  @param   fileName    .
    #  @param   mode        .
    #  
    #  @see     https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
    #  
    def open(self, fileName, mode = "r" ):
        self.file = open( fileName, mode )
        
    ## Closes the file.
    #  
    #  @see     https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
    #
    def close(self):
        self.file.close()

    ## Returns the current file position.
    #  
    #  @return  The current file position.
    #  
    #  @see     https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
    #
    def tell(self):
        return self.file.tell()
        
    ## Sets the current file position.
    #
    #  @param   offset  .
    #  @param   _from   .
    #  
    #  @see     https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
    #
    def seek(self, offset, _from = 0):
        return self.file.seek(offset, _from)
        
    ## Takes an integer values and returns its bits in 8 bits blocks
    #  as a list with characters.
    #
    #  @param   data    Integer to be converted to a list of characters
    #  @param   length  The size of the returned list.
    #  
    def __getBytes( self, data, length = 1 ):
        result = []
       
        for i in range(0,length):
            result.append( (data>>i*8)&255 )
       
        if self.bigEndian:
            result.reverse()
           
        return result
        
    ## Takes a string and returns an integer values.
    #  Each character represents 8 bits of the integer.
    #  The byte order is controlled by the bigEndian attribute.
    #
    #  @param   data    A string returned by file.read.
    #
    def __getInt(self, data):
        length = len(data)
   
        result = 0
        for i in range(0,length):
            if self.bigEndian:
                result = result << i*8 | ord(data[i])
            else:
                result = ord(data[i]) << i*8 | result
               
        return result
        
    ## Writes all bytes into the file.
    #  
    #   @param  bytes   A list with byte(0-255) values
    #
    def __writeBytes(self, bytes):
        for i in bytes:
            self.file.write( chr(i) )
            
    ## Writes a 8 bit integer at the current position.
    #  
    def writeInt8(self, data):
        bytes = self.__getBytes(data,1)
        self.__writeBytes(bytes)
        
    ## Writes a 16 bit integer at the current position.
    #  
    def writeInt16(self, data):
        bytes = self.__getBytes(data,2)
        self.__writeBytes(bytes)
        
    ## Writes a 24 bit integer at the current position.
    #  
    def writeInt24(self, data):
        bytes = self.__getBytes(data,3)
        self.__writeBytes(bytes)
        
    ## Writes a 32 bit integer at the current position.
    #  
    def writeInt32(self, data):
        bytes = self.__getBytes(data,4)
        self.__writeBytes(bytes)
        
    ## Writes a 64 bit integer at the current position.
    #  
    def writeInt64(self, data):
        bytes = self.__getBytes(data,8)
        self.__writeBytes(bytes)
        
    ## Reads a 8 bit integer value at the current position.
    #  
    def readInt8(self):
        data = self.file.read(1)
        return self.__getInt(data)
        
    ## Reads a 16 bit integer value at the current position.
    #  
    def readInt16(self):
        data = self.file.read(2)
        return self.__getInt(data)
        
    ## Reads a 24 bit integer value at the current position.
    #  
    def readInt24(self):
        data = self.file.read(3)
        return self.__getInt(data)
        
    ## Reads a 32 bit integer value at the current position.
    #  
    def readInt32(self):
        data = self.file.read(4)
        return self.__getInt(data)
        
    ## Reads a 64 bit integer value at the current position.
    #  
    def readInt64(self):
        data = self.file.read(8)
        return self.__getInt(data)
        
    ## Peeks a 8 bit integer value at the current position.
    #  
    def peekInt8(self):
        pos = self.tell()
        result = self.readInt8()
        self.seek(pos)
        return result
        
    ## Peeks a 16 bit integer value at the current position.
    #  
    def peekInt16(self):
        pos = self.tell()
        result = self.readInt16()
        self.seek(pos)
        return result
        
    ## Peeks a 24 bit integer value at the current position.
    #  
    def peekInt24(self):
        pos = self.tell()
        result = self.readInt24()
        self.seek(pos)
        return result
        
    ## Peeks a 32 bit integer value at the current position.
    #  
    def peekInt32(self):
        pos = self.tell()
        result = self.readInt32()
        self.seek(pos)
        return result
        
    ## Peeks a 64 bit integer value at the current position.
    #  
    def peekInt64(self):
        pos = self.tell()
        result = self.readInt64()
        self.seek(pos)
        return result