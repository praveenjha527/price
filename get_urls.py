import xlrd
import os 
import json
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('mongodb://localhost:27017/')
wb=xlrd.open_workbook("delhi.xlsx")

db=client.pricedelta
collection=db.pricedata


list_of_ids=[]
xl=wb.sheet_by_index(0)

for i in range(xl.nrows):
	row=xl.row(i)
	list_of_ids.append(row[0])


main_lis=[]
list_of_ids=map(str,list_of_ids)
for k in range(len(list_of_ids)):
    main_lis.append(list_of_ids[k].strip('number:.0'))

#print len(main_lis)

__raw__=[{'$group':{'_id':'$r42product','url':{'$addToSet':'$url'}}}]
result=collection.aggregate(__raw__)


d={}
for item in result['result']:
    d[item['_id']]=item['url']

k=[]
not_exist=[]
for da in range(len(main_lis)):
    if d.has_key(main_lis[da]):
        k.append({'id':main_lis[da],'url':d[main_lis[da]]})
    else:
        not_exist.append(main_lis[da])


def final():
    final_list=[]
    for key_dict in k:
        for item in key_dict['url']:
            final_list.append({key_dict['id']:item})
    return final_list


final()