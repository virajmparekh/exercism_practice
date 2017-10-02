def is_isogram(string):
	import re
	string = re.sub(r'\W+', '', string).lower()
	return len(string) == len(set(string))

