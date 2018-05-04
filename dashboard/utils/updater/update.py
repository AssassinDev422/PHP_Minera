import os
import sys
import json
import requests
import time
import csv
import pprint
from datetime import datetime, timedelta
def calculate_dayindex(d):
    EnteredMonth  = int(d.split('/')[0])
    EnteredDay = int(d.split('/')[1])
    EnteredYear = int(d.split('/')[1])
    return int(datetime(EnteredYear,EnteredMonth,EnteredDay,0,0,0,0).timetuple().tm_yday)
def getdatetime(ts):
    return datetime.fromtimestamp(float(ts)).strftime('%m/%d/%Y %H:%M:%S')
def calculate(blockvalue , ph , h):
    float(blockvalue) * 0.98 * float(h) / float(ph)

slushpool = requests.get('https://blockchain.info/blocks/SlushPool?format=json').json()['blocks']
reader = csv.reader(open(os.path.join( os.getcwd() , "idconverter.csv"), "rb"))
tmpreader = {}
for row in reader:
    if row[0] != '':
        tmpreader[row[0]] = row[1]
slushblocks = {}
for s in slushpool:
    time = getdatetime(s['time'])
    blockid = str(s['height'])
    blockdata = requests.get('https://blockchain.info/rawblock/'+ s['hash']).json()
    del blockdata['tx']
    totalreward = int(blockdata['n_tx']) * 0.005 + 12.5
    slushblocks[blockid] = blockdata
reader = csv.reader(open(os.path.join( 'D:/Signing Miners/Minera/api/public/dashboard/utils/template.csv' ), "rb"))
for row in reader:
    if row == ['blockid', 'blockfoundat', 'duration', 'poolhashrate', 'ourhashrate', 'amount', 'totalreward','yourhashrate']:
        continue
