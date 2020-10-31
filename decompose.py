def decompose(n):
	i=0
	while  i<n:
		a=i*i-i+64
		print(a%n)
		i+=1


decompose(7)