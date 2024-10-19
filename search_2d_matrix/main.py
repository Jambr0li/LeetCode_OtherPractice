def searchMatrix(matrix, target):
	ROWS, COLS = len(matrix), len(matrix[0])

	t, b = 0, ROWS - 1
	while t <= b:
		row = t + (b - t) // 2
		if target > matrix[row][-1]:
			t = row + 1
		elif target < matrix[row][0]:
			b = row - 1
		else:
			break

	if not (t <= b):
		return False

	l, r = 0, COLS - 1
	while l <= r:
		c = l + (r - l) // 2
		if matrix[row][c] > target:
			r = c - 1
		elif matrix[row][c] < target:
			l = c + 1
		else:
			return True
		print("bot")
	return False




# print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
# print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# print(searchMatrix([[1],[3]], 3))
