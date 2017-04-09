class Girl:
        """constructor for class Girl having name,intelligence,attractoveness etc as attribute"""
	def __init__(self,name_id,attr,main_bgt,intlg,t):
		self.name_id = name_id
		self.attr = attr
		self.main_bgt = main_bgt
		self.intlg = intlg
		self.t=t
		self.status = 'single'
		self.happiness=0;
		self.bf=''
	"""condition for couple formation	"""
	def constraint(self,bgt):
		if (self.main_bgt > bgt):
			return False
		else:
			return True
        """set boyfriend for girl if there conditions satisfy"""
	def set_bf(self,bf):
		self.bf=bf
	"""set happiness of girl"""
	def set_happiness(self,happiness) :
		self.happiness=happiness
