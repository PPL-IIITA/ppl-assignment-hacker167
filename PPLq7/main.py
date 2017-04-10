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
from q7_utility import utility
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
def method1(B,G,BL):
	"""USE OF LIST to form couple"""
	C = []
	for i in G:
		for j in B:
			logging.info('Commitment:  Girl: ' + i.name_id + '  is checking out  Boy: ' + j.name_id)
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
        L=[]
        for i in C:
                L += [Couple(i[0],i[1])]
	CB = []
	for i in L:
		CB.append(i.b.name_id)

	for i in BL:
		if (i in CB):
			for j in L:
				if (j.b.name_id == i):
					print i + ' gf - ' + j.g.name_id
					break

def method2(B,G,BL):
	"""USE OF LIST(sorted) to form couple"""
	C = []
	for i in G:
		for j in B:
			logging.info('Commitment:  Girl: ' + i.name_id + '  is checking out  Boy: ' + j.name_id)
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
                
        L=[]
        for i in C:
                L += [Couple(i[0],i[1])]
        L=sorted(L, key=lambda item: item.b.name_id)
	CB = []
	for i in L:
		CB.append(i.b.name_id)
        """Performing linear search"""
	for i in BL:
		if (i in CB):
			for j in L:
				if (j.b.name_id == i):
					print i + ' gf - ' + j.g.name_id
					break

def method3(B,G,BL):
	"""USE OF HASH to store and form couple"""
	for i in G:
		for j in B:
			logging.info('Commitment:  Girl: ' + i.name_id + '  is checking out  Boy: ' + j.name_id)
			if i.status=='single' and j.status=='single' and i.constraint(j.bgt) and j.constraint(i.main_bgt, i.attr) :
                    		i.status= 'Committed'
                    		j.status = 'Committed'	
                    		#display(i,j)
                    		j.gf=i.name_id;
                    		i.bf=j.name_id;
                    		log_maker(i.name_id + ' committed with ' + j.name_id)
                    		"""Boy and Girl are added in list to form couple list"""
                    		break #we will break from inner loop as soon as a macth is found
	"""HASH DATASTRUCTURE"""
	hash={}
       	for i in B:
		if (i.status=='commited'):
			hash.update({i.name_id : i.gf})
		else:
			hash.update({i.name_id : 'none'})

	for i in BL:
		if (hash[i] != 'none'):
			print i + ' gf - ' + hash[i]

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
	for b in B:
		C.append(b.name_id)
	k = randint(1, len(C))
        BL= random.sample(C, k)#from list C we are choosing random k boy names and appending it in Boy list
	#print(len(G))
	#print(k)
        print 'Given Boys list:'
	for b in BL:
	    print b
        print '\n'

        print 'Choose Allocator method : \n1)List\n2)Sorted List\n3)Hash Table\n'
	choice = randint(1,100)
	choice=choice%3
	#print(choice)
	print '\nGirlfriends for given boys:'
	if (choice == 0):
		method1(B, G, BL)
	elif (choice == 1):
		method2(B, G, BL)
	else:
		method3(B, G, BL)

utility() #function call to create and write csv file
mk_cpl() #function call for making couple
