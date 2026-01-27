import random as r

def make_random_list(size):
    l = []
    for i in range(0,size):
        l.append(r.randint(0,10000))
    return l

def make_boolean_list(List):
    bl = []
    for i in range(0,len(List)):
        bl.append(False)
    return bl

def Random_Search(rList,searchNum):
    counter = 0
    bList = make_boolean_list(rList)
    for i in range(0,len(rList)):
        if rList[i] == searchNum:
            return i
        else:
            if bList[i] == True:
                continue
            bList[i] = True
            counter += 1
            if counter == len(rList):
                return counter

def Deterministic_Search(rList,searchNum):
    counter = 0
    for i in range(0,len(rList)):
        if rList[i] == searchNum:
            return i
        counter += 1
    return counter

def Scramble_Search(rList,searchNum):
    L = randomize_in_place(rList)
    return Deterministic_Search(L,searchNum)

def randomize_in_place(A):
    n = len(A)-1
    for i in range(0,n):
        g = r.randint(i,n)
        temp = A[i]
        A[i] = A[g]
        A[g] = temp
    return A


n = 0
for i in range(0,10000):
    rl1 = make_random_list(10000)
    rl1[r.randint(0,9999)] = -1
    temp = Random_Search(rl1, -1)
    n += temp
print(n/10000)

n = 0
for i in range(0,10000):
    rl1 = make_random_list(10000)
    temp = Random_Search(rl1, -1)
    n += temp
print(n/10000)

n = 0
for i in range(0,10000):
    rl2 = make_random_list(10000)
    rl2[r.randint(0,9999)] = -1
    temp = Deterministic_Search(rl2,-1)
    n += temp
print(n/10000)

n = 0
for i in range(0,10000):
    rl3 = make_random_list(10000)
    rl3[r.randint(0,9999)] = -1
    temp = Scramble_Search(rl3,-1)
    n += temp
print(n/10000)
