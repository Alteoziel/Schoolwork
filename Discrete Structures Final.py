import random as r

#Project 1 - Chapter 9 Computer # 8
def projectionInputs():
    num = int(input("How many projections? "))
    if num == 0:
        print(len(n))
        a = r.randint(0,len(n)-1)
        print(a)
        for i in range(0,a):
            p.append(i)
    for i in range(0,num):
        inp = int(input(f"P{i} = ? "))
        p.append(inp)

n = []
for i in range(1,10):
    n.append(r.randint(1,10))
print("n = ",n)

p = []
projectionInputs()
print("p =",p)

projection = []
for i in range(0,len(p)):
    projection.append(n[p[i]])
print(projection)


N = n
s = n
for i in range(0,len(p)):
    N.pop(p[i])
    s = N
    N = n
print(n)


#Project 2 - Chapter 2 Computations and Explorations #5
q = int(input("Randomized? Y=1, N=0: "))
if q == 1:
    n = r.randint(0,1000)
else:
    n = int(input("Length of n? "))

def fib():
    a = 1
    b = 1
    for i in range(0,n):
        c = a+b
        a = b
        b = c
        if i == n-1:
            return f"n = {n}, final fib = {c}"
        if n<10:
            print(c)
print(fib())
