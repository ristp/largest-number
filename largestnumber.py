x = 0
y = 0
z = 0
tempVariable = 0

x = input("Input value of x ")
y = input("Input value of y ")

if x > y:
    tempVariable = x
    x = y
    y = tempVariable
    print(y)
    print(x)
elif y > x:
    print("Hello")

