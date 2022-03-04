base = int(input("Enter triangle base: "))
height = int(input("Enter triangle height: "))

print("Area of triangle", end=" ")
print((lambda x, y: 0.5 * x * y)(base, height))

sqr_side = int(input("Enter side of a square: "))
print("Area of square is", end=" ") 
print((lambda x:x * x)(sqr_side))

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
print("Area of rectangle is", end=" ") 
print((lambda x, y:x * y)(length, width))