def longestConsecutive(nums):
	num_set = set(nums)
	longest = 0

	for n in nums:
		if n - 1 not in num_set:
			length = 1
			while n + length in num_set:
				length += 1
			longest = max(longest, length)
	return longest



# print(longestConsecutive([2,20,4,10,3,4,5]))
print(longestConsecutive([0,-1]))

