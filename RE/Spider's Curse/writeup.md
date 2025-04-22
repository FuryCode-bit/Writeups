# Challenge: Spider's Curse

## Reverse Engineering: Convert from Hex

### Description

Exploring an ancient chamber, you come across a tomb, webs strung from end to end. You brush off the webs and open the tomb, to find yourself cursed! Utter the magic word to free yourself!

Download the tomb here, if you dare.
This challenge is from the October 2024 Flash CTF. It was first solved 2.1 minutes into the competition by smithrog. 55.6% of active users solved it during the competition.

### Solution

Opening the binary in Ghidra (or any decompiler), we see the main function reads user input, converts it to hex with stringToHex, and compares it to a hardcoded hex string:

```
4d6574614354467b68337833645f3572316e67735f3472655f6e305f6d347463685f6630725f6d337d
```

Decoding this hex gives the flag:

```
MetaCTF{h3x3d_5r1ngs_4re_n0_m4tch_f0r_m3}
```