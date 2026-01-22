import random

def randomize_in_place(A):
    n = len(A)-1
    for i in range(0,n):
        g = random.randint(i,n)
        temp = A[i]
        A[i] = A[g]
        A[g] = temp
    return A


def permute_with_all(A):
    n = len(A)-1
    for i in range(0,n):
        g = random.randint(0,n)
        temp = A[i]
        A[i] = A[g]
        A[g] = temp
    return A





dictRandom = {}
a = 0
for j in range(0,1_000_000):
    my_set = [1,2,3,4,5]
    set2=randomize_in_place(my_set)
    dictRandom[a] = set2
    a+=1
print(dictRandom[2])

b = (2,1,3,4,5)
c=0
for i in range(0,len(dictRandom)):
    if b in dictRandom:
        c+=1

print(c)

my_set = [1,2,3,4,5]
set3=permute_with_all(my_set)

print(set2,set3)

