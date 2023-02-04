def test_equal_1():
	import mikesh
	matrix = mikesh.Matrix(rows = [[1,2,3],[1,3,2],[3,2,1]])
	assert matrix == matrix
