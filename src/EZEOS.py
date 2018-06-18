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
import pexpect


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

import sys
from PyQt4 import QtCore, QtGui

class Block():
    number = "1"

class Wallet():
    name = ""
    key = ""
    ownerKey1 = ""
    publicKey1 = ""
    OwnerKey2 = ""
    publicKey2 = ""
    locked = False
    def reset(self):
         self.name = ""
         self.key = ""
         self.ownerKey1 = ""
         self.publicKey1 = ""
         self.ownerKey2 = ""
         self.publicKey2 = ""
         self.locked = False
        

class Account():
    name = ""
    def reset(self):
        self.name = ''
    
class Order():
    to = ""
    amount = 0.0000
    contract = ""
    currency = ""
    contractAccountName = ""
    def reset(self):
        self.to = ""
        self.amount = 0.0000
        self.contract = ""
        self.currency = ""
        self.contractAccountName = ""
    
    
class Dialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.timer = QtCore.QTimer()
        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel
        self.openContractButton = QtGui.QPushButton("Open Contract")    
        self.setWalletNameButton = QtGui.QPushButton("Wallet name")
        self.restartButton = QtGui.QPushButton("Reset chain")
        self.startButton = QtGui.QPushButton("Start chain")
        self.stopButton = QtGui.QPushButton("Stop chain")
        self.flushButton = QtGui.QPushButton("Flush wallets")
        self.createWalletButton = QtGui.QPushButton("Create wallet")
        self.setOwnerKeyButton = QtGui.QPushButton("Set owner Key")
        self.setActiveKeyButton = QtGui.QPushButton("Set active key")
        self.importPrivateKeysButton = QtGui.QPushButton("Import private keys")
        self.setAccountNameButton = QtGui.QPushButton("Account name")
        self.createAccountButton = QtGui.QPushButton("Create account")        
        self.getInfoLabel = QtGui.QLabel()
        self.getInfoLabel.setFrameStyle(frameStyle)
        self.walletNameLabel = QtGui.QLabel()
        self.walletNameLabel.setFrameStyle(frameStyle)
        self.accountNameLabel = QtGui.QLabel()
        self.accountNameLabel.setFrameStyle(frameStyle)
        self.contractNameLabel = QtGui.QLabel()
        self.contractNameLabel.setFrameStyle(frameStyle)    
        self.openFileNameButton = QtGui.QPushButton("Set Contract Steps")
        self.issueButton = QtGui.QPushButton("Issue" + Order.currency)
        self.recipientNameButton = QtGui.QPushButton("Set recipient name")
        self.amountButton = QtGui.QPushButton("amount")
        self.issueToAccountButton = QtGui.QPushButton("Send to receiving account")
        self.chooseCurrencyButton = QtGui.QPushButton("Set Token Name")
        self.getInfoButton = QtGui.QPushButton("GetInfo")        
        self.getBalanceButton = QtGui.QPushButton("Get Balance")    
        self.getAccountDetailsButton = QtGui.QPushButton("Get Account Details")
        self.toggleWalletLock = QtGui.QCheckBox("Lock wallet")
        self.listWalletsButton = QtGui.QPushButton("List Wallets")
        self.getBlockInfoButton = QtGui.QPushButton("Block Info")
        self.setBlockNumberButton = QtGui.QPushButton("Set Block number")

        self.toggleWalletLock.toggled.connect(self.lockWallet)
        self.listWalletsButton.clicked.connect(self.listWallets)
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
        self.openContractButton.clicked.connect(self.LoadContract)
        self.openFileNameButton.clicked.connect(self.setContractSteps)
        self.issueButton.clicked.connect(self.issueCurrency)
        self.flushButton.clicked.connect(self.flushWallets)
        self.amountButton.clicked.connect(self.setAmount)
        self.recipientNameButton.clicked.connect(self.setRecipientName)
        self.issueToAccountButton.clicked.connect(self.issueToAccount)
        self.chooseCurrencyButton.clicked.connect(self.chooseCurrency)
        self.getBlockInfoButton.clicked.connect(self.getBlockInfo)
        self.setBlockNumberButton.clicked.connect(self.setBlockNumber)
         
        self.native = QtGui.QCheckBox()
        self.native.setText("EZEOS")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QtGui.QGridLayout()

        layout.addWidget(self.contractNameLabel, 5, 0)
        layout.addWidget(self.accountNameLabel, 4, 0)    
        layout.addWidget(self.walletNameLabel, 1, 0)
        layout.addWidget(self.getInfoLabel,  0, 0, 1, 7)
        
        
        self.tabs = QtGui.QTabWidget()
        self.tab1 = QtGui.QWidget()	
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()	
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        self.tabs.resize(200,2000) 
 
       
        self.tabs.addTab(self.tab1,"Block chain")
        self.tabs.addTab(self.tab2,"Wallets")
        self.tabs.addTab(self.tab3,"Accounts")
        self.tabs.addTab(self.tab4,"Contract")
        self.tabs.addTab(self.tab5,"eosio.token")
 
       
        self.tab1.layout = QtGui.QVBoxLayout(self)
        self.tab1.layout.addWidget(self.stopButton)
        self.tab1.layout.addWidget(self.restartButton)
        self.tab1.layout.addWidget(self.startButton) 
        self.tab1.layout.addWidget(self.getBlockInfoButton)
        self.tab1.layout.addWidget(self.setBlockNumberButton)
        self.tab1.setLayout(self.tab1.layout)
 
       
        self.tab2.layout = QtGui.QVBoxLayout(self)
        self.tab2.layout.addWidget(self.flushButton)
        self.tab2.layout.addWidget(self.setWalletNameButton)
        self.tab2.layout.addWidget(self.createWalletButton)
        self.tab2.layout.addWidget(self.listWalletsButton)
        self.tab2.layout.addWidget(self.setOwnerKeyButton)
        self.tab2.layout.addWidget(self.setActiveKeyButton)
        self.tab2.layout.addWidget(self.importPrivateKeysButton)
        self.tab2.layout.addWidget(self.toggleWalletLock)
        self.tab2.setLayout(self.tab2.layout)
    
        self.tab3.layout = QtGui.QVBoxLayout(self)
        self.tab3.layout.addWidget(self.setAccountNameButton)
        self.tab3.layout.addWidget(self.createAccountButton)
        self.tab3.layout.addWidget(self.getAccountDetailsButton)
        self.tab3.layout.addWidget(self.getBalanceButton)
        self.tab3.setLayout(self.tab3.layout) 
        
        self.tab4.layout = QtGui.QVBoxLayout(self)
        self.tab4.layout.addWidget(self.openContractButton)
        self.tab4.layout.addWidget(self.openFileNameButton)
        self.tab4.setLayout(self.tab4.layout)
    
        self.tab5.layout = QtGui.QVBoxLayout(self) 
        self.tab5.layout.addWidget(self.chooseCurrencyButton)
        self.tab5.layout.addWidget(self.issueButton)
        self.tab5.layout.addWidget(self.recipientNameButton)
        self.tab5.layout.addWidget(self.amountButton)
        self.tab5.layout.addWidget(self.issueToAccountButton)
        self.tab5.setLayout(self.tab5.layout)
       
    
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        self.setWindowTitle("EZEOS")
        self.showMaximized()
        
    
        
    
    
    def update_label(self):
    
        self.walletNameLabel.setText('Wallet name: ' + Wallet.name)
        self.accountNameLabel.setText('Account name: ' + Account.name)
        self.contractNameLabel.setText('Contract name: ' + Order.contract)
        
        
    
    def lockWallet(self):
        if Wallet.locked == False:
            print('Lock')
            subprocess.check_output(['cleos','wallet', 'lock', '-n', Wallet.name])
            Wallet.locked = True
            self.listWallets()
        else:
            child = pexpect.spawn('cleos', ['wallet', 'unlock', '-n', Wallet.name])
            child.expect('password:')
            out = subprocess.check_output(['cat', os.environ['EZEOS_SOURCE'] +'/'+ Wallet.name]) 
            child.sendline(out)
            child.expect(pexpect.EOF)
            child.close()
            self.listWallets()
            Wallet.locked = False
        
    def stopChain(self):
        subprocess.check_output(['killall','nodeos'])   
        self.getInfoLabel.setText('chain stopped')
        
        
    def startChain(self):
        self.getInfoLabel.setText('chain started')
        subprocess.Popen(['xterm', '-e', 'nodeos --resync'])
        home = os.environ['HOME'] 
        os.environ['EOS_SOURCE'] = home + "/eos"
        os.environ['EOS_NODEOS'] = home + ".local/share/eosio/nodeos/"
        os.environ['EZEOS_SOURCE'] = home + "/EZEOS/src"
        
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)  # every 10,000 milliseconds
        
    def resetChain(self):
        out = subprocess.check_output(['rm', '-rf', '$EOS_NODEOS' + 'data'])
        self.getInfoLabel.setText('chain reset' + out)
        Account.reset()
        Wallet.reset()
        Order.reset()
        
    def setWalletName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Wallet.name = text
            self.getInfoLabel.setText(text)
       
    def createWallet(self):
        createAccount = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(createAccount):
            os.makedirs(createAccount)
        out = subprocess.check_output(['cleos','wallet', 'create', '-n', Wallet.name])
        f = open( Wallet.name, 'w' )
        f.write(out)
        f.close()
        line = subprocess.check_output(['tail', '-1', Wallet.name])
        line = line.replace('"', '')
        f = open( Wallet.name, 'w' )
        f.write(line)
        f.close()
        Wallet.key = line
        Wallet.locked = False
        cwd = os.getcwd()
        text = ' saved to ' + cwd
        self.getInfoLabel.setText(line + text)
    

    def setOwnerKey(self):    
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( Wallet.name + "OwnerKeys", 'w' )
        f.write(key)
        Wallet.ownerKey1 = key
        Wallet.publicKey1 = key2
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
        Wallet.ownerKey2 = key
        Wallet.publicKey2 = key2
        self.getInfoLabel.setText(out)
        
    def importPrivateKeys(self):
        out = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.ownerKey1])
        out1 = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.ownerKey2])
        self.getInfoLabel.setText(Wallet.ownerKey1 +"\n"+ Wallet.ownerKey2 + "\n" + out + "\n" + out1)
        
    def createAccountName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Account name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Account.name = text
            self.getInfoLabel.setText(text)
        
    def createAccount(self): 
        out = subprocess.check_output(['cleos', 'create', 'account', 'eosio', Account.name, Wallet.publicKey1, Wallet.publicKey2])
        self.getInfoLabel.setText(out)
    
    def LoadContract(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                "Load Contract",
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
    
    def setRecipientName(self):#            subprocess.check_output(['cleos','wallet', 'unlock', '-n', Wallet.name])
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
        
        out = subprocess.check_output(['cleos', 'get', 'currency', 'balance', Order.contractAccountName, Account.name,  Order.currency ])
        self.getInfoLabel.setText(out)
    
    def listWallets(self):    
        out = subprocess.check_output(['cleos', 'wallet', 'list'])
        self.getInfoLabel.setText(out)
    
    def setBlockNumber(self):    
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Block number:", QtGui.QLineEdit.Normal,
                Block.number)
        if ok and text != '':
            Account.name = text
            self.getInfoLabel.setText(text)
        
    def getBlockInfo(self):    
        out = subprocess.check_output(['cleos', 'get', 'block', Block.number])
        self.getInfoLabel.setText(out)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    dialog = Dialog()
    sys.exit(dialog.exec_())
