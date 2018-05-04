#!/usr/bin/env python
import os
import sys
import json
import requests
from datetime import datetime, timedelta
def main():
    #print "Earnings Functionality is currenlty being worked on / under construction. Please try again later."
    try:
        sid = sys.argv[1]
        if sid == '':
            print 'Authentication Error'
            return
        r = requests.get('http://api.msunicloud.com:2404/users/me', cookies = {'sid':sid}).json()
        username = r['username']
        email = r['email']
        phone = r['phone']
        html_str = '''<script>
          window.fcSettings = {
            token: "0f2e722b-6b94-450d-9584-7df04431c681",
            host: "https://wchat.freshchat.com",
            externalId: "''' + username + '''",             // user’s id unique to your system
            onInit: function() {
              window.fcWidget.on('widget:loaded', function() {
                window.fcWidget.user.get().then(function(resp) {
                  var status = resp && resp.status,
                      data = resp && resp.data;
                  if (status === 200) {
                    if (data.restoreId) {
                                                    // Update restoreId in your database
                    }
                  }
                }, function(error) {                // User Not Created
                  window.fcWidget.user.setProperties({
                    email: "''' + email + '''",    // user’s email address
                    phone:  "''' + phone + '''",            // phone number without country code
                  });
                  window.fcWidget.on('user:created', function(resp) {
                    var status = resp && resp.status,
                        data = resp && resp.data;
                    if (status === 200) {
                      if (data.restoreId) {
                                                    // Update restoreId in your database
                      }
                    }
                  });
                });
              });
            }
          };
        </script>
        <script src="https://wchat.freshchat.com/js/widget.js" async></script>'''
        print html_str
    except:
        account_data = ''
        html_str = 'Data Error'
        print html_str
        return
