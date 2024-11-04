# We want to return the indices of two numbers inside the provided array that sum up to t.

# We can store num inside a map 
# The key is the index and the num and value is the index

# As we iterate through the array we check if target - cur_num exists in the map

# If it does we return the current index and the key associated with the value we just fouund in the map

# If it doesn't exist in there then we add it to the map

def twoSum(nums,t):
	num_map = {}
	for i, n in enumerate(nums):
		if t - n in num_map.keys():
			return [num_map[t - n], i]
		num_map[n] = i




print(twoSum([1,2,3,4],3)) # should return [1,2]	