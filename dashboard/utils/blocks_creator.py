#!/usr/bin/env python
import os
import sys
import json
import requests
import time
from datetime import datetime, timedelta
import csv
r = requests.post('http://api.msunicloud.com:2404/users/login', data = {'username':'developer','password':'Acce55m3'})
sid =r.json()['id']
o = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid})
orders = {}
for order in o.json():
    if order['userid'] not in orders:
        orders[order['userid']] = order
    else:
        orders[order['userid']] = order
b = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
for b2 in b:
    print b2 , requests.delete('http://api.msunicloud.com:2404/blocks/' + b2['id'],data = b2, cookies = {'sid':sid}).json()
reader = csv.reader(open(os.path.join( os.getcwd() , "idconverter.csv"), "rb"))
tmpreader = {}
for row in reader:
    if row[0] != '':
        print row
        tmpreader[row[0]] = row[1]
reader = csv.reader(open(os.path.join( os.getcwd() , "Ledger.csv"), "rb"))
transactions = []
for row in reader:
    if row == ['blockid', 'blockfoundat', 'duration', 'poolhashrate', 'ourhashrate', 'amount', 'totalreward']:
        continue
    print row
    data = {'blockid':str(tmpreader[row[0]]),'datefound':str(row[1]),'miningduration':str(row[2]),'poolhashrate':str(row[3]),'ourhashrate':str(row[4]),'reward':str(row[5]),'totalreward':str(row[6]),'type':'mined','cointype':'btc','coinprice':'0'}
    print data
    transactions.append( data )
b = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
blocks = []
for tb in b:
    blocks.append(tb['datefound'])
b = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid})
for t in transactions:
    if t['datefound'] not in blocks:
        r = requests.post('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid},data=t)
        print r.json()
