import sequences

i = 0
f = sequences.fib(i)
s = 0
while(f < 4000000):
	if not f%2:
		s = s + f
	i = i + 1
	f = sequences.fib(i)
print(s)