M,Q=0,1
t=[["coal",30],["rice",50],["iron",5],["rice",42],["coal",45]]
def cargoQuantity(t,m):
    q=0
    for i in t:
        if i[M]==m:
            q+=i[Q]
    return q
def fd(t,m):
    lst=[]
    for i in t:
        if i[M]==m:
            lst.append([i[M],i[Q]])
    return lst


def main():  
    m=input("Qual o tipo de mercadoria: ")
    print(fd(t,m))
    print(cargoQuantity(t,m))

main()