# Variable is a container of value, Behaves as the value that it contain
name = "Karthik" #Both '' & " " can be used
print("Hello " +name) 

# to check data type of variable
print(type(name))

# string concatination
first_name = "Karthik"
last_name = "Sridhara"
full_name = first_name + " " + last_name + " " + first_name
print(full_name)

# integer data type
age = 21 #int must not be within quotes
age += 1
print(age)
print(type(age))

#string data type
age = "21"
print(type(age))
age += 1 #doesn't work as the age is a string
print(age)
print("Your age is "+age)

# int to str data type conversion
age = 21
print(type(age))
print("your age is "+str(age))

# float data type
height = 178.5
weight = 81.2
print(type(height))
print("Your height is "+str(height)+"cm and weight is "+str(weight)+"kg")

# boolean data type
human = False
print(human)
print(type(human))
print("Are you a human - "+str(human))