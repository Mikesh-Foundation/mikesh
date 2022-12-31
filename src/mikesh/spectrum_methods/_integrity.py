def _integrity_check(self):
	for group in range(1, len(self._grp), 1):
		if not(self._e_high[group-1] == self._e_low[group]):
			raise ValueError(
				"\'e_up\' of energy group {:d} and ".format(group) +
				"\'e_down\' of energy group " +
				"{:d}are not identical".format(group+1)
			)
		if not(self._grp[group-1] == self._grp[group]-1):
			raise ValueError(
				"energy group {:d} is missing".format(group)
			)

	for group in self._grp:
		if not(self._flux[group-1] >= 0):
			raise ValueError(
				"flux in energy group {:d} is negative".format(group)
			)
		if not(self._flux[group-1] >= 0):
			raise ValueError(
				"uncertainty in energy group {:d} is negative".format(group)
			)
