d1=dict()
n1=int(input("enter no of elements in dict1"))
for i in range(n1):
      key1=input("enter key")
      value1=input("enter value")
      d1[key1]=value1
print(d1)      
sort=sorted(d1)
for i in sort:
    print(i,":",d1[i])
