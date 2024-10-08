def trap(heights):
	l = 0
	r = len(heights) - 1
	maxL = heights[l]
	maxR = heights[r]

	total_area = 0

	while l < r:
		if min(maxL, maxR) == maxL:
			l += 1
			area = maxL - heights[l]
			if area > 0:
				total_area += area
			maxL = max(maxL, heights[l])
		elif min(maxL, maxR) == maxR:
			r -= 1
			area = maxR - heights[r]
			if area > 0:
				total_area += area
			maxR = max(maxR, heights[r])
	return total_area







print(trap([0,2,0,3,1,0,1,3,2,1]))