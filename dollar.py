n=input("enter a string")
l=len(n)
k=list()
s=[]
for j in range(0,l):
    k.append(n[j])
for i in range(1,l):
    if(k[0]==k[i]):
        k[i]="$"
for j in range(1,l):
    k[0]=k[0]+k[j]
print(k[0])
