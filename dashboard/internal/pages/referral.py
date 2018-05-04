import os
import sys
import json
import requests
import smtplib
def main():
    email = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    phone_number =  sys.argv[4]
    referralid = sys.argv[5]
    hashpower = sys.argv[6]
    sid =  requests.post('http://api.msunicloud.com:2404/users/login',data={'username':'developer','password':'Acce55m3'}).json()['id']
    r = requests.get('http://api.msunicloud.com:2404/users/'+ referralid ,cookies={'sid':sid}).json()
    user = r
    user['referrals'] = int(user['referrals'])+ int(hashpower)
    r = requests.post('http://api.msunicloud.com:2404/users/'+ referralid ,data = user, cookies={'sid':sid}).json()
    reg_user = {'accounttype':'customer','btcavailible':0,'btchashpower':0,'ltcaddress':'.','dashaddress':'.','btcaddress':'.','referrals':0,'username':username,'email':email,'phone':phone_number,'password':password}
    r = requests.post('http://api.msunicloud.com:2404/users/', data = reg_user, cookies={'sid':sid})
    t = r.json()
    _id = t['id']
    url = 'http://api.msunicloud.com:2404/users/login'
    r = requests.post(url, data = {'username':username,'password':password})
    sid = r.json()['id']
    print sid
if __name__ == '__main__':
    main()
