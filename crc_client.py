import socket


def xor(a, b):
    res = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            res.append('0')
        else:
            res.append('1')

    return ''.join(res)


def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def encode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword


s = socket.socket()
port = 12345

s.connect(('127.0.0.1', port))

input_string = input("Enter data you want to send: ")

data = (''.join(format(ord(x), 'b') for x in input_string))
key = input("Enter the key: ")

ans = encode_data(data, key)

ans = int(ans)
for i in range(1):
    ans = (ans ^ (1 << i))
ans = str(ans)
print("After flipping" + ans)
print(ans)

ans = ans.encode()
s.sendall(ans)
result = s.recv(1024)
result = result.decode()
print(result)
s.close()
