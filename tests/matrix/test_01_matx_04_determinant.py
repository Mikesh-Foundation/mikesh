def test_determinant_1():
	import mikesh
	matrix        = mikesh.Matrix(rows = [[1,2,3],[1,0,2],[3,2,1]])
	result        = matrix.determinant()
	assert result == 12

def test_determinant_2():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[1,2,3,4],[1,0,2,3],[3,2,1,4],[4,3,2,1]]
	)
	result        = matrix.determinant()
	assert result == -60

def test_determinant_3():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	)
	result        = matrix.determinant()
	assert result == 1

def test_determinant_4():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	)
	result        = matrix.determinant()
	assert result == 0

def test_determinant_5():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]
	)
	result        = matrix.determinant()
	assert result == 0

def test_determinant_6():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
	)
	result        = matrix.determinant()
	assert result == 0

def test_determinant_7():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[1,2],[1,1]]
	)
	result        = matrix.determinant()
	assert result == -1

def test_determinant_8():
	import mikesh
	matrix        = mikesh.Matrix(
		rows = [[1]]
	)
	result        = matrix.determinant()
	assert result == 1
