import time, random as r

def ran(n):
    a = r.randint(0,10**n)
    b = r.randint(0,10**n)
    return a*b

def ranD(n):
    a = r.randint(0,10**n)
    b = r.randint(0,10**n)
    return a/b

L = []
n1 = 100000
n2 = 1000000 
n3 = 10000000 #30
n4 = 20000000 #78
n5 = 30000000 #

sT = time.time()
ranD(n1)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ranD(n2)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ranD(n3)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ranD(n4)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ranD(n5)
eT = time.time()
t = eT-sT
L.append(t)
print(t)







sT = time.time()
ran(n1)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ran(n2)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ran(n3)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ran(n4)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

sT = time.time()
ran(n5)
eT = time.time()
t = eT-sT
L.append(t)
print(t)

print(L)
