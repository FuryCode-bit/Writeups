def extract_bits(byte_array):
    """Extract individual bits from each byte (MSB to LSB)."""
    bits = []
    for byte in byte_array:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits

def build_password_from_bits(bits):
    """Pack the given bits into a 27-byte password as expected by the check function."""
    password = [0] * 27
    bit_index = 0
    bit_offset = 1  # starts at 1 per logic

    for _ in range(184):  # 23 bytes * 8 bits
        byte_idx = bit_index // 8
        if bit_offset == 8:
            bit_offset = 0
            bit_index += 1
            byte_idx = bit_index // 8

        if byte_idx >= 27:
            break

        if bits[_]:  # if the bit from list_char is 1
            password[byte_idx] |= 1 << (7 - bit_offset)

        bit_offset += 1

    return bytes(password)

# Original list_char values
list_char = bytearray([
    0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 
    0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
    0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4
])

# Step 1: Extract bits from list_char (184 bits)
bits = extract_bits(list_char)

# Step 2: Build the valid password
password = build_password_from_bits(bits)

# Show result
print("Recovered password (bytes):", password)
print("Recovered password (ascii):", ''.join(chr(c) if 32 <= c <= 126 else '.' for c in password))
