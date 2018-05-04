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
        url = 'https://dash.suprnova.cc/index.php?page=api&action=getusertransactions&api_key=76fc75025c363f0d981f7b02e635ff3afc7713ecf065d4931b67ce3b3c716c47'
        td = requests.get(url).json()['getusertransactions']['data']
        transactions_data = td['transactions']
        url = 'https://dash.suprnova.cc/index.php?page=api&action=getuserworkers&api_key=76fc75025c363f0d981f7b02e635ff3afc7713ecf065d4931b67ce3b3c716c47'
        worker_data = requests.get(url).json()['getuserworkers']['data']
        pricing_data = requests.get('https://www.worldcoinindex.com/apiservice/json?key=efYT0UJJflquRJiFI4K3jkbtw').json()['Markets']
        dash_price = 0.00
        for pd in pricing_data:
            if 'DASH/BTC' in pd['Label']:
                dash_price = pd['Price_usd']
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
    transactions = {}
    confirmed_reward = float(0.00)
    estimated_reward = float(0.00)
    for tran in transactions_data:
        idstr = tran['id']
        del tran['coin_address']
        del tran['blockhash']
        del tran['height']
        del tran['id']
        del tran['txid']
        if tran['confirmations'] > 99:
            confirmed_reward += tran['amount']
        else:
            estimated_reward += tran['amount']
        transactions[idstr] = tran
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Confirmed Reward  : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( confirmed_reward ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Estimated Reward  : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( estimated_reward ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-lg-12">'
    html_str = html_str + '<div class="panel panel-default">'
    html_str = html_str + '<div class="panel-heading">BTC Workers</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example1">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Name</th>'
    html_str = html_str + '<th>Hashrate</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    items = worker_data
    for i in items:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' +str(i['username']) + '</td>'
        html_str = html_str + '<td>' + str(i['hashrate']) + '</td>'
        html_str = html_str + '</tr>'
    html_str = html_str +'</tbody>'
    html_str = html_str + '</table>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div><!-- /.panel-body -->'
    html_str = html_str + '</div><!-- /.panel -->'
    html_str = html_str + '</div><!-- /.col-lg-12 -->'
    html_str = html_str + '</div><!-- /.row -->'
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
    html_str = html_str + '<th>Timestamp</th>'
    #html_str = html_str + '<th>Date Found</th>'
    #html_str = html_str + '<th>Duration ( Days:Hrs:Min:Sec )</th>'
    html_str = html_str + '<th>Confirmations</th>'
    html_str = html_str + '<th>Rewards ( BTC )</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    items = transactions
    for i in items:
        if items[i]['amount'] == "0.00000000":
            continue
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + str(i) + '</td>'
        html_str = html_str + '<td>' + str(items[i]['timestamp']) + '</td>'
        '''
        html_str = html_str + '<td>' + str(items[i]['date_started']) + '</td>'
        html_str = html_str + '<td>' + str(items[i]['date_found']) + '</td>'
        sec = timedelta(seconds=int(items[i]['mining_duration']))
        d = datetime(1,1,1) + sec
        html_str = html_str + '<td>' + str("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second)) + '</td>'
        '''
        conf = ''
        if items[i]['confirmations'] > 99:
            conf = 'confirmed'
        if items[i]['confirmations'] < 0 :
            conf = 'orphaned'
        else:
            conf = str(items[i]['confirmations'])
        html_str = html_str + '<td>' + conf + '</td>'
        html_str = html_str + '<td>' + str(items[i]['amount']) + '</td>'
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
