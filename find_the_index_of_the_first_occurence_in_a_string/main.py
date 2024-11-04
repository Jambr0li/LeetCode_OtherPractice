# Find s2 inside of s2 
# Index of first occurence

# Probably just iterate through the second string and check if first letter matchess
# If first letter matches then take the slice and compare.
# Also need to check if there are enough characters following the first occurence for the word to fit.
# We can do this by subtracting the current index from the length of the whole array 
# Then check if the len os s2 is greater or equal to the cur lengt

def strStr(s1,s2):
	len1, len2 = len(s1), len(s2)
	for i, c in enumerate(s1):
		if s2[0] == c:
			if len1 - i < len2:
				return -1
			if s1[i:i + len2] == s2:
				return i
	return -1

print(strStr("sadbutsad","sad"))


