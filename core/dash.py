from moneywagon import AddressBalance

def getBalance(address):
    return AddressBalance().action('dash', address)
