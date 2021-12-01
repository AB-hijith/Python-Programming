l=input("Enter values separated by space:")
b=l.split()
a=list(map(int, b))
for i in a:
    if i%2!=0:
    	print(i)        
        
