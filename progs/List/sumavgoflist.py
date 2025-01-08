def sumavglist(L):
    sum = 0
    for i in L:
        sum += i
    avg = sum//len(L)
    return sum, avg

L = [1,2,3,4,5,6]
sumavg = sumavglist(L)
print(sumavg[0])
print(sumavg[1])
    