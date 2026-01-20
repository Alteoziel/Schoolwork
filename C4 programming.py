import math

def find_max_crossing_subarray(A,low,mid,high):
    left_sum = float("-inf")
    summ = 0
    for i in range(mid, low, -1):
        summ = sum+A[i]
        if summ>left_sum:
            left_sum = summ
            max_left = i
    right_sum = float("-inf")
    summ = 0
    for j in range(mid+1,high):
        summ = summ+A[j]
        if summ>right_sum:
            right_sum = summ
            max_right = j
    return(max_left,max_right,left_sum+right_sum)

def find_max_subarray(A,low,high):
    if high==low:
        return (low,high,A[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low,left_high,left_sum) = find_max_subarray(A,low,mid)
        (right_low,right_high,right_sum) = find_max_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(A,low,mid,high)

def find_max_subarray_bruteforce(A):
    if len(A) == 0:
        return
    if len(A) == 1:
        return A[0]
    else:
        for i in A:
            for j in A:
                
