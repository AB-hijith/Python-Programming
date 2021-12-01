m=int(input("Enter first number:"))
n=int(input("Enter second number:"))
if m>n:
    temp=n
else:
    temp=m
for i in range(1,temp+1):
    if(m%i==0) and (n%i==0):
        gcd=i
print(gcd)
