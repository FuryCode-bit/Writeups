import math

def getTriNumber(n):
    return n * (n + 1) // 2

def unpair(z):
    w = math.floor((math.isqrt(8 * z + 1) - 1) / 2)
    t = getTriNumber(w)
    k2 = z - t
    k1 = w - k2
    return k1, k2

def unpair_array(arr):
    result = []
    for z in arr:
        k1, k2 = unpair(z)
        result.extend([k1, k2])
    return result

def decrypt(encoded_flag, rounds=6):
    temp = [encoded_flag]
    for _ in range(rounds):
        temp = unpair_array(temp)
    return ''.join(chr(x) for x in temp if x != 0)

# Provided encoded flag
encoded_flag = 4036872197130975885183239290191447112180924008343518098638033545535893348884348262766810360707383741794721392226291497314826201270847784737584016

# Decrypt it
decrypted_flag = decrypt(encoded_flag)
print(decrypted_flag)
