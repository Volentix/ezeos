#!/bin/python

import os
import requests
from bs4 import BeautifulSoup


def build_url(account, testnet):
    hostname = 'etherscan.io'
    if testnet:
        hostname = 'ropsten.' + hostname
    url = 'https://%s/address/%s' % (hostname, account)
    return url


def parse_balance(url):
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("div", {"class": "card-body"})
    value = table.find("div", {"class": "col-md-8"}).text
    return value


def getBalance(address):
    testnet = False
    if 'testnet' == os.getenv('GET_ETH_BALANCE_CHAIN'):
        testnet = True

    if not address:
        return "No address specified"
    else:
        return "Address: " + address + "\n" + parse_balance(build_url(address, testnet))
