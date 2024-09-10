def isPalindrome(s): 
        s = s.lower()
        s = list(''.join(s.split(' ')))
        letters = []
        for char in s:
            if char.isalnum():
                letters.append(char)
        s = letters
        start = 0
        end = len(s) - 1
        while start < end:
            print(f"start is {s[start]} and end is {s[end]}")
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

print(isPalindrome("racecar"))