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
print len(main_lis)
#main_lis=map(int,main_lis)
 
'''
quer=[]
for dta in range(len(main_lis)):
    qe=collection.find({"r42product":main_lis[dta]},{"url":1})
    qer=[x for items in qe]
    if qer=='':
        coll_dict={'id':main_list[dta]}
    else:
        quer.append(qer)

print dumps(quer)'''
        
    
 
'''
for i in range(222):
    print i
    row=xl.row(i)
    print row[0]'''
