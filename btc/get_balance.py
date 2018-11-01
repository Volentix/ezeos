#!/usr/bin/python3
#
# Bitcoin GetBalance
#
# Supported Currencies ARS, AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, ILS, INR, MXN, NOK, NZD, PLN, RUB, SEK, SGD, THB, USD, ZAR
# 
# Usage:
# python GetBalance.py <Currency> <BitcoinAddress> ...
#

import argparse, urllib3, json, certifi

parser = argparse.ArgumentParser(description='Get Balance of Bitcoin Addresses.')
parser.add_argument('Currency', nargs=1, help='Currency')
parser.add_argument('BitcoinAddresses', metavar='BitcoinAddress', nargs='+',
                   help='a Bitcoin Address')

args = parser.parse_args()

def GetBalance():
    for BitcoinAddr in args.BitcoinAddresses:
        blockchain = urllib3.PoolManager()
        req = blockchain.request('GET', 'http://blockchain.info/q/addressbalance/' + BitcoinAddr)
        print("BTC balance:")
        print(req.data)
        print(" BTC")
        break
        exit()
        SatoshiConvert = int(req.data) / 100000000
        if FiatValue() == 'Error: No Such Currency':
            print('no such currency {}'.format(args.Currency[0]))
            break
        else:
            FiatConvert = FiatValue() * SatoshiConvert
            print('{} - {} ({:,} {})'.format(BitcoinAddr, SatoshiConvert, round(FiatConvert, 2), args.Currency[0]))

def FiatValue():
	fiatvalues = urllib3.PoolManager(
			cert_reqs='CERT_REQUIRED',
    		ca_certs=certifi.where(),
		)
	req = fiatvalues.request('GET', 'https://localbitcoins.com/bitcoinaverage/ticker-all-currencies')
	jsondata = json.loads(req.data.decode('utf-8'))
	try:
		return float(jsondata[args.Currency[0]]['rates']['last'])
	except:
		return 'Error: No Such Currency'

GetBalance()
