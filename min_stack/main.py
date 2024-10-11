class MinStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, val):
		self.stack.append(val)
		value = min(val, self.min_stack[-1] if self.min_stack else val)
		self.min_stack.append(value)

	def pop(self):
		self.stack.pop()
		self.min_stack.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.min_stack[-1]

minStack = MinStack()
minStack.push(1)
print(minStack.getMin())
minStack.push(0)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())

