#!/usr/bin/python

def answer(x):
	x = set(x); x = list(x)
	for key in x:
		for value in enumerate(x):
			if key == value[1]: continue
			if key[::-1] == value[1]: del x[value[0]]
	return len(x)
