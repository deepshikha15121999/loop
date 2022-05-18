n=int(input('enter no:-'))
num=n
if n<=9 and n>0:
    n=n**2
while n>9:
    sum=0
    while n!=0:
        b=n%10
        sum=sum+b**2
        n=n//10
    n=sum
if sum==1:
    print('happy no')
else:
    print('not happy no')