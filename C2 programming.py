import random as ra
import math

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

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L=[]
    R=[]
    #print(A,p,q,r)
    for n in range(1,n1+1):
        L.append("")
    for m in range(1,n2+1):
        R.append("")
    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    #print(L)
    #print(R)
    for k in range(p,r+1):
        #print(L[i],R[j])
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def mergesort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

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

c = [8,4,1,9,5,3,5,1,8,96]
mergesort(c,0,9)
print(c)

d = [1,4,8,9,5,3,5,1,8,96]
bubblesort(d)
print(d)
