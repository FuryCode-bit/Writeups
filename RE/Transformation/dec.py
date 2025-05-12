enc = "enc"
enc = open(enc).read()

for letter in enc:
    print(hex(ord(letter)).lstrip("0x"), end=' ')
