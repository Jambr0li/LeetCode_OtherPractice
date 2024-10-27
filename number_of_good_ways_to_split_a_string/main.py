def numSplits(s):
	count = 0
	l = len(s)
	map1, map2 = {}, {}
	for c in s:
		map1[c] = map1.get(c, 0) + 1
	for i in range(l):
		map2[s[i]] = map2.get(s[i], 0) + 1
		if s[i] in map1.keys():
			if map1[s[i]] == 1:
				map1.pop(s[i])
			else:
				map1[s[i]] -= 1
		if len(map1.keys()) == len(map2.keys()):
			count += 1
	return count

print(numSplits("aacaba"))