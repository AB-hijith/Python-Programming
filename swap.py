a=int(input("First number="))
b=int(input("Second number="))
print("Before Swapping")
print(a,b,sep="      ")
a = a + b 
b = a - b
a = a - b
print("After Swapping")
print(a,b,sep="      ")


