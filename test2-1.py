#!/usr/bin/python
# -*- coding:utf8 -*-


# SList=[5,6,3,4,8,1,9,0,2]
# SList.sort();
# for i in range(len(SList))[::-1]:
#     print SList[i]
#
# SList=[5,6,3,4,8,1,9,0,2]
# for i in range(len(SList)-1):
#     for j in range(len(SList)-1-i):
#         if SList[j]<SList[j+1]:
#             SList[j],SList[j+1]=SList[j+1],SList[j]
# print SList

import json
x={'160501':'1','1260502':'1','160503':'1','160509':'0'}
y=json.dumps(x) #将x转为字符串
f=open('chapter.json','w')
json.dump(x,f) #dump需传两个参数，第一个为字典，第二个为相应的文件
f.close()

print x['160501']
