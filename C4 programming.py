import math, random, time

def find_max_crossing_subarray(A,low,mid,high):
    left_sum = float("-inf")
    summ = 0
    max_left=0
    max_right=0
    for i in range(mid, low, -1):
        summ = summ+A[i]
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
    return[max_left,max_right,left_sum+right_sum]

def find_max_subarray(A,low,high):
    if high==low:
        return [low,high,A[low]]
    else:
        mid = math.floor((low+high)/2)
        #[left_low,left_high,left_sum]
        left= find_max_subarray(A,low,mid)
        #[right_low,right_high,right_sum]
        right= find_max_subarray(A,mid+1,high)
        #[cross_low,cross_high,cross_sum]
        cross= find_max_crossing_subarray(A,low,mid,high)
        if left[2]>right[2] and left[2]>cross[2]:
            return left
        if right[2]>left[2] and right[2]>cross[2]:
            return right
        if cross[2]>right[2] and cross[2]>left[2]:
            return cross
        
def find_max_subarray_bruteforce(A):
    if len(A) == 0:
        return
    if len(A) == 1:
        return A[0]
    else:
        m = A[0]
        tempMax = float("-inf")
        for startIndex in range(0,len(A)):
            for endIndex in range(0,len(A)):
                for n in range(startIndex,endIndex+1):
                    tempMax+=A[n]
                    if tempMax > m:
                        m=tempMax
                        tempMax=0
                tempMax = 0          

def hybrid(A):
    if len(A)<10:
        find_max_subarray_bruteforce(A)
    else:
        find_max_subarray(A,0,len(A))


#Bruteforce
a = []
for i in range(0,100):
    a.append(random.randint(-100000,100000))

b = []
for i in range(0,200):
    b.append(random.randint(-100000,100000))

c = []
for i in range(0,400):
    c.append(random.randint(-100000,100000))

st = time.time()
find_max_subarray_bruteforce(a)
et = time.time()
total = et-st
print(total)

st = time.time()
find_max_subarray_bruteforce(b)
et = time.time()
total = et-st
print(total)

st = time.time()
find_max_subarray_bruteforce(c)
et = time.time()
total = et-st
print(total)                        


#Maximum subarray
a = []
for i in range(0,100):
    a.append(random.randint(-100000,100000))

b = []
for i in range(0,200):
    b.append(random.randint(-100000,100000))

c = []
for i in range(0,400):
    c.append(random.randint(-100000,100000))

st = time.time()
find_max_subarray(a,0,len(a)-1)
et = time.time()
total = et-st
print(total)

st = time.time()
find_max_subarray(b,0,len(b)-1)
et = time.time()
total = et-st
print(total)

st = time.time()
find_max_subarray(c,0,len(c)-1)
et = time.time()
total = et-st
print(total) 
