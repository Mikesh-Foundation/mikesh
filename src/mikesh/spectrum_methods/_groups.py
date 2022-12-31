def _groups_in_interval(self, e_down, e_up):
	groups = []
	for grp in self._grp:
		if (self._e_low[grp-1] >= e_down and self._e_high[grp-1] <= e_up):
			if not(grp in groups):
				groups.append(grp)
		else:
			if (self._e_low[grp-1] < e_down and self._e_high[grp-1] > e_down):
				if not(grp in groups):
					groups.append(grp)
			if (self._e_low[grp-1] < e_up and self._e_high[grp-1] > e_up):
				if not(grp in groups):
					groups.append(grp)
	return groups

def group(self, number):
	return([
		self._grp[number-1],
		self._e_low[number-1],
		self._e_high[number-1],
		self._flux[number-1],
		self._stdev[number-1]
	])
