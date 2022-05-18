# b=input('enter no:-')
# i=0
# s=""
# while i<len(b):
#     if b[i]=="1":
#         s+="one"
#     if b[i]=="2":
#         s+="two"
#     if b[i]=="3":
#         s+="three"
#     if b[i]=="4":
#         s+="four"
#     if b[i]=="5":
#         s+="five"
#     if b[i]=="6":
#         s+="six"
#     if b[i]=="7":
#         s+="seven"
#     if b[i]=="8":
#         s+="eight"
#     if b[i]=="9":
#         s+="nine"
#     if b[i]=="0":
#         s+="zero"
#     i+=1
# print(s)

# OR


a=int(input('enter no:-'))
s1=""
while a!=0:
    d=a%10
    s1+=str(d)
    a=a//10
f=int(s1)
s=''
while f!=0:
    b=f%10
    f=f//10
    if b==1:
        s+="one "
    if b==2:
        s+="two"
    if b==3:
        s+="three"
    if b==4:
        s+="four"
    if b==5:
        s+="five"
    if b==6:
        s+="six"
    if b==7:
        s+="seven"
    if b==8:
        s+="eight"
    if b==9:
        s+="nine"
    if b==0:
        s+="zero"
print(s)
    


    
    