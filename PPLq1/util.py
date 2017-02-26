import csv
from random import randint
from random import choice
import random
#test case generator 
def utility():
	
	boy_t = ['Miser','Generous','Geek','Not_committed'] #list of type of boys
	arr_b=[]
	girl_t = ['Choosy','Normal','Desperate'] #list of type of girls
	arr_g=[]
	for i in range (0,500):
		arr_b+= [('boy_'+str(i),randint(0,100),randint(0,3000),randint(0,100),randint(0,10), choice(boy_t))]
	make_csv('./boys.csv',arr_b)#create csv file of boys
	for i in range (0,50):
	    arr_g+=[('girl_'+str(i),randint(0,120),randint(0,2500),random.randint(0,90), choice(girl_t))]
	make_csv('./girls.csv',arr_g)#create csv file of girls
#function that open and write into file
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
