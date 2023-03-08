#exercicio 8

def countdown(n):
	print(n)
	if (n > 0):
		countdown(n-1)

n = int(input("Introduza o valor de n: "))
countdown(n)
