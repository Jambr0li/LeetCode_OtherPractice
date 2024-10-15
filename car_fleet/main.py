def carFleet(target, position, speed):
	pairs = [[x,y] for x,y in zip(position,speed)]
	pairs.sort(reverse=True)
	print(pairs)

	stack = []
	for p, s in pairs:
		stack.append((target - p) / s)
		print(stack)
		if len(stack) >= 2 and stack[-1] <= stack[-2]:
			stack.pop()
	return len(stack)



print(carFleet(10,[1,4],[3,2]))
print(carFleet(10,[4,1,0,7],[2,2,1,1]))
