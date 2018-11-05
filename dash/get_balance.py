import argparse
from moneywagon import AddressBalance
parser = argparse.ArgumentParser()
parser.add_argument("address")
args = parser.parse_args()
print(args.address)
if args.address != '':
    out = AddressBalance().action('dash', args.address)
print(out)
