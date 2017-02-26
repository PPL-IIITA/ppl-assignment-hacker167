class Girl:
        #constructor for class Girl
	def __init__(self,name_id,attr,main_bgt,intlg,t):
		self.name_id = name_id
		self.attr = attr
		self.main_bgt = main_bgt
		self.intlg = intlg
		self.t=t
		self.status = 'single'
	#condition for couple formation
	def constraint(self,bgt):
		if (self.main_bgt > bgt): # if girl maintenance budget is greater than boy budget no couple formation will take place
			return False
		else:
			return True
