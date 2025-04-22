# Challenge: Slithering Security

## Reverse Engineering: CyberChef Base64

### Description

Help me test my sssecurity, can you get the flag from this ssssecure sssscript?

This challenge is from the November 2024 Flash CTF. It was first solved 45 seconds into the competition by matdaneth. 77.6% of active users solved it during the competition.

### Solution

In the script, we see that the flag is stored in the SECRET_FLAG variable, which has a bunch of characters in the format \x__. This is just a series of bytes. The \x in this case means we’re dealing with hexadecimal characters, which we can convert to a more…readable format.

Using a tool like CyberChef, we can copy/paste the contents of the SECRET_FLAG variable and decode from hex, giving us the following string:

TWV0YUNURntkMG43XzdydXM3X2NsMW43c193aTdoX3MzY3IzN3Nzc3Nzc3N9

After we enter our input and it’s checked against the hashed password, one of two things will happen – the flag will be decoded if our password is correct, or we’ll be told our password is incorrect. The important thing to pay attention to here is how the flag is decoded if we’re correct – specifically, the code fragment b64decode(SECRET_FLAG).decode(). The b64decode function within the base64 module is used to decode Base64 strings, which we can assume our secret flag is in the form of. Luckily for us, CyberChef can decode Base64 strings too, so let’s try it!

After using the “From Base64” recipe in CyberChef on the string we got earlier, we get the flag:

MetaCTF{d0n7_7rus7_cl1n7s_wi7h_s3cr37sssssss}
