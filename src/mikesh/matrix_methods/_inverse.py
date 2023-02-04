def inverse(self):
	det = 1/self.determinant()
	adj = self.adjugate()
	return (det*adj)
