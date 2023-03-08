#exercicio 4

segT=int(input("Quantos segundos? "))

h=segT//3600
m=(segT%3600)//60
s=(((segT%3600)%60)%60)

print("{:02d}:{:02d}:{:02d}".format(h, m, s))
