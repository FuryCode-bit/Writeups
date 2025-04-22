
# Challenge: Perplexed PicoCTF 2025

## Reverse Engineering: Bitstream Check

### Description

We are given a binary that validates user input through a custom `check` function.  
The binary requires the password to be **exactly 27 characters** long.  
If the length is incorrect, it immediately exits with failure.

Internally, the binary loads three hardcoded 64-bit constants into memory.  
However, **due to misaligned memory writes**, the third constant (`c3`) overwrites the last byte of the second constant (`c2`), creating a non-trivial memory layout.

Additionally, the validation is performed **bit-by-bit** instead of byte-by-byte:  
- The input bits must match the bits stored in memory.
- 7 bits are used for each character, not 8.
- Hence, **27 × 7 = 189 bits** are validated.

### Solution

**Step 1: Rebuild the Secret Memory Layout**

Constants from the binary:
```c
c1 = 0x617b2375f81ea7e1;
c2 = 0xd269df5b5afc9db9;
c3 = 0xf467edf4ed1bfed2;
```

Packing and layout:
```python
import struct

c1_bytes = struct.pack("<Q", 0x617b2375f81ea7e1)
c2_bytes = struct.pack("<Q", 0xd269df5b5afc9db9)
c3_bytes = struct.pack("<Q", 0xf467edf4ed1bfed2)

# Construct the memory layout (taking misalignment into account)
secret = c1_bytes + c2_bytes[:7] + c3_bytes + b'\x00' * 4
```

**Step 2: Extract Bitstream and Decode Flag**

Since only 189 bits are validated, and each character uses 7 bits:
```python
bits = "".join(f"{byte:08b}" for byte in secret)[:189]

password = ""
for i in range(27):
    chunk = bits[i*7:(i+1)*7]
    char_val = int(chunk, 2)
    password += chr(char_val)

print(password)
```

### Final Flag
```
picoCTF{0n3_bi7_4t_a_7im3}
```
