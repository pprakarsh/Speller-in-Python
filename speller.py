from dictionary import check, load, size, unload
import time
import re
from sys import argv

DICTIONARY = "large"
LENGTH = 45

if(len(argv) != 1 and len(argv) != 2):
	exit("Usage: speller [dictionary] text")

time_load, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

dictionary = argv[1] if len(argv)==3 else DICTIONARY

before = time.process_time()
loaded = load(dictionary)
after = time.process_time()

if not loaded:
	exit(f"Could not load {dictionary}")

time_load = after-before

text = argv[-1]
file = open(text, "r")
if not file:
	unload()
	exit(f"could not open {text}")

print("MISSPELLED WORDS!\n")

index, misspellings, words = 0, 0, 0
word = ""
wrong_words = []

while True:
	c = file.read(1)
	if not c:
		break

	if re.match(r"[A-Za-z]", c) or (c == "'" and index > 1):
		word = word + c
		index += 1
		if index > LENGTH:
			while True:
				c = file.read(1)
				if (not c) or ((not c.isdigit()) and (not re.match(r"[A-Za-z]", c)) and (not c == "'")):
					index = 0
					word = ""
					break

	elif c.isdigit():
		while True:
			c = file.read(1)
			if (not c) or ((not c.isdigit()) and (not re.match(r"[A-Za-z]", c)) and (not c == "'")):
				index = 0
				word = ""
				break

	else:
		if word == "":
			continue
		before = time.process_time()
		if not check(word):
			after = time.process_time()
			misspellings += 1
			wrong_words.append(word)
		check_time = after-before

		words += 1
		word = ""
		index = 0


print(wrong_words)

print(f"Total words: 								{words: }")
print(f"Total misspelled words: 			        {misspellings: }")

print(f"Total load time: 							{time_load: .2f}")
print(f"Total time for checking spelling of words   {time_check: .5f}")








