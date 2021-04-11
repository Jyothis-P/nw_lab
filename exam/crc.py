def xor(x, y):
    return ''.join(str(int(x[i]) ^ int(y[i])) for i in range(len(x)))


def modulo_2_division(divident, divisor):
    i = len(divisor)

    current_divident = divident[0: i]
    while i < len(divident):
        if current_divident[0] == '1':
            current_divident = xor(current_divident[1:], divisor[1:]) + divident[i]
        else:
            current_divident = xor(current_divident[1:], ('0' * i)[1:]) + divident[i]
        i += 1

    if current_divident[0] == '1':
        current_divident = xor(current_divident[1:], divisor[1:])
    else:
        current_divident = xor(current_divident[1:], ('0' * i)[1:])

    return current_divident


def encode_crc(plaintext, key):
    binary_plaintext = ''.join(format(ord(c), 'b') for c in plaintext.upper())
    augmented_plaintext = binary_plaintext + '0' * (len(key) - 1)
    redundant_bits = modulo_2_division(augmented_plaintext, key)
    cipher = binary_plaintext + redundant_bits
    return cipher


def decode_crc(cipher, key):
    augmented_cipher = cipher + '0' * (len(key) - 1)
    check = modulo_2_division(augmented_cipher, key)
    if check == '0' * (len(key) - 1):
        data = cipher[:-(len(key) - 1)]
        res = ''.join(chr(int(data[i:i + 7], 2)) for i in range(0, len(data), 7))
        return res
    else:
        return False


print(encode_crc('Evn', '1001'))
print(decode_crc('100010110101101001110111', '1001'))
