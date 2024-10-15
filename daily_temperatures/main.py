def dailyTemperatures(temperatures):
	stack = []
	result = [0] * len(temperatures)
	for i,t in enumerate(temperatures):
		while stack and stack[-1][1] < t:
			stackInd, stackTemp = stack.pop()
			result[stackInd] = i - stackInd
		stack.append([i,t])
	return result



print(dailyTemperatures([30,38,30,36,35,40,28]))
