
def sum(array,k):
	solution = set()
	for x in array:
		if x in sloution: 
			return True
		solution.add(k-x)

	return False

sum([10,15,3,7], 17)