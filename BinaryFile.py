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
       
        if fileName != None:
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
    def __getBytes( self, data, length = 1, bigEndian = -1 ):
        result = []
       
        for i in range(0,length):
            result.append( (data>>i*8)&255 )
       
        if bigEndian == -1:
            bigEndian = self.bigEndian
        
        if bigEndian:
            result.reverse()
           
        return result
        
    ## Takes a string and returns an integer values.
    #  Each character represents 8 bits of the integer.
    #  The byte order is controlled by the bigEndian attribute.
    #
    #  @param   data    A string returned by file.read.
    #
    def __getInt(self, data, bigEndian = -1):
        length = len(data)
   
        if bigEndian == -1:
            bigEndian = self.bigEndian
        
        result = 0
        for i in range(0,length):
            if bigEndian:
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
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for writeign multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def writeInt16(self, data, bigEndian = -1):
        bytes = self.__getBytes(data,2,bigEndian)
        self.__writeBytes(bytes)
        
    ## Writes a 24 bit integer at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for writeign multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def writeInt24(self, data, bigEndian = -1):
        bytes = self.__getBytes(data,3,bigEndian)
        self.__writeBytes(bytes)
        
    ## Writes a 32 bit integer at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for writeign multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def writeInt32(self, data, bigEndian = -1):
        bytes = self.__getBytes(data,4,bigEndian)
        self.__writeBytes(bytes)
        
    ## Writes a 64 bit integer at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for writeign multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def writeInt64(self, data, bigEndian = -1):
        bytes = self.__getBytes(data,8,bigEndian)
        self.__writeBytes(bytes)
        
    ## Writes a char at the current position.
    #  
    def writeChar(self, data):
        self.file.write(data)
        
    ## Reads a 8 bit integer value at the current position.
    #  
    def readInt8(self):
        data = self.file.read(1)
        return self.__getInt(data)
        
    ## Reads a 16 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def readInt16(self, bigEndian = -1):
        data = self.file.read(2)
        return self.__getInt(data,bigEndian)
        
    ## Reads a 24 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def readInt24(self, bigEndian = -1):
        data = self.file.read(3)
        return self.__getInt(data,bigEndian)
        
    ## Reads a 32 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def readInt32(self, bigEndian = -1):
        data = self.file.read(4)
        return self.__getInt(data,bigEndian)
        
    ## Reads a 64 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def readInt64(self, bigEndian = -1):
        data = self.file.read(8)
        return self.__getInt(data,bigEndian)
      
    ## Reads a char value at the current position.
    #  
    def readChar(self):
        return self.file.read(1)
        
    ## Peeks a 8 bit integer value at the current position.
    #  
    def peekInt8(self):
        pos = self.tell()
        result = self.readInt8()
        self.seek(pos)
        return result
        
    ## Peeks a 16 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def peekInt16(self, bigEndian = -1):
        pos = self.tell()
        result = self.readInt16(bigEndian)
        self.seek(pos)
        return result
        
    ## Peeks a 24 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def peekInt24(self, bigEndian = -1):
        pos = self.tell()
        result = self.readInt24(bigEndian)
        self.seek(pos)
        return result
        
    ## Peeks a 32 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def peekInt32(self, bigEndian = -1):
        pos = self.tell()
        result = self.readInt32(bigEndian)
        self.seek(pos)
        return result
        
    ## Peeks a 64 bit integer value at the current position.
    #  
    #  @param   bigEndian   Controls what byteOrder to use
    #                       for reading multi byte integer
    #                       default: -1 => uses the settings from
    #                                      bigEndian class setting
    #
    def peekInt64(self, bigEndian = -1):
        pos = self.tell()
        result = self.readInt64(bigEndian)
        self.seek(pos)
        return result
        
    ## Peeks a charactor value at the current position.
    #  
    def peekChar(self):
        pos = self.tell()
        result = self.readChar()
        self.seek(pos)
        return result