lt=input("Enter values separated by space:")
a=lt.split()
b=list(map(int, a))
len= len(b)
for i in range(0,len):
    if b[i]>100:
        b[i]="over"
print(b)
