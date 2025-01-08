def occ(L,key):
    if key in L:
        return True
    else:
        return False

L = [1,2,3,4,5,6,7,8,9]
key = 9
occ_check = occ(L,key)
print(occ_check)        