def findMin(nums):
	if len(nums) == 1:
		return nums[0]
	l, r = 0, len(nums) - 1

	while l <= r:
		c = l + (r - l) // 2

		if nums[c-1] > nums[c]:
			return nums[c]
		elif nums[c] > nums[r]: # move right
			l = c + 1
		else:
			r = c - 1


print(findMin([3,4,5,6,1,2]))
print(findMin([4,5,0,1,2,3]))
print(findMin([4,5,6,7]))
