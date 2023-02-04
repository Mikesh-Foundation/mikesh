def __rmul__(self, other):
	result = []
	if isinstance(other, float):
		for row in self._rows:
			result.append([])
			for element in row:
				result[-1].append(other * element)
	return self.__class__(rows=result)
