# Loop Control Statements = change a loops execution from its normal sequence
# break = used to termininate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing,  acts as a placeholder

while True:
    name = input("Enter name : ")
    if name != "":
        break
print("Hello "+name)

mob_num = "1234-567-789"
for i in mob_num:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)