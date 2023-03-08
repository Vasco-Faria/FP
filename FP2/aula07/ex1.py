from encodings import utf_8
import sys
page3333=sys.argv


with open(page3333,"r",encoding="utf-8") as text:
    d={}
    char=text.read(1)
    while char:
        if char.isalpha():
            char=char.lower()
            d[char]=d.get(char,0)+1
        char=text.read(1)


for e in sorted(d):
    print(e,d[e])

        