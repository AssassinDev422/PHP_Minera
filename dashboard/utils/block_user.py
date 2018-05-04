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
rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}).json()
userid = '509b02bedab5db0c'
for r in rewards:
    if str(r['userid']) ==userid:
        print r , requests.delete('http://api.msunicloud.com:2404/rewards/' + r['id'], cookies = {'sid':sid}).json()
o = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid})
orders = {}
for order in o.json():
    if order['userid'] not in orders:
        orders[order['userid']] = order
    else:
        orders[order['userid']] = order
b = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid})
reader = csv.reader(open(os.path.join( os.getcwd() , "idconverter.csv"), "rb"))
tmpreader = {}
for row in reader:
    if row[0] != '':
        print row
        tmpreader[row[0]] = row[1]
user_totals = {}
datadir = 'D:/Signing Miners/Ledger'
files = ['ScottDeden.csv']
for f in files:
    username = f.replace('.csv','')
    user_totals[username] = 0
    idstr = ''
    users = requests.get('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}).json()
    for u in users:
        if u['username'] == username:
            idstr = u['id']
    src = os.path.join( datadir , f )
    reader = csv.reader(open(os.path.join( src ), "rb"))
    transactions = []
    totalreward = 0
    for row in reader:
        if row == ['blockid', 'blockfoundat', 'duration', 'poolhashrate', 'ourhashrate', 'amount', 'totalreward','yourhashrate']:
            continue
        print row
        data = {'userid':idstr,'blockid':str(tmpreader[row[0]]),'datefound':str(row[1]),'miningduration':str(row[2]),'poolhashrate':str(row[4]),'ourhashrate':str(row[7]),'reward':str(row[5]),'totalreward':str(row[6]),'type':'mined','cointype':'btc','coinprice':'0'}
        transactions.append( data )
        print data , requests.post('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}, data = data).json()
        print os.path.join( src )
        user_totals[username] += float(row[5])
users = requests.get('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}).json()
for u in users:
    if u['username'] not in user_totals:
        continue
    u['btcavailible'] = user_totals[u['username']]
    requests.post('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}, data = u).json()
