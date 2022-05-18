n=int(input('enter no:-'))
i=1
while i<=n:
    b=i**2
    print(b)
    i=i+1


sa='javascriptloops'
i=0
i2=0
d=''
while i<len(sa):
    if sa[i]=='a'or sa[i]=='e'or sa[i]=='i'or sa[i]=='o'or sa[i]=='u'or sa[i]=='A'or sa[i]=='E'or sa[i]=='O'or sa[i]=='I'or sa[i]=='U':
        # print(sa[i])
        e=d+sa[i]
        print(e)
    i=i+1
while i2<len(sa):
    if sa[i2]=='a'or sa[i2]=='e'or sa[i2]=='i'or sa[i2]=='o'or sa[i2]=='u'or sa[i2]=='A'or sa[i2]=='E'or sa[i2]=='O'or sa[i2]=='I'or sa[i2]=='U':
        pass
    else:
        print(sa[i2])
    i2=i2+1
   