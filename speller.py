words = set()

def check(word):
	if word.lower() in set:
		return True
	else:
		return False

def load(dictionary):
	with open(dictionary, "r") as file:
		for line in file:
			words.add(line.rstrip("\n"))	#store word in data structure
	return True

def size():
	return len(words)

def unload():
	return True