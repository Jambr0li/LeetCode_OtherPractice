def stock_list(stocklist, categories):

	category_map = {}

	for stock in stocklist:
		items = stock.split()
		identifier = items[0][0]
		number = int(items[1])
		category_map[identifier] = category_map.get(identifier, 0) + number

	return_str = ""

	for category in categories:
		if category in category_map:
			return_str += f"({category} : {category_map[category]}) - "
		else:
			return_str += f"({category} : 0) - "

	return return_str[0:-3]


b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
c = ["A", "B", "C", "W"]
print(stock_list(b, c))
