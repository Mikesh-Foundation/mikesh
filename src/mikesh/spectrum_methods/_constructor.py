from io import IOBase



def __init__(self, source=None, name=None, group_flux="diff"):
	if not(group_flux in ["diff", "intg"]):
		raise AttributeError(
			"\'group_flux\' attribute takes values \'diff\' or \'intg\'"
		)
	if not(
		isinstance(source, IOBase)      or \
		isinstance(source, list)        or \
		isinstance(source, type(None))
	):
		raise AttributeError(
			"\'source\' attribute must be of class \'list\' or \'IOBase\'"
		)

	self._grp    = []
	self._e_low  = []
	self._e_high = []
	self._flux   = []
	self._stdev  = []
	if (isinstance(source, IOBase)):
		for line in source:
			if not("#" == line[0]):
				self._grp.append(int(line.split()[0]))
				self._e_low.append(float(line.split()[1]))
				self._e_high.append(float(line.split()[2]))
				self._flux.append(float(line.split()[3]))
				self._stdev.append(float(line.split()[4]))
	if (isinstance(source, list)):
		self._grp    = source[0]
		self._e_low  = source[1]
		self._e_high = source[2]
		self._flux   = source[3]
		self._stdev    = source[4]
	self._name = name

	if (group_flux=="intg"):
		for group in self._grp:
			delta_e = self._e_high[group-1] - self._e_low[group-1]
			self._flux[group-1] = self._flux[group-1] / delta_e

	self._integrity_check()
