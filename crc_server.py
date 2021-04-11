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

    check_word = tmp
    return check_word


def decode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return remainder


s = socket.socket()
print("Socket successfully created")
port = 12345

s.bind(('', port))
print("socket bound to %s" % (port))
# put the socket into listening mode 
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(1024)
    data = data.decode()
    print(data)
    if not data:
        break

    key = input("Enter the key: ")

    ans = decode_data(data, key)
    print("Remainder after decoding is->" + ans)

    temp = "0" * (len(key) - 1)
    if ans == temp:
        result = "THANK you Data  Received No error FOUND"
        result = result.encode()
    else:
        result = "Error in data"
        result = result.encode()
    c.sendall(result)
    c.close()
