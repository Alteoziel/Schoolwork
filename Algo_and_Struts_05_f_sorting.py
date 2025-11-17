import random, time
from Algo_and_Struts_05_g_quick_sort import quick_sort

def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])

def bubble_sort_short(a_list):
    for i in range(len(a_list)):
        exchanges = False
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])
        if not exchanges:
            break

def selection_sort(a_list):
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        #print("After increments of size", sublist_count, "the list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val

def merge_sort(a_list):
    #print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    #print("Merging", a_list)


#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#bubble_sort(a_list)
# bubble_sort_short(a_list)
# selection_sort(a_list)
# insertion_sort(a_list)
# shell_sort(a_list)
# merge_sort(a_list)
print("\n")
print("\n")


#Setup lists
L1 = []
L2 = []
L3 = []
L4 = []

#fill lists
for i in range(1,101):
    L1.append(random.randint(1,100))
for i in range(1,10001):
    L2.append(random.randint(1,10000))
for i in range(1,100001):
    L3.append(random.randint(1,100000))
for i in range(1,1000001):
    L4.append(random.randint(1,1000000))




#bubble sort
print("\n", "Bubble Sort:")
start = time.time()
bubble_sort(L1)
end = time.time()
print(end-start)

start = time.time()
bubble_sort(L2)
end = time.time()
print(end-start)
"""
start = time.time()
#bubble_sort(L3) #too long
end = time.time()
print(end-start)


start = time.time()
bubble_sort(L4) #too long
end = time.time()
print(end-start)
"""


#selection sort
print("\n", "Selection Sort:")
start = time.time()
selection_sort(L1)
end = time.time()
print(end-start)

start = time.time()
selection_sort(L2)
end = time.time()
print(end-start)

"""
start = time.time()
selection_sort(L3)) #too long
end = time.time()
print(end-start)

start = time.time()
selection_sort(L4)) #too long
end = time.time()
print(end-start)
"""


#insertion sort
print("\n", "Insertion Sort:")
start = time.time()
insertion_sort(L1)
end = time.time()
print(end-start)

start = time.time()
insertion_sort(L2)
end = time.time()
print(end-start)

"""
start = time.time()
insertion_sort(L3) #too long
end = time.time()
print(end-start)

start = time.time()
insertion_sort(L4) #too long
end = time.time()
print(end-start)
"""


#shell sort
print("\n", "Shell Sort:")
start = time.time()
shell_sort(L1)
end = time.time()
print(end-start)

start = time.time()
shell_sort(L2)
end = time.time()
print(end-start)

start = time.time()
shell_sort(L3)
end = time.time()
print(end-start)

start = time.time()
shell_sort(L4)
end = time.time()
print(end-start)


#merge sort
print("\n", "Merge Sort:")
start = time.time()
merge_sort(L1)
end = time.time()
print(end-start)

start = time.time()
merge_sort(L2)
end = time.time()
print(end-start)

start = time.time()
merge_sort(L3)
end = time.time()
print(end-start)

start = time.time()
merge_sort(L4)
end = time.time()
print(end-start)



#quick sort
print("\n", "Quick Sort:")

start = time.time()
quick_sort(L1)
end = time.time()
print(end-start)

"""
#hits maximum depth recursion
start = time.time()
quick_sort(L2)
end = time.time()
print(end-start)

#hits maximum depth recursion
start = time.time()
quick_sort(L3)
end = time.time()
print(end-start)

#hits maximum depth recursion
start = time.time()
quick_sort(L4)
end = time.time()
print(end-start)
"""
