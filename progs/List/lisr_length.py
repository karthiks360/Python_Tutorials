def list_length(List):
    count = 0
    for i in List:
        count +=1
    return count

List = [1,2,3,4,5,6,7,8]
count= list_length(List)
print(count)