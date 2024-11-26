def rev_rot(strng, sz):
	if sz == 0:
		return ""
	if sz > len(strng):
		return strng
	new_str = ""
	for i in range(0,len(strng), sz):
		if len(strng) < i + sz:
			# print(new_str)
			# new_str += strng[i:len(strng)]
			# print(new_str)
			break

		odds_cnt = 0
		for num in strng[i : i + sz]:
			if int(num) % 2 == 1:
				odds_cnt += 1

		if odds_cnt % 2 == 1: # Odd total
			# rotate left
			new_str += strng[i + 1: i + sz]
			new_str += strng[i]
		else:
			print(new_str)
			str_slice = strng[i : i + sz]
			new_str += str_slice[::-1]
			# reverse
		# print(strng[i:i + sz])
	return new_str


# print(rev_rot("123456987654", 6))
# print(rev_rot("1234", 5))
print(rev_rot("2468", 4))

# s = "733049910872815764"
# print(rev_rot(s, 5))
# print("330479108928157")

# "234561876549"