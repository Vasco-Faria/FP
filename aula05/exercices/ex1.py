
def inputFloatList():
    list=[]
    numero=input("Qual o número a adicionar á lista?  ")
    while numero != "":
        list.append(float(numero))
        numero=(input("Qual o número a adicionar á lista?  "))
        list.sort()
    return list


def countLower(lst, v):
    x=0
    for i in range(len(lst)):
        if lst[i]<v:
            x+=1
    return x


def minmax(lst):
    min=lst[0]
    max=lst[0]
    for i in lst:
        if i<=min:
            min = i
        elif i>=max:
            max=i   
    m =(max+min)/2
    x=0
    for i in range(len(lst)):
        if lst[i]<m:
            x+=1
    return max, min, m , x

            




def main():
    v=float(input("Qual o valor de v?  "))
    lst=inputFloatList()
    print(lst)
    print(countLower(lst,v))
    print("Média da lista= ", minmax(lst)[2])
    print("Valores da lista mais baixos que a média= ", minmax(lst)[3])

   


main()