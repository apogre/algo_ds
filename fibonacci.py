def fibo(num):
	if num <= 1: return 1
	else:
		return fibo(num-2)+fibo(num-2)


for i in range(20):
	print fibo(i)
