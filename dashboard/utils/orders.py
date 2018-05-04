import os
import sys
import json
import requests
import pprint
import time
from datetime import datetime, timedelta
def convert_date(d):
    EnteredMonth  = int(d.split('/')[0])
    EnteredDay = int(d.split('/')[1])
    EnteredYear = int(d.split('/')[1])
    return int(datetime(EnteredYear,EnteredMonth,EnteredDay,0,0,0,0).timetuple().tm_yday)
def main():
    sid =  requests.post('http://api.msunicloud.com:2404/users/login',data={'username':'developer','password':'Acce55m3'}).json()['id']
    users = requests.get('http://api.msunicloud.com:2404/users/', cookies={'sid':sid}).json()
    orders = requests.get('http://api.msunicloud.com:2404/orders/', cookies={'sid':sid}).json()
    order_data = {}
    for o in orders:
        for u in users:
            userid = o['userid']
            username = ''
            if u['id'] == userid:
                username = u['username']
                break
        if username not in order_data:
            order_data[username] = []
        order_data[username].append({'start': o['startdate']  , 'hashpower':int(o['hashpower'])})
    pprint.pprint( order_data )
    users = {}
    for od in order_data:
        for c in order_data[od]:
            if od not in users:
                users[od] = {'total':0,'contracts':[]}
            if 'total' not in users[od]:
                users[od]['total'] = 0
            if 'contracts' not in users[od]:
                users[od]['contracts'] = []
            users[od] = {'contracts': users[od]['contracts'].append(c) , 'total': (int(users[od]['total']) + int(c['hashpower']))}
    order_data = users
    pprint.pprint( order_data )
if __name__ == '__main__':
    main()
