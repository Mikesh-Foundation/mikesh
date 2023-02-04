from .._matrix_rs import adjugate as adj



def adjugate(self):
	return self.__class__(adj(self._rows))
