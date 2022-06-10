a,b=map(int,input().split())
while a%b!=0:
    re=a%b
    a=b
    b=re
print(b)