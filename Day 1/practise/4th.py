#find the triangle weather the triangle is an  equilateral, isosceles or scalene

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")

elif x == y or y == z or z == x:
    print("Isosceles triangle")

else:
    print("Scalene triangle") 
