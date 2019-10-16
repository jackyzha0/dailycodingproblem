# quick implementation of merge sort

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    len_l = len(left)
    len_r = len(right)
    i, j = 0,0

    res = []

    while i < len_l and j < len_r:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len_l:
        res.append(left[i])
        i += 1

    while j < len_r:
        res.append(right[j])
        j += 1

    return res

print(mergeSort([1,2,3,6,1,35,123]))
