from .._matrix_rs import determinant as det



def determinant(self):
	if self._det == None:
		self._det = det(self._rows)
	return self._det
