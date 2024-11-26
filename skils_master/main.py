def count_skills(skill_tree, desired_skills):
	if len(desired_skills) == 0:
		return 0
	if len(desired_skills) == len(skill_tree):
	    return len(desired_skills)

	skills_set = set()

	for skill in desired_skills:
		if skill in skills_set:
			continue
		while True:
			if skill in skills_set:
				break
			if skill == 0:
				skills_set.add(0)
				break
			skills_set.add(skill)
			skill = skill_tree[skill]
	# print(skills_set)
	return len(skills_set)




print(count_skills([ 0, 0, 0, 1, 3, 3, 2 ], {6}))
print(count_skills([ 0, 0, 0, 1, 3, 3, 2 ], set()) )
print(count_skills([ 0, 0, 0, 1, 3, 3, 2 ], { 1, 2 }))