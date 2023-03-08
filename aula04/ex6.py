#exercicio 6





n=int(input("Qual a quantidade de termos:"))
pi= ((-1)**n)/(2*n+1)

def leibnizPi4(n):
	while n>=0:
		pi=pi+((-1)**n)/2*n+1
		n-=1


print("A soma dos primeiros termos é: ", pi) 
