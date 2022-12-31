import json



def dump_txt(self, path):
	with open(path, "w") as fs:
		fs.write("#{:} {:11} {:11} {:11} {:5}\n".format(
			"grp",
			"e_down",
			"e_up",
			"flux",
			"stdev"
		))
		for group in self._grp:
			fs.write("{:04d} {:.5E} {:.5E} {:.5E} {:06.3f}\n".format(
				self._grp[group-1],
				self._e_low[group-1],
				self._e_high[group-1],
				self._flux[group-1],
				self._stdev[group-1]
			))

def dump_json(self, path):
	dict = {}
	for group in self._grp:
		dict[str(group)] = {}
		dict[str(group)]["e_down"] = self._e_low[group-1]
		dict[str(group)]["e_up"]   = self._e_high[group-1]
		dict[str(group)]["flux"]   = self._flux[group-1]
		dict[str(group)]["stdev"]  = self._stdev[group-1]
	with open(path, "w") as fs:
		json.dump(fs, dict)
