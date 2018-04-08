def missing(arr):
	max_val = 100
	i = 0
	for i in range(len(arr)-1):
		if arr[i+1] - arr[i] == 1: continue
		elif arr[i+1] - arr[i] > 2:
			print arr[i]+1,"-",arr[i+1]-1
		else:
			print arr[i]+1


arr = [1,2,3,5,50,88,90]

print missing(arr)