#!/usr/bin/env python
import os
import sys
import requests
def main():
    sid = sys.argv[1]
    try:
        r = requests.get('http://api.msunicloud.com:2404/users/me', cookies = {'sid':sid})
        accounttype = r.json()['accounttype']
    except:
        print ''
        return ''
    ru = requests.get('http://api.msunicloud.com:2404/usertypes', cookies = {'sid':sid}).json()
    user = ''
    for u in ru:
        if u['type'] == accounttype:
            user = u
    html_str = ''
    html_str = html_str + '<nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">'
    html_str = html_str + '<div class="navbar-header">'
    html_str = html_str + '<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">'
    html_str = html_str + '<span class="sr-only">Toggle navigation</span>'
    html_str = html_str + '<span class="icon-bar"></span>'
    html_str = html_str + '<span class="icon-bar"></span>'
    html_str = html_str + '<span class="icon-bar"></span>'
    html_str = html_str + '</button>'
    html_str = html_str + '<a class="navbar-brand" href="/dashboard/internal/pages/index.php?sid=' + sid + '">SigningMiners</a>'
    html_str = html_str + '</div>'
    html_str = html_str + '<!-- /.navbar-header -->'
    html_str = html_str + '<ul class="nav navbar-top-links navbar-right">'
    html_str = html_str + '<li class="dropdown">'
    html_str = html_str + '<a class="dropdown-toggle" data-toggle="dropdown" href="#">'
    html_str = html_str + '<i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>'
    html_str = html_str + '</a>'
    html_str = html_str + '<ul class="dropdown-menu dropdown-user">'
    html_str = html_str + '<li><a href="/dashboard/internal/pages/UserProfile.php?sid=' + sid + '"><i class="fa fa-user fa-fw"></i> User Profile</a>'
    html_str = html_str + '</li>'
    html_str = html_str + '<li class="divider"></li>'
    html_str = html_str + '<li><a href="../../logout.php?sid=' + sid + '"><i class="fa fa-sign-out fa-fw"></i> Logout</a>'
    html_str = html_str + '</li>'
    html_str = html_str + '</ul>'
    html_str = html_str + '<!-- /.dropdown-user -->'
    html_str = html_str + '</li>'
    html_str = html_str + '<!-- /.dropdown -->'
    html_str = html_str + '</ul>'
    html_str = html_str + '<!-- /.navbar-top-links -->'
    html_str = html_str + '<div class="navbar-default sidebar" role="navigation" >'
    html_str = html_str + '              <div class="sidebar-nav navbar-collapse">'
    html_str = html_str + '                  <ul class="nav" id="side-menu">'
    '''
    html_str = html_str + '                      <li class="sidebar-search">'
    html_str = html_str + '                          <div class="input-group custom-search-form">'
    html_str = html_str + '                             <a href="/dashboard/internal/pages/invest.php?sid=' + sid + '" style="font-size: 20px; text-align: center;"> <center>Invest</center></a>'
    html_str = html_str + '                          </span>'
    html_str = html_str + '                          </div>'
    html_str = html_str + '                          <!-- /input-group -->'
    html_str = html_str + '                      </li>'
    '''
    html_str = html_str + '                      <li>'
    html_str = html_str + '                          <a href="/dashboard/internal/pages/index.php?sid=' + sid + '" class="active"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>'
    html_str = html_str + '                      </li>'
    html_str = html_str + '                      <li>'
    html_str = html_str + '                           <a href="#"><i class="fa fa-book fa-fw"></i> Orders<span class="fa arrow"></span></a>'
    html_str = html_str + '                          <ul class="nav nav-second-level">'
    html_str = html_str + '                              <li>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=btc">BTC</a>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=ltc">LTC</a>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=eth">ETH</a>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/orders.php?sid=' + sid + '&typestr=dash">Dash</a>'
    html_str = html_str + '                              </li>'
    html_str = html_str + '                          </ul>'
    html_str = html_str + '                      </li>'
    #html_str = html_str + '                      <li>'
    #html_str = html_str + '                           <a href="#"><i class="fa fa-book fa-fw"></i> Miners<span class="fa arrow"></span></a>'
    #html_str = html_str + '                          <ul class="nav nav-second-level">'
    #html_str = html_str + '                              <li>'
    #html_str = html_str + '                                 <a href="/dashboard/internal/pages/miners.php?sid=' + sid + '&typestr=btc">BTC</a>'
    #html_str = html_str + '                                 <a href="/dashboard/internal/pages/miners.php?sid=' + sid + '&typestr=ltc">LTC</a>'
    #html_str = html_str + '                                 <a href="/dashboard/internal/pages/miners.php?sid=' + sid + '&typestr=eth">ETH</a>'
    #html_str = html_str + '                                 <a href="/dashboard/internal/pages/miners.php?sid=' + sid + '&typestr=dash">Dash</a>'
    #html_str = html_str + '                              </li>'
    #html_str = html_str + '                          </ul>'
    #html_str = html_str + '                      </li>'
    html_str = html_str + '                      <li>'
    html_str = html_str + '                          <a href="#"><i class="fa fa-book fa-fw"></i> Account<span class="fa arrow"></span></a>'
    html_str = html_str + '                          <ul class="nav nav-second-level">'
    html_str = html_str + '                              <li>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/UserProfile.php?sid=' + sid + '">Profile</a>'
    html_str = html_str + '                                 <a href="/dashboard/internal/pages/Cashout.php?sid=' + sid + '">Cashout</a>'
    html_str = html_str + '                                 <a href="/dashboard/logout.php?sid=' + sid + '">Logout</a>'
    html_str = html_str + '                              </li>'
    html_str = html_str + '                          </ul>'
    html_str = html_str + '                          <!-- /.nav-second-level -->'
    if user['displayusers'] is True or user['displayorders'] is True or user['allowregister'] is True or user['displayblocks'] is True or user['displayrewards'] is True:
        html_str = html_str + '                      <li>'
        html_str = html_str + '                          <a href="#"><i class="fa fa-book fa-fw"></i> Admin<span class="fa arrow"></span></a>'
        html_str = html_str + '                          <ul class="nav nav-second-level">'
        if user['displayorders'] is True or user['displayuser'] is True or user['displayblocks'] is True or user['displayrewards'] is True:
            html_str = html_str + '                              <li>'
            if user['displayblocks'] is True:
                html_str = html_str + '                                  <a href="/dashboard/internal/pages/ViewBlocks.php?sid=' + sid + '">Blocks</a>'
            if user['displayrewards'] is True:
                html_str = html_str + '                                  <a href="/dashboard/internal/pages/viewrewards.php?sid=' + sid + '">Rewards</a>'
            if user['displayusers'] is True:
                html_str = html_str + '                                  <a href="/dashboard/internal/pages/viewCustomers.php?sid=' + sid + '">Customers</a>'
            if user['displayorders'] is True:
                html_str = html_str + '                                  <a href="/dashboard/internal/pages/viewOrders.php?sid=' + sid + '">Orders</a>'
            html_str = html_str + '                              </li>'
        if user['allowregister'] is True:
            html_str = html_str + '                              <li>'
            html_str = html_str + '                                  <a href="#"> Setup<span class="fa arrow"></span></a>'
            html_str = html_str + '                                  <ul class="nav nav-third-level">'
            html_str = html_str + '                                      <li><a href="/dashboard/internal/pages/addOrder.php?sid=' + sid + '">Add Order</a></li>'
            html_str = html_str + '                                      <li><a href="/dashboard/internal/pages/addCustomer.php?sid=' + sid + '">Add Customer</a></li>'
            html_str = html_str + '                                  </ul>'
            html_str = html_str + '                              </li>'
        html_str = html_str + '                          </ul>'
        html_str = html_str + '                          <!-- /.nav-second-level -->'
        html_str = html_str + '                      </li>'
    html_str = html_str + '                  </ul>'
    html_str = html_str + '              </div>'
    html_str = html_str + '              <!-- /.sidebar-collapse -->'
    html_str = html_str + '</div>'
    html_str = html_str + '<!-- /.navbar-static-side -->'
    html_str = html_str + '</nav>'
    print html_str
if __name__ == '__main__':
    main()
