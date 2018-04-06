def quick_sort(arr, start, end):
	if start < end:
		pi = partition(arr, start, end)
		quick_sort(arr,0,pi-1)
		quick_sort(arr,pi+1,end)
	return arr

def partition(arr, start, end):
	pivot = arr[end]
	i = start - 1
	for j in range(start,end):
		if arr[j] <= pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return i+1

arr = [1,4,2,5,8,3,4]
n = len(arr)
print quick_sort(arr,0,n-1) 