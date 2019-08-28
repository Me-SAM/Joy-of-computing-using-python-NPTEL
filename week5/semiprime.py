a=[]
def isPrime(n): 
    if n <= 1 : 
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False
  
    return True
def printPrime(n): 
    for i in range(2, n + 1): 
        if isPrime(i):
        	a.append(i)
n=int(input()) 
printPrime(n)

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
