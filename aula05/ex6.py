#exercicio 6

s=input("Qual a string?")

def countDigits(s):
	list(s)
	c=0
	for a in s:
		if a.isdigit(s):
			c=c+1
	return c

print(countDigits(s))
