# Challenge: Suspicious script

## Reverse Engineering: Base64 Decode

### Description

A suspicious .ps1 (PowerShell) script was found on a homework help site. The user was unfamiliar with it and asked for an investigation. The flag format is DawgCTF{...}.

### Solution

Opening `homeworkHelper.ps1`, we find a long Base64 string. Decoding it reveals another Base64-encoded payload. Decoding again reveals reversed PowerShell code.

After reversing the text, we find a command constructing a URL and using a WebClient to upload a file. Embedded in the code is the flag:

DawgCTF{Wr4pped_5c1pt5!}