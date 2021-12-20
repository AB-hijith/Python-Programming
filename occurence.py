t=input("enter a sentence")
li=t.split(" ")
f=[]
for i in li:
    if i not in f:
        f.append(i)
for i in f:
        print(i,"occur",li.count(i))
