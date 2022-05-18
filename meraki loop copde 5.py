i=1
sum=0
while i<=3:
    a=int(input('enter no:-'))
    sum=sum+a
    i=i+1
print(sum/3)
if (sum/3)%5==0:
    print('divisible')
else:
    print('not divisible')

