def getMedian(A, B):
    n, m = len(A), len(B)
    if (n+m)%2 == 1:
        first, second = (n+m)//2, (n+m)//2
    else:
        first, second = (n+m)//2-1, (n+m)//2

    ia, ib = 0, 0
    ind = 0
    mid1, mid2 = -1, -1
    while ia < n and ib < m:
        if ind == first:
            mid1 = min(A[ia], B[ib])
        if ind == second:
            mid2 = min(A[ia], B[ib])
        if A[ia] < B[ib]:
            ia += 1
        else:
            ib += 1
        ind += 1
    if mid1 != -1 and mid2 != -1:
        return (mid1+mid2)/2.0

    while ia < n:
        if ind == first:
            mid1 = A[ia]
        if ind == second:
            mid2 = A[ia]
        ia += 1
    while ib < m:
        if ind == first:
            mid1 = B[ib]
        if ind == second:
            mid2 == B[ib]
        ib += 1

    return (mid1+mid2)/2.0
