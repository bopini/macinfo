import urllib.request as urllib2
import json
import codecs
import re
import sys

def getMacAddressInput():
    """ Get Mac Address from User Input"""
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()
    elif len(sys.argv) < 2:
        print('Please provide Mac address as argument')
        sys.exit()
    else:
        mac_address = sys.argv[1]
    return mac_address

def getCompanyName(mac_address):
    """ Get Company Name with Mac address as"""
    valid = validateMacAddress(mac_address)
    if valid:
        url = "http://macvendors.co/api/"
        try:
            request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
            response = urllib2.urlopen( request )
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            return (obj['result']['company'])
        except urllib2.HTTPError as e:
            print(e)
    else:
        print("Not a valid Mac address")

def validateMacAddress(mac_address):
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
        return True
    else:
        return False

def main():
    mac_address = getMacAddressInput()
    company_name = getCompanyName(mac_address)
    print(company_name)

if __name__ == "__main__":
    main()