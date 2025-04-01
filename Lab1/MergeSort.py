# Merge Sort

def Merging(A, left, right):
    nl = len(left)
    nr = len(right)
    i = 0
    j = 0
    k = 0
    while i < nl and j < nr:
        if left[i] < right[j]:
            A[k] = left[i]
            i = i+ 1

        else:
            A[k] = right[j]
            j = j+1

        k = k + 1

    while i < nl:
        A[k] = left[i]
        i = i + 1
        k = k+1
    while j < nr:
        A[k] = right[j]
        j = j+1
        k = k+1

    return A

def Merge(A):
    if len(A) < 2:
        return
    n = len(A)//2
    left = A[:n]
    right = A[n:]
    print('Left: ', left)
    print('Right: ', right)
    Merge(left)
    Merge(right)
    ans = Merging(A, left, right)
    print('Merging: ' ,ans)
    print()

A = [10, 1, 8, 7, 6, 5, 4, 4, 2, 1]
Merge(A)
