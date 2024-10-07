def maxArea(heights):
	l = 0
	r = len(heights) - 1
	max_area = (r - l) * min(heights[r],heights[l])
	while l < r:
		cur_area = 0
		if heights[l] > heights[r]:
			r -= 1
			cur_area = (r - l) * min(heights[r],heights[l])
		else:
			l += 1
			cur_area = (r - l) * min(heights[r],heights[l])
		max_area = max(cur_area,max_area)

	return max_area


print(maxArea([1,7,2,5,4,7,3,6]))