def graph(arr):
	maxVal = max(arr)
	res = ""
	for i in range(maxVal,-1,-1):
		line = ""
		for num in arr:
			if num == i:
				line += " ____ "
			elif num < i:
				line += "......"
			else:
				line += "|    |"
		if i == maxVal:
			line += f" ^ {i}\n"
		else:	
			line += f" | {i}\n"
		res += line
	return "".join(list(res)[0:-1])


print(graph([10,5,3,1,4]))
# print(graph([10,12,8,2,4]))
# print(graph([0]))
