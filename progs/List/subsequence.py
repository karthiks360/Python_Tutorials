def subsequence(arr, sarr):
    i = 0
    j = 0
    
    while i < len(arr) and j < len(sarr):
        if arr[i] == sarr[j]:
            j += 1
        i += 1
    return j == len(sarr)

arr = [1, 2, 3, 4, 5, 6, 7]
sarr = [1, 2, 4]
print(subsequence(arr, sarr))  
