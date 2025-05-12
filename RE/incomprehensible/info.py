
# Description

print(__import__('base64').b64encode(b''.join(
    [([l.append(bytes([v[0]for v in sorted(zip([p[j]^l[-1][(i+j+1+(16//2))%16]for j in range(16)],(lambda x:[([l.append((lambda n,u:(lambda f,*a:f(f,*a))((lambda r,i,u:i if i not in u else r(r,(i+1)%16,u+[i])),n%16,u))(c,l))for c in x[::-1]],l)for l in [[]]][0][1])(l[-1])),key=lambda x:x[1])]))for i,p in enumerate([f[i*16:(i+1)*16]for i,f in enumerate((lambda x,y:[y]*x)(*[f if i else len(f)//16 for i,f in enumerate([b''.join([f if i else bytes(list(range(f+1))[1::][::-1])for i,f in enumerate([f if i else 16-(len(f)%16)for i,f in enumerate([bytes(input(),'utf-8')]*2)])])]*2)]))])],l) for l in[[b'CoOL N0nCE duD3!']]][0][1][1:])))

import base64

nonce = b'CoOL N0nCE duD3!'

# Read user input
user_input = "flag123456"
user_bytes = bytes(user_input, 'utf-8')

# Pad the input
pad_len = 16 - (len(user_bytes) % 16)
padding = bytes(list(range(pad_len + 1))[1:][::-1])
padded_input = user_bytes + padding

# Repeat the padded input twice
doubled_input = padded_input * 2

# Create blocks of 16 bytes
blocks = [doubled_input[i*16:(i+1)*16] for i in range(len(doubled_input) // 16)]

l = [nonce]

# Process each block
for i, p in enumerate(blocks):
    zipped = zip(
        [p[j] ^ l[-1][(i + j + 1 + (16 // 2)) % 16] for j in range(16)],
        (lambda x: [
            (
                [l.append(
                    (lambda n, u: (
                        lambda f, *a: f(f, *a)
                    )(
                        (lambda r, i, u: i if i not in u else r(r, (i + 1) % 16, u + [i])),
                        n % 16,
                        u
                    ))(c, l)
                ) for c in x[::-1]],
                l
            )
            for l in [[]]
        ][0][1])(l[-1])
    )

    sorted_block = sorted(zipped, key=lambda x: x[1])
    new_block = bytes([v[0] for v in sorted_block])
    l.append(new_block)

# Join and encode the result
result = b''.join(l[1:])
encoded = base64.b64encode(result)
print(encoded)
