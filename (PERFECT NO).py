n=int(input('enter no:-'))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print('it is a perfect no')
else:
    print('it is not a perfect no')