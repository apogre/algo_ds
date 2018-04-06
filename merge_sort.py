def merge_sort(arr):
	if len(arr) < 2: return arr
	mid = len(arr)/2
	left = merge_sort(arr[0:mid])
	right = merge_sort(arr[mid:])
	new_arr = merge(arr, left, right)
	return new_arr


def merge(arr,left, right):
	new_arr = []
	i, j = 0, 0
	while len(new_arr) < (len(left) + len(right)):
		if left[i] <= right[j]:
			new_arr.append(left[i])
			i+=1
		elif left[i] >= right[j]:
			new_arr.append(right[j])
			j+=1
		if i==len(left) or j==len(right):
			new_arr.extend(left[i:] or right[j:])
			return new_arr

arr = [2,1,3,1,2]

result = merge_sort(arr)
print result