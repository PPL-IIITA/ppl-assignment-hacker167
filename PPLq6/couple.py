import math
class Couple:
        """constructor for class Couple having object of boy and girl as attribute to make couple"""
        """self is by default used in python as argument"""
        def __init__(self,b,g):
        	self.c_hap=0
        	self.gifts=[]
        	self.compat_status=0
        	self.b=b
		self.g=g
        """define and set level of happiness among couples"""
        def set_happiness(self):
        	a=self.b.happiness
        	b=self.g.happiness
        	self.c_hap=a+b
        'define and set compatibility ampng couples'
        def set_compatibility(self):
        	self.compat_status=(self.b.bgt-self.g.main_bgt)+abs(self.b.attr-self.g.attr)+abs(self.b.intlg-self.g.intlg)
