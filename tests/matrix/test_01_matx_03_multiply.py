def test_multiplication_1():
	import mikesh
	matrix        = mikesh.Matrix(rows = [[1,2,3],[1,3,2],[3,2,1]])
	identity      = mikesh.Matrix(rows = [[1,0,0],[0,1,0],[0,0,1]])
	matrix_mult   = matrix * identity
	assert matrix_mult == matrix

def test_multiplication_2():
	import mikesh
	matrix        = mikesh.Matrix(rows = [[1,2,3],[1,3,2],[3,2,1]])
	matrix_mult   = matrix * matrix
	matrix_result = mikesh.Matrix(rows = [[12,14,10],[10,15,11],[8,14,14]])
	assert matrix_mult == matrix_result

def test_multiplication_3():
	import mikesh
	matrix_1      = mikesh.Matrix(rows = [[1,2,3],[1,3,2]])
	matrix_2      = mikesh.Matrix(rows = [[1,2],[1,3],[3,2]])
	matrix_mult   = matrix_1 * matrix_2
	matrix_result = mikesh.Matrix(rows = [[12,14],[10,15]])
	assert matrix_mult == matrix_result
