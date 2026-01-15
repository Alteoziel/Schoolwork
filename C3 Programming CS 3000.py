import time, random as r

def ran(n):
    a = r.randint(0,10**n)
    b = r.randint(0,10**n)
    return a*b
    

for i in range(0,1):
    sT = time.time()
    ran(3000000)
    eT = time.time()
    t = eT-sT
    print(t)
