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

def binary_recursive_last(arr, k , start, end, n):
	if end <= start: return -1
	mid = start+(end-start)//2
	print "mid==>", mid
	if arr[mid] == k and (mid==n-1 or arr[mid+1]>k):
		print "here1"
		return mid
	elif arr[mid] > k:
		return binary_recursive(arr,k ,0,mid-1,n)
	else:
		print "here"
		return binary_recursive(arr, k , mid+1,end,n)

def last(arr, low, high, x, n) :
    if (high >= low) :
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) :
            return mid
        elif (x < arr[mid]) :
            return last(arr, low, (mid - 1), x, n)
        else :
            return last(arr, (mid + 1), high, x, n)
             
    return -1

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



arr = [1,2,2,3,4,5,6]
k = 2
n = len(arr)-1

# print binary_search(arr,k)
# print binary_recursive(arr,k,0,None)
print binary_recursive_last(arr,k,0,n,n)
# print last(arr, 0, n, k, n)