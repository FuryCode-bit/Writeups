from pwn import *

elf = ELF("esp_ota_client.elf")

ADDR_SHARED_STRING      = 0x40811f5c
ADDR_PREFIX_PART        = 0x42063774  # 5 bytes: 'd', 'a', 'm', '{', 'F'
ADDR_MIDDLE_FLAG        = 0x4206377c  # 9 bytes: '_on_the_'
ADDR_SUFFIX_FLAG        = 0x42063788  # 8 bytes: 'esp32c6X'



# Step 1: Get sharedString
shared_bytes = elf.read(ADDR_SHARED_STRING, 17) # Extracts 17 flag bytes. To get the string decode manually from hex in Ghidra.
shared_string = shared_bytes.decode('ascii', errors='ignore')

# Step 2: Get prefix (5 bytes: "d", "a", "m", "{", and DAT_42063778)
prefix_bytes = elf.read(ADDR_PREFIX_PART, 5)
prefix_str = prefix_bytes.decode("ascii", errors="ignore")

# Step 3: Get middle flag part (9 bytes total) 
middle_bytes = elf.read(ADDR_MIDDLE_FLAG, 9)
middle_str = middle_bytes.decode("ascii", errors="ignore")

# Step 4: Get final part (8 bytes: "esp32c6X")
tail_bytes = elf.read(ADDR_SUFFIX_FLAG, 8)
tail_str = tail_bytes.decode("ascii", errors="ignore")

# Step 5: Assemble final flag
flag = f"{prefix_str}{shared_string}{middle_str}{tail_str}"

print("[+] Final Reconstructed Flag:\n", flag)
