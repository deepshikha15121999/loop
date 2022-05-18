# SUM OF ALL PRIME NO

# num=int(input('enter any no:-'))
# a=1
# sum=0
# while a<=num:
#     i=1
#     count=0
#     while i<=a:
#         if a%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         sum=sum+a
#     a=a+1
# print(sum)

# POSITION OF PRIME NO

b=int(input('enter no:-'))
a=1
j=1
while a<=b:
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("position of ",a,'is',j)
        j=j+1
    a=a+1

