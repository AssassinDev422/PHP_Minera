import os
import sys
import json
import requests
def main():
    sid = sys.argv[1]
    r = requests.post('http://api.msunicloud.com:2404/users/logout',cookies={'sid':sid})
    print 'testing'
if __name__ == '__main__':
    main()
