# BinaryFile
A Python class for easy binary data handling.


```python
from BinaryFile import BinaryFile


f = BinaryFile( )

f.open( "temp.dat", "wb+" )

f.bigEndian = False

f.writeInt16( 60665 )

f.seek(0)


print f.peekInt16()
print f.peekInt16()
print f.peekInt16()
print f.peekInt16()
print f.peekInt16()

 

print f.readInt8()
print f.readInt8()

 

f.close()
```
