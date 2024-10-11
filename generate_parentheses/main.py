def generateParenthesis(n):
	stack = []
	result = []

	def addparenthesis(openN, closedN):
		if openN == closedN == n:
			result.append("".join(stack))
			return

		if openN < n:
			stack.append("(")
			addparenthesis(openN + 1, closedN)
			stack.pop()

		if openN > closedN:
			stack.append(")")
			addparenthesis(openN, closedN + 1)
			stack.pop()

	addparenthesis(0,0)
	return result


print(generateParenthesis(3))


# n = 1	
# ["()"]

# n = 2
# ["(())","()()"]

# n = 3
# ["((()))","(()())","(())()","()(())","()()()"]



