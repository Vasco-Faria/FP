def floatinput(prompt, mn=None, mx=None):

	while True:
		s=input(prompt)
		if isfloat(s):
			v=float(s)
			if mn==None or mx==None:
				return v
			if mn<v<mx:
				return v
