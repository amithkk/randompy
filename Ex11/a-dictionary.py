
store = {}

def addEntry(word, meaning):
	store[word] = meaning

def getMeaning(word):
	try:
		return store[word]
	except KeyError:
		return "NoDef"

def getWordsWithMeaning(meaning):
	return [k for k,v in store.items() if v == meaning]

def deleteWord(word):
	try:
		del store[word]
	except KeyError:
		pass

def getSortedWordList():
	return sorted(store.keys(), key=lambda x:x.lower())

while True:
	opt = int(input("\nDictionary:\n(1)Add Word\n(2)Delete Word\n(3)Get Words With Meaning\n(4)Get Meaning\n(5)Show All Words (A-Z)\n(6)Exit\n>> "))

	if opt is 1:
		w = input('Enter Word:')
		m = input('Enter Meaning:')
		addEntry(w,m)
	elif opt is 2:
		w = input('Enter Word:')
		deleteWord(w)
	elif opt is 3:
		m = input('Enter Meaning:')
		print("Words Matching (If Any):", ",".join(getWordsWithMeaning(m)))
	elif opt is 4:
		w = input('Enter Word:')
		print("Meaning:",getMeaning(w))
	elif opt is 5:
		print("Words:", ",".join(getSortedWordList()))
	elif opt is 6:
		break


