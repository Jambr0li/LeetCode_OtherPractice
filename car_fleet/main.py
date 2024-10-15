def carFleet(target, position, speed):
	pairs = [(p,s) for p, s in zip(position,speed)]

	stack = []
	for p, s in sorted(pairs)[::-1]:
		stack.append((target - p) / s)
		if len(stack) >= 2 and stack [-1] <= stack[-2]:
			stack.pop()
	return len(stack) 

print(carFleet(10,[1,4],[3,2]))
print(carFleet(10,[4,1,0,7],[2,2,1,1]))
