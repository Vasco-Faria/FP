def endX(s):
   return endXa(s,"","")
def endXa(s,sx,cx):
   if s=="":
      return sx+cx
   c=s[0]
   if c=="x":
      return endXa(s[1:],sx,cx+c)
   return endXa(s[1:],sx+c,cx)