class Boy:
        """constructor for class Boy"""
	def __init__(self,name_id,attr,bgt,intlg,min_attr,t):
		self.name_id = name_id
		self.bgt = bgt
		self.t=t
		self.intlg = intlg
		self.attr = attr
		self.min_attr = min_attr
		self.status='single'
		self.happiness=0
		self.gf=''
        """condition for couple formation"""
	def constraint(self,main_bgt,attr):
		if (self.bgt < main_bgt) or (attr < self.min_attr):
			return False
		else:
			return True
	"""set boy happiness just like setter method"""
	def set_happiness(self,happiness) :
		self.happiness=happiness

    """set girlfirend of boy"""
	def set_gf(self,gf):
		self.gf=gf
	"""modify boy budget if he can't afford gift in gift basket"""
	def mod_bgt(self,bgt):
		self.bgt=bgt
