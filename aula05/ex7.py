#exercicio 7

s=str(input("Qual o nome?"))

def shorten(s):
	l=list(s)
	rs=""
	for a in l:
		if a.isupper():
			rs+=a
	return rs

print(shorten(s))
