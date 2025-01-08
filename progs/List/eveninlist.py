def eveninlist(list):
    res = []
    for i in list:
        if i%2 ==0:
            res.append(i)
    return res

L=[1,2,3,4,5,6,7,8,12]
print(eveninlist(L))