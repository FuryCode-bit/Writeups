import struct

# The three constants (from the disassembled code)
c1 = 0x617b2375f81ea7e1
c2 = 0xd269df5b5afc9db9
c3 = 0xf467edf4ed1bfed2

# Pack each constant in little‑endian format (each 8 bytes)
c1_bytes = struct.pack("<Q", c1) # 8 bytes: bytes 0–7
c2_bytes = struct.pack("<Q", c2) # 8 bytes: but only first 7 will be used from here
c3_bytes = struct.pack("<Q", c3) # 8 bytes; stored starting at byte 15

# Construct the secret buffer according to the overlapping layout:
# • Bytes 0–7: c1_bytes (8 bytes)
# • Bytes 8–14: first 7 bytes of c2_bytes
# • Bytes 15–22: c3_bytes (8 bytes)
# • Bytes 23–26: 4 bytes of 0x00 (not explicitly set in the binary)

secret = c1_bytes + c2_bytes[:7] + c3_bytes + b'\x00'*4
assert len(secret) == 27

# Convert the 27-byte secret into a bitstring
bits = "".join(f"{byte:08b}" for byte in secret)

# Only use the first 189 bits (27×7)
bits = bits[:189]

# Reconstruct the 27-byte password by splitting into 27 groups of 7 bits
password = ""
for i in range(27):
 chunk = bits[i*7:(i+1)*7]
 char_val = int(chunk, 2)
 password += chr(char_val)

# Use repr() to show any non-printable characters (like the final null byte)
print(repr(password))