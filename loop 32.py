n=int(input('enter no:-'))
i=1
sum=0
while i<=n:
    if i%2==0:
        b=i*i
        print(b)
        sum=sum+b
    else:
        b=(-1)*i*i
        print(b)
        sum=sum+b
    i=i+1
print('sum is:-',sum)
