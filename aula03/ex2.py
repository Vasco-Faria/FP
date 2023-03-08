#exercicio 4

import math

def poli(x):
	p=x**2+2*x+3
	return p



print("p(0)=", poli(0))
print("p(1)=", poli(1))
print("p(2)=", poli(2))
print("P(p(1))=", poli(poli(1)))
