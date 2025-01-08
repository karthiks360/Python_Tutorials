def max2inlist(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i-1]
    
    return max

L= [2,5,7,3,2,1,6,5]
print(max2inlist(L))