from mystring.palindrome import palindrome
from mystring.countvowels import countvowels

inp = input("Enter String:")
opt = int(input("\nSelect:\n(1)Palindrome Check\n(2)Count Vowels\n>>>"))

if opt == 1:
		if palindrome(inp):
			print("Is Palindrome")
		else:	
			print("Is not Palindrome")
elif opt == 2:
		print("Number Of Vowels :", countvowels(inp))





