# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def addContact(dic):
    num=input("Qual o número de telémovel a adicionar: ")
    nome=input("Qual o Nome do contacto: ")
    if num in dic:
        print("Este número já se encontra registado")
    else:
        dic[num]=nome
        print ("Adicionado com sucesso")

def RemoveContact(dic):
    num=input("Qual o número que deseja remover: ")
    if num in dic:
        dic.pop(num)
    else:
        print("Esse número não existe")

def searchContact(dic):
    num=input("Qual o número que deseja procurar")
    if num in dic:
        nome=dic.get(num)
        print("Nome:", nome)
    else:
        print("Número não existe")


def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    d={}
    string=input("Letras: ")
    for num in contacts:
        nome=contacts.get(num)
        if string in nome:
            d[num]=nome
    listContacts(d)



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
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op=="A":
            addContact(contactos)
        elif op=="R":
            RemoveContact(contactos)
        elif op=="N":
            searchContact(contactos)
        elif op=="P":
            filterPartName(contactos)
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

