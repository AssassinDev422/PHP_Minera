import os
import sys
import json
import requests
import time
from datetime import datetime, timedelta
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
