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
    # $command = 'python cashout_proc.py' . ' ' . $sid . ' ' . $email . ' ' . $username . ' ' . $password . ' '. $phone . ' ' . $wallet;
    password = sys.argv[5]
    user['btcaddress'] = sys.argv[6]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sales@signingminers.com", "Acce55m3")
    header = 'To:' + user['email'] + '\n' + 'From: ' + 'support@signingminers.com'  + '\n' + 'Subject:Minera Password Reset \n'
    msg = header + '\n  You have requested to be cashed out , we will be in touch with you shortly to confirm the amount and destination address. \n\n'
    server.sendmail("sales@signingminers.com", user['email'], str(msg))
    server.quit()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sales@signingminers.com", "Acce55m3")
    header = 'To:' + user['email'] + '\n' + 'From: ' + 'support@signingminers.com'  + '\n' + 'Subject:Minera Password Reset \n'
    msg = header + '\n  User ' + user['username'] + ' has requested to be cashed out. \n Please contact via : ' + user['email']+ ' or ' + user['phone']+ ' to confirm the request and amount. \n\n'
    server.sendmail("sales@signingminers.com", 'support@signingminers.com', str(msg))
    server.quit()

    r = requests.put('http://api.msunicloud.com:2404/users/', data = user, cookies={'sid':sid})
    t = r.json()
    url = 'http://api.msunicloud.com:2404/users/login'
    r = requests.post(url, data = {'username':user['username'],'password':password}, cookies={'sid':sid})
    sid = r.json()['id']
    print sid
if __name__ == '__main__':
    main()
