def swap(pos1,pos2,L):
    temp = L[pos1-1]
    L[pos1-1] = L[pos2-1]
    L[pos2-1] = temp
    return L

List = [1,2,3,4,5,6]
print(swap(3,1,List))