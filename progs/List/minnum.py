def min_num(A,B):
    if B > A:
        return A
    else:
        return B
    
A = float(input("Enter num1 = "))
B = float(input("Enter num2 = "))
minnum = min_num(A,B)
print("Amongst ("+str(A)+","+str(B)+") : "+str(minnum)+" is smaller" )