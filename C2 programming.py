import random as ra

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        #print(key)
        #Insert A[j] into the sorted sequence A[1..j-1].
        i = j-1
        #print(i)
        while i>0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
        #print(A)

def reversedInsertionSort(A):
    for j in reversed(range(1,len(A)-1)):
        key = A[j]
        #print(key)
        #Insert A[j] into the sorted sequence A[1..j-1].
        i = j+1
        #print(i)
        while i<len(A) and A[i] > key:
            A[i-1] = A[i]
            i = i+1
        A[i-1] = key
        #print(A)

def merge(A,p,q,r): ???
    n1 = q-p+1
    n2 = r-q
    L=[]
    R=[]
    for n in range(1,n1+1):
        L.append(n)
    for m in range(1,n2+1):
        R.append(m)
    for i in range(1,n1):
        L[i] = A[p+i-1]
    for j in range(1,n2):
        R[j] = A[q+j]
    L.append(float('inf'))
    R.append(float('inf'))
    i=1
    j=1
    for k in range(p,r):
        if L[i]<=R[j]:
            A[k] = L[i]
            i = i+1
        elif A[k] == R[j]:
            j = j+1

def bubblesort(A):
    for i in range(1,len(A)-1):
        for j in range(len(A)-1,i-1,-1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp


a = [1,4,8,9,5,3,5,1,8,96]
insertion_sort(a)
print(a)

b = [96,8,1,5,3,5,9,8,4,1]
reversedInsertionSort(b)
print(b)

c = [1,4,8,9,5,3,5,1,8,96]
merge(c,0,4,8)
#print(c)

d = [1,4,8,9,5,3,5,1,8,96]
bubblesort(d)
print(d)
