import math
def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)

def extended_euclid(a,b):
    if b==0:
        return [a,1,0]
    else:
        [a,b,c] = extended_euclid(b,a%b)
        [d,x,y] = [a,b,c-math.floor(a/b)*b]
        return [d,x,y]

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
        return "composite"
    else:
        return "prime"



print(pseudoprime(203025))
print(modular_exponentiation(10,100,3))
print(extended_euclid(1001,2000))
print(euclid(1001,2000))
