def __eq__(self, other):
	# LOW ENERGIES COMPARISON
	if not(len(self._e_low) == len(other._e_low)):
		return False
	else:
		for group in range(1, len(self._e_low)+1, 1):
			if not(self._e_low[group-1] == other._e_low[group-1]):
				return False
	# HIGH ENERGIES COMPARISON
	if not(len(self._e_high) == len(other._e_high)):
		return False
	else:
		for group in range(1, len(self._e_high)+1, 1):
			if not(self._e_high[group-1] == other._e_high[group-1]):
				return False
	# FLUXES COMPARISON
	if not(len(self._flux) == len(other._flux)):
		return False
	else:
		for i in range(1, len(self._flux)+1, 1):
			if not(self._flux[group-1] == other._flux[group-1]):
				return False
	# UNCERTAINTIES COMPARISON
	if not(len(self._stdev) == len(other._stdev)):
		return False
	else:
		for i in range(1, len(self._stdev)+1, 1):
			if not(self._stdev[group-1] == other._stdev[group-1]):
				return False

	return True
