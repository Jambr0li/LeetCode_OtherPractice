def twoSum(nums,t):
	pt1 = 0
	pt2 = len(nums) - 1
	curSum = 0;
	while pt1 < pt2:
		curSum = nums[pt1] + nums[pt2]
		if curSum > t:
			pt2 -= 1
		elif curSum < t:
			pt1 += 1
		elif curSum == t:
			return [pt1 + 1, pt2 + 1]	


print(twoSum([1,2,3,4],3)) # should return [1,2]	