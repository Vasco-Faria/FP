#exercicio 5

litros=float(input("Quantidade de litros: "))

gasolina=1.40
if litros<40:
	preço=gasolina*litros
	print("Preço a pagar: ", preço)
else:
	preço=(gasolina*litros)*0.90
	print("Preço a pagar: ", preço)
