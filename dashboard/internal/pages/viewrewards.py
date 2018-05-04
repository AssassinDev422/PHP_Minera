#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
def main():
    #print "Earnings Functionality is currenlty being worked on / under construction. Please try again later."
    try:
        sid = sys.argv[1]
        if sid == '':
            print 'Authentication Error'
            return
        blocks = requests.get('http://api.msunicloud.com:2404/rewards/' , cookies = {'sid':sid}).json()
        price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
        #price = requests.get('https://api.coindesk.com/v1/bpi/currentprice/usd.json').json()['bpi']['rate']'
        users = requests.get('http://api.msunicloud.com:2404/users/' , cookies = {'sid':sid}).json()
        userdata = {}
        for u in users:
            userdata[str(u['id'])] = u['username']
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Current BTC Price : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    pricestr = ''
    pricestr = '$' +  str(price)
    html_str = html_str + '<td>' +  str( pricestr ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Total Rewards: </div>'
    html_str = html_str + '<div class="col-xs-6">'
    totalrew = 0
    for i in blocks:
        totalrew += float(i['reward'])
    html_str = html_str + '<td>' +  str( totalrew ) + 'BTC</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-lg-12">'
    html_str = html_str + '<div class="panel panel-default">'
    html_str = html_str + '<div class="panel-heading">BTC Blocks</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example2">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Block ID</th>'
    html_str = html_str + '<th>Reward Amount</th>'
    html_str = html_str + '<th>User ID</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    for i in blocks:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i['blockid'] + '</td>'
        html_str = html_str + '<th>' + str( i['reward']) + 'BTC / $' + str(float( i['reward']) * float(price))  + '</th>'
        html_str = html_str + '<td>' + i['userid'] + '</td>'
        html_str = html_str + '</tr>'
    html_str = html_str +'</tbody>'
    html_str = html_str + '</table>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div><!-- /.panel-body -->'
    html_str = html_str + '</div><!-- /.panel -->'
    html_str = html_str + '</div><!-- /.col-lg-12 -->'
    html_str = html_str + '</div><!-- /.row -->'
    print html_str
if __name__ == '__main__':
    main()
