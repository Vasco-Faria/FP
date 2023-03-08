from tkinter import filedialog
from tokenize import Name
from unicodedata import name

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    # name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File")    #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(name):
    total=0
    with open(name) as numbers:
        for line in numbers:
            total+=float(line)
    return total


if __name__ == "__main__":
    main()

