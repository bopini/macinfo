import argparse
import urllib.request as urllib2
import json
import codecs
import re
import sys

class MacAddressInfo(object):

    """
       This is a class which provides company name by taking mac address as input .

       Attributes:
            None
    """

    def __init__(self, mac_address, company_name=None):
        """
        The constructor for MacAddressInfo class.

        Parameters:
           mac_address : Mac address
           company_name : None
        """

        self.mac_address = mac_address
        self.company_name = company_name

    def getCompanyName(self):
        """
        The function to get Company Name.

        Parameters:
            none.

        Returns:
            Company name

        >>> test1 = MacAddressInfo('BC:92:6B:A0:00:01')
        >>> test1.getCompanyName()
        'Apple, Inc.'
        >>> test2 = MacAddressInfo('BC-92-6B-A0-00-01')
        >>> test2.getCompanyName()
        'Apple, Inc.'
        >>> test3 = MacAddressInfo('BC926BA00001')
        >>> test3.getCompanyName()
        'Apple, Inc.'
        >>> test4 = MacAddressInfo('BC-92-6B-A0-00')
        >>> test4.getCompanyName()
        Not a valid MAC Address
        Only Traditional 12-digit MAC addresses is supported
        Example: BC-92-6B-A0-00-01 or BC:92:6B:A0:00:01 or BC926BA00001
        """

        valid = self.validateMacAddress()
        if valid:
            url = "http://macvendors.co/api/"
            try:
                request = urllib2.Request(url+self.mac_address, headers={'User-Agent' : "API Browser"})
                response = urllib2.urlopen( request )
                reader = codecs.getreader("utf-8")
                obj = json.load(reader(response))
                if  "company" in obj['result']:
                    self.company_name = obj['result']['company']
                return self.company_name
            except urllib2.HTTPError as e:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            except urllib2.URLError as e:
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
        else:
            str="Not a valid MAC Address\nOnly Traditional 12-digit MAC addresses is supported\nExample: BC-92-6B-A0-00-01 or BC:92:6B:A0:00:01 or BC926BA00001"
            print(str)
            return None
            sys.exit()

    def validateMacAddress(self):
        """
        The function to validate Mac address.

        Parameters:
            none.

        Returns:
            Boolean value by validating address

        >>> test1 = MacAddressInfo('BC:92:6B:A0:00:01')
        >>> test1.validateMacAddress()
        True
        >>> test2 = MacAddressInfo('BC-92-6B-A0-00-01')
        >>> test2.validateMacAddress()
        True
        >>> test3 = MacAddressInfo('BC-92-6B-A0-00-01')
        >>> test3.validateMacAddress()
        True
        >>> test4 = MacAddressInfo('BC-92-6B-A0-00')
        >>> test4.validateMacAddress()
        False
        """

        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", self.mac_address.lower()):
            return True
        else:
            return False

    def displayOutput(self, mac_address, company_name):
        """
        The function to Display Output

        Parameters:
            mac_address
            company_name

        Returns:
            Output of mac_address and company_name

        >>> address = 'BC:92:6B:A0:00:01'
        >>> test1 = MacAddressInfo(address)
        >>> out = test1.getCompanyName()
        >>> test1.displayOutput(address, out)
        Mac Address: BC:92:6B:A0:00:01
        Company Name: Apple, Inc.
        """

        print("Mac Address: " + self.mac_address)
        print("Company Name: " + self.company_name)

def main():

    """ Main Function. Validate arguments through argparser """
    parser = argparse.ArgumentParser()
    parser.add_argument('--mac_address', required=True)
    args = parser.parse_args()
    address=args.mac_address

    obj = MacAddressInfo(address)
    company_name = obj.getCompanyName()
    if company_name:
        obj.displayOutput(address, company_name)
    else:
        print("Company name is not found for given Mac address")

if __name__ == '__main__':
    """ """
    main()