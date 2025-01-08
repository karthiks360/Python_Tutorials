def npcount(n1,n2):
    i = n1
    ncount = 0
    pcount = 0
    for i in range(n1,n2):
        if i < 0:
            ncount += 1
        else:
            pcount += 1    
        i += 1
    return ncount,pcount

print(npcount(-100,1000))