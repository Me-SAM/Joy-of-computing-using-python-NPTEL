n,v1,v2=(map(int,input().split()))
d_cab=2*n
d_arun=(2**(1/2))*n
time_cab=d_cab/v2
time_arun=d_arun/v1
if(time_arun<time_cab):
	print('walk',end="")
else:
	print('cab',end="")