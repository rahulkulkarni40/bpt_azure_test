# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:43:34 2020

@author: Rahul
"""

from azure.storage.table import TableService, Entity
import pandas as pd

acc_name = 'cloudshell1616726778'
acc_key = 'EN22MEbUMKghbQ14H7VxdX7Ij2mae8X8hMobGkRgpSGhFtfVoaOnywW5mYeOwoDLPFgytiwyIdpbCAe9gd82Gg==' 
def connection(tasks,query,types):
    table_service = TableService(account_name= acc_name, account_key=acc_key)
    table_service.create_table('customer')
    if types == "insert":
        print(tasks)
        table_service.insert_entity('customer', tasks)
        return "added Successfully!!!!"
    elif types == "reterive":
        #print(query)
        tasks = table_service.query_entities('customer', filter=query)
        #print(tasks)
        df = pd.DataFrame(df_con(tasks))
        data1 = df.to_json(orient='records')
        #print(data1)
        return data1
    
def df_con(tasks):
    for task in tasks:
        yield task