#exercicio 8


s=float(input("Qual o valor booleano?"))

def ispalindrome(s):
	for i in range(len(s)/2+1):
		if s[i]!=s[-1*(i+1)]:
			return False
	return True




	i=0
	c=len(s)
	while true:
		if s[i]!=s[c-1]:
			return True
		if i>c/2+1:
			return False


print(ispalindrome(s))
