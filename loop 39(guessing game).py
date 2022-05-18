i=0
while i<9:
    a=int(input('enter no:-'))
    if 1<=a<=9:
        if a>5:
            print('greater than 5')
        elif a<5:
            print('less than 5')
        elif a==5:
            print('winner')
    else:
        print('choose between 1 to 9')
        break
    i=i+1