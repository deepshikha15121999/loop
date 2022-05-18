a=int(input('enter no:-'))
sum=0
num=a
while a!=0:
    b=a%10
    a=a//10
    sum=sum+(b**3)
if sum==num:
    print('it is armstrong')
else:
    print('it is not armstrong')

