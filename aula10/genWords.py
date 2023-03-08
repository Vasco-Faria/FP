
# Generates all length-3 words with symbols taken from the given alphabet.
def genWords3(symbols):
    return [ x+y+z for x in symbols for y in symbols for z in symbols ]


# Generates all length-n words with symbols taken from the given alphabet.
def genWords(symbols, n):
    assert (n>0)
    if n==1:
        return [c for c in symbols]
    else:
        lst=genWords(symbols,n)
        newlist=[]
        for i in symbols:
            for x in lst:
                newlist.append(i+x)
        return newlist

def genWordsRecursive(symbols,n):
    assert(n>0)
    if n==1:
        return [c for c in symbols]
    else:
        lst=genWordsRecursive(symbols,n-1)
        return[c+p for c in symbols for p in lst]


        

def main():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("01", 4)  # should return all length-4 binary words
    print(lstC)

if __name__ == "__main__":
    main()

