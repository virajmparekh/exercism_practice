"""
* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`
"""

	

def to_rna(dna):
	transcriptions = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

	if set(dna).issubset(set(transcriptions)):
	    return ''.join([transcriptions[x] for x in dna])
	return ''

