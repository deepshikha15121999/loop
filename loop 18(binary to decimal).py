bin=int(input('enter no:-'))
i=0
sum=0
while bin!=0:
    c=bin%10
    bin=bin//10
    sum=sum+c*(2**i)
    i=i+1
print(sum)