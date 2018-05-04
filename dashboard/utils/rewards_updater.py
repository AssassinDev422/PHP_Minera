import os
import sys
import json
import requests
import time
from datetime import datetime, timedelta
r = requests.post('http://api.msunicloud.com:2404/users/login', data = {'username':'developer','password':'Acce55m3'})
sid =r.json()['id']
def convert_date(d):
    EnteredMonth  = int(d.split('/')[0])
    EnteredDay = int(d.split('/')[1])
    EnteredYear = int(d.split('/')[1])
    return int(datetime(EnteredYear,EnteredMonth,EnteredDay,0,0,0,0).timetuple().tm_yday)
def delete_all_rewards():
    rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}).json()
    for r in rewards:
        print r , requests.delete('http://api.msunicloud.com:2404/rewards/' + r['id'], cookies = {'sid':sid}).json()
def get_blocks(idstr):
    blocks = []
    le = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid}).json()
    contracts = []
    for l in le:
        days = convert_date(l['startdate'])
        if l['userid'] == idstr:
            contracts.append(days)
    startindex = sorted(contracts)[0]
    tmpblocks = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
    for b in tmpblocks:
        days = convert_date(b['datefound'])
        if startindex <= days:
            blocks.append(b)
    return blocks
def get_rewardhistogram(idstr):
    data_blocks = get_blocks(idstr)
    ledger = get_ledger(idstr)
    rewards = []
    summer = 0
    for db in data_blocks:
        days = convert_date(db['datefound'])
        for l in ledger:
            if l['index'] <= days:
                E =  float( db['reward'] ) * int(l['hashpower'])
                E = E / float(  l['totalhashrate'] )
                #print db['reward'], l['hashpower'] , l['totalhashrate'] , E
                rewards.append( E )
                summer = summer + float( E )
    print summer
    return rewards
def get_ledger(idstr):
    histogram = []
    le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
    for l in le:
        if 'userids' not in l:
            continue
        uis =  json.loads(l['userids'])
        for u in uis:
            if 'idstr' not in uis[u]:
                continue
            if uis[u]['idstr'] == idstr:
                d = {'index':uis[u]['day'] , 'hashpower': uis[u]['hashpower'],'totalhashrate':l['totalhashrate']}
                histogram.append( d  )
    histogram = [dict(s) for s in set(frozenset(d.items()) for d in histogram)]
    return histogram
def get_totalhistogram(noval=True):
    histogram = []
    le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
    for l in le:
        h = int(l['totalhashrate'])
        histogram.append(h)
    return histogram
def get_histogram(idstr):
    histogram = []
    le = requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json()
    for l in le:
        if 'userids' in l:
            if idstr in l['userids']:
                contracts = json.loads( l['userids'] )
                th = 0
                for c in contracts:
                    if 'hashpower' not in contracts[c]:
                        continue
                    if idstr == contracts[c]['idstr']:
                        th += int(contracts[c]['hashpower'])
                histogram.append(th)
    return histogram
