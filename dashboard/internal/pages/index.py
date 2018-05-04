import os
import sys
import json
import requests
def main():
    user = ''
    try:
        sid = sys.argv[1]
        user = requests.get('http://api.msunicloud.com:2404/users/me' , cookies={'sid':sid}).json()
        price = requests.get('https://blockchain.info/ticker').json()['USD']['last']
        orders = requests.get('http://api.msunicloud.com:2404/orders' , cookies={'sid':sid}).json()
        price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
        ltcprice = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=LTC').json()['data']['rates']['USD']
        ethprice = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=ETH').json()['data']['rates']['USD']
        pricing_data = requests.get('https://www.worldcoinindex.com/apiservice/json?key=efYT0UJJflquRJiFI4K3jkbtw').json()['Markets']
        dash_price = 0.00
        for pd in pricing_data:
            if 'DASH/BTC' in pd['Label']:
                dash_price = pd['Price_usd']
        contracts = {'contracts':[],'hashrate':0}
        for o in orders:
            if str(user['id']) == str(o['userid']):
                contracts['contracts'].append( o )
                contracts['hashrate'] += int(o['hashpower'])
        orders = requests.get('http://api.msunicloud.com:2404/ltcorders' , cookies={'sid':sid}).json()
        ltccontracts = {'contracts':[],'hashrate':0}
        for o in orders:
            if str(user['id']) == str(o['userid']):
                ltccontracts['contracts'].append( o )
                ltccontracts['hashrate'] += int(o['hashpower'])
        orders = requests.get('http://api.msunicloud.com:2404/dashorders' , cookies={'sid':sid}).json()
        dashcontracts = {'contracts':[],'hashrate':0}
        for o in orders:
            if str(user['id']) == str(o['userid']):
                dashcontracts['contracts'].append( o )
                dashcontracts['hashrate'] += int(o['hashpower'])
        orders = requests.get('http://api.msunicloud.com:2404/ethorders' , cookies={'sid':sid}).json()
        ethcontracts = {'contracts':[],'hashrate':0}
        for o in orders:
            if str(user['id']) == str(o['userid']):
                ethcontracts['contracts'].append( o )
                ethcontracts['hashrate'] += int(o['hashpower'])
        colocations = requests.get('http://api.msunicloud.com:2404/colocate' , cookies={'sid':sid}).json()
        colocates = {'btc':{'contracts':[],'hashrate':0},'dash':{'contracts':[],'hashrate':0},'ltc':{'contracts':[],'hashrate':0},'eth':{'contracts':[],'hashrate':0}}
        for o in colocations:
            for t in ['btc','ltc','dash','eth']:
                if str(o['cointype']).lower() == str(t).lower():
                    if str(user['id']) == str(o['userid']):
                        colocates[t]['contracts'].append( o )
                        colocates[t]['hashrate'] += int(o['hashpower'])
    except:
        return ''
    html_str = '<br>'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-primary">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-cloud fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(contracts['hashrate']) + int(colocates['btc']['hashrate']))
    if total != float(0):
        ration = int(contracts['hashrate']) / total
        btcearnings = float(float(user['btcavailible']) * ration)
    else:
        btcearnings = 0
    amount ="{0:.8f}".format(btcearnings)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( amount )+ '</div>'
    html_str = html_str +  '<div>Bitcoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=btc">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(contracts['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">BTC Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(contracts['hashrate']) + ' TH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">BTC Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(price)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(btcearnings * float(price)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['btcaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-yellow">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-cloud fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(ltccontracts['hashrate']) + int(colocates['ltc']['hashrate']))
    if total != float(0):
        ration = int(ltccontracts['hashrate']) / total
        ltcearnings = float(float(user['ltcavailible']) * ration)
    else:
        ltcearnings = 0
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(ltcearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Litecoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=ltc">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(ltccontracts['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">LTC Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(ltccontracts['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">LTC Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(ltcprice)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str("{0:.2f}".format(round(float(ltcearnings) * float(ltcprice),2))) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['ltcaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-green">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-cloud fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(dashcontracts['hashrate']) + int(colocates['dash']['hashrate']))
    if total != float(0):
        ration = int(dashcontracts['hashrate']) / total
        dashearnings = float(float(user['dashavailible']) * ration)
    else:
        dashearnings = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(dashearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Dashcoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=dash">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(dashcontracts['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">DASH Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(dashcontracts['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">DASH Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(dash_price)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(float(dashearnings) * float(dash_price)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['dashaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-red">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-cloud fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(ethcontracts['hashrate']) + int(colocates['eth']['hashrate']))
    if total != float(0):
        ration = int(ethcontracts['hashrate']) / total
        ethearnings = float(float(user['ethavailible']) * ration)
    else:
        ethearnings = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(ethearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Ethereum</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=eth">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(ethcontracts['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">ETH Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(ethcontracts['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">ETH Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(ethprice)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(float(ethearnings) * float(ethprice)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['ethaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-primary">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-home fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(contracts['hashrate']) + int(colocates['btc']['hashrate']))
    if total != float(0):
        ration = int(colocates['btc']['hashrate']) / total
        btcearnings = float(float(user['btcavailible']) * ration)
    else:
        btcearnings = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(btcearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Bitcoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=btc">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(colocates['btc']['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">BTC Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(colocates['btc']['hashrate']) + ' TH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">BTC Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(price)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(btcearnings * float(price)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['btcaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-yellow">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-home fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(ltccontracts['hashrate']) + int(colocates['ltc']['hashrate']))
    if total != float(0):
        ration = int(colocates['ltc']['hashrate']) / total
        ltcearnings = float(float(user['ltcavailible']) * ration)
    else:
        ltcearnings = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(ltcearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Litecoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=ltc">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(colocates['ltc']['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">LTC Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(colocates['ltc']['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">LTC Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str( "{0:.2f}".format(round(float(ltcprice),2)) )  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(float(ltcearnings) * float(ltcprice)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['ltcaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-green">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-home fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(dashcontracts['hashrate']) + int(colocates['dash']['hashrate']))
    if total != float(0):
        ration = int(colocates['dash']['hashrate']) / total
        dashearnings = float(float(user['dashavailible']) * ration)
    else:
        total = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(dashearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Dashcoin</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=dash">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(colocates['dash']['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">DASH Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(colocates['dash']['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">DASH Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(dash_price)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(float(dashearnings) * float(dash_price)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['dashaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-lg-3 col-md-6">'
    html_str = html_str +  '<div class="panel panel-red">'
    html_str = html_str +  '<div class="panel-heading">'
    html_str = html_str +  '<div class="row">'
    html_str = html_str +  '<div class="col-xs-3">'
    html_str = html_str +  '<i class="fa fa-home fa-5x"></i>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="col-xs-9 text-right">'
    total = float(int(ethcontracts['hashrate']) + int(colocates['eth']['hashrate']))
    if total != float(0):
        ration = int(colocates['eth']['hashrate']) / total
        ethearnings = float(float(user['ethavailible']) * ration)
    else:
        ethearnings = float(0)
    html_str = html_str +  '<div class="huge" style="font-size:20px;">' + str( "{0:.8f}".format(round(ethearnings,2)) )+ '</div>'
    html_str = html_str +  '<div>Ethereum</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=eth">'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">' + str(len(colocates['eth']['contracts'] ))+ ' Orders</span>'
    html_str = html_str +  '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">ETH Hashrate</span>'
    html_str = html_str +  '<span class="pull-right">' + str(colocates['eth']['hashrate']) + ' MH/s</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">ETH Price</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(ethprice)  + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '<div class="panel-footer">'
    html_str = html_str +  '<span class="pull-left">USD Earnings</span>'
    html_str = html_str +  '<span class="pull-right">$' + str(float(ethearnings) * float(ethprice)) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '<a href="#" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<div class="panel-footer" style="overflow:hidden !important;text-overflow: ellipsis;">'
    html_str = html_str +  '<span style="overflow:hidden !important;text-overflow: ellipsis;">' + str(user['ethaddress']) + '</span>'
    html_str = html_str +  '<div class="clearfix"></div>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</a>'
    html_str = html_str +  '</div>'
    html_str = html_str +  '</div>'
    #html_str = html_str + '<div class="col-lg-6">'
    #html_str = html_str + '<div class="alert alert-info">'
    #html_str = html_str + 'Purchase Hashpower via : <a href="#" class="alert-link">CC</a> <a href="#" class="alert-link">B</a>'
    #html_str = html_str + '</div>'
    #html_str = html_str + '</div>'
    #html_str = html_str + '<div class="col-lg-6">'
    #html_str = html_str + '<div class="alert alert-success">'
    #html_str = html_str + 'Purchase Hashpower via Earnings: <a href="#" class="alert-link">L</a> <a href="#" class="alert-link">B</a> <a href="#" class="alert-link">D</a> <a href="#" class="alert-link">E</a>'
    #html_str = html_str + '</div>'
    #html_str = html_str + '</div>'
    #html_str = html_str + '</div>'
    #html_str = html_str +  '</div>'
    #html_str = html_str +  '</div>'

    print html_str
if __name__ == '__main__':
    main()
