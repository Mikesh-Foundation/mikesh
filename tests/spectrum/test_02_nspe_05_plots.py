from matplotlib import pyplot as plt



def test_plot_1():
	import mikesh
	# Spectra loading
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum_1 = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	with open("./tests/spectrum/spectrum_2") as file:
		spectrum_2 = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	# Plot data of original spectrum
	x_orig = []
	y_orig = []
	for group in spectrum_1.groups():
		x_orig.append(spectrum_1.es_low()[group-1])
		y_orig.append(spectrum_1.fluxes()[group-1])
		x_orig.append(spectrum_1.es_high()[group-1])
		y_orig.append(spectrum_1.fluxes()[group-1])
	# Plot data of regrouped spectrum
	spectrum_1_regr = spectrum_1.regroup(
		spectrum_2.es_low(),
		spectrum_2.es_high()
	)
	x_regr = []
	y_regr = []
	for group in spectrum_1_regr.groups():
		x_regr.append(spectrum_1_regr.es_low()[group-1])
		y_regr.append(spectrum_1_regr.fluxes()[group-1])
		x_regr.append(spectrum_1_regr.es_high()[group-1])
		y_regr.append(spectrum_1_regr.fluxes()[group-1])
	# Data plotting
	plt.figure(figsize=(16, 9))
	plt.plot(x_orig, y_orig, "b-", label="Original spectrum")
	plt.plot(x_regr, y_regr, "r--", label="Regrouped spectrum")
	plt.xlabel("Energy", fontsize=16)
	plt.ylabel("Neutron flux density", fontsize=16)
	plt.xscale("log")
	plt.yscale("log")
	plt.savefig("./tests/test_plot_1.png")
	assert True

def test_plot_2():
	import mikesh
	# Spectra loading
	with open("./tests/spectrum/spectrum_1") as file:
		spectrum_1 = mikesh.NSpectrum(
			source=file,
			name="test"
		)
	# Plot data of original spectrum
	x_orig  = []
	y_orig  = []
	for group in spectrum_1.groups():
		x_orig.append(spectrum_1.es_low()[group-1])
		y_orig.append(spectrum_1.fluxes()[group-1])
		x_orig.append(spectrum_1.es_high()[group-1])
		y_orig.append(spectrum_1.fluxes()[group-1])
	x_lines = []
	y_lines = []
	for group in spectrum_1.groups():
		delta_e  = spectrum_1.es_high()[group-1] - spectrum_1.es_low()[group-1]
		middle_e = spectrum_1.es_low()[group-1] + delta_e / 2
		for i in range(0,10,1):
			a = spectrum_1._lin[group-1][0][0]
			b = spectrum_1._lin[group-1][0][1]
			e = middle_e + (i-10) * delta_e / 20
			x_lines.append(e)
			y_lines.append(a * e + b)
		for i in range(0,10,1):
			a = spectrum_1._lin[group-1][1][0]
			b = spectrum_1._lin[group-1][1][1]
			e = middle_e + i * delta_e / 20
			x_lines.append(e)
			y_lines.append(a * e + b)
	# Data plotting
	plt.figure(figsize=(16,9), dpi=256)
	plt.plot(x_orig, y_orig, "b-", label="Original spectrum")
	plt.plot(x_lines, y_lines, "r-", label="Regrouped spectrum")
	plt.xlabel("Energy", fontsize=16)
	plt.ylabel("Neutron flux density", fontsize=16)
	plt.xscale("log")
	plt.yscale("log")
	plt.savefig("./tests/test_plot_2.png")
	assert True
