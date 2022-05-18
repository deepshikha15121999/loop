# i=1
# while i<=3:
#     x = input("enter the  password:")

#     if ('a' in x  or 'b' in x  or 'c' in x or 'd' in x or 'e' in x or 'f' in x or 'g' in x or 'h' in x or 'i' in x or 'j' in x or 'k' in x or 'l' in x or 'm' in x or 'n' in x or 'o' in x or 'p' in x or 'q' in x or 'r' in x or 's' in x or 't' in x or 'u' in x or 'v' in x or 'w' in x or 'x' in x or 'y' in x or 'z' in x ) and ('A' in x or 'B' in x or 'C' in x or 'D' in x or 'E' in x or 'F' in x or 'G' in x or 'H' in x or 'I' in x or 'J' in x or 'K' in x or 'L' in x or 'M' in x or 'N' in x or 'O ' in x or 'P' in x or 'Q' in x or 'R' in x or 'S' in x or 'T' in x  or 'U' in x or 'V' in x or 'W' in x or 'X' in x or 'Y' in x or 'Z'in x) and ('0'  in x or '1' in x or '2' in x or '3'in x or '4' in x or '5' in x or  '6' in x or '7' in x or '8' in x or '9' in x) and ('@'in x or '#'in x or '$'in x):
#         print('correct pasword')
#         break
#     else:
#         print('not correct password')
#     i=i+1

# p=input("enter password:")
# if p is 'A'or p is 'Z' and p is 'a' or p is 'z' and p is '0' or p is '9'and p is '@' or p is '!':
#     print("correct password:")
# else:
#     print('not correct password')


x = input("enter the  password:")
a='a','b','c','d','e','f','g'
# or'h'or'i'or'j'or 'k' or'l' or 'm'or'n'or 'o'or'p'or'q'or'r'or 's'or't'or'u'or'v'or'w'or'x'or'y'or'z'
b='1','2','3','4','5','6','7','8','9','0'
# b=1 or 2 or 3
c='A','B','C','D','E'
d='!','@','#'
i=0
while i<=len(x):
    if a[i] in x :
        if  b[i] in x 
            if c[i] in x 
                if d[i] in x:
    print('correct')
else:
    print('not correct')  


# x=input('enter no:-')
# if x=='Deep12@':
#     print('strong password')
# else:
#     print('not strong password')