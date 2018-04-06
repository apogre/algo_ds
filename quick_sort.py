import sys

def partition(arr, start, end):
	pivot = arr[end]
	i = start -1
	for j in range(start,end):
		print arr, i , j
		if arr[j] <= pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1] , arr[end] = arr[end], arr[i+1]
	print arr
	return i+1

def quick_sort(arr, start, end):
	if start < end:
		pi = partition(arr,start, end)
		print pi
		quick_sort(arr,start, pi-1)
		quick_sort(arr,pi+1,end)
	print arr

arr = [10, 80, 30, 90, 40, 50, 70]
n = len(arr)
print quick_sort(arr, 0, n-1)
