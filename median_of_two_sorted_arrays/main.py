def findMedianSortedArrays(nums1, nums2):
	A, B = nums1,nums2
	if len(A) > len(B):
		A,B = B,A # I want A to be the smaller array.
	ALength = len(A) - 1
	BLength = len(B) - 1
	TotalLength = ALength + BLength  + 2

	l, r = 0, ALength
	while True: # Loop forever because median is guaranteed
		cA = l + (r - l) // 2
		cB = (TotalLength // 2) - cA - 2

		Aleft = A[cA] if cA >= 0 else float("-infinity")
		Aright = A[cA + 1] if (cA + 1) < len(A) else float("infinity")
		Bleft = B[cB] if cB >= 0 else float("-infinity")
		Bright = B[cB + 1] if (cB + 1) < len(B) else float("infinity")

		if Aleft <= Bright and Bleft <= Aright:
			if TotalLength % 2 == 1:
				return min(Aright, Bright)
			return (min(Aright, Bright) + max(Bleft, Bleft)) / 2
		elif Aleft > Bright:
			r = cA - 1
		else: 
			l = cA + 1








print(findMedianSortedArrays([1,2],[3]))