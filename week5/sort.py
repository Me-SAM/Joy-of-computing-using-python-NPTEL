a=list(map(int,input().split()))
x1=sorted(a)
c=0
for i in range(len(a)):
    if a[i]==x1[c]:
        c=c+1
print(len(a)-c,end="")
