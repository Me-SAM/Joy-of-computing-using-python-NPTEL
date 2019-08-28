import sympy

n=int(input())
a=list(sympy.primerange(2,n+1))
a.sort()
semiprime=[]
for i in a:
	for j in a:
		if i!=j:
			semiprime.append(i*j)
semiprime.sort()
semiprimes=[]
for num in semiprime:
	if num not in semiprimes:
		semiprimes.append(num)
sums=[]
for i in semiprime:
	for j in semiprime:
		sums.append(i+j)
sumof=[]
for num in sums:
	if num not in sumof:
		sumof.append(num)
		sumof.sort()

if n not in sumof:
	print('No',end="")
else:
	print('Yes',end="")
