# while loop =  a statement that will execute it's block of code, as long as it's condition remains true
while 1 == 1:
    print("Im Stuck in a loop")

# Promt input unless it is entered
name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+name)