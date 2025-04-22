# Challenge interns'Project: TexSAW 2025

Bypass `geteuid()` Check

## Reverse Engineering: / Bypass `geteuid()` Check

## Description

The remote binary provides a simple menu interface:

- Option 2 prints the flag, **but only if `geteuid() == 0`** (i.e., running as root).
- Obviously, you can't use `sudo` or escalate privileges directly on a remote netcat service.

However, due to a logical flaw in the input parsing, it's possible to bypass the root check and still trigger the flag printing.

## Solution

Upon analyzing the provided logic, we see the following snippet from `handleOption()`:

```cpp
std::getline(std::cin, input);  // gets a whole line of text
std::istringstream iss(input);
while (...) {
  iss >> option;
  if (option == 2 && geteuid() != 0) {
    std::cout << "Error" << std::endl;
  } else {
    if (option == 2) printFlag();
  }
}
```

The key insights are:

- The program reads an entire **line** of input.
- It **processes multiple options** from a single line.
- The `geteuid()` check only triggers **if option 2 is encountered first**.

Thus, if we input **multiple options in one line**, and **option 2 is not first**, the `geteuid()` check is skipped, but `printFlag()` still executes.

### Step-by-Step Attack:

1. Connect to the server:

   ```bash
   nc challs.example.com 31337
   ```

2. When prompted for an option, input multiple options in one line, making sure that `2` is not the first:

   ```bash
   3 2
   ```

   or

   ```bash
   1 2
   ```

3. The binary will process the first option (e.g., creating an account), then encounter `2` and **call `printFlag()` without rechecking privileges**.

After a fake account creation message, the flag will be printed.

