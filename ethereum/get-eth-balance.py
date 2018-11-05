#!/bin/python

import os
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser


# ----------------------------------------------------------------------------------------------------
# Command line Arguments
# -t use Ropsten testnet otherwise default to mainnet chain
# -a account
#
# Environment variables
# Use these in liu of the command line arguments
# GET_ETH_BALANCE_CHAIN=[testnet|mainnet]        - Default to mainnet if not set
# GET_ETH_BALANCE_ACCOUNT=account
#
# Command line arguments will take precedence
# ----------------------------------------------------------------------------------------------------

def build_url(account, testnet):
    hostname = 'etherscan.io'
    if testnet:
        hostname = 'ropsten.' + hostname
    url = 'https://%s/address/%s' % (hostname, account)
    return url


def get_balance(url):
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class" : "table"})
    value = table.findAll('td')[1].text.split(' ')[0].strip()
    return value


if __name__ == "__main__":
    # check for environment variables
    testnet = False
    account = None
    if 'testnet' == os.getenv('GET_ETH_BALANCE_CHAIN'):
        testnet = True

    if os.getenv('GET_ETH_BALANCE_ACCOUNT'):
        account = os.getenv('GET_ETH_BALANCE_ACCOUNT')

    # Any command line parameters
    parser = ArgumentParser()
    parser.add_argument("-a", "--account", dest="account", help="ACCOUNT to return value of")
    # parser.add_argument("-t", "--testnet", dest="testnet", help="Use testnet", default=False, action="store_false")

    parser.add_argument("-t", "--testnet",
                        action="store_true", dest="testnet",
                        default=False,
                        help="Use testnet")

    args = parser.parse_args()

    if args.account:
        print("Args account: " + args.account)
        account = args.account

    if args.testnet:
        print("Args testnet: " + str(args.testnet))
        testnet = True

    if not account:
        print("No account specified")
    else:
        print("Testnet: " + str(testnet))
        print("Account: " + account)
        print("Value  : " + get_balance(build_url(account, testnet)))
