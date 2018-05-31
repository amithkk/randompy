def countvowels(strng):
	vowels = "aeiou"
	strng = strng.lower()
	return sum(letter in vowels for letter in strng)