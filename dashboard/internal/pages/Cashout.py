#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
from coinbase.wallet.client import Client
def main():
    try:
        sid = sys.argv[1]
        url = 'http://api.msunicloud.com:2404/users/me'
        r = requests.get(url , cookies={'sid':sid})
        username = r.json()['username']
        email = r.json()['email']
        phone = r.json()['phone']
        btcaddress = r.json()['btcaddress']
        ltcaddress = r.json()['ltcaddress']
        dashaddress = r.json()['dashaddress']
        if sid == '':
            print 'Authentication Error'
            return
    except:
        html_str = 'Data Error'
        print html_str
        return
    html_str ='<div class="form-group">'
    html_str = html_str + '<input type="hidden" name="username" id="username" tabindex="1" class="form-control" placeholder="Username" value="' + username + '">'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="form-group">'
    html_str = html_str + '<input type="hidden" name="email" id="email" tabindex="1" class="form-control" placeholder="Email Address" value="'+ email  + '">'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="form-group">'
    html_str = html_str + '<input type="password" name="password" id="password" tabindex="2" class="form-control" placeholder="Password">'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="form-group">'
    html_str = html_str + '<input type="hidden" name="phone" id="phone" tabindex="2" class="form-control" placeholder="Phone #" value="' + phone + '">'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="form-group">'
    html_str = html_str + '<p>BTC Address </p>'
    html_str = html_str + '<input type="text" name="btcaddress" id="btcaddress" tabindex="2" class="form-control" placeholder="Wallet Address" value="' + btcaddress + '">'
    html_str = html_str + '<p>LTC Address </p>'
    html_str = html_str + '<input type="text" name="ltcaddress" id="ltcaddress" tabindex="2" class="form-control" placeholder="Wallet Address" value="' + ltcaddress + '">'
    html_str = html_str + '<p>Dash Address </p>'
    html_str = html_str + '<input type="text" name="dashaddress" id="dashaddress" tabindex="2" class="form-control" placeholder="Wallet Address" value="' + dashaddress + '">'
    html_str = html_str + '</div>'
    html_str = html_str + '</br>'
    html_str = html_str + '</br>'
    html_str = html_str + '<div class="form-group">'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-sm-6 col-sm-offset-3">'
    html_str = html_str + '<input type="submit" name="register-submit" id="register-submit" tabindex="4" class="form-control btn btn-register" value="Update Now">'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</form>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    print html_str
if __name__ == '__main__':
    main()
