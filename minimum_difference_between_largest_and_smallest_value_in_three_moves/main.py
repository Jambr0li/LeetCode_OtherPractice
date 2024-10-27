def minDifference(n):
    if len(n) < 5:
        return 0
    n.sort()
    print(n)
    return min(n[-1] -  n[3], n[-2] - n[2], n[-3] - n[1], n[-4] - n[0])

print(minDifference([1,2,0,10,14]))
