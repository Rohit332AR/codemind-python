def pal(n):
    k=n
    r=0
    while n!=0:
        s=n%10
        r=r*10+s
        n//=10
    if k==r:
        return 1
    else:
        return 0
n=int(input())
x=n+1
for i in range(n-1,1,-1):
    if pal(i):
        a=i
        break
while x!=0:
    if pal(x):
        b=x
        break
    x+=1
y=n-a
z=b-n
if y==z:
    print(a,b)
elif y>z:
    print(b)
else:
    print(a)