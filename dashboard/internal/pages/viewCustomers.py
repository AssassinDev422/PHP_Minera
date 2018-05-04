#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
def main():
    try:
        sid = sys.argv[1]
        if sid == '':
            print 'Authentication Error'
            return
        users = requests.get('http://api.msunicloud.com:2404/users', cookies = {'sid':sid}).json()
        price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Number of Customers : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( len(users) ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Current BTC Price : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    pricestr = ''
    pricestr = '$' +  str(price)
    html_str = html_str + '<td>' +  str( pricestr ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-lg-12">'
    html_str = html_str + '<div class="panel panel-default">'
    html_str = html_str + '<div class="panel-heading">Customers</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example2">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Username</th>'
    html_str = html_str + '<th>Email</th>'
    html_str = html_str + '<th>Phone</th>'
    html_str = html_str + '<th>BTC Earned</th>'
    html_str = html_str + '<th>BTC HashPower</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in users:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i['username'] + '</td>'
        html_str = html_str + '<td>' + i['email'] + '</td>'
        html_str = html_str + '<td>' + i['phone'] + '</td>'
        html_str = html_str + '<td>' + i['btcavailible'] + 'BTC / $' + str(float(i['btcavailible'])* float(price))  + '</td>'
        html_str = html_str + '<td>' + i['btchashpower'] + '</td>'
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
