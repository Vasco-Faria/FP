#Neste programa utilizamos o método bissect_left que analisa a posição do elemento que começa com com o argumento dado e devolve a posição anterior
#Caso o elemento não exista, ele devolve a posição anterior a onde o elemento se inseria
#Por exemplo: Carlos, Maria bisect.bisect_left(lst,"Daniel",0,len(lst)) devolve a posição do Carlos, porque o Daniel ficaria entre o Carlos e a Maria
#_left devolve o elemento (se existir), _right, o seguinte

#O método .startswith(arg) verifica se a palavra começa pelo argumento inserido

import bisect

def main():
    with open("words.txt", "r") as f:
        lst=[]
        for line in f:
            lst.append(line.strip())
        ea=bisect.bisect_left(lst,"ea",0,len(lst))
        eb=bisect.bisect_left(lst,"eb",0,len(lst))
        print("Há {} palavras começadas por ea, na lista words.txt".format(eb-ea))
        
        tb=bisect.bisect_left(lst,"tb",0,len(lst))
        print(tb)
        print(lst[tb-1])
        print(lst[tb])
        print(lst[tb+1])
        print(bisect.bisect_left(lst,"tc",0,len(lst)))



#O programa começa aqui
main()
