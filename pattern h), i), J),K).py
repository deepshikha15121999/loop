# QIUESTION H)

n=int(input('enter no:-'))
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(' ',end=' ')
        b=b+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i+1
    print()

# QUESTION I)

# n=int(input('enter no:-'))
# i=1
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(' ',end=' ')
#         b=b+1
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     i=i+1
#     print()

# QUESTION J)


# n=int(input('enter no:-'))
# i=1
# k=5
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(' ',end=' ')
#         b=b+1
#     j=5
#     while j>=k:
#         print(j-(n-i),end=" ")
#         j=j-1
#     k=k-1
#     i=i+1
#     print()

# QUESTION K IS SIMILAR TO J WHEN WE DELETE THE (B=1 WHILE J>=K) PORTION 
n=int(input('enter no:-'))
i=1
k=5
while i<=n:
    # b=1
    # while b<=n-i:
    #     print(' ',end=' ')
    #     b=b+1
    j=5
    while j>=k:
        print(j-(n-i),end=" ")
        j=j-1
    k=k-1
    i=i+1
    print()