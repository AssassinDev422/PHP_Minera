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
price = requests.get('https://blockchain.info/ticker').json()['USD']
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
le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
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
        hashed =  new_blocks['blocks'][b]['hash']
        try:
            blockdata = requests.get('https://blockchain.info/rawblock/'+hashed).json()
        except:
            continue
        totalreward = float(float(blockdata['n_tx'])*0.001 + 12.5)
        ohr = ''
        ledge = ''
        for l in le:
            if str(l['index']) == str(calculate_dayindex(mo +'/' + day + '/' + yr)):
                ohr = int(l['totalhashrate'])
                ledge = l
        reward =  float(totalreward) * 0.98 * float(ohr) / float(float(  hr   ) * 1000 )
        rawstr = {'blockid':b,'datefound':datefound,'miningduration':duration,'poolhashrate':hr,'ourhashrate':ohr,'reward':reward, 'totalreward':totalreward,'type':'mined','cointype':'btc','coinprice':price['last']}
        to_update.append(rawstr)
print len( to_update )
for tu in to_update:
    print tu , requests.post('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}, data= tu).json()
# Delete Rewards :
rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}).json()
for r in rewards:
    print requests.delete('http://api.msunicloud.com:2404/rewards/' + r['id'], cookies = {'sid':sid}).json()
# Calculate User Rewards:
blocks = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
user_totals = {}
for b in blocks:
    df = b['datefound'].split(' ')
    index = calculate_dayindex( df[0] )
    ohr = ''
    ledge = ''
    for l in le:
        if str(l['index']) == str(index):
            contracts = json.loads(l['userids'])
            for co in contracts:
                if 'hashpower' not in contracts[co]:
                    continue
                hp = contracts[co]['hashpower']
                tr = float(b['reward']) * int(hp) / float( b['ourhashrate'] )
                tu = {'userid':contracts[co]['idstr'],
                      'blockid':b['blockid'],
                      'datefound':b['datefound'],
                      'miningduration':b['miningduration'],
                      'poolhashrate':l['totalhashrate'],
                      'ourhashrate':hp,
                      'reward':tr,
                       'totalreward':b['reward'],
                       'type':'mined',
                       'cointype':'btc',
                       'coinprice':price['last']}
                print tu, requests.post('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}, data= tu).json()
reward_data = {}
user_totals = {}
users = requests.get('http://api.msunicloud.com:2404/users/' , cookies = {'sid':sid}).json()
user_idstr = []
for u in users:
    user_idstr.append( u['id'] )
for r in requests.get('http://api.msunicloud.com:2404/rewards/', cookies = {'sid':sid}).json():
    idstr = r['userid']
    if idstr not in user_idstr:
        continue
    reward = r['reward']
    if idstr not in reward_data:
        reward_data[idstr] = []
    print reward
    reward_data[idstr].append( float(reward) )
username_data = {}
for u in reward_data:
    if u not in username_data:
        username_data[u] = 0
    if u not in reward_data:
        continue
    username_data[u] =  sum(reward_data[u])
users = requests.get('http://api.msunicloud.com:2404/users/' , cookies = {'sid':sid}).json()
for user in users:
    idstr = user['id']
    username = user['username']
    if username not in user_totals:
        user_totals[username] = float(0)
    user_totals[username] = float(user['btcavailible'])
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
