# for loop = a statement that will execute its block of code a limited number of times
# while loop = unlimited whereas for loop = limited

# print till the max range value
for i in range(10):
    print(i+1)

# print values between the range
for i in range(50,100):
    print(i+1)

# print values between the rage with steps
for i in range(50,100,2):
    print(i)

# print the msg after the designated task gets over
import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New year !!!")    

# print the range of chars in string
for i in "Karthik":
    print(i)