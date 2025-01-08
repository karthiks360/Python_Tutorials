def dupremover(L):
    org = []
    for i in L:
        if i not in org:
            org.append(i)
    return org

L = [1,2,3,4,1,2,3,4,7,4,6,9,0,4,5,7,90]
print(dupremover(L))