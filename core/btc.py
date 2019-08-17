from moneywagon import AddressBalance

def getBalance(address):
    return AddressBalance().action('btc', address)
