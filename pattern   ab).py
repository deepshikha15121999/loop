# QUESTION OF (AB)

n=int(input('enter no:-'))
i=1
z=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end=' ')
        b=b+1
    j=1
    while j<=z:
        print(i,end=' ')
        j=j+1
    z=z+2
    i=i+1
    print()

