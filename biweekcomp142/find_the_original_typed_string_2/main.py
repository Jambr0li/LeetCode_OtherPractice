def possibleStringCount(word, k):
    if word == "":
        return 0
    if len(word) == k:
    	return 1

    count = 1
    l = 0
    r = 0
    subcount = 0
    subcounts = []
    while l < len(word):
        while r < len(word) and word[l] == word[r] and len(word) - subcount >= k:
            subcount += 1
            r += 1
        if subcount > 1:
            count += subcount
            # print(subcount)
            subcounts.append(subcount)
            print(subcounts)
        subcount = 0
        l = r 

    res = 1
    for n in subcounts:
    	res *= n
    return res - 1
    return count


print(possibleStringCount("aabbccdd", 7))
print(possibleStringCount("aabbccdd", 8))
print(possibleStringCount("aaabbb", 3))




