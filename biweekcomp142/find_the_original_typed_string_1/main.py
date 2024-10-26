def possibleStringCount(word):
    if word == "":
        return 0
    count = 1
    l = 0
    r = 0
    subcount = 0
    while l < len(word):
        while r < len(word) and word[l] == word[r]:
            subcount += 1
            r += 1
        if subcount > 1:
            count += subcount - 1
        subcount = 0
        l = r 
    return count










print(possibleStringCount("abbcccc"))
# print(possibleStringCount("abcd"))
# print(possibleStringCount("aaaa"))
        