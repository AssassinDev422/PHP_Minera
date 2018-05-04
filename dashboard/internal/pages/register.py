import os
import sys
import json
import requests
import smtplib
def main():
    sid = sys.argv[1]
    email = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    phone_number =  sys.argv[5]
    hashpower = sys.argv[6]
    reg_user = {'referrals':0,'btcavailible':0,'username':username,'email':email,'phone':phone_number,'password':password,'btchashpower':hashpower,'btcaddress':'.','ltcaddress':'.','dashaddress':'.','accounttype':'customer'}
    r = requests.post('http://api.msunicloud.com:2404/users/', data = reg_user, cookies={'sid':sid})
    t = r.json()
    _id = t['id']
if __name__ == '__main__':
    main()
