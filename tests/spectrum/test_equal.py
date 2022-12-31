def test_equal_empty():
	import mikesh
	# EMPTY CLASS
	spectrum_empty = mikesh.NSpectrum()
	assert (spectrum_empty == spectrum_empty)

def test_equal_data():
	import mikesh
	# CLASS WITH DATA
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum_data = mikesh.NSpectrum(
			source = file
		)
	assert (spectrum_data == spectrum_data)
