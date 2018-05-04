#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
import time
def calculate_dayindex(d):
    EnteredMonth  = int(d.split('/')[0])
    EnteredDay = int(d.split('/')[1])
    EnteredYear = int(d.split('/')[1])
    return int(datetime(EnteredYear,EnteredMonth,EnteredDay,0,0,0,0).timetuple().tm_yday)
def main():
    try:
        sid = sys.argv[1]
        idstr = sys.argv[2]
        if sid == '':
            print 'Authentication Error'
            return
        r = requests.get('http://api.msunicloud.com:2404/users/'+idstr, cookies = {'sid':sid})
        availible = [r.json()['btchashpower'] , r.json()['btcavailible'] ]
        rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid})
        price = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()['data']['rates']['USD']
        # We want to get some information from slushpool about our account , specifically the blocks.
        url = 'https://slushpool.com/stats/json/1697720-7902793772e814218b795a5b2c49dffe'
        block_data = requests.get(url).json()['blocks']
        poolhashrate = int(float(requests.get(url).json()['ghashes_ps'].replace('e+',' ').split(' ')[0]) * 1000)
        # We want to get the blocks in our system , and save by the block id as a key.
        saved_blocks = {}
        blocks = requests.get('http://api.msunicloud.com:2404/blocks', cookies = {'sid':sid}).json()
        for b in blocks:
            saved_blocks[b['blockid']] = b
        pending_blocks_count = 0
        pending_blocks = []
        pending_block_display = {}
        numbers = []
        blockavg = 0
        # Now we want to check if the new blocks already exist in the saved blocks.
        for blockid in block_data:
            if blockid not in saved_blocks:
                pending_blocks.append(blockid)
                data = requests.get('https://blockchain.info/rawblock/' + block_data[blockid]['hash']).json()
                del data['tx']
                duration = time.strftime("%H:%M:%S", time.gmtime(int( block_data[blockid]['mining_duration'] )))
                dates = block_data[blockid]['date_found'].split(' ')[0]
                datefound = dates.split('-')[1]  + '/' + dates.split('-')[2] + '/' + dates.split('-')[0]
                dayindex = calculate_dayindex(datefound)
                ledge = ''
                for l in requests.get('http://api.msunicloud.com:2404/ledger', cookies = {'sid':sid}).json():
                    if str(l['index']) == str( dayindex ):
                        ledge = l
                total = float(12.5 + float(data['n_tx']) * 0.0005)
                E = total * 0.98 * float(availible[0]) / float(float(poolhashrate) * 1000 )
                numbers.append(float(E))
                blockavg = float(sum(numbers)) / max(len(numbers), 1)
                pending_block_display[blockid] = {'totalreward':(12.5 + float(data['n_tx']) * 0.0005) , 'miningduration':duration,'datefound':block_data[blockid]['date_found'] ,'reward' : float( E ) }
                pending_blocks_count += 1
        user_blocks = []
        for ub in rewards.json():
            if ub['userid'] == idstr:
                if ub['blockid'] in pending_blocks:
                    continue
                user_blocks.append([ub['blockid'],ub['datefound'],ub['miningduration'],ub['reward']])
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
    html_str = html_str + '<div class="col-xs-6">Available Hashpower ( TH/s ) : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( availible[0] ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Availible : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( availible[1] ) + 'BTC / $' + str(float(availible[1])* float(price)) +  '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Pending Rewards : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( pending_blocks_count ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Estimated Pending Rewards : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( blockavg * pending_blocks_count ) + 'BTC / $' + str(float(blockavg * pending_blocks_count)* float(price)) +  '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="col-lg-12">'
    html_str = html_str + '<div class="panel panel-default">'
    html_str = html_str + '<div class="panel-heading"> Pending BTC Blocks</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example3">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Block ID</th>'
    html_str = html_str + '<th>Date Found</th>'
    html_str = html_str + '<th>Duration ( Hours:Mins:Secs)</th>'
    # html_str = html_str + '<th>Block Reward ( BTC )</th>'
    html_str = html_str + '<th>Your Reward ( BTC )</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in pending_block_display:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i + '</td>'
        html_str = html_str + '<td>' + pending_block_display[i]['datefound']+ '</td>'
        html_str = html_str + '<td>' + pending_block_display[i]['miningduration']+ '</td>'
        #html_str = html_str + '<th>' + str( float( pending_block_display[i]['totalreward'] )) + 'BTC / $' + str(float( pending_block_display[i]['totalreward']  ) * float(price))  + '</th>'
        html_str = html_str + '<th>' + str( float( pending_block_display[i]['reward'] )) + 'BTC / $' + str(float( pending_block_display[i]['reward']  ) * float(price))  + '</th>'
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
    html_str = html_str + '<div class="panel-heading">Earned BTC Blocks</div><!-- /.panel-heading -->'
    html_str = html_str + '<div class="panel-body">'
    html_str = html_str + '<div class="dataTable_wrapper">'
    html_str = html_str + '<table class="table table-striped table-bordered table-hover" id="dataTables-example2">'
    html_str = html_str + '<thead>'
    html_str = html_str + '<tr>'
    html_str = html_str + '<th>Block ID</th>'
    html_str = html_str + '<th>Date Found</th>'
    html_str = html_str + '<th>Duration</th>'
    html_str = html_str + '<th>Reward ( BTC )</th>'
    html_str = html_str + '</tr>'
    html_str = html_str + '</thead>'
    html_str = html_str + '<tbody>'
    data_output = []
    for i in user_blocks:
        html_str = html_str + '<tr class="odd gradeX">'
        html_str = html_str + '<td>' + i[0] + '</td>'
        html_str = html_str + '<td>' + i[1] + '</td>'
        html_str = html_str + '<td>' + i[2] + '</td>'
        html_str = html_str + '<th>' + str( float( i[3])) + 'BTC / $' + str(float( i[3] ) * float(price))  + '</th>'
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
