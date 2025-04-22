
# Challenge: shinyclean_budget — DawgCTF 2025

## Reverse Engineering: Rebuilding Flag with XOR

### Description

We were provided a piece of assembly code where multiple `MOV` instructions directly store hardcoded values into memory.

Each instruction was of the form:

```
MOV byte ptr [RSP + offset], value
```

This pattern suggested that the program was building a flag in memory byte-by-byte.

However, the flag was not immediately readable because non-printable characters were mixed in and a decryption step (XOR 0x3F) was needed based on previous analysis.

### Solution

#### 🧠 Step-by-step:

- Reconstructed the memory by tracking the MOV operations.

```bash
| Offset  | Hex | ASCII |
|:--------|:----|:------|
| flag[0] | 0x7b | { |
| flag[1] | 0x5e | ^ |
| flag[2] | 0x48 | H |
| flag[3] | 0x58 | X |
| flag[4] | 0x7c | ` |
| flag[5] | 0x6b | k |
| flag[6] | 0x79 | y |
| flag[7] | 0x44 | D |
| flag[8] | 0x79 | y |
| flag[9] | 0x6d | m |
| flag[10] | 0x0c | (non-printable) |
| flag[11] | 0x0c | (non-printable) |
| flag[12] | 0x60 | ` |
| flag[13] | 0x7c | ` |
| flag[14] | 0x0b | (non-printable) |
| flag[15] | 0x6d | m |

Then the next local bytes:

| Offset  | Hex | ASCII |
|:--------|:----|:------|
| local_b7 | 0x60 | ` |
| local_b6 | 0x68 | h |
| local_b5 | 0x0b | (non-printable) |
| local_b4 | 0x0a | (non-printable) |
| local_b3 | 0x77 | w |
| local_b2 | 0x1e | (non-printable) |
| local_b1 | 0x42 | B |
| local_b0 | 0x00 | NULL terminator |
```
---

#### 📈 Important:

- The string contained multiple non-printable characters.
- XOR 0x3F operation was needed for decryption.

---

#### 🚀 After applying XOR 0x3F byte-by-byte:
```bash
| Original | XORed | ASCII |
|:---------|:------|:------|
| 0x7b | 0x44 | D |
| 0x5e | 0x61 | a |
| 0x48 | 0x77 | w |
| 0x58 | 0x67 | g |
| 0x7c | 0x43 | C |
| 0x6b | 0x54 | T |
| 0x79 | 0x46 | F |
| 0x44 | 0x7b | { |
| 0x79 | 0x46 | F |
| 0x6d | 0x52 | R |
| 0x0c | 0x33 | 3 |
| 0x0c | 0x33 | 3 |
| 0x60 | 0x5f | _ |
| 0x7c | 0x43 | C |
| 0x0b | 0x34 | 4 |
| 0x6d | 0x52 | R |
| 0x60 | 0x5f | _ |
| 0x68 | 0x57 | W |
| 0x0b | 0x34 | 4 |
| 0x0a | 0x35 | 5 |
| 0x77 | 0x48 | H |
| 0x1e | 0x21 | ! |
| 0x42 | 0x7d | } |
```

🎯 **Final Decoded Flag**:

```
DawgCTF{FR33_C4R_W45H!}
```