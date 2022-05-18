n=int(input('enter  nno:-'))
num=n
while n>9:
    sum=0
    while n!=0:
        b=n%10
        n=n//10
        sum=sum+b
    n=sum
if n==1:
    print('magic no')
else:
    print('not magic no')

