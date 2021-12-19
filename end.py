# -*- coding: utf-8 -*-
import csv
import copy
from os import X_OK
from mining2 import test
# import hashlib, json

#csvint
filename = 'end.csv'
with open (filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row) #これ文字列

for i in range(len(row)):
    row[i] = int(row[i])

    print(row)
    #for j in range(len(row)):
     #   print(type(row[j]))



#配列のint型が必要
#print(type(row[j]))

#配列の最後だけ取得
nasubi = []
nasubi = copy.copy(row)

print('ああああ')
print(nasubi)

#配列の合計
print(sum(nasubi))

if sum(nasubi) > 0.7
    test()







#print(sum(print(type(row[j]))))
#print(x)
#x =
