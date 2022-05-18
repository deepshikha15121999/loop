i=1
e=''
o=''
while i<10:
	if i%2==0:
		e+=str(i)
		e+='\n'
	else:
		o+=str(i)
		o+='\n'
	i+=1
print('even')
print(e)
print('odd')
print(o)