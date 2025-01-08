def max_num(A,B):
    if B < A:
        return A
    else:
        return B
    
A = float(input("Enter num1 = "))
B = float(input("Enter num2 = "))
print(max_num(A,B))