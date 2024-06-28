# nested loops = the "inner loop" finish all of its iterations before finishing one iteration of the "outer loop"
rows = int(input("Enter rows : "))
cols = int(input("Enter cols : "))
symbol = input("Enter Symbol : ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()    