def maxinlist(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    
    return max

L= [2,5,7,3,2,1,5]
print(maxinlist(L))