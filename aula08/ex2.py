def main():
    with open("names.txt", "r", encoding="utf8") as f:
        dic={}
        f.readline()
        for line in f:
            names=line.strip().split(" ")
            lastname=names[len(names)-1]
            if lastname not in dic:
                dic[lastname]=[names[0]]
            else:
                if names[0] not in dic[lastname]:
                    dic[lastname].append(names[0])
    for x in dic:
            print(x,":",dic[x])

print("Lista dos nomes")
main()
