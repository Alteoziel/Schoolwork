import random

def modular_exponentiation(a,b,n):
    d = 1
    binary_b = bin(b)[2:]
    print(binary_b)
    for i in range(len(binary_b)-1,0,-1):
        d = (d*d)%n
        if binary_b[i] == 1:
            d = (d*a)%n
    return d

def pseudoprime(n):
    if modular_exponentiation(2,n-1,n) != 1%n:
        return False
    else:
        return True

def extended_euclid(a,b):
    if b==0:
        return [a,1,0]
    else:
        [a,b,c] = extended_euclid(b,a%b)
        [d,x,y] = [a,b,c-math.floor(a/b)*b]
        return [d,x,y]

rand1 = random.randint(2**1021,2**1024)
rand2 = random.randint(2**1021,2**1024)

while pseudoprime(rand1) == False:
    rand1 = random.randint(2**1021,2**1024)
while pseudoprime(rand2) == False:
    rand2 = random.randint(2**1021,2**1024)

n = rand1*rand2
with open("n.txt", "w") as nFile:
    nFile.write(str(n))

e = 65537
with open("e.txt", "w") as eFile:
    eFile.write(str(e))

N = (rand1-1)*(rand2-1)
d = (e**-1)%(N)
if d<0:
    d+=N
with open("d.txt", "w") as eFile:
    eFile.write(str(d))
