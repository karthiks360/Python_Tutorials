# Interchange first and Last element

def interc(List):
    List[0], List[-1] = List[-1], List[0]
    return List

# List = [1,2,3,4,5,6]
List = list(input("Enter the list contents :"))
print(interc(List))