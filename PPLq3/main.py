import random
from random import randint
import logging
from log import log_maker
import csv
from couple import Couple
import math
from boy import Boy
from girl import Girl
from gift import Gift
import pprint
from q3_utility import utility
from choosy import choosy
from desperate import desperate
from normal import normal
from geek import Geek
from generous import Generous
from miser import Miser
from essential import Essential
from luxury import Luxury
from utility import Utility


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
	g=open('./gift.csv')
	gp=csv.reader(g,delimiter=',')
	GT=[]
	for row in gp:
		if(row[3]=='Essential'):
			GT.append(Essential(row[0],int(row[1]),int(row[2]),row[3]))
		elif(row[3]=='Luxury'):
			GT.append(Luxury(row[0],int(row[1]),int(row[2]),row[3],int(row[4]),int(row[5])))
		else:
			GT.append(Utility(row[0],int(row[1]),int(row[2]),row[3],int(row[4]),int(row[5])))
	'Open gift file and write its content in gift list'
	GT=sorted(GT,key=lambda x: x.price)
	'sort list in ascending order of price'
	for i in L:
		while(i.b.bgt<GT[0].price):
			i.b.mod_bgt(i.b.bgt+100)
	if(i.b.t=='Generous'):
		generous(GT,i)
	elif(i.b.t=='Miser'):
		miser(GT,i)
	elif(i.b.t=='Geek'):
		geek(GT,i)

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
		L+=[Couple(i[0],i[1])]
        #print(len(L))
	'cal happiness'
	calc_hap(L)
                         
def mk_cpl():
	b=open('./boys.csv')
	B=[]
	bp=csv.reader(b,delimiter=',')
	for row in bp:
		if(row[5]=='Miser'):
			B.append(Miser(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))
		elif(row[5]=='Generous'):
			B.append(Generous(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))
		elif(row[5]=='Geek'):
			B.append(Geek(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))
	g=open('./girls.csv')
	G=[]
	gp=csv.reader(g,delimiter=',')
	for row in gp:
		if(row[4]=='Choosy'):
			G.append(choosy(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))
		elif(row[4]=='Desperate'):
			G.append(desperate(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))
		elif(row[4]=='Normal'):
			G.append(normal(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))
	C=[]
	'Empty list of couples'
	'ALGO to form couple'
	for i in G:
		for j in B:
			if i.status=='single' and j.status=='single' and i.constraint(j.bgt) and j.constraint(i.main_bgt,i.attr):
				i.status='Committed'
				j.status='Committed'
				j.gf=i.name_id
				i.bf=j.name_id
				log_maker(i.name_id+'committed with '+j.name_id)
				C+=[(j,i)]
				break#boys and girls are added in couple list and is breaked when we found a match
	print('\nLucky Couples :\n')
	display(G)
	'display couple'
	'function for checking happiness and compatibility'
	make_cpl(C)

utility() #function call to create and write csv file
mk_cpl() #function call for making couple
