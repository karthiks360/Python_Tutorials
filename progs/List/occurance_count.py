def occ_count(L,key):
    count = 0
    for i in L:
        if i == key:
            count += 1
    return count

List = [1,2,5,7,2,4,6,0,7,8,9,5,6,7]
Key = 7
occcount = occ_count(List,Key)
print(occcount)