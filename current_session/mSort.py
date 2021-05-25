"""
Merge sort
"""
def mergeSort(arr):
    """
    divide and conquer
    1. split the array
    2. sort L and R seperately
    3. merge L and R: use 2 pointers, add each of these elements one by one
    4. add the remaining parts from L (or R)
    """
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = mergeSort(arr[:mid]), mergeSort(arr[mid:])

        # mergeSort(L)
        # mergeSort(R)

        i, j, k = 0, 0, 0

        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                arr[k], i, k = L[i], i+1, k+1
            else:
                arr[k], j, k = R[j], j+1, k+1

        while i<len(L):
            arr[k], i, k = L[i], i+1, k+1

        while j<len(R):
            arr[k], j, k = R[j], j+1, k+1

    return arr

# print mergeSort([1,9,2,8,3,7,4,6,5])
# print mergeSort([1,2,3,6,9,8,7,5,4])
