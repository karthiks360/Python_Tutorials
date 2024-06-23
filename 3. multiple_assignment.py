# Multiple assignment = allows to assign multiple variables at the same time in one line of code

# multiple assignment for various data types
# individual assignment
# name = "Karthik"
age = 25
attractive = True
print(name)
print(age)
print(attractive)
# multiple assignment
name, age, attractive = "Karthik",25,True
print(name)
print(age)
print(attractive)
print(name + " " + str(age) + " " + str(attractive))

# multiple assignment for same data type and value
# individual assignment
Maths = 100
Science = 100
Social = 100
print(Maths)
print(Science)
print(Social)
# multiple assignment
Maths = Science = Social = 100
print(Maths)
print(Science)
print(Social)