def test_creation():
	import mikesh
	matrix = mikesh.Matrix(rows = [[1,2,3],[1,3,2],[3,2,1]])
	assert matrix.dimensions() == (3,3)
