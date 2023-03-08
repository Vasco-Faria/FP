#exercicio 3

x=int(input("Escolha um número: " ))
y=int(input("Escolha um segundo número: "))



def max2(x,y):
	if x>y:
		return x
	else:
		return y


print("O número maior é", max(x,y))

z=int(input("Escolha um terceiro número: "))


def max3(x,y,z):
	if z>max2(x,y):
		return z
	else:
		return max2(x,y)


print("O número maior é", max3(x,y,z))
