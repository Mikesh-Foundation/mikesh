def __init__(self, rows=[]):
	# INPUT CHECK
	if not(rows ==  []):
		m = len(rows)
	else:
		m = 0
	for i in range(1,m+1,1):
		if not(m==len(rows)):
			raise IndexError(
				"Row {:d} length does not equal m = {:d}".format(i, m)
			)

	self._rows = rows
