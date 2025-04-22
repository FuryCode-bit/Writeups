# Challenge: Architecture Astronaut

## Reverse Engineering: Guess Architecture

### Description

We recovered this executable from a device, but we can't figure out how to make the program run. We suspect the code was compiled for a system with a different CPU architecture.

Can you figure out which architecture it was compiled for? The flag is the name of the architecture. You don't need to run or take apart the executable.

The flag is not in MetaCTF{} format, it's just the name of the architecture. You only have 10 attempts on this challenge.
This challenge is from the April 2024 Flash CTF. It was first solved 18 seconds into the competition by asinghani. 72.3% of active users solved it during the competition.

### Solution

This was straightforward enough; inquiring what the file type was:

❯ file astronaut
astronaut: ELF 32-bit LSB executable, Tensilica Xtensa, version 1 (SYSV), statically linked, with debug_info, not stripped

…and the flag is xtensa.