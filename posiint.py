n=input("enter integers seperated by space")
l=n.split(" ")
le=len(l)
s=map(int,l)
d=[i for i in s if i>0]
print(d)
