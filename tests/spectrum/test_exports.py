def test_dump_txt():
	import os, mikesh
	path_orig = "./tests/spectrum/spectrum_1"
	path_dump = "./tests/spectrum/spectrum_dump_test.tmp"
	with open(path_orig) as fs:
		spectrum = mikesh.NSpectrum(fs)
	spectrum.dump_txt(path_dump)
	
	files_equal = True
	with open(path_dump, "r") as fs_dump:
		with open(path_orig, "r") as fs_orig:
			for line_orig in fs_orig:
				line_dump = fs_dump.readline()
				if not(line_dump.strip() == line_orig.strip()):
					files_equal = False
	os.remove(path_dump)
	assert files_equal
