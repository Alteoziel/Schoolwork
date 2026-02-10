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
    c = 0
    d = 1
    binary_b = bin(b)[2:]
    print(binary_b)
    for i in range(len(binary_b)-1,0,-1):
        c = 2*c
        d = (d*d)%n
        if binary_b[i] == 1:
            c = c + 1
            d = (d*a)%n
    return d

print(modular_exponentiation(10,100,3))
