

try:
	print(1+'lol')
except TypeError:
	print("TypeError Caught")

try:
	a = [1,2,3]
	print(a[4])
except IndexError:
	print("IndexError Caught")