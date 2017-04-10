class Girl:
	'constructor for class girl'
	def __init__(self,name_id,attr,main_bgt,intlg,t):
		self.name_id=name_id
		self.attr=attr
		self.main_bgt=main_bgt
		self.intlg=intlg
		self.t=t
		self.status='single'
		self.happiness=0
		self.bf=''
	'couple formation condition'
	def constraint(self,bgt):
		if(self.main_bgt>bgt):
			return False
		else:
			return True
	'set bf for girl if condition satisfies'
	def set_bf(self,bf):
		self.bf=bf
	'set happiness'
	def set_happiness(self,happiness):
		self.happiness=happiness



