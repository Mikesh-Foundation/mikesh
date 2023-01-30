def test_group_integral_1():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.00000E-09, 5.00000E-09)
	assert (result[2] == 2.53449200E+03 and result[3] == 0.2)

def test_group_integral_2():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(6.25000E-07, 7.80000E-07)
	assert (result[2] == 6.337252500E+04 and result[3] == 0.2)

def test_group_integral_3():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.00000E+01, 2.00000E+01)
	assert (result[2] == 1.9400700E+11 and result[3] == 0.2)

def test_subgroup_integral_1():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.00000E-09, 3.00000E-09)
	assert (result[2] == 1267.246 and result[3] == 0.2)

def test_subgroup_integral_2():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(3.00000E-09, 5.00000E-09)
	assert (result[2] == 1.26724600E+03 and result[3] == 0.2)

def test_subgroup_integral_3():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(2.00000E-09, 3.00000E-09)
	assert (result[2] == 633.6229999999996 and result[3] == 0.2)

def test_multigroup_integral_1():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.00000E-01, 1.00000E+00)
	assert ( result[2] == 2.0877033500E+12 and result[3] == 0.447213595499958)

def test_multigroup_integral_2():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.00000E-09, 2.00000E+01)
	assert (
		result[2] == 18982578850313.453 and
		result[3] == 1.6733200530681518
	)

def test_multigroup_integral_3():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(3.00000E-09, 1.5000E+01)
	assert (
		result[2] == 18885575349046.203 and
		result[3] == 1.6733200530681518
	)

def test_multigroup_integral_4():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	result = spectrum.integral(1.11000E-06, 4.00000E-01)
	assert (
		result[2] == 729781817936.1079 and
		result[3] == 1.0770329614269012
	)
