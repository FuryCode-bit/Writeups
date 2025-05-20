# Challenge: Secret (ACM&xSTF CTF 2025)

## PWN: Command Injection via Buffer Overflow

### Description

In this challenge, we interact with a binary remotely hosted at `ctf.acm.xstf.pt:32775`. The objective is to exploit the binary to retrieve the contents of `flag.txt`. The challenge appears to involve a simple buffer overflow vulnerability that leads to command injection.

---

### Solution

We begin by analyzing the input handling of the binary. It reads a fixed number of bytes and likely executes a command based on that input. By overflowing the buffer and injecting our own command, we can hijack the control flow and execute `cat flag.txt` to print the flag.

This payload exploits a buffer overflow to inject the cat flag.txt command into the program's execution flow, leaking the contents of the flag file.

#### 🔓 Final Flag

```
acmxstf{C0mManD_Inj3ct10N}
```