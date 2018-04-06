stri = 'ACVCBA'

count = {}
def count_string(stri):
	for s in stri:
		print s, count
		if s not in count.keys():
		    count[s] = 1
		else:
			count[s]+=1
			if count[s] >1:
				return s				
	return 'none'

print count_string(stri)
