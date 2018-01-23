def negativefirst(A):
    for i, n in enumerate(A):
        if n < 0:
            A = [n] + A
            del A[i + 1]
    return A

def negativefirst2(A):
    last_negative = -1

    for i, n in enumerate(A):
        if n < 0:
            del A[i]
            last_negative = last_negative + 1
            A.insert(last_negative, n)
    return A

def quicksort(A):

    if len(A) < 2:
        return A

    pivot = A[0]
    gt = []
    lt = []
    eq = []

    for i in A:
        if i > pivot:
            gt.append(i)
        elif i < pivot:
            lt.append(i)
        else:
            eq.append(i)

    return quicksort(lt) + eq + quicksort(gt)

def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            del b[0]
        else:
            c.append(a[0])
            del a[0]

    if len(a) > 0:
        c = c + a
    elif len(b) > 0:
        c = c + b

    return c

def mergesort(A):
    if len(A) < 2:
        return A

    mid = len(A) // 2

    a = mergesort(A[:mid])
    b = mergesort(A[mid:])

    return merge(a, b)

def bubblesort(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

A = [1, 2, 3, -3, 4, 5, 3, -1, -11]

print(bubblesort(A))