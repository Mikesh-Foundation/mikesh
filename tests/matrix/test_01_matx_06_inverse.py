def test_inverse_1():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1,0,0],[0,1,0],[0,0,1]])
	result         = matrix.inverse()
	inverse_matrix = mikesh.Matrix(rows = [[1,0,0],[0,1,0],[0,0,1]])
	assert result == inverse_matrix

def test_inverse_2():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1]])
	result         = matrix.inverse()
	inverse_matrix = mikesh.Matrix(rows = [[1]])
	assert result == inverse_matrix

def test_inverse_3():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[5]])
	result         = matrix.inverse()
	inverse_matrix = mikesh.Matrix(rows = [[1/5]])
	assert result == inverse_matrix


def test_inverse_4():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1,0,1],[0,1,0],[0,1,1]])
	result         = matrix.inverse()
	inverse_matrix = mikesh.Matrix(rows = [[1,1,-1],[0,1,0],[0,-1,1]])
	assert result == inverse_matrix
