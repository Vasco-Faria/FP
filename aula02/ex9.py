#exericio 9 

nCTP= float(input("Nota de CTP: "))
nCP= float(input("Nota de CP: "))

nF=int((nCTP*0.36)+(nCP*0.64))

if nCTP<6.5 or nCP <6.5:
	print("Código 66")
elif nF>=10 and nF<=20:
	print("Nota final: ", nF)
else:
	nATPR=float(input("Nota de ATPR: "))
	nAPR=float(input("Nota de APR: "))
	nFinal=int(36% max(nCTP, nATPR)+ 64% max(nCP, nAPR))
	print("Nota final: ", nFinal)

