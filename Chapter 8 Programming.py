import csv

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
    B = [0] * n-1
    for i in range(0,n-1):
        B[i] = []
    for i in range(0,n):
        B[n//A[i]] = A[i]
    for i in range(0,n-1):
        insertion_sort(B[i])
    for i in range(0,n):
        C = C + B[i]


