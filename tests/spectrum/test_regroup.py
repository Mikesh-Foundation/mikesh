import os



def test_regroup_1():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	result = spectrum.regroup(spectrum.es_low(), spectrum.es_high()
	)
	assert result == spectrum

def test_regroup_2():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	spectrum_regrouped = mikesh.NSpectrum(
		source = [
			[1],
			[1.00E-09],
			[2.00E+01],
			[949128942563.1292],
			[1.6733200530681518]
		]
	)
	result = spectrum.regroup([1.00E-09], [2.00E+01])

	assert result == spectrum_regrouped

def test_regroup_3():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	spectrum_regrouped = mikesh.NSpectrum(
		source = [
			[1],
			[1.00E-09],
			[2.00E+01],
			[10],
			[1.6733200530681518]
		]
	)
	result = spectrum.regroup([1.00E-09], [2.00E+01])

	assert ((result == spectrum_regrouped) == False)

def test_regroup_4():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	spectrum_regrouped = mikesh.NSpectrum(
		source = [
			[1],
			[1.00E-10],
			[2.00E+02],
			[949128942563.1292],
			[1.6733200530681518]
		]
	)
	result = spectrum.regroup([1.00E-10], [2.00E+02])

	assert result == spectrum_regrouped

def test_regroup_5():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	spectrum_regrouped = mikesh.NSpectrum(
		source = [
			[1],
			[1.00E-09],
			[2.00E+02],
			[949128942563.1292],
			[1.6733200530681518]
		]
	)
	result = spectrum.regroup([1.00E-09], [2.00E+02])

	assert result == spectrum_regrouped

def test_regroup_6():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum = mikesh.NSpectrum(
			source = fs
		)
	spectrum_regrouped = mikesh.NSpectrum(
		source = [
			[1],
			[1.00E-10],
			[2.00E+01],
			[949128942563.1292],
			[1.6733200530681518]
		]
	)
	result = spectrum.regroup([1.00E-10], [2.00E+01])

	assert result == spectrum_regrouped

def test_regroup_7():
	import mikesh
	path_dump = "./tests/spectrum/spectrum_dump_test.tmp"
	with open("./tests/spectrum/spectrum_1") as fs:
		spectrum_1 = mikesh.NSpectrum(
			source = fs
		)
	with open("./tests/spectrum/spectrum_2") as fs:
		spectrum_2 = mikesh.NSpectrum(
			source = fs
		)
	result = spectrum_1.regroup(
		spectrum_2._e_low,
		spectrum_2._e_high
	)
	result.dump_txt(path_dump)
	with open(path_dump) as fs:
		result = mikesh.NSpectrum(
			source = fs
		)
	os.remove(path_dump)

	assert result == spectrum_2
