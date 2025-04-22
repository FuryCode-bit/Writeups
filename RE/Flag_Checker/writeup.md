# Challenge: Flag Checker

## Reverse Engineering:

### Description

I hid the flag in this Python script. It asks you for a flag and tells you if it's correct or not. Can you reverse engineer it to find the correct flag?

The flag that the script above validates as correct is the flag for this challenge.

You can also access the script in an online Python IDE here: https://www.online-python.com/1i6lX9bv0a. Click the green "Run" button to run the program.
This challenge is from the February 2024 Flash CTF. It was first solved 102 seconds into the competition by NickC. 48.6% of active users solved it during the competition.

### Solution

In this challenge, we are given a Python script that validates a user-entered flag. The validation logic checks the flag against an "encrypted" string using a specific character-based formula. Our task is to reverse the logic to recover the correct flag without guessing.

The script compares each character of the flag to a character in the encrypted string using this formula:

```
ord(flag[i]) - 1 == ord(encrypted[i]) + i
```

Rearranging it, we find:

```
ord(flag[i]) = ord(encrypted[i]) + i + 1
```

This means that for each character, we add the character’s position index and 1 to the ASCII value of the encrypted character to get the flag's character.

Using a simple loop to apply this formula, we recover the flag:

```python
encrypted = "Lcq]>N?s]bV[R[_OaScQ]]NGPYDKDNG]"
flag = ""

for i in range(len(encrypted)):
    flag += chr(ord(encrypted[i]) + i + 1)

print(flag)
```

The recovered flag is:

MetaCTF{bruteforcing_is_fun_right}
