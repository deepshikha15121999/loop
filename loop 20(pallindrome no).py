n=int(input('enter no:-'))
num=n
pal=""
while n!=0:
    b=n%10
    n=n//10
    pal+=str(b)
if int(pal)==num:
    print('number is pallindrome no')
else:
    print('it is not a pallindrome no')
