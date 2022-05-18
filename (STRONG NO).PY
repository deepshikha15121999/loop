n=int(input('enter no:-'))
num=n
sum=0
while n!=0:
    b=n%10
    n=n//10
    j=1
    c=b
    while (b-j)!=0: 
        c=c*(b-j)
        j=j+1
    sum=sum+c
if sum==num:
    print('strong no')
else:
    print('not strong')


    


