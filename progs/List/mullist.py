def mullist(L):
    mul = 1
    for i in L:
        mul *= i
    return mul

L = [1,2,3,4,5,6]
mul = mullist(L)
print(mul)