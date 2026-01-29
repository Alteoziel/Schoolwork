import math

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def bucket_sort(A):
    n = len(A)
    B = [0] * (n)
    C = []
    for i in range(0,n):
        B[i] = []
    for i in range(0,n):
        m = A[i]
        p = math.floor(int(n*m))
        B[p].append(m)
    for i in range(0,n):
        insertion_sort(B[i])
    for i in range(0,n):
        if B[i] != []:
            C.extend(B[i])
    print(C)


p10list = []
a = open("points_10.csv")
for line in a:
    b = line.split(",")
    x = float(b[0])
    y = float(b[1])
    c2 =(x*x) + (y*y)
    c = math.sqrt(c2)
    p10list.append(c)

bucket_sort(p10list)
