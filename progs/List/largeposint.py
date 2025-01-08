# Largest positive integer that exists with its negative

def largeposint(arr):
    posarr = []
    negarr = []
 
    for i in arr:
        if i > 0:
            posarr.append(i)
        else:
            negarr.append(i)
    maxint = 0
    for j in posarr:
        if -j in negarr:
            if j > maxint:
                maxint = j
    return maxint

def largeposint1(arr):
    num_set = set(arr)
    maxint = 0
    for num in arr:
        if num > 0 and -num in num_set:
            maxint = max(maxint, num)
    
    return maxint

arr = [-9, 1, 2, 3, 4, -3, -7, 9, -2, 6, 8, 7, -8]
print(largeposint1(arr))