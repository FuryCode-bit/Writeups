
# Challenge: ShinyClean™ Rust Remover: Club Edition

## Reverse Engineering:

### Description

We are given a Rust binary. By inspecting it using a decompiler and navigating to the `shinyclean2::main` function, we uncover how the input is processed.

The program uses `to_ne_bytes` in Rust, which transforms values into 4-byte arrays.  
Since flags in CTFs often start with a known pattern, we use that knowledge (`"Dawg"`) to recover the hidden key.

### Solution

🧠 Step-by-step:

- **Decompile the binary** and jump to the `shinyclean2::main` function.
- **Understand the logic**: input bytes are processed using `to_ne_bytes`, giving 4-byte outputs.
- **Recognize the format**: The first 4 bytes of the flag are known (`Dawg`).
- Using the known flag start, we can **recover the 4-byte XOR keys**.

We then use the recovered keys to decrypt the entire flag.

Here's the reconstruction script:

```python
enc = [0x0CF,0x9,0x1E,0x0B3,0x0C8,0x3C,0x2F,0x0AF,
       0x0BF,0x24,0x25,0x8B,0x0D9,0x3D,0x5C,0x0E3,
       0x0D4,0x26,0x59,0x8B,0x0C8,0x5C,0x3B,0x0F5,0x0F6]

known = b'Dawg'
keys = []

for i in range(4):
    keys.append(enc[i] ^ known[i])

for i in range(len(enc)):
    print(chr(enc[i] ^ keys[i % 4]), end='')
```

✅ Running this script successfully decrypts the flag.

---

### Final Flag

```
DawgCTF{b17_f0rg1v3n_0n3_c4n_c0nv3rg3}
```
