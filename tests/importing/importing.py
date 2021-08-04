import os



def test_importing(self):
	folders = os.listdir("./")
	if not("target" in folders):
		assert False

	files = os.listdir("./target/release")
	if ("mikesh.so" in files):
		import mikesh
	if ("mikesh.dll" in files):
		import ctypes
		mikesh = ctypes.cdll.LoadLibrary("./target/release/mikesh.dll")

	return mikesh
