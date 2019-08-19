r,c=map(int,input().split())
k=1
for i in range(r):
	for j in range(c-1):
		print(k,end=" ")
		k+=1
	print(k)
	k+=1
