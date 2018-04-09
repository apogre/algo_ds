def fibo(num):
	if num <= 2: return 1
	else:
		return fibo(num-1)+fibo(num-2)


print fibo(3)
