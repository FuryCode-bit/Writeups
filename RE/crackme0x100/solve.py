output = list("apijaczhzgtfnyjgrdvqrjbmcurcmjczsvbwgdelvxxxjkyigy")

def transform_char(c, i):
    uVar1 = ((i % 0xff) >> 1 & 0x55) + ((i % 0xff) & 0x55)
    uVar1 = (uVar1 >> 2 & 0x33) + (uVar1 & 0x33)
    iVar2 = (uVar1 >> 4) + ord(c) - 0x61 + (uVar1 & 0xf)
    return chr((iVar2 % 26) + ord('a'))

def apply_transform(s):
    s = list(s)
    for _ in range(3):
        for i in range(len(s)):
            s[i] = transform_char(s[i], i)
    return ''.join(s)

# Reverse the input
recovered = ['?'] * len(output)

for i in range(len(output)):
    for c in range(ord('a'), ord('z') + 1):
        test = recovered.copy()
        test[i] = chr(c)
        if apply_transform(test)[i] == output[i]:
            recovered[i] = chr(c)
            break


print("Recovered password:", ''.join(recovered))
