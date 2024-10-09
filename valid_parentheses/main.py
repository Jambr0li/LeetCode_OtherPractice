def isValid(s):
	stack = []
	par = list(s)

	for parenth in par:
		if parenth == '{' or parenth == '(' or parenth == '[':
			stack.append(parenth)
		else:
			if parenth == '}' and len(stack) > 0 and stack[-1] == '{':
				stack.pop()
			elif parenth == ']' and len(stack) > 0 and stack[-1] == '[':
				stack.pop()
			elif parenth == ')' and len(stack) > 0 and stack[-1] == '(':
				stack.pop()
			else:
				return False
	if len(stack) != 0:
		return False
	return True

print(isValid("{}"))
print(isValid("[]"))
print(isValid("(){}]"))
