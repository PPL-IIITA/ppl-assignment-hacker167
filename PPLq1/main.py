import csv

from girl import Girl
from boy import Boy
from util import utility
from logs import log_maker
#display couple formation
def display(i,j):
        print(i.name_id + '  committed with '+j.name_id)

utility()
"""arr_b=[]
b=open('./boys.csv')
list_b = csv.reader(b,delimiter = ',')
for i in list_b:
	arr_b+=[Boy(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
arr_g=[]
g=open('./girls.csv')
list_g = csv.reader(g, delimiter = ',')
for i in list_g:
	arr_g+=[Girl(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]"""
#open and read from file
b = open('./boys.csv','r')
bp = csv.reader(b, delimiter = ',')
B = [ Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]) for row in bp]
g = open('./girls.csv')
gp = csv.reader(g, delimiter = ',')
G = [ Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) for row in gp]
"""for i in G:
        print(i.name_id)"""
#algo to check whether girl is committed with any boy or not
#loop check connditions and status of both boy and girl and couple is then made accordingly
for i in  G:
	for j in  B:
		if i.status=='single' and j.status=='single' and i.constraint(j.bgt) and j.constraint(i.main_bgt, i.attr) :
			i.status= 'Committed'
			j.status = 'Committed'	
			display(i,j)
			log_maker(i.name_id + ' committed with ' + j.name_id)
			break #breaks from inner loop as soon as we will make a couple (to avoid multiple couple formation)


