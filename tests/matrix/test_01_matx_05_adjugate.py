def test_adjugate_1():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1,0,0],[0,1,0],[0,0,1]])
	result         = matrix.adjugate()
	adjoint_matrix = mikesh.Matrix(rows = [[1,0,0],[0,1,0],[0,0,1]])
	assert result == adjoint_matrix

def test_adjugate_2():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1,2],[3,4]])
	result         = matrix.adjugate()
	adjoint_matrix = mikesh.Matrix(rows = [[4,-2],[-3,1]])
	assert result == adjoint_matrix

def test_adjugate_3():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1]])
	result         = matrix.adjugate()
	adjoint_matrix = mikesh.Matrix(rows = [[1]])
	assert result == adjoint_matrix

def test_adjugate_4():
	import mikesh
	matrix         = mikesh.Matrix(rows = [[1,2,3],[1,0,2],[3,2,1]])
	result         = matrix.adjugate()
	adjoint_matrix = mikesh.Matrix(rows = [[-4,4,4],[5,-8,1],[2,4,-2]])
	assert result == adjoint_matrix
