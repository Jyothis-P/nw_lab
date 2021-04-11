def encrypt_rail_fence(plaintext, key):
    rail = [['' for i in range(len(plaintext))] for j in range(key)]
    r, c = 0, 0
    for i in range(len(plaintext)):
        rail[r][c] = plaintext[i]
        c += 1
        r = (r + 1) % key

    cipher = ''.join([''.join(l) for l in rail])
    return cipher


def decrypt_rail_fence(cipher, key):
    rail = [['' for i in range(len(cipher))] for j in range(key)]
    r, c = 0, 0
    for i in range(len(cipher)):
        rail[r][c] = cipher[i]
        c += key
        if c >= len(cipher):
            c -= len(cipher) - 1
            r += 1
    plaintext = ''
    r, c = 0, 0
    for i in range(len(cipher)):
        plaintext += rail[r][c]
        c += 1
        r = (r + 1) % key
    return plaintext


print(encrypt_rail_fence('RAILFENCE', 3))
print(decrypt_rail_fence('RLNAFCIEE', 3))
