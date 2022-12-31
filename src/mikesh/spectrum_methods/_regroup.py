def regroup(self, e_low, e_high, inter="const"):
	tmp_grp    = []
	tmp_e_low  = []
	tmp_e_high = []
	tmp_flux   = []
	tmp_stdev  = []
	for group in range(1,len(e_low)+1,1):
		# WITHIN DEFINED ENERGIES OF SPECTRUM BEEING REGROUPED
		if (
			(e_low[group-1]  >= self._e_low[0])   and
			(e_low[group-1]  <= self._e_high[-1]) and
			(e_high[group-1] >= self._e_low[0])   and
			(e_high[group-1] <= self._e_high[-1])
		):
			integral = self.integral(e_low[group-1], e_high[group-1])
			tmp_grp.append(group)
			tmp_e_low.append(e_low[group-1])
			tmp_e_high.append(e_high[group-1])
			tmp_flux.append(integral[2] / (e_high[group-1] - e_low[group-1]))
			tmp_stdev.append(integral[3])

		# OUTSIDE DEFINED ENERGIES OF SPECTRUM BEEING REGROUPED
		if (
			(e_low[group-1]  <  self._e_low[0])   and
			(e_high[group-1] <= self._e_low[0])   or
			(e_low[group-1]  >= self._e_high[-1]) and
			(e_high[group-1] >  self._e_high[-1])
		):
			tmp_grp.append(group)
			tmp_e_low.append(e_low[group-1])
			tmp_e_high.append(e_high[group-1])
			tmp_flux.append(0.0)
			tmp_stdev.append(0.0)

		# PARTIALY DEFINED ENERGIES OF SPECTRUM BEEING REGROUPED
		# LOWER END
		if (
			(e_low[group-1]  <  self._e_low[0])   and
			(e_high[group-1] > self._e_low[0])   and
			(e_high[group-1] <= self._e_high[-1])
		):
			integral = self.integral(self._e_low[0], e_high[group-1])
			tmp_grp.append(group)
			tmp_e_low.append(e_low[group-1])
			tmp_e_high.append(e_high[group-1])
			tmp_flux.append(integral[2] / (e_high[group-1] - self._e_low[0]))
			tmp_stdev.append(integral[3])

		# PARTIALY DEFINED ENERGIES OF SPECTRUM BEEING REGROUPED
		# UPPER END
		if (
			(e_low[group-1]  >= self._e_low[0])   and
			(e_low[group-1]  <= self._e_high[-1]) and
			(e_high[group-1] >  self._e_high[-1])
		):
			integral = self.integral(e_low[group-1], self._e_high[-1])
			tmp_grp.append(group)
			tmp_e_low.append(e_low[group-1])
			tmp_e_high.append(e_high[group-1])
			tmp_flux.append(integral[2] / (self._e_high[-1] - e_low[group-1]))
			tmp_stdev.append(integral[3])

		# PARTIALY DEFINED ENERGIES OF SPECTRUM BEEING REGROUPED
		# BOTH ENDS
		if (
			(e_low[group-1]  < self._e_low[0])   and
			(e_high[group-1] > self._e_high[-1])
		):
			integral = self.integral(self._e_low[0], self._e_high[-1])
			tmp_grp.append(group)
			tmp_e_low.append(e_low[group-1])
			tmp_e_high.append(e_high[group-1])
			tmp_flux.append(integral[2] / (self._e_high[-1] - self._e_low[0]))
			tmp_stdev.append(integral[3])

	return self.__class__(
			source = [tmp_grp, tmp_e_low, tmp_e_high, tmp_flux, tmp_stdev]
		)
