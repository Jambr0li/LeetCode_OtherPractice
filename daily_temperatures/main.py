def dailyTemperatures(temperatures):
	stack = [] #[temp,index]
	res = [0] * len(temperatures)

	for i, t in enumerate(temperatures):
		while stack and t > stack[-1][0]:
			stackT,stackInd = stack.pop()
			res[stackInd] = (i - stackInd)
		stack.append([t, i])
	return res


print(dailyTemperatures([22,21,20]))
print(dailyTemperatures([30,38,30,36,35,40,28]))
