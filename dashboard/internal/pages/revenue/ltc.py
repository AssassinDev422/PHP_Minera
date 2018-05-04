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
        url = 'https://www.litecoinpool.org/api?api_key=8b4828cef867e265697201b975d2931e'
        account_data = requests.get(url).json()
        url = 'https://slushpool.com/stats/json/1697720-7902793772e814218b795a5b2c49dffe'
        block_data = requests.get(url).json()
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Confirmed Reward  : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( account_data['confirmed_reward'] ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Estimated Reward  : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( account_data['estimated_reward'] ) + '</td>'
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
    html_str = html_str + '<th>Status</th>'
    html_str = html_str + '<th>Hashrate</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    items = account_data['workers']
    for i in items:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i + '</td>'
        status = ''
        if items[i]['alive'] == True:
            status = 'Alive'
        else:
            status = 'Offline'
        html_str = html_str + '<td>' + str(status) + '</td>'
        html_str = html_str + '<td>' + str(items[i]['hashrate']) + '</td>'
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
    html_str = html_str + '<th>Date Started</th>'
    html_str = html_str + '<th>Date Found</th>'
    html_str = html_str + '<th>Duration ( Days:Hrs:Min:Sec )</th>'
    html_str = html_str + '<th>Confirmations</th>'
    html_str = html_str + '<th>Rewards ( BTC )</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    items = block_data['blocks']
    for i in items:
        if items[i]['reward'] == "0.00000000":
            continue
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i + '</td>'
        html_str = html_str + '<td>' + str(items[i]['date_started']) + '</td>'
        html_str = html_str + '<td>' + str(items[i]['date_found']) + '</td>'
        sec = timedelta(seconds=int(items[i]['mining_duration']))
        d = datetime(1,1,1) + sec
        html_str = html_str + '<td>' + str("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second)) + '</td>'
        conf = ''
        if items[i]['confirmations'] > 99:
            conf = 'confirmed'
        else:
            conf = str(items[i]['confirmations'])
        html_str = html_str + '<td>' + conf + '</td>'
        html_str = html_str + '<td>' + str(items[i]['reward']) + '</td>'
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
