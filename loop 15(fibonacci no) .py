x=int(input('enter no :-'))
i=0
a=0
b=1
print(a,end=" ")
print(b,end=" ")
c=a+b
while i<x-2 :
    # print(c,end= '  ')
    a=b
    b=c
    print(c,end= '  ')
    c=a+b
    i=i+1

