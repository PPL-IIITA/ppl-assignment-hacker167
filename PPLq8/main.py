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
from q8_utility import utility
from choosy import choosy
from desperate import desperate
from normal import normal
from geek import Geek
from generous import Generous
from miser import Miser
from essential import Essential
from luxury import Luxury
from utility import Utility
from gifting import Gifting

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
                GT = []
                for row in gp:
			if (row[3] == 'Essential'):
				GT.append(Essential(row[0], int(row[1]), int(row[2]), row[3]))
			elif (row[5] == 'Luxury'):
				GT.append(Luxury(row[0], int(row[1]), int(row[2]), row[3], int(row[4]), int(row[5])))
			elif(row[5]=='Utility'):
				GT.append(Utility(row[0], int(row[1]), int(row[2]), row[3], int(row[4]), int(row[5])))                    
                """open gift file and then all write all its content in gifts list"""
                GT = sorted(GT, key=lambda x: x.price)
                """sort given list in ascending order on basis of price"""
		print 'Choose your Gifting method:\n1 - Default Method\n2 - New method'
		choice=randint(1,2)
		print '\n'
		a = Gifting()
		a.gifting(L, GT,choice)
		details(L)       
                

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
		#print(len(L))
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
