from gift import Gift
class Luxury(Gift):
	def __init__(self,name_id,price,val,type_):
		"""constructor"""
		Gift.__init__(self,name_id,price,val,type_)
