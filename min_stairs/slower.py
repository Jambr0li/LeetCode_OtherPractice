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



# Brute force method:

def min_stairs(stairs):
	return min(return_val(stairs,0), return_val(stairs, 1))


def return_val(stairs, i):
	if i >= len(stairs): # Base case
		return 0
	# For each element we need to check the cost of going 1 or 2 steps.
	return stairs[i] + min(return_val(stairs,i + 1), return_val(stairs, i + 2))



# print(min_stairs([10,15,20]))
print(min_stairs([10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20,10,15,20]))
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
