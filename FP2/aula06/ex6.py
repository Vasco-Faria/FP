def comparefiles(file1,file2):
    with open(file1,"rb") as f1, open(file2,"rb") as f2:
        b1=f1.read(1024)
        b2=f2.read(1024)
        if (b1!=b2):
            return ("Different")
        elif (len(b1)==0)
            return ("Equal")
        

file1=input("Ficheiro 1: ")
file2=input("Ficheiro 2: ")
x=comparefiles(file1,file2)
print(x)

            
