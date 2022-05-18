a=int(input('enter binary no 0 and 1 only:-'))
i=0
sum=0
while a!=0:
    b=a%10
    a=a//10
    sum=sum+b*(2**i)
    i=i+1
print(sum)
