import socket
def detectError(arr, nr): 
	n = len(arr) 
	res = 0
	for i in range(nr): 
		val = 0
		for j in range(1, n + 1): 
			if(j & (2**i) == (2**i)): 
				val = val ^ int(arr[-1 * j]) 
		res = res + val*(10**i) 
		return int(str(res), 2) 


s = socket.socket() 
port = 12334  
s.bind(('localhost', port)) 
s.listen(5) 
print ("socket is listening") 
while True:  
    c, addr = s.accept() 
    print('Got connection from', addr)  
    arr = c.recv(1024)
    r = c.recv(1024)
    
    r = int(r)
    correction = detectError(arr, r)
    if(str(correction) == '0'):
        print("No error")
    else:
        d = len(arr)-correction
        print("Presence of error.The position of error is at position" + str(d))
        arr = arr[:d]+str(int(not bool(int(arr[d]))))+arr[d+1:]
        print ("Corrected data is"+arr)
    c.close()
