a = int(input("side 1:"))
b = int(input("side 2:"))
c = int(input("side 3:"))

if a+b>c and b+c>a and c+a>b :
    print("it is a triangle")
else:
    print("it is not a triangle")    