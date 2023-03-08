#exercicio 5

l=str(input("Quais as equipas para os jogos?"))

def allmatches(l):
	x=list(l)
	jogos=[]
	for i in x:
		for j in x:
			if i!=j:
				continue
			jogos.append((l[i],l[j]))
	return jogos


print(allmatches(l))
