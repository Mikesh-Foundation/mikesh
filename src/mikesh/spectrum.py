class NSpectrum:
	_name       = None
	_grp        = []
	_e_low      = []
	_e_high     = []
	_flux       = []
	_stdev      = []

	from .spectrum_methods._constructor  import __init__
	from .spectrum_methods._integrity    import _integrity_check
	from .spectrum_methods._equal        import __eq__
	from .spectrum_methods._integral     import integral
	from .spectrum_methods._groups       import _groups_in_interval
	from .spectrum_methods._groups       import group
	from .spectrum_methods._regroup      import regroup
	from .spectrum_methods._export       import dump_txt
	from .spectrum_methods._export       import dump_json

	def max_energy(self):
		return self._e_high[-1]

	def min_energy(self):
		return self._e_low[0]

	def groups(self):
		return self._grp

	def es_low(self):
		return self._e_low

	def es_high(self):
		return self._e_high

	def fluxes(self):
		return self._flux

	def stdevs(self):
		return self._stdev

	def name(self):
		return self._name
