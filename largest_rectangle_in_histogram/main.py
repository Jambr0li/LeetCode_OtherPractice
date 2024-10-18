def largestRectangleArea(heights):
	maxArea = 0
	stack = []
	for i, h in enumerate(heights):

		if stack and len(stack) > 0 and stack[-1][0] > h:
			while len(stack) > 0 and stack[-1][0] > h:
				latest_H, latest_I = stack.pop()
				length = i - latest_I
				maxArea = max(maxArea, latest_H * length)
			stack.append((h,latest_I))
		else:
			stack.append((h,i))

	for (h, i) in stack:
		maxArea = max(maxArea, (len(heights) - i) * h)

	return maxArea

print(largestRectangleArea([7,1,7,2,2,4]))
# print(largestRectangleArea([2,1,5,6,2,3]))