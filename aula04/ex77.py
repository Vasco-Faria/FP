#exercicio 7


c=0
sum=0
s=""
while s!="":
	s=input("number?")
	if s=="":
		break
	c=c+1
	sum=sum+ float(s)
	
if c==0:
	print("Nao inseriu nada")
else:
	avg=sum/c
	print("avg;", avg)
 

#-----------------------

def frankenstein():
	l=[]
	c=0
	sum=0
	s=""
	while s!="":
		s=input("number?")
		if s=="":
			break
		c=c+1
		sum=sum+ float(s)
		
	if c==0:
		print("Nao inseriu nada")
	else:
		avg=sum/c
		print("avg;", avg)
 
	return l, c, sum
	
	
l,c,sum=frankenstein()
