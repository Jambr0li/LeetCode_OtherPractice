def generateParenthesis(n):
	stack = []
	result = []

	def add_par(openN, closedN):
		if openN == closedN == n:
			result.append("".join(stack))
			return

		if openN < n:
			stack.append("(")
			add_par(openN + 1, closedN)
			stack.pop()

		if openN > closedN:
			stack.append(")")
			add_par(openN, closedN + 1)
			stack.pop()
	add_par(0,0)
	return result
print(generateParenthesis(3))


# n = 1	
# ["()"]

# n = 2
# ["(())","()()"]

# n = 3
# ["((()))","(()())","(())()","()(())","()()()"]



