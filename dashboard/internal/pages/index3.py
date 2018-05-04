import sys
import json
import requests
def main():
    debug = []
    try:
        sid = sys.argv[1]
        debug.append('sid reached')
        r = requests.get('http://api.msunicloud.com:2404/users/me' , cookies={'sid':sid})
        debug.append('got user reached')
        username = r.json()['username']
        debug.append('got username reached')
        userid = r.json()['id']
        debug.append('got id reached')
        email = r.json()['email']
        debug.append('got email reached')
        phone = r.json()['phone']
        debug.append('got phone reached')
        btcaddress = r.json()['btcaddress']
        debug.append('got btcaddress reached')
        ltcaddress = r.json()['ltcaddress']
        debug.append('got ltcaddress reached')
        dashaddress = r.json()['dashaddress']
        debug.append('got dashaddress reached')
        idstr = r.json()['id']
        debug.append('got id reached')
        btcavailible = r.json()['btcavailible']
        debug.append('got btcavailible reached')
        number = r.json()['referrals']
        debug.append('got referrals reached')
        rewards = requests.get('http://api.msunicloud.com:2404/rewards', cookies = {'sid':sid}).json()
        debug.append('got rewards reached ')
        total = 0
        for r in rewards:
            if 'userid' not in r:
                continue
            if str(r['userid']) == str(userid):
                debug.append('get reward reached ' + r)
                total = total + float(json.loads(r)['reward'])
                debug.append('got total reached ' + total)
    except:
        print sys.exc_info()[0]  , json.dumps( debug )
        return ''
    html_str = '<br>'
    html_str = html_str + '<div class="col-lg-6">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<h4>Account Information</h4>'
    html_str = html_str + '</center>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Username : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( username ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Email : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( email ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Phone : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( phone ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">BTC Wallet : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td> <font size="-2">' +  str( btcaddress ) + '</font></td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">LTC Wallet : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td> <font size="-2">' +  str( ltcaddress ) + '</font></td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Dash Wallet : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td> <font size="-2">' +  str( dashaddress ) + '</font></td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-6 -->'
    ## ROW COLUMN 2 ##
    html_str = html_str + '<div class="col-lg-4">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<h4>Referral Information</h4>'
    html_str = html_str + '</center>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Code : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td><a href="/dashboard/internal/pages/referral.php?idstr=' +  str( idstr ) + '">' +  str( idstr ) + '</a></td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Referrals : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' + str(number ) +  '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'
    ## ROW COLUMN 3 ##
    html_str = html_str + '<div class="col-lg-4">'
    html_str = html_str + '<div class="well">'
    html_str = html_str + '<center>'
    html_str = html_str + '<h4>Account Earnings</h4>'
    html_str = html_str + '</center>'
    html_str = html_str + '<br>'
    html_str = html_str + '<div class="row">'
    html_str = html_str + '<div class="row show-grid">'
    html_str = html_str + '<div class="col-xs-6">Availble BTC : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( btcavailible ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '<div class="col-xs-6">Total Earned BTC : </div>'
    html_str = html_str + '<div class="col-xs-6">'
    html_str = html_str + '<td>' +  str( total ) + '</td>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div>'
    html_str = html_str + '</div><!-- /.well -->'
    html_str = html_str + '</div><!-- /.col-lg-4 -->'

    #html_str = html_str + '<div class="col-lg-12">'
    #html_str = html_str + '<center>'
    #html_str = html_str + '<object style="width:100%;height:750px;" type="text/html" data="https://signingminers.com/purchase.html"></object>'
    #html_str = html_str + '</center>'
    #html_str = html_str + '</div><!-- /.col-lg-12 -->'

    print html_str
if __name__ == '__main__':
    main()
