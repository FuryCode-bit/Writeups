
# Challenge: shinyclean_pro — DawgCTF 2025

## Reverse Engineering:

### Description

We are given a Rust binary `shinyclean_pro` that asks the user for a "challenge phrase". If correct, it prints a success message; otherwise, it says "Loser! Try again?"

At first, it appears like a black-box guessing game. However, using reverse engineering, we are expected to recover the correct input without guessing blindly.

Using Ghidra and basic static analysis, we determined that:

- The binary uses a **stateful transformation**.
- It employs a **lookup table** to transform each input byte.
- The transformed bytes are compared against a hardcoded array.

### Solution

#### 🧠 Step-by-step:

1. **Finding the Main Logic**:

    Using `nm -C shinyclean_pro | grep main`, we found the Rust main function.

2. **Identifying the Transformation**:

    Decompiling with Ghidra revealed that:

    ```rust
    state = 0x75;
    for each input_byte:
        index = (state + input_byte) % 256;
        output = table[index];
        state += input_byte;
    ```
    The state changes after each input byte.

3. **Extracting Important Values**:

    - **Target Output** (hardcoded in binary):

    ```python
    target = [
        0xea, 0xd9, 0x31, 0x22, 0xd3, 0xe6, 0x97, 0x70,
        0x16, 0xa2, 0xa8, 0x1b, 0x61, 0xfc, 0x76, 0x68,
        0x7b, 0xab, 0xb8, 0x27, 0x96
    ]
    ```

    - **Lookup Table**:

    Extracted 256 bytes starting at memory address `0x00161298`.

4. **Building the Solver Script**:

    To find the original input, we wrote a Python script that:

    - Starts with `state = 0x75`.
    - For each target byte:
      - Tries all printable ASCII characters.
      - Selects the character that maps correctly after transformation.
      - Updates the state.

    ```python
    # target output values from acStack_a5
    target = [
        0xea, 0xd9, 0x31, 0x22, 0xd3, 0xe6, 0x97, 0x70,
        0x16, 0xa2, 0xa8, 0x1b, 0x61, 0xfc, 0x76, 0x68,
        0x7b, 0xab, 0xb8, 0x27, 0x96
    ]

    # 256-byte transformation table from Ghidra
    table = [0x9f, 0xd2, 0xd6, 0xa8, 0x99, 0x76, 0xb8, 0x75, 0xe2, 0x0e, 0x50, 0x67, 0xc9, 0x3a, ...]  # truncated for readability

    # Reconstruct original input (aka the flag)
    flag = []
    state = 0x75

    for expected in target:
        for b in range(0x20, 0x7f):  # Try printable ASCII
            if table[(state + b) % 256] == expected:
                flag.append(b)
                state = (state + b) % 256
                break
        else:
            flag.append(ord('?'))  # fallback if nothing matches

    print("Flag:", bytes(flag).decode())
    ```

5. **Result**:

    Running the script produced the final flag.

---

### Final Flag

```
DawgCTF{S0lUt10n_N0t_St4t1c}
```

---

### Key Lessons

- Rust binaries often have a complex layout, but the logic itself can be simple.
- Tracking **state** carefully is essential when reversing transformations.
- Rust channel communication (thread sending transformed bytes) can seem confusing but is readable after decompilation.
- Patience pays off more than brute-forcing in reverse engineering challenges.

**Mission complete. 🫡**
