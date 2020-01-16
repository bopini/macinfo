import urllib.request as urllib2
import json
import codecs
import re
import sys
import argparse

def getMacAddressInput():
    """ Get Mac Address from User Input"""
    #parser = argparse.ArgumentParser(description='Mac Address application')
    if len(sys.argv) < 2:
        print('Please provide Mac address as argument')
        sys.exit()
    elif len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()
    else:
        mac_address = sys.argv[1]
    return mac_address

def getCompanyName(mac_address):
    """
    >>> getCompanyName('BC:92:6B:A0:00:01')
    'Apple, Inc.'
    >>> getCompanyName('BC-92-6B-A0-00')
    None
    """
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
        print('Not a valid MAC Address.')
        print('Only Traditional 12-digit MAC addresses is supported.')
        print('Example: BC-92-6B-A0-00-01 or BC:92:6B:A0:00:01')
        sys.exit()

def validateMacAddress(mac_address):
    """ Validate Mac Address"""
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
        return True
    else:
        return False

def output(mac_address, company_name):
    """ Output company name for the mac address"""
    print("Mac Address: " + mac_address)
    print("Company Name: " + company_name)

def main():
    """ Main """
    mac_address = getMacAddressInput()
    company_name = getCompanyName(mac_address)
    if company_name:
        output(mac_address, company_name)

if __name__ == "__main__":
    main()