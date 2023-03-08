#exercicio 6

X1=float(input("X1?"))
Y1=float(input("Y1?"))
X2=float(input("X2?"))
Y2=float(input("Y2?"))

c=math.sqrt((X1-X2)**2+(Y1-Y2)**2)
h=c**2+c**2
sin=c/h
ang=math.degrees(sin)

print("hipotenusa:",h)
print("Angulo:", ang , "º")
