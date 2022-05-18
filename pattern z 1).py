n=int(input('enter no:-'))
i=1
k=1
f=3
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end=' ')
        b=b+1
    j=1
    while j<=k:
        print('*',end=' ')
        j=j+1
    i=i+1
    k=k+2
    print()
i=1
k=1
f=3
while i<=n:
    t=1
    while t<=k:
        print(' ',end=' ')
        t=t+1
    p=1
    while p<=f:
        print('*',end =' ')
        p=p+1
    
    k=k+1
    i=i+1
    f=f-2
    print()
