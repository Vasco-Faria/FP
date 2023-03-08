
# Complete este programa como pedido no guião da aula.

def listContacts(dic):
	"""Print the contents of the dictionary as a table, one item per row."""
	print("{:>12s} : {:^30}: {:<20}".format("Numero", "Nome", "Morada"))
	for num in dic:
		print("{:>12s} : {:^30}: {:<20} ".format(num, dic[num][0], dic[num][1]))

def filterPartName(contacts):
	"""Returns a new dict with the contacts whose names contain partName."""
	string=input("letras: ")
	newdic = {}
	for numero in contacts:
		nome=contacts.get(numero)
		if string in nome:
			newdic[numero]=nome
	listContacts(newdic)
		



def findContact(dic):
	numero=input("Qual o numero que deseja procurar")
	if numero in dic:
		nome=dic.get(numero)
		print("Nome:", nome)
	else:
		print("Contacto nao existe") 

	

def addContact(dic):
	print("Preencha os dados corretamente, para adicionar um contacto à sua lista.")
	nome = input("Nome: ")
	numero = input("Numero: ")
	adress=input("Morada? ")
	if numero in dic:
		print("Numero já existe")
	else:
		dic[numero]=(nome, adress)
		print("Numero adicionado com sucesso")


def removeContact(dic):
	numero=input("Qual o número que deseja eliminar? ")
	if numero in dic:
		dic.pop(numero)
	else:
		print("O numero não se encontra na lista")
	

def menu():
	"""Shows the menu and gets user option."""
	print()
	print("(L)istar contactos")
	print("(A)dicionar contacto")
	print("(R)emover contacto")
	print("Procurar (N)úmero")
	print("Procurar (P)arte do nome")
	print("(T)erminar")
	op = input("opção? ").upper()   # converts to uppercase...
	return op


def main():
	"""This is the main function containing the main loop."""

	# The list of contacts (it's actually a dictionary!):
	contactos = {"234370200": ("Universidade de Aveiro","Santiago,Aveiro"),
		"727392822": ("Cristiano Aveiro", "Aveiro"),
		"387719992": ("Maria Matos", "Porto"),
		"887555987": ("Marta Maia", "Viana do Castelo"),
		"876111333": ("Carlos Martins", "Rua da Fonte Grossa, Viana do Castelo"),
		"433162999": ("Ana Bacalhau", "Amén")
		}

	op = ""
	while op != "T":
		op = menu()
		if op == "A":
			addContact(contactos)
		elif op == "T":
			print("Fim")
		elif op =="R":
			removeContact(contactos)
		elif op=="N":
			findContact(contactos)
		elif op == "L":
			print("Contactos:")
			listContacts(contactos)
		elif op=="P":
			filterPartName(contactos)
		else:
			print("Não implementado!")
	

# O programa começa aqui
main()

