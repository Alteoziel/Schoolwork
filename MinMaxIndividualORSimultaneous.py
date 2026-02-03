import time as t, random as r
def minimum(A):
    mini = A[0]
    for i in range(1,len(A)):
        if mini > A[i]:
            mini = A[i]
    return mini
def maximum(A):
    maxi = A[0]
    for i in range(1,len(A)):
        if A[i] > maxi:
            maxi = A[i]
    return maxi
def simultaneous(A):
    if len(A)%2 == 0:
        if A[0] < A[1]:
            mx = A[1]
            mn = A[0]
        else:
            mx = A[0]
            mn = A[1]
    else:
        mx = A[0]
        mn = A[0]
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            tmx = A[i]
            tmn = A[i-1]
        else:
            tmx = A[i-1]
            tmn = A[i]
        if tmx > mx:
            mx = tmx
        if tmn < mn:
            mn = tmn
    return mn,mx
def individual_timecheck(A):
    st = t.time()
    print(minimum(A))
    print(maximum(A))
    et = t.time()
    return et-st
def simultaneous_timecheck(A):
    st = t.time()
    print(simultaneous(A))
    et = t.time()
    return et-st


a1 = []
a2 = []
a3 = []
a4 = []
for i in range(0,100):
    a1.append(r.randint(0,100))
for i in range(0,1000):
    a2.append(r.randint(0,1000))
for i in range(0,10000):
    a3.append(r.randint(0,10000))
for i in range(0,100000):
    a4.append(r.randint(0,100000))
print(individual_timecheck(a1))
print(individual_timecheck(a2))
print(individual_timecheck(a3))
print(individual_timecheck(a4))
print("\n"), print("\n")
print(simultaneous_timecheck(a1))
print(simultaneous_timecheck(a2))
print(simultaneous_timecheck(a3))
print(simultaneous_timecheck(a4))
