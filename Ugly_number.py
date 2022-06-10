def u(n,div):
    if n<=0:
        return 0
    while n%div==0:
           n//=div
    return n
n=int(input())
n=u(n,2)
n=u(n,3)
n=u(n,5)
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")