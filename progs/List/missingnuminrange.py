def missinrange(List):
    List.sort()
    res = []
    s = List[0]
    e = List[-1]
    for i in range(s,e):
        if i not in List:
            res.append(i)
    return res

L= [13,18,2,5,8,10,11]
M = missinrange(L)
print(M)

FA = (L + M)
FA.sort()
print(FA)