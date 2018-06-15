#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################
# MIT License
#
# Copyright (c) 2018 Volentix Labs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#############################################################################

# Author
# Sylvain Cormier sylvain@volentixlabs.com/sylvaincormier@protonmail.com

import subprocess
import os

# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

import sys
from PyQt4 import QtCore, QtGui

class Wallet():
    name = ""
    OwnerKey1 = ""
    PublicKey1 = ""
    OwnerKey2 = ""
    PublicKey2 = ""

class Account():
    name = ""
    
class Order():
    to = ""
    amount = 0.0000
    contract = ""
    currency = ""
    contractAccountName = ""
    
    
class Dialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel
        #self.setMinimumSize(1280, 1024)

#        self.openContractLabel = QtGui.QLabel()
#        self.openContractLabel.setFrameStyle(frameStyle)
        self.openContractButton = QtGui.QPushButton("Open Contract")    

#        self.setWalletNameLabel = QtGui.QLabel()
#        self.setWalletNameLabel.setFrameStyle(frameStyle)
        self.setWalletNameButton = QtGui.QPushButton("Wallet name")
        
#        self.restartLabel = QtGui.QLabel()
#        self.restartLabel.setFrameStyle(frameStyle)
        self.restartButton = QtGui.QPushButton("Reset chain")
        
#        self.startLabel = QtGui.QLabel()
#        self.startLabel.setFrameStyle(frameStyle)
        self.startButton = QtGui.QPushButton("Start chain")
        
#        self.stopLabel = QtGui.QLabel()
#        self.stopLabel.setFrameStyle(frameStyle)
        self.stopButton = QtGui.QPushButton("Stop chain")
        
#        self.flushLabel = QtGui.QLabel()
#        self.flushLabel.setFrameStyle(frameStyle)
        self.flushButton = QtGui.QPushButton("Flush wallets")
        
#        self.createWalletLabel = QtGui.QLabel()
#        self.createWalletLabel.setFrameStyle(frameStyle)
        self.createWalletButton = QtGui.QPushButton("Create wallet")

#        self.setOwnerKeyLabel = QtGui.QLabel()
#        self.setOwnerKeyLabel.setFrameStyle(frameStyle)
        self.setOwnerKeyButton = QtGui.QPushButton("Set owner Key")
        
#        self.setActiveKeyLabel = QtGui.QLabel()
#        self.setActiveKeyLabel.setFrameStyle(frameStyl self.setMinimumSize(1280, 1024)e)
        self.setActiveKeyButton = QtGui.QPushButton("Set active key")

#        self.importPrivateKeysLabel = QtGui.QLabel()
#        self.importPrivateKeysLabel.setFrameStyle(frameStyle)
        self.importPrivateKeysButton = QtGui.QPushButton("Import private keys")
        
#        self.setAccountNameLabel = QtGui.QLabel()
#        self.setAccountNameLabel.setFrameStyle(frameStyle)
        self.setAccountNameButton = QtGui.QPushButton("Account name")

#        self.createAccountLabel = QtGui.QLabel()
#        self.createAccountLabel.setFrameStyle(frameStyle)
        self.createAccountButton = QtGui.QPushButton("Create account")

        
        self.getInfoLabel = QtGui.QLabel()
        self.getInfoLabel.setFrameStyle(frameStyle)
        
#        self.openFileNameLabel = QtGui.QLabel()
#        self.openFileNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton = QtGui.QPushButton("set Contract Steps")

#        self.issueLabel = QtGui.QLabel()
#        self.issueLabel.setFrameStyle(frameStyle)
        self.issueButton = QtGui.QPushButton("Issue" + Order.currency)

#        self.recipientNameLabel = QtGui.QLabel()
#        self.recipientNameLabel.setFrameStyle(frameStyle)
        self.recipientNameButton = QtGui.QPushButton("set recipient name")
       
#        self.amountLabel = QtGui.QLabel()
#        self.amountLabel.setFrameStyle(frameStyle)
        self.amountButton = QtGui.QPushButton("amount")
        
#        self.issueToAccountLabel = QtGui.QLabel()
#        self.issueToAccountLabel.setFrameStyle(frameSt self.setMinimumSize(1280, 1024)yle)
        self.issueToAccountButton = QtGui.QPushButton("Send to receiving account")
        
#        self.chooseCurrencyLabel = QtGui.QLabel()
#        self.chooseCurrencyLabel.setFrameStyle(frameStyle)
        self.chooseCurrencyButton = QtGui.QPushButton("Set Token Name")
        
