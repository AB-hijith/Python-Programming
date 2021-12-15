d1={}
d2=dict()
n1=int(input("enter no of elements in dict1"))
for i in range(n1):
      key1=input("enter key")
      value1=input("enter value")
      d1[key1]=value1
n2=int(input("enter no of elements in dict1"))
for i in range(n2):
      key2=input("enter key")
      value2=input("enter value")
      d2[key2]=value2
print(d1,d2)
d1.update(d2)
print(d1)
