from gift import Gift
class Utility(Gift):
	def __init__(self,name_id,price,val,type_,uval,uclass):
		"""constructor"""
		Gift.__init__(self,name_id,price,val,type_)
		self.uval=uval
		self.uclass=uclass
