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
l1 = 0
l2=0
l3=0
l4=0
for j in range(0,1_000_000):
    my_set = [1,2,3,4,5]
    set2=randomize_in_place(my_set)
    if set2 == [1,2,3,4,5]:
        l1+=1
    if set2 == [2,1,3,4,5]:
        l2+=1
    if set2 == [3,2,1,4,5]:
        l3+=1
    if set2 == [4,2,3,1,5]:
        l4+=1
    dictRandom[a] = set2
    a+=1
print("[1,2,3,4,5] = ",l1,"[2,1,3,4,5] = ",l2,"[3,2,1,4,5] = ",l3,"[4,2,3,1,5] = ",l4)



dictRandom = {}
a = 0
l1 = 0
l2=0
l3=0
l4=0
for j in range(0,1_000_000):
    my_set = [1,2,3,4,5]
    set2=permute_with_all(my_set)
    if set2 == [1,2,3,4,5]:
        l1+=1
    if set2 == [2,1,3,4,5]:
        l2+=1
    if set2 == [3,2,1,4,5]:
        l3+=1
    if set2 == [4,2,3,1,5]:
        l4+=1
    dictRandom[a] = set2
    a+=1
print("[1,2,3,4,5] = ",l1,"[2,1,3,4,5] = ",l2,"[3,2,1,4,5] = ",l3,"[4,2,3,1,5] = ",l4)
