def oecount(n1,n2):
    i = n1
    ocount = 0
    ecount = 0
    for i in range(n1,n2):
        if i%2 != 0:
            ocount += 1
        else:
            ecount += 1    
        i += 1
    return ocount,ecount

print(oecount(1,47))