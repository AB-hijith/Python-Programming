def fib(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fib(int(input("enter limit: ")))
