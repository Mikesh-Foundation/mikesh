def test_creation():
	import mikesh
	result = True
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	with open("./tests/spectrum/spectrum_1") as file:
		first_line = True
		for i,line in enumerate(file):
			if not(first_line):
				spectrum_group = spectrum.group(i)
				if not(spectrum_group[0] == int(line.split()[0])):
					result = False
				if not(spectrum_group[1] == float(line.split()[1])):
					result = False
				if not(spectrum_group[2] == float(line.split()[2])):
					result = False
				if not(spectrum_group[3] == float(line.split()[3])):
					result = False
				if not(spectrum_group[4] == float(line.split()[4])):
					result = False
			else:
				first_line = False
		if not(len(spectrum.groups()) == i):
			result = False
		if not(len(spectrum.es_low()) == i):
			result = False
		if not(len(spectrum.es_high()) == i):
			result = False
		if not(len(spectrum.fluxes()) == i):
			result = False
		if not(len(spectrum.stdevs()) == i):
			result = False
	assert result
