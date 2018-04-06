#recursive
def binary_recursive(arr, k , start=0, end=None):
	if end==None:
		end = len(arr)-1
	mid = (start+end)/2
	if arr[mid] == k:
		return mid
	elif arr[mid] < k:
		return binary_recursive(arr,k ,mid+1,end=None)
	else:
		return binary_recursive(arr, k , 0,mid-1)

def binary_recursive_last(arr, k , start=0, end=None):
	if end > start: return -1
	if end==None:
		end = len(arr)-1
	mid = (start+(end-start))/2
	print mid
	if arr[mid] == k and (mid==len(arr)-1 or arr[mid+1]>k):
		print "here",len(arr), arr[mid+1]
		return mid
	elif arr[mid] > k:
		return binary_recursive(arr,k ,0,mid-1)
	else:
		print "here2"
		print arr, k , 0,mid-1
		return binary_recursive(arr, k , mid+1,None)

#iterative
def binary_search(arr,k):
	start, end = 0, len(arr)-1
	while start <= end:
		mid = (start + end)/2
		if arr[mid] == k:
			return mid
		elif arr[mid] < k:
			start = mid + 1
		else:
			end = mid -1 



arr = [1,2,2,2,3,4,5,6,6,7]
k = 2

# print binary_search(arr,k)
# print binary_recursive(arr,k,0,None)
print binary_recursive_last(arr,k,0,None)