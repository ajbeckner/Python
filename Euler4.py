def numDigits(n):
	i = 1
	d = 0
	while (i <= n):
		i *= 10
		d += 1
	return d

def nthDigitFromBack(num,n):
	if (n > numDigits(num)): 
		return 0 
	return (num % (10 ** (n) ))/ (10 ** (n-1))

def nthDigitFromFront(num,n):
	if (n > numDigits(num)): 
		return 0 
	m = numDigits(num) - n + 1
	return nthDigitFromBack(num,m)


def isPalindrome(num):
	d = numDigits(num)/2
	if d == 0: return True
	for i in xrange(1,d+1):
		if not ((nthDigitFromBack(num,i) == nthDigitFromFront(num,i))):
			return False
	return True

m = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
    	n = i*j
    	if isPalindrome(n):
    		if (n > m):
    			m = n
print(m)