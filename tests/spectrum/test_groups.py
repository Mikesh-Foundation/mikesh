def test_groups_1():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(1.00000E-09, 5.00000E-09)
	result = True
	if not(len(groups) == len([1])):
		result = False
	for i,x in enumerate([1]):
		if not(groups[i]==x):
			result = False
	assert result

def test_groups_2():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(1.00000E-01, 1.00000E+00)
	result = True
	if not(len(groups) == len([61,62,63,64,65])):
		result = False
	for i,x in enumerate([61,62,63,64,65]):
		if not(groups[i]==x):
			result = False
	assert result

def test_groups_3():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(9.00000E-02, 1.00000E+00)
	result = True
	if not(len(groups) == len([60,61,62,63,64,65])):
		result = False
	for i,x in enumerate([60,61,62,63,64,65]):
		if not(groups[i]==x):
			result = False
	assert result

def test_groups_4():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(1.00000E-01, 1.10000E+00)
	result = True
	if not(len(groups) == len([61,62,63,64,65,66])):
		result = False
	for i,x in enumerate([61,62,63,64,65,66]):
		if not(groups[i]==x):
			result = False
	assert result

def test_groups_5():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(9.00000E-02, 1.10000E+00)
	result = True
	if not(len(groups) == len([60,61,62,63,64,65,66])):
		result = False
	for i,x in enumerate([60,61,62,63,64,65,66]):
		if not(groups[i]==x):
			result = False
	assert result

def test_groups_6():
	import mikesh
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	groups = spectrum._groups_in_interval(0, 1.0E+05)
	result = True
	if not(len(groups) == len(range(1,71,1))):
		result = False
	for i,x in enumerate(range(1,71,1)):
		if not(groups[i]==x):
			result = False
	assert result
