def checkInclusion(s1,s2):
	if len(s1) > len(s2):
		return False

	map1 = {}
	map2 = {}
	for c in s1:
		map1[c] = map1.get(c,0) + 1

	for c in s2[0:len(s1)]:
		map2[c] = map2.get(c,0) + 1

	l = 0
	if map1 == map2:
		return True
	for i in range(len(s1),len(s2)):
		if map2.get(s2[l], 0) == 1:
			map2.pop(s2[l])	
		else: 
			map2[s2[l]] -= 1
		map2[s2[i]] = map2.get(s2[i], 0) + 1
		l += 1
		if map1 == map2:
			return True

	return False



# print(checkInclusion("abc","lecabee"))
# print(checkInclusion("adc","dcda"))
# print(checkInclusion("abc","ccccbbbbaaaa"))
print(checkInclusion("ab","a"))
