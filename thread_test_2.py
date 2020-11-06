import msvcrt

num = 0
done = False
buff = ''
while not done:
    b = msvcrt.getch()
    char = b.decode("utf-8")
    buff += char
    print(b, char)
    if char == '\r':
        print(buff)
        print("okay")
        done = True
    # if msvcrt.kbhit():
    #     buff += msvcrt.getch()
    #     print("you pressed", msvcrt.getch(), "so now i will quit")
    #     done = True
