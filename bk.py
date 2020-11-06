import threading 
mean=0
median=0
  
def find_mean(l):
    global mean
    mean=sum(l)/len(l)
  
def find_median(l):
    global median
    l.sort()
    n=len(l)
    if n % 2 == 0: 
        median1 = l[n//2] 
        median2 = l[n//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = l[n//2] 
	
    
  
if __name__ == "__main__": 
    l = [0,2,3,3,5,6]
    t1 = threading.Thread(target=find_mean, args=(l,)) 
    t2 = threading.Thread(target=find_median, args=(l,)) 
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 
    print(mean)
    print(median)
