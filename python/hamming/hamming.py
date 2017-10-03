def distance(strand_one, strand_two):
    if len(strand_two) != len(strand_one):
    	raise ValueError("Strands were not equal length")
    differences = 0
    m = [i for i, j in zip(list(strand_one),list(strand_two)) if i == j]
    return len(strand_one) - len(m)

