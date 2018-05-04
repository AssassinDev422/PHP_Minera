import os
import sys
import json
import requests
import smtplib
def main():
    username = sys.argv[1]
    sid = requests.post('http://api.msunicloud.com:2404/users/login', data={'username':'developer','password':'Acce55m3'}).json()['id']
    users = requests.get('http://api.msunicloud.com:2404/users', cookies={'sid':sid}).json()
    user = ''
    for u in users:
        if u['username'] == username:
            user = u
            break
        if u['email'] == username:
            user = u
            break
    user['password'] = user['id']
    requests.post('http://api.msunicloud.com:2404/users/' + user['id'], cookies={'sid':sid}, data=user).json()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sales@signingminers.com", "Acce55m3")
    header = 'To:' + user['email'] + '\n' + 'From: ' + 'support@signingminers.com'  + '\n' + 'Subject:Minera Password Reset \n'
    msg = header + '\n Your password has been changed. Your new temporary password is: ' + user['password'] + '\n If you have not made this change, contact support@signingminers.com  \n\n'
    server.sendmail("sales@signingminers.com", user['email'], str(msg))
    server.quit()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sales@signingminers.com", "Acce55m3")
    header = 'To:' + user['email'] + '\n' + 'From: ' + 'support@signingminers.com'  + '\n' + 'Subject:Minera Password Reset \n'
    msg = header + '\n  User ' + user['username'] + ' password was changed. \n\n'
    server.sendmail("sales@signingminers.com", 'support@signingminers.com', str(msg))
    server.quit()
if __name__ == '__main__':
    main()
