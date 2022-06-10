n=int(input())
while(len(str(n))>1):
    n=int(n)
    c=0
    while n>0:
        re=n%10
        c+=re**2
        n//=10
    if c>9:
        n=c
if c==1 or c==7:
    print("True")
else:
    print("False")

        
        