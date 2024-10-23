def search(nums, target):
	# Find the rotation point, then set the bounds for binary search
	l,r = 0,len(nums) - 1
	leftVal = nums[l]
	rightVal = nums[r]
	highestVal = -1
	lowestVal = -1

	while l <= r:
		c = l + (r - l) // 2
		if nums[c-1] > nums[c]: # Found it , c-1 is highest val and c is lowest
			highestVal = c-1
			lowestVal = c
			break
		elif nums[c] >rightVal:
			l = c + 1
		else:
			r = c -1

	if not l <= r:
		return -1

	if target <= rightVal:
		l, r = c, len(nums) -1
	else:
		l, r = 0, c - 1

	while l <= r:
		c = l + (r - l) // 2
		if nums[c] > target:
			r = c - 1
		elif nums[c] < target:
			l = c + 1
		else:
			return c







print(search([3,4,5,6,1,2],1)) # 4