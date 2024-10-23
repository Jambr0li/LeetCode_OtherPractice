def lengthOfLongestSubstring(s):
	# if len(s) == 1:
		# return 1
	s = list(s)
	start = -1
	maxL = 0
	letter_map = {}
	for i,l in enumerate(s):
		if l in letter_map:
			start = max(start,letter_map[l])
		maxL = max(maxL,i - start)
		letter_map[l] = i
		print(letter_map)
		print(maxL)
	return maxL



# print(lengthOfLongestSubstring("zxyzxyz"))
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("b"))
# print(lengthOfLongestSubstring("au"))
# print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("abba"))
