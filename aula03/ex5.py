#exercicio 5
r=float(input("Qual o valor de r: "))
def tax(r):
	if r<= 1000:
		tx=0.1*r
	elif r>1000 and r<=2000:
		tx=0.2*r-100
	else:
		tx=0.3*r-300
	return tx


print("tax(",r,")= ",tax(r))
