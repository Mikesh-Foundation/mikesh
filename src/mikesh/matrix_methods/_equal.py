def __eq__(self, other):
	m = len(self._rows)
	n = len(self._rows[0])
	for s_i in range(0,m,1):
		for s_j in range(0,n,1):
			if not(self._rows[s_i][s_j] == other._rows[s_i][s_j]):
				return False

	return True
