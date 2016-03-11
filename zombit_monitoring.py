#!/usr/bin/python

def answer(intervals):
	normalized = []; observed = 0
	
	if any(isinstance(i,list) for i in intervals):
		for shift in intervals:
			for timestamp in shift:
				normalized.append(timestamp)
	else:
		normalized = intervals
	normalized = set(normalized); normalized = list(normalized)
	normalized.sort(); normalized.reverse()
	print normalized
	while normalized:
		if len(normalized) == 1: break
		temp = normalized[0]; del normalized[0]
		observed += (temp - normalized[0])
	return observed 
	
print answer([[1,3],[3,6]])
