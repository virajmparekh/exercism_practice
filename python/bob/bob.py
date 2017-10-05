def hey(orig_string):
	import re
	if string != '':
		#if more than half the letters in the string are uppercase, we'll call that yelling
		if sum(1 for s in string if s.isupper()) > .5*(len(''.join(filter(str.isalpha, string)))):
			return "Whoa, chill out!"
		elif string[len(string)-1] == '?':
			return "Sure."
		else: 
			return 'Whatever.'
	return 'Fine. Be that way!'

