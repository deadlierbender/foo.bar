#!/usr/bin/python

import math

def answer(n):
	bought = 0
	
	while n > 0:
		coins = n
		while math.modf(math.sqrt(coins))[0] != 0.0:
			coins -= 1
		bought += 1
		n -= coins
			
	return bought

print answer(160)
