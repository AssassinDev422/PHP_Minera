#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
import math
def main():
    try:
        sid = sys.argv[1]
        typestr = sys.argv[2]
        if sid == '':
            print 'Authentication Error'
            return
        r = requests.get('http://api.msunicloud.com:2404/users/me', cookies = {'sid':sid})
        availible = [ r.json()['btchashpower'] ]
        idstr = r.json()['id']
        orders = ''
        if typestr == 'btc':
            orders = requests.get('http://api.msunicloud.com:2404/orders', cookies = {'sid':sid})
        if typestr == 'eth':
            orders = requests.get('http://api.msunicloud.com:2404/ethorders', cookies = {'sid':sid})
        if typestr == 'dash':
            orders = requests.get('http://api.msunicloud.com:2404/dashorders', cookies = {'sid':sid})
        if typestr == 'ltc':
            orders = requests.get('http://api.msunicloud.com:2404/ltcorders', cookies = {'sid':sid})
        orderdata = []
        sumcost = 0
        sumearnings = 0
        hp = 0
        price = 1
        if typestr == 'btc':
            price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
        if typestr == 'eth':
            price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=ETH').json()['data']['rates']['USD']
        if typestr == 'dash':
            pricing_data = requests.get('https://www.worldcoinindex.com/apiservice/json?key=efYT0UJJflquRJiFI4K3jkbtw').json()['Markets']
            price = 0.00
            for pd in pricing_data:
                if 'DASH/BTC' in pd['Label']:
                    price = pd['Price_usd']
        if typestr == 'ltc':
            price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=LTC').json()['data']['rates']['USD']
        for o in orders.json():
            if o['userid'] == idstr:
                orderdata.append(o)
                sumcost += float(o['cost'].replace('$','').replace(',',''))
                sumearnings += (float(o['estimatedday']) * float(price))
                hp += float(o['hashpower'])
        TotalBreakEven = int(math.ceil( sumcost / sumearnings ))
        totalcontracts = len( orderdata )
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
    html_str = '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Current ' + typestr + ' Price : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    pricestr = ''
    pricestr = '$' +  str(price)
    html_str = html_str + '<td>' +  str( pricestr ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Total Hashpower ( TH/s ) : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( hp ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Total Contracts : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( totalcontracts ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Break Even : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' + str( TotalBreakEven )+ '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-lg-12">'
    html_str = html_str + '<div class="panel panel-default">'
    html_str = html_str + '<div class="panel-heading">Contract Information</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example2">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Invoice Number</th>'
    html_str = html_str + '<th>Start Date</th>'
    html_str = html_str + '<th>Contract Length ( months ) </th>'
    html_str = html_str + '<th>Cost</th>'
    html_str = html_str + '<th>Break Even ( Days ) </th>'
    html_str = html_str + '<th>Payment Type</th>'
    html_str = html_str + '<th>HashPower </th>'
    html_str = html_str + '<th>Documentation </th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in orderdata:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<th>' + i['invoicenumber'] + '</th>'
        html_str = html_str + '<th>' + i['startdate'] + '</th>'
        html_str = html_str + '<th>' + i['contractlength'] + '</th>'
        html_str = html_str + '<th>' + i['cost'] + '</th>'
        c  = float(i['cost'].replace('$','').replace(',',''))
        ea = float(i['estimatedday']) * float(price)
        be = int(math.ceil( c / ea ))
        html_str = html_str + '<th>' +  str( be )  + '</th>'
        html_str = html_str + '<th>' + i['paymenttype'] + '</th>'
        html_str = html_str + '<th>' + i['hashpower'] + '</th>'
        html_str = html_str + '<th>' + i['contractlink'] + '</th>'
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
    html_str = html_str + '<div class="panel-heading">Estimated Earnings By Contract BTC / USD</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example3">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Invoice Number</th>'
    html_str = html_str + '<th>Daily</th>'
    html_str = html_str + '<th>Monthly</th>'
    html_str = html_str + '<th>Yearly</th>'
    html_str = html_str + '<th>Estimated Contract Earnings BTC / USD </th>'
    html_str = html_str + '<th>Break Even 6 Months</th>'
    html_str = html_str + '<th>Break Even 1 Year</th>'
    html_str = html_str + '<th>Break Even 2 Years</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in orderdata:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<th>' + str(i['invoicenumber']) + '</th>'
        html_str = html_str + '<th>' + str(i['estimatedday']) + 'BTC / $' + str(float(i['estimatedday'])* float(price))  + '</th>'
        html_str = html_str + '<th>' + str(i['estimatedmo']) + 'BTC / $' + str(float(i['estimatedmo'])* float(price))  + '</th>'
        html_str = html_str + '<th>' + str(i['estimatedyr']) + 'BTC / $' + str(float(i['estimatedyr']) * float(price))  + '</th>'
        html_str = html_str + '<th>' + str(float(i['estimatedyr'])* 2) + 'BTC / $' + str(float(i['estimatedyr']) * float(price) * 2 )  + '</th>'
        est = float(i['cost'].replace('$','').replace(',','')) /  ( float(i['estimatedmo']) * 6 )
        est = round(est,2)
        html_str = html_str + '<th>$' + str(est) + '</th>'
        est = float(i['cost'].replace('$','').replace(',','')) /  ( float(i['estimatedyr']) )
        est = round(est,2)
        html_str = html_str + '<th>$' + str(est) + '</th>'
        est = float(i['cost'].replace('$','').replace(',','')) /  ( float(i['estimatedyr']) * 2 )
        est = round(est,2)
        html_str = html_str + '<th>$' + str(est) + '</th>'
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
