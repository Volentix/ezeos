from moneywagon import AddressBalance

def getBalance(address):
    return AddressBalance().action('bch', address)
