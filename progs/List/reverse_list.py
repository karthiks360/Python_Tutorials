def rev_list(L):
    i = 0
    size = len(L)
    while i < size //2:
        L[i], L[size -i -1] = L[size -i -1], L[i]
        i += 1
    return L

L = [1,2,3,4,5,6,7]
print(rev_list(L))