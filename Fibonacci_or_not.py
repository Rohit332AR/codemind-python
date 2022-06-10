def fib(n):
    a=0
    b=1
    i=3
    while True:
        c=a+b
        a=b
        b=c
        if c==n:
            print("True")
            break
        elif c>n:
            print("False")
            break
n=int(input())
fib(n)