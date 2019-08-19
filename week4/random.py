from random import randint
n=int(input())
a=list(map(int,input()))
for i in range(n-1):
	a.append(int(input()))
a.sort()
print(*a,end="")
