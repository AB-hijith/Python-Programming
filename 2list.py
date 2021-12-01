l=input("Enter values separated by space:")
l1=l.split()
k=input("Enter values separated by space:")
l2=k.split()
a=list(map(int, l1))
b=list(map(int, l2))
len1=len(a)
len2=len(b)
if len1==len2:
    print("The list are of same length")
else:
    print("The list are not of same length")
s1=0
s2=0
for i in range(0,len1):
    s1=s1+a[i]
for i in range(0,len2):
    s2=s2+b[i]
if s1==s2:
    print("The sum of list are the same")
else:
    print("The sum of list are not the same")
for i in range(0,len1):
    for j in range(0,len2):
        if a[i]==b[j]:
            print(b[j],"occur in both")
       
