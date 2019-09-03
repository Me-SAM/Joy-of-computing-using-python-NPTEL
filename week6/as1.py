n=int(input())
a=list(map(int,input().split()))
k=int(input())
sor=sorted(a)
pos=a[k-1]
if pos in sor:
  ind=sor.index(pos)+1
print(ind,end='')
