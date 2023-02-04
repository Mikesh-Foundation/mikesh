def __mul__(self, other):
	s_m = len(self._rows)
	s_n = len(self._rows[0])
	o_m = len(other._rows)
	o_n = len(other._rows[0])
	result = []

	for s_i in range(1,len(self._rows)+1,1):
		result.append([])
	for s_i in range(0,o_n,1):
		for s_j in range(0,s_m,1):
			result[s_i].append(0)
			for x in range(0,s_n,1):
				result[s_i][s_j] += self._rows[s_i][x] * \
				                   other._rows[x][s_j]

	return self.__class__(rows=result)
