def vowelCount(input):
	count = list(map(input.lower().count, "aeiou"))
	count = ','.join(map(str, count))
	print("a,e,i,o and u appear, respectively," , count , "times")