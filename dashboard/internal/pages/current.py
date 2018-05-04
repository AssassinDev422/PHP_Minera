import os
import sys
import json
import requests
def main():
    try:
        r = requests.get('http://api.msunicloud.com:2404/users/me', cookies = {'sid':sid})
        username = r.json()['username']
        print username
    except:
        username = ''
        print username
if __name__ == '__main__':
    sid = str(sys.argv[1])
    main()