#        self.getInfoLabel = QtGui.QLabel()
#        self.getInfoLabel.setFrameStyle(frameStyle)
        self.getInfoButton = QtGui.QPushButton("GetInfo")
        
        self.getBalanceButton = QtGui.QPushButton("Get Balance")
    
        self.getAccountDetailsButton = QtGui.QPushButton("Get Account Details")
        
        
        self.getBalanceButton.clicked.connect(self.getBalance)    
        self.getAccountDetailsButton.clicked.connect(self.getAccountDetails)
        self.getInfoButton.clicked.connect(self.getInfo)
        self.stopButton.clicked.connect(self.stopChain)
        self.startButton.clicked.connect(self.startChain)
        self.restartButton.clicked.connect(self.resetChain)    
        self.setWalletNameButton.clicked.connect(self.setWalletName)
        self.createWalletButton.clicked.connect(self.createWallet)
        self.setOwnerKeyButton.clicked.connect(self.setOwnerKey)
        self.setActiveKeyButton.clicked.connect(self.setActiveKey)
        self.importPrivateKeysButton.clicked.connect(self.importPrivateKeys)
        self.setAccountNameButton.clicked.connect(self.createAccountName)
        self.createAccountButton.clicked.connect(self.createAccount)
        self.openContractButton.clicked.connect(self.loadTokenContract)
        self.openFileNameButton.clicked.connect(self.setContractSteps)
        self.issueButton.clicked.connect(self.issueCurrency)
        self.flushButton.clicked.connect(self.flushWallets)
        self.amountButton.clicked.connect(self.setAmount)
        self.recipientNameButton.clicked.connect(self.setRecipientName)
        self.issueToAccountButton.clicked.connect(self.issueToAccount)
        self.chooseCurrencyButton.clicked.connect(self.chooseCurrency)
         
        self.native = QtGui.QCheckBox()
        self.native.setText("EZEOS")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QtGui.QGridLayout()
        
        layout.addWidget(self.issueToAccountButton, 7, 2)
        layout.addWidget(self.amountButton, 7, 1)
        layout.addWidget(self.recipientNameButton, 7, 0)        
        layout.addWidget(self.issueButton, 6, 3)
        layout.addWidget(self.openFileNameButton, 6, 2)
        layout.addWidget(self.chooseCurrencyButton, 6, 1)
        layout.addWidget(self.openContractButton, 6, 0)
        layout.addWidget(self.getBalanceButton, 5, 3)
        layout.addWidget(self.getAccountDetailsButton, 5, 2)
        layout.addWidget(self.setAccountNameButton, 5, 0)
        layout.addWidget(self.createAccountButton, 5, 1)
        layout.addWidget(self.importPrivateKeysButton, 4, 4)
        layout.addWidget(self.setOwnerKeyButton, 4, 3)
        layout.addWidget(self.setActiveKeyButton, 4, 2)
        layout.addWidget(self.createWalletButton, 4, 1)
        layout.addWidget(self.setWalletNameButton, 4, 0)    
        layout.addWidget(self.flushButton, 1, 4 )                
        layout.addWidget(self.restartButton, 1, 3)
        layout.addWidget(self.startButton, 1, 2)
        layout.addWidget(self.stopButton, 1, 1)
        layout.addWidget(self.getInfoButton, 1, 0)
        layout.addWidget(self.getInfoLabel,  0, 0, 1, 6)
       
        
        
        self.setLayout(layout)
        self.setWindowTitle("EZEOS")
        self.showMaximized()
        
        
    def stopChain(self):
        
        subprocess.check_output(['killall','nodeos'])   
        self.getInfoLabel.setText('chain stopped')
        
        
    def startChain(self):
      

        out = subprocess.Popen(['xterm', '-e', 'nodeos --resync'])
        home = os.environ['HOME'] 
        os.environ['EOS_SOURCE'] = home + "/eos"
        os.environ['EOS_NODEOS']= home + ".local/share/eosio/nodeos/"
        self.getInfoLabel.setText('chain started' + out )
        
    def resetChain(self):
      
        out = subprocess.check_output(['rm', '-rf', '$EOS_NODEOS' + 'data'])
        self.getInfoLabel.setText('chain reset' + out)
        
    def setWalletName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Wallet.name = text
            self.getInfoLabel.setText(text)
       
    def createWallet(self):
        createAccount = os.environ['HOME'] + '/eosio-wallet'
        print('***' + createAccount + '***')
        if not os.path.exists(createAccount):
            os.makedirs(createAccount)
        #cleos wallet create -n test
        out = subprocess.check_output(['cleos','wallet', 'create', '-n', Wallet.name])
        f = open( Wallet.name, 'w' )
        f.write(out)
        f.close()
        self.getInfoLabel.setText(out)
        

    def setOwnerKey(self):    
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( Wallet.name + "OwnerKeys", 'w' )
        f.write(key)
        Wallet.OwnerKey1 = key
        Wallet.PublicKey1 = key2
        self.getInfoLabel.setText(out)
       

    def setActiveKey(self):
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( Wallet.name + "PrivateKey", 'w' )
        f.write(key)
        f.close()
        Wallet.OwnerKey2 = key
        Wallet.PublicKey2 = key2
        self.getInfoLabel.setText(out)
        
    def importPrivateKeys(self):
        out = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.OwnerKey1])
        out1 = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.OwnerKey2])
        self.getInfoLabel.setText(Wallet.OwnerKey1 +"\n"+ Wallet.OwnerKey2 + "\n" + out + "\n" + out1)
        
    def createAccountName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Account name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Account.name = text
            self.getInfoLabel.setText(text)
        
    def createAccount(self): 
        out = subprocess.check_output(['cleos', 'create', 'account', 'eosio', Account.name, Wallet.PublicKey1, Wallet.PublicKey2])
        self.getInfoLabel.setText(out)
    
    def loadTokenContract(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                "QFileDialog.getExistingDirectory()",
                self.getInfoLabel.text(), options)
        if directory:
            Order.contract = directory
            Order.contractAccountName = os.path.basename(directory)
            
        self.getInfoLabel.setText(directory)
        
    def setContractSteps(self):
        out = subprocess.check_output(['cleos', 'set', 'contract', Account.name,  Order.contract, '-p', Account.name ])
        self.getInfoLabel.setText(out)

    def chooseCurrency(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Token name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Order.currency = ' ' + text
            self.getInfoLabel.setText(text)

    
    def issueCurrency(self):
        token1 = '{"issuer": "'
        token2 = Account.name
        token3 = '", "maximum_supply": "1000000.0000 '
        token4 = Order.currency
        token5 = '", "can_freeze": 1, "can_recall": 1, "can_whitelist": 1}'
        finalToken = token1 + token2 + token3 + token4 + token5
        print(finalToken)
        out = subprocess.check_output(['cleos', 'push', 'action', Account.name, 'create', finalToken, '-p', Account.name + '@active']) 
        self.getInfoLabel.setText(out)
    
    def setRecipientName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Recipient name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Order.name = text
            self.getInfoLabel.setText(text)
    
    def setAmount(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Amount:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Order.amount = text + Order.currency
            self.amountLabel.setText(Order.amount)
            self.getInfoLabel.setText(Order.amount)
    
    def issueToAccount(self):
        
        out = subprocess.check_output(['cleos', 'get', 'account', Account.name ])
        self.getInfoLabel.setText(out)
        #cleos push action eosio.token issue '{"to": "scott", "quantity": "900.0000 EOS", "memo": "testing"}' -p eosio.token@active
        token1 = '{"to": "'
        token2 = Order.name
        token3 = '", "quantity": "'
        token4 = Order.amount
        token5 = '", "memo": "testing"}'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        out = subprocess.check_output(['cleos', 'push', 'action', Account.name, 'issue', finalToken, '-p', Account.name]) # + '@active']) 
        self.getInfoLabel.setText(out)
    
    def flushWallets(self):
        subprocess.check_output(['rm', '-rf', os.environ['HOME'] + '/eosio-wallet/'])
        self.getInfoLabel.setText("Deleted Wallets")
        
    def getInfo(self):
        out = subprocess.check_output(['cleos', 'get', 'info'])
        self.getInfoLabel.setText(out)
        
    def getAccountDetails(self):
        
        out = subprocess.check_output(['cleos', 'get', 'account', Account.name ])
        self.getInfoLabel.setText(out)
    
    def getBalance(self):
        #cmd = 'cleos ' + 'get ' + 'currency ' + 'balance ' + Account.name + ' ' + Order.contractAccountName + ' ' + Order.currency 
        #print(cmd)
        out = subprocess.check_output(['cleos', 'get', 'currency', 'balance', Order.contractAccountName, Account.name,  Order.currency ])
        self.getInfoLabel.setText(out)
    


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    dialog = Dialog()
    sys.exit(dialog.exec_())
