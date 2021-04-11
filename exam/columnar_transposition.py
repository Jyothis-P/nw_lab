import math


def encode_columnar(plaintext, key):
    order = [x for _, x in sorted([ord(c), i] for i, c in enumerate(key))]
    rows = math.ceil(len(plaintext) / len(key))
    plaintext += ' ' * (rows * len(key))
    return ''.join(''.join(plaintext[j * len(key) + i] for j in range(rows)) for i in order)


print(encode_columnar('Geeks for Geeks', 'HACK'))
