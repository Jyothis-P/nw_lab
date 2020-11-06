from _thread import *
import time
import msvcrt

c = 0


def disp():
    print(input('Say something'))

start_new_thread(disp, ())
time.sleep(1)
print('asdasdasd')


time.sleep(10)
# print(c)
