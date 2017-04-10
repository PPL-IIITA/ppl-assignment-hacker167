import csv
from random import randint
from random import choice
import random
"""create files boys,girls and gifts by inputting random values"""
def utility():
	"""boy type"""
	boy_t = ['Miser','Generous','Geek','Not_committed']
	arr_b=[]
	arr_b=[('boy_'+str(i),randint(0,100),randint(0,3000),randint(0,100),randint(0,10), choice(boy_t))for i in range (0,500)]
	make_csv('./boys.csv',arr_b)#create boys.csv
	"""girl type"""
	girl_t = ['Choosy','Normal','Desperate','Not_committed']
	arr_g=[]
	arr_g=[('girl_'+str(i),randint(0,120),randint(0,2500),random.randint(0,90), choice(girl_t))for i in range (0,50)]
	make_csv('./girls.csv',arr_g)#create girls.csv
	arr_gft=[]
	"""gift type"""
	gift_t = ['Essential','Luxury','Utility']
	for i in range(55):
		c = choice(gift_t)
		if (c == 'Essential'):
			arr_gft.append(['Gift_'+str(i),randint(0,2600),randint(0,100), c])
		else:
			arr_gft.append(['Gift_'+str(i), randint(0,2600),randint(0,100), c, randint(1,15),randint(1,15)])
	make_csv('./gift.csv',arr_gft)#create gift.csv
"""create function for file creation by opening file using file pointer and then writing data from list"""
def make_csv(name,list_):
 filepointer = open(name, 'w')
 wr = csv.writer(filepointer, delimiter = ',')
 for i in list_:
    wr.writerow(i)
 filepointer.close()
"""with open('name', 'w') as myfile:
       wr = csv.writer(myfile, delimiter =',' ,quoting=csv.QUOTE_ALL)
       for i in list_:
          wr.writerow(i)"""

utility() 
