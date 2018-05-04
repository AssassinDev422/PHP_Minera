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
    html_str = '<br>'
    html_str = html_str + '<div class="col-lg-4">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<p> To USD </p>'
    html_str = html_str + '<iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/bitcoin/usd?id=bitcoin" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowTransparency="true"></iframe>'
    html_str = html_str + '</center>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    html_str = html_str + '<div class="col-lg-4">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<p> To USD </p>'
    html_str = html_str + '<iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/dash/usd?id=dash" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowTransparency="true"></iframe>'
    html_str = html_str + '</center>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    html_str = html_str + '<div class="col-lg-4">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<p> To USD </p>'
    html_str = html_str + '<iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/litecoin/usd?id=litecoin" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowTransparency="true"></iframe>'
    html_str = html_str + '</center>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="col-lg-6">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<p> To BTC </p>'
    html_str = html_str + '<iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/ethereum/btc" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowtransparency="true"></iframe>'
    html_str = html_str + '</center>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    html_str = html_str + '<div class="col-lg-6">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<p> To BTC </p>'
    html_str = html_str + '<iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/litecoin/btc?id=dash" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowTransparency="true"></iframe>'
    html_str = html_str + '</center>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    print html_str
if __name__ == '__main__':
    main()
