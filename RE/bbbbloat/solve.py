import struct

data = [
    0x4c75257240343a41,
    0x3062396630664634,
    0x65623066635f3d33,
    0x4e326560623535
]

# Little-endian decode
decoded = b''.join(struct.pack('<Q', val) for val in data).rstrip(b'\x00')
print(decoded.decode('ascii', errors='ignore'))