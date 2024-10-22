def maxProfit(prices):

	res = 0

	lowest_current_price = prices[0]

	for p in prices:
		if p < lowest_current_price:
			lowest_current_price = p
		res = max(res,p - lowest_current_price)
	return res

print(maxProfit([10,1,5,6,7,1])) 
print(maxProfit([10,8,7,5,2]))

