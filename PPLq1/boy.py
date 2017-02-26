class Boy:
        #constructor for class Boy
	def __init__(self,name_id,attr,bgt,intlg,min_attr,t): 
		self.name_id = name_id
		self.bgt = bgt
		self.t=t
		self.intlg = intlg
		self.attr = attr
		self.min_attr = min_attr
		self.status='single'
        #condition check for couple formation
	def constraint(self,main_bgt,attr):
		if (self.bgt < main_bgt) or (attr < self.min_attr): #if boy budget is less than girl maintenance budget or attractivenes of girl is not equal to min.attraction then no couple formation 
			return False
		else:
			return True
