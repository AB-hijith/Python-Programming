
n=int(input("enter a number"))
s=0
for i in range(2,n):
    if n%i==0:
        s=1
if s==1:
    print("not prime")
else:
    print("prime")
