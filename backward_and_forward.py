#foo.bar - Backward and Forward

def answer(n):
	if n <= 2: return 2
	for b in range(2, n+1):
		x = ''; y = n
		while y:
			x = x + str(y % b); y /= b
		if x == x[::-1]: return b

print answer(10)
