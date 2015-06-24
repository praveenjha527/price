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
#print main_lis
#
#main_lis=map(int,main_lis)
__raw__=[{'$group':{'_id':'$r42product','url':{'$addToSet':'$url'}}}]
result=collection.aggregate(__raw__)
#print result


d={}
for item in result['result']:
    d[item['_id']]=item['url']
k=[]
not_exist=[]
for da in range(len(main_lis)):
    if d.has_key(main_lis[da]):
        k.append({'id':main_lis[da],'url':d[main_lis[da]]})
    else:
        not_exist.append({'id':main_lis[da]})


def final():
    final_list=[]
    for key_dict in k:
        for item in key_dict['url']:
            final_list.append({key_dict['id']:item})
    return final_list



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