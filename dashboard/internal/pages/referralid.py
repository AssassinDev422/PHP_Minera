import os
import sys
def main():
    html_str = ''
    html_str = html_str + '<div class="form-group">'
    if len(sys.argv) > 1 :
        idstr = sys.argv[1]
        html_str = html_str + ' <input type="text" name="referralid" id="referralid" tabindex="2" class="form-control" placeholder="' + idstr +'">'
    else:
        html_str = html_str + ' <input type="text" name="referralid" id="referralid" tabindex="2" class="form-control" placeholder="Referral ID">'
    html_str = html_str + '</div>'
    print html_str
if __name__ == '__main__':
    main()
