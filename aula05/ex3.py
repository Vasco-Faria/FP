#exercicio 3
#jfernan@ua.pt

def inputFloatList():
	l=[]
	a=input("Introduza um número: ")
	while a!="":
		l.append(float(a))
		a=(input("Introduza um número: "))
		l.sort()
	return l




def CountLower(lst, v):
	sum=0
	for i  in range(len(lst)):
		if lst[i]<v:
			sum=sum+1
	return sum


def minimax(lst):
	min=lst[0]
	max=lst[0]
	for i in lst:
		if i >= max:
			max=i
		if i<=min:
			min=i
		m=(max+min)/2
	return min, max, m 
	

def main():
	v=float(input("Qual o valor de v? "))
	lst=inputFloatList()
	print(CountLower(lst,v))
	print(minimax(lst))
main()
