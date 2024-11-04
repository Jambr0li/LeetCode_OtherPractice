# [11:07 AM] Sigvartson (US), Cody J
'''
Given an n×n matrix, find the maximum sum of an n/2 × n/2 submatrix in the upper-left corner.
 
You are allowed to reverse any rows or columns to maximize the sum.
 
For example, if given a 4×4 matrix, you want to find the maximum possible sum of the 2×2 matrix in the top-left corner after flipping rows or columns.
''' 

# [1,1,4,1]
# [1,1,1,4]
# [1,1,1,4]
# [1,1,1,4]

# [1,1,4,1,1,1]
# [1,1,4,1,1,1]
# [1,1,4,1,1,1]
# [1,1,4,1,1,1]
# [1,1,4,1,1,1]
# [1,1,4,1,1,1]


def maxUpperLeftSubmatrixSum(matrix):
	total = 0
	dim = len(matrix) - 1	
	for r in range(0, dim // 2 + 1):
		for c in range(0, dim // 2 + 1):
			val = max(matrix[r][c],matrix[r][dim - c],matrix[dim-r][c], matrix[dim-r][dim-c])
			print(val)
			total += val
	return total

print(maxUpperLeftSubmatrixSum([[1,1,4,1], [1,1,1,4], [1,1,1,4],[1,1,1,4]]))
print(maxUpperLeftSubmatrixSum([[1,1,4,1,1,1],[1,1,4,1,1,1],[1,1,4,1,1,1],[1,1,4,1,1,1],[1,1,4,1,1,1],[1,1,4,1,1,1]]))
 
 