from web3.auto import w3

connected = w3.isConnected()

if connected and w3.version.node.startswith('Parity'):
    enode = w3.parity.enode

elif connected and w3.version.node.startswith('Geth'):
    enode = w3.admin.nodeInfo['enode']

else:
    enode = None
print(enode)   
