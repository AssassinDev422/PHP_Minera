import os
import sys
import json
import requests
import smtplib
import datetime
def main():
    sid = sys.argv[1]
    username = sys.argv[2]
    purchasetype = sys.argv[3]
    hashpower = int(sys.argv[4])
    order_contract = {}
    users = requests.get('http://api.msunicloud.com:2404/users/', cookies={'sid':sid}).json()
    orders = requests.get('http://api.msunicloud.com:2404/orders/', cookies={'sid':sid}).json()
    userid = ''
    for u in users:
        if u['username']  == username:
            userid = u['id']
    cost = ''
    price = str(float(hashpower * 200.00)) + '0'
    pricestr = ''
    pricestr = '$' +  str(price)
    daily   = hashpower  *  0.0001731
    monthly = hashpower  *  0.0051920
    yearly  = hashpower  *  0.0631700
    now = datetime.datetime.now()
    startdate = str(str(now).split(' ')[0].split('-')[1] + '/' + str(now).split(' ')[0].split('-')[2] + '/' + str(now).split(' ')[0].split('-')[0])
    order_contract = {'hashpower':hashpower,'contractlink':'...','invoicenumber':len(orders)+1,'userid':userid,'startdate':'','contractlength':24,'cost':cost,'startdate':startdate,'paymenttype':purchasetype,'estimatedday':str(daily),'estimatedmo':str(monthly),'estimatedyr':str(yearly)}
    r = requests.post('http://api.msunicloud.com:2404/orders/', data = order_contract, cookies={'sid':sid})
if __name__ == '__main__':
    main()
