n=int(input('enter no:-'))
s=''
while n!=0:
    b=n%2
    s=s+str(b)
    n=n//2
    # print(b,end='')
print(s[::-1])
