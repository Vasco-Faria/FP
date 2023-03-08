def main():
    with open("page3333.txt","r") as doc:
        dic={}
        for line in doc:
            for char in line:
                if char.isalpha():
                    char=char.lower()
                    if char not in dic:
                        dic[char]=1
                    else:
                        dic[char]+=1


    for k,v in sorted(dic.items(), reverse=True, key=lambda x:x[1]):
        print(k,":",v)
main()