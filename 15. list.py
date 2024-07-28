# list = used to store multiple items in a  single variable

food = ["pizza","burger","fries"]
print(food[0])

food[0] = "sushi"
print(food)

for x in food:
    print(x)

food.append("ice cream")
print(food)

food.remove("fries")
print(food)

food.pop()
print(food)

food.insert(0,"cutlet")
food.sort()
food.clear()

print(food)