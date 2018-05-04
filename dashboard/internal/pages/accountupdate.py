import os
import sys
import json
import requests
import smtplib
def main():
    sid = sys.argv[1]
    url = 'http://api.msunicloud.com:2404/users/me'
    r = requests.get(url , cookies={'sid':sid})
    user = r.json()
    # $command = 'python accountupdate.py' . ' ' . $sid . ' ' . $email . ' ' . $username . ' ' . $password . ' ' . $phone . ' ' . $wallet;
    user['email'] = sys.argv[2]
    user['username'] = sys.argv[3]
    user['password'] = sys.argv[4]
    user['phone'] =  sys.argv[5]
    user['btcaddress'] = sys.argv[6]
    user['ltcaddress'] = sys.argv[7]
    user['dashaddress'] = sys.argv[8]
    r = requests.put('http://api.msunicloud.com:2404/users/', data = user, cookies={'sid':sid})
    t = r.json()
    _id = t['id']
    '''
    server = smtplib.SMTP('smtp.signingminers.com', 587)
    server.ehlo()
    server.starttls()
    server.login("cloud@signingminers.com", "cloudMiner5")
    header = 'To:' + email + '\n' + 'From: ' + 'cloud@signingminers.com'  + '\n' + 'Subject:cloud Signup \n'
    msg = header + '\n username : '+ username + ' , password : ' + password + ', unique ID : ' + _id  + ' \n\n'
    server.sendmail("cloud@signingminers.com", email, msg)
    server.quit()
    '''
    url = 'http://api.msunicloud.com:2404/users/login'
    r = requests.post(url, data = {'username':username,'password':password})
    sid = r.json()['id']
    print sid
if __name__ == '__main__':
    main()
