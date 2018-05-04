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
        contracts = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid}).json()
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
    html_str = html_str + '<div class="col-xs-6">Number of Orders : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( len(users) ) + '</td>'
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
    html_str = html_str + '<th>Invoice #</th>'
    html_str = html_str + '<th>Start Date</th>'
    html_str = html_str + '<th>Cost</th>'
    html_str = html_str + '<th>Estimated Daily</th>'
    html_str = html_str + '<th>Estimated Monthly</th>'
    html_str = html_str + '<th>Estimated Yearly</th>'
    html_str = html_str + '<th>User ID</th>'
    html_str = html_str + '<th>HashPower</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in contracts:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i['invoicenumber'] + '</td>'
        html_str = html_str + '<td>' + i['startdate'] + '</td>'
        html_str = html_str + '<td>' + i['cost'] + '</td>'
        html_str = html_str + '<td>' + i['estimatedday'] + 'BTC</td>'
        html_str = html_str + '<td>' + i['estimatedmo'] + 'BTC</td>'
        html_str = html_str + '<td>' + i['estimatedyr'] + 'BTC</td>'
        for u in users:
            if u['id'] == i['userid']:
                html_str = html_str + '<td>' + u['username'] + '</td>'
        html_str = html_str + '<td>' + i['hashpower'] + '</td>'
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
