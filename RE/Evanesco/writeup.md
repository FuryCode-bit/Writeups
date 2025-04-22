# Challenge: Evanesco DawgCTF 2025

## Reverse Engineering: Encoded String

## Description

I was in my chambers brewing a new flag, but at the last moment, I spilled my invisibility potion all over it! Can you find it for me?

## Solution

Opening the provided binary in Ghidra, the `main` function quickly caught my attention. Inside, there was a call to `builtin_strncpy` that copied a strange-looking string into a local buffer:

```c
builtin_strncpy(local_a8,
   "\x000e0001\x000e0044\x000e0061\x000e0077\x000e0067\x000e0043\x000e0054\x000e0046\x000e007b"
   "\x000e0075\x000e005f\x000e0063\x000e0061\x000e006e\x000e005f\x000e0074\x000e0061\x000e0067"
   "\x000e005f\x000e0062\x000e0075\x000e0074\x000e005f\x000e0075\x000e005f\x000e0063\x000e0061"
   "\x000e006e\x000e0074\x000e005f\x000e0068\x000e0069\x000e0064\x000e0065\x000e007d\x000e007f",
0x91);
```

The encoded string appeared suspicious: every character sequence was prefixed with `\x000e`. It suggested that the real data was hidden within these sequences.

Upon further analysis, I realized that each two-byte group after `\x000e` held the meaningful information. By extracting the actual byte values and discarding the `000e` part, the data looked like this:

```
01, 44, 61, 77, 67, 43, 54, 46, 7b, 75, 5f, 63, 61, 6e, 5f, 74,
61, 67, 5f, 62, 75, 74, 5f, 75, 5f, 63, 61, 6e, 74, 5f, 68, 69,
64, 65, 7d, 7f
```

Converting these bytes to ASCII and ignoring non-printable characters (`01` and `7f`), the output revealed:

```
DawgCTF{u_can_tag_but_u_cant_hide}
```

