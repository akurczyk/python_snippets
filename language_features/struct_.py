from struct import Struct

# https://docs.python.org/2/library/struct.html

MyStruct = Struct('c?if')
packed = MyStruct.pack(b'A', True, 100, 55.55)
print(packed)
unpacked = MyStruct.unpack(packed)
print(unpacked)
