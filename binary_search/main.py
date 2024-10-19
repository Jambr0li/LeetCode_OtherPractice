def search(nums, target):

	l, r = 0, len(nums) - 1

	while l <= r:
		c = l + (r - l) // 2
		if nums[c] < target:
			l = c + 1
		elif nums[c] > target:
			r = c - 1
		else:
			return c
	return -1



# print(search([-1,0,2,4,6,8], 4))
# print(search([-1,0,2,4,6,8], 3))
print(search([-1,0,3,5,9,12], 9))
