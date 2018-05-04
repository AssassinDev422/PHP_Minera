#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
import time
import csv
def calculate_dayindex(d):
    EnteredMonth  = int(d.split('/')[0])
    EnteredDay = int(d.split('/')[1])
    EnteredYear = int(d.split('/')[1])
    return int(datetime(EnteredYear,EnteredMonth,EnteredDay,0,0,0,0).timetuple().tm_yday)

index = 0
r = requests.post('http://api.msunicloud.com:2404/users/login', data = {'username':'developer','password':'Acce55m3'})
sid =r.json()['id']
# Clear out the Ledger of User Contract data
l = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
for la in l:
    print la, requests.delete('http://api.msunicloud.com:2404/ledger/' + la['id'], data = la, cookies = {'sid':sid}).json()
dom = [31,28,31,30,31,30,31,31,30,31,30,31]
for month in range(0,12):
    for i in range(1 , dom[month]  + 1 ):
        cd = calculate_dayindex(str( month + 1) + '/' + str(i) + '/2017')
        tmp = {'day':i,'month':(month + 1),'year':2017,'index' : cd , 'userids':[]}
        print tmp, requests.post('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}, data=tmp).json()
contracts = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid}).json()
contractor_data = {}
for c in contracts:
    days = calculate_dayindex(c['startdate'])
    if c['userid'] not in contractor_data:
        contractor_data[c['id']] = [{'idstr':c['userid'],'day':days,'hashpower':c['hashpower']}]
    else:
        contractor_data[c['id']].append({'idstr':c['userid'],'day':days,'hashpower':c['hashpower']})
le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
for l in le:
    mo = l['month']
    day = l['day']
    year = l['year']
    days = calculate_dayindex(str( mo) + '/' + str(day) + '/' + str(year))
    if 'userids' not in l:
        contracts = {}
    else:
        contracts = json.loads(l['userids'])
    for c in contractor_data:
        if c not in contracts:
            contracts[c] = {}
        for co in contractor_data[c]:
            userid = co['idstr']
            contract_day = co['day']
            if contract_day <= days:
                contracts[c] = co
                if 'userids' in l:
                    l['userids'] = ''
                l['userids'] = json.dumps( contracts )
                print requests.put('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}, data=l).json()
le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
for l in le:
    if 'userids' not in l:
        l['totalhashrate'] = 0
        print requests.put('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}, data=l).json()
    else:
        contracts = json.loads( l['userids'] )
        th = 0
        for c in contracts:
            if 'hashpower' not in contracts[c]:
                continue
            th += int(contracts[c]['hashpower'])
        l['totalhashrate'] = th
        print requests.put('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}, data=l).json()
#Now Update The Blocks
sid = requests.post('http://api.msunicloud.com:2404/users/login' , data={ 'username':'developer' , 'password':'Acce55m3' }).json()['id']
blocks = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
saved_blocks = {}
for b in blocks:
    saved_blocks[b['blockid']] = b
price = requests.get('https://blockchain.info/ticker').json()['USD']
new_blocks = requests.get('https://slushpool.com/stats/json/1697720-7902793772e814218b795a5b2c49dffe').json()
hr = float(new_blocks['ghashes_ps'].split('e')[0]) * 1000
hr = int(hr)
to_update = []
for b in new_blocks['blocks']:
    if b not in saved_blocks :
        df = new_blocks['blocks'][b]['date_found'].replace('-','/').split(' ')
        df1 = df[0]
        df2 = df[1]
        yr = df1.split('/')[0]
        mo = df1.split('/')[1]
        day = df1.split('/')[2]
        datefound = mo +'/' + day + '/' + yr + ' ' + df[1]
        duration = str(timedelta(seconds=int(new_blocks['blocks'][b]['mining_duration'])))
        blockdata = requests.get('https://blockchain.info/rawblock/'+ new_blocks['blocks'][b]['hash']).json()
        totalreward = float(float(blockdata['fee']) + 12.5)
        le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
        ohr = ''
        ledge = ''
        for l in le:
            if str(l['index']) == str(calculate_dayindex(mo +'/' + day + '/' + yr)):
                ohr = int(l['totalhashrate'])
                ledge = l
        reward =  float(totalreward) * 0.98 * float(ohr) / float( float(  hr  ) * 1000 )
        rawstr = {'blockid':b,'datefound':datefound,'miningduration':duration,'poolhashrate':hr,'ourhashrate':ohr,'reward':reward, 'totalreward':totalreward,'type':'mined','cointype':'btc','coinprice':price['last']}
        to_update.append(rawstr)
print len( to_update )
for tu in to_update:
    print tu , requests.post('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}, data= tu).json()
# Delete Rewards :
rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}).json()
for r in rewards:
    print r , requests.delete('http://api.msunicloud.com:2404/rewards/' + r['id'], cookies = {'sid':sid}).json()
# Calculate User Rewards:
blocks = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
for b in blocks:
    df = b['datefound'].split(' ')[0]
    index = calculate_dayindex( df )
    for l in le:
        if str(l['index']) == str(index):
            E = float(b['totalreward']) * 0.98 * float(l['totalhashrate']) / float(float( b['poolhashrate']  ) * 1000 )
            b['reward'] = E
            print b , requests.post('http://api.msunicloud.com:2404/blocks/' + b['id'], cookies = {'sid':sid} , data=b).json()
for b in blocks:
    df = b['datefound'].split(' ')
    index = calculate_dayindex( df )
    ohr = ''
    ledge = ''
    for l in le:
        if str(l['index']) == str(index):
            users = json.loads(l['userids'])
            for u in users :
                hp = users[u]['hashpower']
                tr = float(b['reward']) * 0.98 * int(hp) / float( b['ourhashrate'] )
                print u , tr , hp



users = requests.get('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}).json()
for u in users:
    if u['username'] not in user_totals:
        continue
    u['btcavailible'] = user_totals[u['username']]
    requests.post('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}, data = u).json()
b = requests.get('http://api.msunicloud.com:2404/cashout', cookies = {'sid':sid}).json()
for c in b:
    user = requests.get('http://api.msunicloud.com:2404/users/' + c['userid'], cookies = {'sid':sid}).json()
    user['btcavailible'] = float(user['btcavailible']) - float(c['amount'])
    requests.post('http://api.msunicloud.com:2404/users/' + user['id'], cookies = {'sid':sid}, data=user).json()
