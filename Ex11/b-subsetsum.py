from itertools import combinations

def subsetsum(list, target):
	for e in combinations(list, 3):
		if sum(e) == target:
			return True
	return False

# Test Driver For Program

lis = [2,3,4,5,6,7]
tar = 12

if subsetsum(lis,12):
	print('Program Works')

 