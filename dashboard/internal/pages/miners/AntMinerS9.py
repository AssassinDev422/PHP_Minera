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
        if sid == '':
            print 'Authentication Error'
            return
    except:
        html_str = 'Data Error'
        print html_str
        return
    HashRate = {'rate':'13.5','unit':'TH/s'}
    upfront = [-3500.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
    estimated_mined = [0.00,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387,0.095387]
    mined = [0.01458111,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
    client = Client('J7JoGURLa5oeawtZ',' t2CWvRTQ7q2y65S0ytlzH9BDIy4CgjJC', api_version='2017-09-04')
    price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
    data_ouput = [['1',float(-3850.00),float(0.01458111),float(float(0.01458111) * float(price)), float(-3850.00) + float(float(0.01458111) * float(price))],
                 ['2',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(1))],
                 ['3',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(2))],
                 ['4',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(3))],
                 ['5',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) *float(4))],
                 ['6',float(0.00),float(0.095387),float(float(0.095387095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(5))],
                 ['7',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(6))],
                 ['8',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(7))],
                 ['9',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(8))],
                 ['10',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(9))],
                 ['11',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(10))],
                 ['12',float(0.00),float(0.095387),float(float(0.095387) * float(price)), float(-3850.00) + float(float(0.095387) * float(price) * float(11))],
                 ]
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">HashRate  : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( HashRate['rate'] + " " + HashRate['unit']   ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Current BTC Price : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( price ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Days To Break Even : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    daily = (float(0.095387) * float(price) / float(31))
    html_str = html_str + '<td>' +  str( float(3850.00)/ daily ) + '</td>'
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
    html_str = html_str + '<th>Month</th>'
    html_str = html_str + '<th>Upfront Cost</th>'
    html_str = html_str + '<th>Estimated Coins Mined</th>'
    html_str = html_str + '<th>Estimated Profit</th>'
    html_str = html_str + '<th>Estimated Revenue</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    for i in range(0,len(data_ouput)):
        html_str = html_str + '<tr class="odd gradeX">'
        for i2 in range(0,len(data_ouput[i])):
            html_str = html_str + '<td>' + str(data_ouput[i][i2]) + '</td>'
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
