from gift import Gift

class Luxury(Gift):
      def __init__(self,name_id,price,val,type_,rating,eco):
                """constructor"""
                Gift.__init__(self,name_id,price,val,type_)
                self.rating=rating
                self.eco=eco
