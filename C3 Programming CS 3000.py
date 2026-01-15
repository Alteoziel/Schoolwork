import time, random as r

def ran(n):
    a = r.randint(0,10**n)
    b = r.randint(0,10**n)
    return a*b
    

L = []
for i in range(0,3000000):
    sT = time.time()
    ran(i)
    eT = time.time()
    t = eT-sT
    L.append(t)
print(L)
