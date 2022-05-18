n=int(input('enter no:-'))
num=n
sum=0
while n!=0:
    b=n%10
    n=n//10
    sum=sum+b
if num%sum==0:
    print('harshad no')
else:
    print('not harshad no')