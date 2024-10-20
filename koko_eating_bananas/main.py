import math

def minEatingSpeed(piles, h):
	l, r = 1, max(piles)
	res = r

	while l <= r:
		k = (l + r) // 2

		totalTime = 0
		for p in piles:
			totalTime += math.ceil(float(p) / k)
		if totalTime <= h:
			res = k
			r = k - 1
		else:
			l = k + 1
	return res


print(minEatingSpeed([1,4,3,2], 9))
# print(minEatingSpeed([312884470],312884469))
