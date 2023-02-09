# -*- coding:utf-8 -*-
import os
import csv
import json
#---------不用pandas库手写，filename写你自己的--------------
#定义一个写入函数
def csv_write(path,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f,dialect='excel')
        for row in data:
            writer.writerow(row)
    return True
filename="index.json"
with open(filename) as f:
  trump_list=json.load(f)
data=[]
for line in trump_list:
  value_list=list(line.values())
  data.append(value_list)
csv_write("trump_meet2.csv",data)