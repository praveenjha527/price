import xlrd
import os 
import json
from pymongo import MongoClient
from bson.json_util import dumps
 
client = MongoClient('mongodb://localhost:27017/')
 
wb=xlrd.open_workbook("mrp_list.xlsx")
db=client.pricedelta
collection=db.pricedata
 
sheet=wb.sheet_names()
'''
for i in range(14):
    s=wb.sheet_by_name(sheet[i])
    print s'''
li=[]
for i in range(14):
    xl=wb.sheet_by_index(i)
    #print ('Sheet name: %s' % xl.name)
    k=xl.nrows
    for j in range(k):
        row=xl.row(j)
        #print row[0]
        li.append(row[0])
#print li
main_lis=[]
li=map(str,li)
for k in range(len(li)):
    main_lis.append(li[k].strip('number:.0'))
print main_lis
#main_lis=map(int,main_lis)

result=collection.aggregate(__raw__={$group:{'_id':'$r42product','url':{$addToSet:'$url'}}})
print result
