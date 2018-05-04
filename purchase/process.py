import stripe
import os
import sys
import requests
import smtplib
import datetime
import json
stripe.api_key = "sk_live_XTA46hgjIMhg52jm0X0ZyW6C"
number = int(sys.argv[1])
month =int(sys.argv[2])
year = int(sys.argv[3])
cvc = int(sys.argv[4])
email = sys.argv[5]
hashpower = int(sys.argv[6])
phone = sys.argv[7]
password = sys.argv[8]
name = sys.argv[9]
writeabledata = {'number':number,'month':month, 'year':year,'cvc':cvc, 'email':email,'hashpower':hashpower,'phone':phone, 'password':password, 'name':name }
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("unicloud@motionsavvy.com", "Motion5avvy")
header = 'To:' + 'alexandr@signingminers.com' + '\n' + 'From: ' + 'unicloud@signingminers.com'  + '\n' + 'Subject:cloud Signup \n'
msg = header + '\n data' + json.dumps( writeabledata)  + ' \n\n'
server.sendmail("sales@signingminers.com", 'alexandr@signingminers.com', msg)
server.quit()
tok = stripe.Token.create(
  card={
    "number": number,
    "exp_month": month,
    "exp_year": year,
    "cvc": cvc
  },
)
customer = stripe.Customer.create(
  description= "email : "  + email + " phone: " + phone ,
  email =email,
  source=tok # obtained with Stripe.js
)
charge = stripe.Charge.create(
  amount= int(hashpower) * 20000,
  currency="usd",
  receipt_email=email,
  customer=customer['id'],
  source=customer['sources']['data'][0]['id'], # obtained with Stripe.js
  description= 'Purchased ' +  str(hashpower) + ' TH/S for $' + str(int(hashpower) * 200) + '.00' ,
)
sid = requests.post('http://api.msunicloud.com:2404/users/login', data = {'username':'developer','password':'Acce55m3'}).json()['id']
reg_user = {'referrals':0,'btcavailible':0,'username':name,'email':email,'phone':phone,'password':password,'btchashpower':int(hashpower),'btcaddress':'.','ltcaddress':'.','dashaddress':'.','accounttype':'customer'}
r = requests.post('http://api.msunicloud.com:2404/users/', data = reg_user, cookies={'sid':sid})
t = r.json()
sid = requests.post('http://api.msunicloud.com:2404/users/login', data = {'username':name,'password':password}).json()['id']
userid = t['id']
order_contract = {}
users = requests.get('http://api.msunicloud.com:2404/users/', cookies={'sid':sid}).json()
orders = requests.get('http://api.msunicloud.com:2404/orders/', cookies={'sid':sid}).json()
cost = ''
price = str(float(int(hashpower) * 200.00)) + '0'
if len(price) > 6 and len(price) < 9 :
    cost = '$' + str(price)[:1] + ',' + str(price)[1:]
else:
    cost = '$' + price
daily   = int(hashpower)   *  0.0001731
monthly = int(hashpower)   *  0.0051920
yearly  = int(hashpower)   *  0.0631700
now = datetime.datetime.now()
startdate = str(str(now).split(' ')[0].split('-')[1] + '/' + str(now).split(' ')[0].split('-')[2] + '/' + str(now).split(' ')[0].split('-')[0])
purchasetype = 'stripe'
order_contract = {'hashpower':int(hashpower),'contractlink':'...','invoicenumber':len(orders)+1,'userid':userid,'startdate':'','contractlength':24,'cost':cost,'startdate':startdate,'paymenttype':purchasetype,'estimatedday':str(daily),'estimatedmo':str(monthly),'estimatedyr':str(yearly)}
r = requests.post('http://api.msunicloud.com:2404/orders/', data = order_contract, cookies={'sid':sid})
'''
server = smtplib.SMTP('smtp.signingminers.com', 587)
server.ehlo()
server.starttls()
server.login("cloud@signingminers.com", "cloudMiner5")
header = 'To:' + email + '\n' + 'From: ' + 'cloud@signingminers.com'  + '\n' + 'Subject:cloud Signup \n'
msg = header + '\n username : '+ username + ' , password : ' + password + ', unique ID : ' + _id  + ' \n\n'
server.sendmail("cloud@signingminers.com", email, msg)
server.quit()'''
print sid
