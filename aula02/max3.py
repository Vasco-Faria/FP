#exercicio 3 

x1=float(input("Number: "))
x2=float(input("Number: "))
x3=float(input("Number: "))

if x1>x2 and x1>x3:
	print("Maximum",x1)
elif x2>x3 and x2>x1:
	print("Maximum",x2)
else:
	print("Maximum",x3)
