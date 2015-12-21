import checks

num = 600851475143

for i in xrange(1,num+1):
	if (not(num%i)):
		if(checks.isPrime(num/i)):
			print(num/i)
			break
	