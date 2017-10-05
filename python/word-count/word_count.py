"""My way"""

def word_count(string):
	import re

	words = re.sub('[^a-zA-Z\d]+', ' ', string).lower().split()
	count = {}
	for val in set(words):
		count[val] = words.count(val)
	return count
    
