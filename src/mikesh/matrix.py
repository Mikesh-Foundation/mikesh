class Matrix:
	# Rows are denoted by i and max(i) is denoted by m
	# Columns are denoted by j and max(j) is denoted by n
	_rows = []
	_det  = None

	from .matrix_methods._constructor     import __init__
	from .matrix_methods._equal           import __eq__
	from .matrix_methods._multiply        import __mul__
	from .matrix_methods._rmultiply       import __rmul__
	from .matrix_methods._determinant     import determinant
	from .matrix_methods._adjugate        import adjugate
	from .matrix_methods._inverse         import inverse

	def row(self, i):
		# INPUT CHECK
		if (i>len(self.rows)):
			raise ValueError(
				"\'i\' is larger than the number of rows in the matrix"
			)
		if (i<=0):
			raise ValueError(
				"\'i\' lower than 1"
			)

		return self._rows[i-1]

	def column(self, j):
		# INPUT CHECK
		if (j>len(self.rows[0])):
			raise ValueError(
				"\'j\' is larger than the number of columns in the matrix"
			)
		if (i<=0):
			raise ValueError(
				"\'j\' lower than 1"
			)

		column = []
		for row in self._rows:
			column.append(row[j-1])

		return column

	def dimensions(self):
		return (len(self._rows), len(self._rows[0]))
