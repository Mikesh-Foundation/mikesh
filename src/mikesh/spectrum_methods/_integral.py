from math import sqrt, pow



def integral(self, e_down, e_up, inter="const"):
	# INPUT CHECK
	if (e_down > e_up):
		raise ValueError("\'e_down\' is larger than \'e_up\'")
	if (e_down < 0):
		raise ValueError("\'e_down\' cannot be negaitve")
	if (e_up < 0):
		raise ValueError("\'e_up\' cannot be negaitve")
	if (e_down < self._e_low[0]):
		raise ValueError(
			"\'e_down\' is lower than lowest possible energy = {:f}".format(
				self._e_low[0]
			)
		)
	if (e_up > self._e_high[-1]):
		raise ValueError(
			"\'e_down\' is higher than highest possible energy = {:f}".format(
				self._e_high[-1]
			)
		)
	if (e_down == e_up):
		raise ValueError(
			"\'e_down\' is the same as \'e_up\' with value = {:f}".format(
				e_down
			)
		)

	# GROUPS WITHIN INTERVAL (E_DOWN, E_UP)
	groups = self._groups_in_interval(e_down, e_up)

	# FLUX IN LOWEST GROUP OR ITS FRACTION
	if (self._e_low[groups[0]-1] == e_down):
		delta_e    = self._e_high[groups[0]-1] - self._e_low[groups[0]-1]
		lower_flux = self._flux[groups[0]-1] * delta_e
	else:
		group_width = self._e_high[groups[0]-1] - self._e_low[groups[0]-1]
		delta_e     = self._e_high[groups[0]-1] - e_down
		lower_flux  = self._flux[groups[0]-1] * delta_e

	# FLUX IN LOWEST GROUP OR ITS FRACTION
	if (self._e_high[groups[-1]-1] == e_up):
		delta_e    = self._e_high[groups[-1]-1] - self._e_low[groups[-1]-1]
		upper_flux = self._flux[groups[-1]-1] * delta_e
	else:
		group_width = self._e_high[groups[0]-1] - self._e_low[groups[0]-1]
		delta_e     = e_up-self._e_low[groups[-1]-1]
		upper_flux  = self._flux[groups[-1]-1] * delta_e

	# INTEGRAL
	integral = lower_flux
	for group in groups[1:-1]:
		delta_e   = self._e_high[group-1] - self._e_low[group-1]
		integral += self._flux[group-1] * delta_e
	if (len(groups)>1):
		integral += upper_flux
	else:
		delta_e  = self._e_high[groups[0]-1] - self._e_low[groups[0]-1]
		integral = self._flux[groups[0]-1] * delta_e
		integral = lower_flux + upper_flux - integral

	# INTEGRAL UNCERTAINTY
	uncertainty = 0
	for group in groups:
		uncertainty += pow(self._stdev[group-1], 2)
	uncertainty = sqrt(uncertainty)

	return [e_down, e_up, integral, uncertainty]
