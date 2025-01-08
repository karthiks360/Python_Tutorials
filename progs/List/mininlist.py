def mininlist(L):
    min = L[0]
    for i in range(len(L)):
        if L[i] < min:
            min = L[i]
    
    return min

L= [2,5,7,3,2,1,5]
print(mininlist(L))