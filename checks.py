def isPrime(n):
	for i in xrange(2,int(n**.5)+1):
		if (not n % i): return False
	return True