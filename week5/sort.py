def sorting(a):
	n=len(a)
	count=0
	for i in range(n):
		for j in range(0,n-i-1):
			if(a[j]>a[j+1]):
				a[j],a[j+1]=a[j+1],a[j]
				count+=1
	print(count)


a=list(map(int,input().split()))
sorting(a)
