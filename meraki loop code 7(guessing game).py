i=0
while i<5:
    num=int(input('enter any number between 1 to 10:-'))
    if 1<=num<=10:
        if num==5:
            print('you won')
            break
        else:
            print('loose try again')
            i=i+1
    else:
        print('choose less then 10') 

        
    