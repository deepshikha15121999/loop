a=int(input('enter no:-'))
b=int(input('enter no:-'))
sum1=0
sum2=0
while a<=b:
    if a%2==0:
        sum1=sum1+a
    else:
        sum2=sum2+a
    a=a+1
print(sum1)
print(sum2)
