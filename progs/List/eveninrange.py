def eveninlist(n1,n2):
    res = []
    i = n1
    for i in range(n1,n2):
        if i%2 == 0:
            res.append(i)
        i += 1
    return res

print(eveninlist(1,50))