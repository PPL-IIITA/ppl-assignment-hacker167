import logging
from math import exp, log10

class Gifting:
	'gifting brute force algo'
	def gifting(self, L, GT, choice):
		logging.warning('Gift transfer:\n')
                for i in L:
                    while (i.b.bgt<GT[0].price):
                          i.b.mod_bgt(i.b.bgt+100)
                          """condition to check if boy budget is less than min gift cost then increase his budget"""
                    if (i.b.t== 'Generous'):
                        self.generous(GT, i,choice)
                    if (i.b.t == 'Miser'):
                        self.miser(GT, i,choice)
                    if (i.b.t == 'Geek'):
                         self.geek(GT, i,choice)

        def generous(self,GT, i,choice):
                        x=0
                        y=0
                        z=0
                        """Formula for choosy log10(sum((gift_cost)+2*value)-maint_cost)"""
                        for j in GT:
                                if  (i.b.bgt - j.price > 0) and ((i.b.bgt-j.price <= 400) or (j.price == i.b.bgt) )  :
                                        if (j.type_ == 'Luxury'):
                                                x = x + 2*j.val + j.price
                                        else:
                                                y = y + j.price+j.val
                                        z = z + j.price
                                        i.gifts = i.gifts + [j]
                                        i.b.bgt = i.b.bgt - j.price
                                        logging.info(i.b.name_id + '  gave  ' + i.g.name_id + ' a  Gift:| ' + j.name_id + '| of price =Rs. ' + str(j.price) + '\-.')
                        self.gifting_choice(GT, i, x,y,z, choice, 'Generous')

        def miser(self,GT, i,choice):
                x=0
                y=0
                z=0
                """Formula for choosy log10(sum((gift_cost)+2*value)-maint_cost)"""
                for j in GT:
                        if  (i.b.bgt - j.price > 0) and ((i.b.bgt-j.price <= 150) or (j.price == i.b.bgt) )  :
                                if (j.type_ == 'Luxury'):
                                        x = x + 2*j.val + j.price
                                else:
                                        y = y + j.price+j.val
                                z = z + j.price
                                i.gifts = i.gifts + [j]
                                i.b.bgt = i.b.bgt - j.price
                                logging.info(i.b.name_id + '  gave  ' + i.g.name_id + ' a  Gift:| ' + j.name_id + '| of price =Rs. ' + str(j.price) + '\-.')

                self.gifting_choice(GT, i,x,y,z,choice, 'Miser')

        def geek(self,GT, i,choice):
                x=0
                y=0
                z=0
                """Formula for choosy log10(sum((gift_cost)+2*value)-maint_cost)"""
                for j in GT:
                        if  (i.b.bgt - j.price > 0) and ((i.b.bgt-j.price <= 400) or (j.price == i.b.bgt) )  :
                                if (j.type_ == 'Luxury'):
                                        x = x + 2*j.val + j.price
                                else:
                                        y = y + j.price+j.val
                                z = z + j.price
                                i.gifts = i.gifts + [j]
                                i.b.bgt = i.b.bgt - j.price
                                logging.info(i.b.name_id + '  gave  ' + i.g.name_id + ' a  Gift:| ' + j.name_id + '| of price =Rs. ' + str(j.price) + '\-.')
                self.gifting_choice(GT, i,x,y,z,choice, 'geek')

        def gifting_choice(self, GT, i, x, y,z,choice, btype):
		'choice 1 :-default choice 2:-user defined'
		if (choice == 2):
			v1 = 0
			v2 = 0
			v3 = 0
			for g in i.gifts:
				if (g.type_ == 'Essential'):
					v1 = v1 + 1
				elif (g.type_ == 'Luxury'):
					v2 = v2 + 1
				else:
					v3 = v3 + 1
			if (v1 == 0):
				for g in GT:
					if (g.type_ == 'Essential'):
						z = z + g.price
						y= y+g.price+g.val
						i.gifts = i.gifts + [g]
						break
			if (v2 == 0):
				for g in GT:
					if (g.type_ == 'Luxury'):
						x = x + 2*g.val+g.price
						y = y + g.price+g.val
						z=z+g.price
						i.gifts = i.gifts + [g]
						break

			if (v3 == 0):
				for g in GT:
					if (g.type_ == 'Utility'):
						z = z + g.price
						y = y + g.price
						i.gifts = i.gifts + [g]
						break


		if (i.g.t == 'Choosy'):
                        x=x-i.g.main_bgt
                        if (x>0):
                           i.g.happiness = log10(x)
         
                elif (i.g.t== 'Normal'):
                             y=y-i.g.main_bgt
                             i.g.happiness = y
                
                else:
                             i.g.happiness = exp(z%40)
                """formula for normal sum((gift_cost)+value))-main_cost"""
                """formula for desperate exp(sum((gift_cost))-main_cost)"""
                i.b.happiness = i.g.intlg
                i.set_compatibility()
                i.set_happiness()
                                
