class rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle1: "))
b=int(input("Enter breadth of rectangle1: "))
c=int(input("Enter length of rectangle2: "))
d=int(input("Enter breadth of rectangle2: "))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
d=obj1.area()
f=obj2.area()
print("Area of rectangle1:",d)
print("Area of recatangle2:",f)
print()
if(d == f):
    print("Matching Rectangle ")
else:
    print("Non Matching Rectangle ")