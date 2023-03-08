list=[]
def primeUpto(num):
    for i in range(2,num+1):
        list.append(i)
    print(list)
    for x in list:
        for y in list:
            if x!=y:
                if y%x==0:
                    list.pop(list.index(y))
    print(list)



def main():
    print()
    num = int(input("Qual o número máximo? "))
    primeUpto(num)
main()