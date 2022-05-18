# num=int(input('enter any number:-'))
# i=1
# bus=0
# while i<=num:
#     if num%i==0:
#         bus=bus+1
#     i+=1
# if bus==2:
#     print('prime number')
# else:
#     print('not a prime number')


 
# HOW MANY PRIME NO BETWEEN 1 TO 100



b=int(input('enter no:-'))
a=1
while a<=b:
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
        print(a,'is prime no its square is',a**2)
    a=a+1


# OUTPUT SHOULD BE PRIME NO AND ITS PERFECT NO


# b=int(input('enter no:-'))
# a=1
# while a<=b:
#     i=1
#     count=0
#     while i<=a:
#         if a%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print(a,'is prime no')
#     a=a+1
# j=1
# while j<=b:
#         if b%j==0:
#             print(j)
#         j=j+1


