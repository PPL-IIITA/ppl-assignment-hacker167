import random
from random import randint
import logging
from q2_log import log_maker
import csv
from q2_cpl import Couple
import math
from q2_boy import Boy
from q2_girl import Girl
from q2_gift import Gift
import pprint
from q2_util import utility


logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')


def hap_cpl(L, k):
                A = sorted(L, key=lambda x: x.compat_status, reverse=True)
                print ('\nCompatible couples:')
                for i in range(k):
                        print (A[i].b.name_id + ' <-> ' + A[i].g.name_id)
                        """sort list H in descending order according to compatibility to find k most compatible couples"""
                B = sorted(L, key=lambda x: x.c_hap, reverse=True)
                print ('\nHappy couples :')
                for i in range(k):
                        print (B[i].b.name_id + ' <-> ' + B[i].g.name_id)
                        """sort list H in descending order according to happiness to find k most happiest  couples"""

def calc_hap(L):
                g = open('./gift.csv')
                gp = csv.reader(g, delimiter = ',')
                GT = [ Gift(row[0],int(row[1]),int(row[2]),row[3]) for row in gp]
                """open gift file and then all write all its content in gifts list"""
                GT = sorted(GT, key=lambda x: x.price)
                """sort given list in ascending order on basis of price"""
                for i in L:
                    while (i.b.bgt<GT[0].price):
                          i.b.mod_bgt(i.b.bgt+100)
                          """condition to check if boy budget is less than min gift cost then increase his budget"""
                    if (i.b.t== 'Generous'):
                        generous(GT, i)
                    elif (i.b.t == 'Miser'):
                        miser(GT, i)
                    elif (i.b.t == 'Geek'):
                                 geek(GT, i)

                details(L)
	
def generous(GT, i):
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
                        if (i.g.t == 'Choosy'):
                                x=x-i.g.main_bgt
                                if (x>0):
                                   i.g.happiness = math.log10(x)

                        elif(i.g.t== 'Normal'):
                                y=y-i.g.main_bgt
                                i.g.happiness = y
                        else:
                                i.g.happiness = math.exp(z%40)
                        """formula for normal sum((gift_cost)+value))-main_cost"""
                        """formula for desperate exp(sum((gift_cost))-main_cost)"""
                        i.b.happiness = i.g.happiness
                        i.set_compatibility()
                        i.set_happiness()

def miser(GT, i):
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
                if (i.g.t == 'Choosy'):
                        x=x-i.g.main_bgt
                        if (x>0):
                           i.g.happiness = math.log10(x)
                
                elif (i.g.t== 'Normal'):
                        y=y-i.g.main_bgt
                        i.g.happiness = y
                
                else:
                        i.g.happiness = math.exp(z%40)
                """formula for normal sum((gift_cost)+value))-main_cost"""
                """formula for desperate exp(sum((gift_cost))-main_cost)"""
                i.b.happiness = i.b.bgt
                i.set_compatibility()
                i.set_happiness()

def geek(GT, i):
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
                if (i.g.t == 'Choosy'):
                        x=x-i.g.main_bgt
                        if (x>0):
                           i.g.happiness = math.log10(x)
         
                elif (i.g.t== 'Normal'):
                        y=y-i.g.main_bgt
                        i.g.happiness = y
                
                else:
                        i.g.happiness = math.exp(z%40)
                """formula for normal sum((gift_cost)+value))-main_cost"""
                """formula for desperate exp(sum((gift_cost))-main_cost)"""
                i.b.happiness = i.g.intlg
                i.set_compatibility()
                i.set_happiness()

def details(L):
	for i in L: 
		"""function to print gift exchange between couple"""
		print ('Gifts given from : ' + i.b.name_id + ' to : ' + i.g.name_id + ':\n') 
		k = randint(1, len(L))
		for j in i.gifts:
			print ( j.name_id + 'Type: ' + j.type_)
		print ('\n')
	"""function call for printing and logging happiest couple and compatible couple"""
	hap_cpl(L,k)
def display(G):
                for i in G:
                    """if i.status == 'single' or i.t== 'Not_committed':
                        print (i.name_id+ ' not_committed.\n')"""
                    if i.status == 'Committed':
                         print (i.name_id + ' committed  ' + i.bf+'\n')
                         
def make_cpl(C):
                L=[]
                for i in C:
                        L += [Couple(i[0],i[1])]
                """ calculate couple happiness"""
                calc_hap(L)
                
def mk_cpl():
                b = open('./boys.csv')
                bp = csv.reader(b, delimiter = ',')
                B = [ Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]) for row in bp] 
                """boys.csv is opened and all its content are wriiten in list B(Boys)"""
                g = open('./girls.csv')
                gp = csv.reader(g, delimiter = ',')
                G = [ Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) for row in gp] 
                """girls.csv is opened and all its content are wriiten in list G(Girls)"""
                C=[] 
                """Empty list of Couples"""
                """algo to make couple
                checks for all boys and girls and whenever suitable match is made corresponding attributes are set """
                for i in  G:
                    for j in  B:
                        if i.status=='single' and j.status=='single' and i.constraint(j.bgt) and j.constraint(i.main_bgt, i.attr) :
                                i.status= 'Committed'
                                j.status = 'Committed'	
                                #display(i,j)
                                j.gf=i.name_id;
                                i.bf=j.name_id;
                                log_maker(i.name_id + ' committed with ' + j.name_id)
                                C+=[(j,i)];
                                """Boy and Girl are added in list to form couple list"""
                                break #we will break from inner loop as soon as a macth is found
                print ('\nLucky_Couples:\n')
                display(G)
                """display couples """
                """function used for checking happiness and compatibility"""
                make_cpl(C) 
                """L=[]
                for i in C:
                        L += [Couple(i[0],i[1])]
                calc_hap(L)#calculate couple happiness"""

utility() #function call to create and write csv file
mk_cpl() #function call for making couple
