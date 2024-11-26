def min_stairs(stairs):

	stairs.append(0)
	one = stairs[len(stairs) - 2]
	two = stairs[len(stairs) - 1]
	for i in range(len(stairs) - 3, -1, -1):
		temp = stairs[i]
		temp += min(one,two)
		temp_one = one
		one = temp
		two = temp_one

	return min(one,two)

print(min_stairs([10,15,20]))


# [10,15,20,0]
#        ^  ^

# temp = 15
# one = 20
# two = 0

# temp = 10
# one = 15
# two = 20

# 
# one = 25
# two = 15
