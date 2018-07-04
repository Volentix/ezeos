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
import json
import time
from pprint import pprint

# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)
import sys
from PyQt4 import QtCore, QtGui


home = os.environ['HOME'] 
os.environ['EOS_SOURCE'] = home + "/eos"
os.environ['EOS_NODEOS'] = home + ".local/share/eosio/nodeos/"
os.environ['EZEOS_SOURCE'] = home + "/ezeos/src"

class BlockChain():
    class Block():
        def __init__(self):
            self.number = "1"
    def __init__(self):
        self.net = ['main', 'test', 'local']
        self.block = self.Block()
        self.running = False
        self.producer = ""
        self.testProducer = ""
        self.producerList =     [
                                    'https://api.eosnewyork.io:443', 
                                    'https://api.eosdetroit.io:443',
                                    'https://eos.greymass.com:443',
                                    'https://api.eosmetal.io:18890',
                                    'http://api.hkeos.com:80',
                                    'https://eosapi.blockmatrix.network:443',
                                    'https://fn.eossweden.se:443',
                                    'http://api.blockgenicbp.com:8888',
                                    'http://mainnet.eoscalgary.io:80',
                                    'http://mainnet.eoscalgary.io:80',
                                    'https://node1.eosphere.io',
                                    'https://eos.saltblock.io',
                                    'http://eos-api.worbli.io:80',
                                    'https://eos-api.worbli.io:443',
                                    'http://mainnet.eoscalgary.io:80',
                                    'https://user-api.eoseoul.io:443',
                                    'http://user-api.eoseoul.io:80', 
                                    'https://node2.liquideos.com:8883',
                                    'http://node2.liquideos.com:8888',
                                    'https://api.eosuk.io:443',
                                    'http://api1.eosdublin.io:80',
                                    'http://api.eosvibes.io:80',
                                    'http://api.cypherglass.com:8888',
                                    'https://api.cypherglass.com:443',
                                    'http://bp.cryptolions.io:8888',
                                    'http://dc1.eosemerge.io:8888',
                                    'https://dc1.eosemerge.io:5443',
                                    'https://api.eosio.cr:443',
                                    'https://api.eosn.io',
                                    'https://eu1.eosdac.io:443',
                                ]
        self.testProducerList = [
                                     'eosgreen.uk.to:9875',
                                     'ctestnet.edenx.io:62071',
                                     '54.194.49.21:9875',
                                     'superhero.cryptolions.io:9885',
                                     'venom.eoscalgary.com:9877',
                                     'joker.superhero.eos.roelandp.nl:9873',
                                     'ctestnet.eosdetroit.com:1339',
                                     'bp7-d3.eos42.io:9876',
                                     'superheroes.eosio.africa:9876',
                                     '156.38.160.91:9876',
                                     '166.70.202.194:9877',
                                     '18.188.52.250:9889',
                                     'ctest.eosnewyork.io:9870',
                                     '35.195.161.56:9876',
                                     '159.89.197.162:9877',
                                     'dawn3-seed.tokenika.io:9876',
                                     'bp.blockgenic.io:9876',
                                     '47.52.18.70:9876',
                                     '120.27.130.60:9876',
                                     'ctest.koreos.io:9876',
                                     'ctestnet.objectcomputing.com:9876',
                                     'test.eosys.io:9875',
                                     'bp-test.eosasia.one:9876',
                                     '138.68.15.85:9876',
                                     '47.88.222.80:9876',
                                     '54.233.222.22:9875',
                                     '39.108.231.157:9877',
                                     'ctestnet.eoshenzhen.io:9876',
                                     'eosbp.enjoyshare.net:9876',
                                     'bpt1.eosbixin.com:9876',
                                     '46.4.253.242:7610',
                                     'superhero-bp1.eosphere.io:9876',
                                     '138.68.238.129:9875',
                                     '178.49.174.48:9876',
                                     'superhero.worbli.io:9876',
                                     'wonderwoman.eosreal.io:9876',
                                     'eosbrazil.com:9878',
                                     '35.202.41.160:9876',
                              ]

class Wallet():
    
    def __init__(self):
        self.name = ""
        self.key = ""
        self.ownerPrivateKey = ""
        self.ownerPublicKey = ""
        self.activePrivateKey = ""
        self.activePublicKey = ""
        self.locked = False
        self.url = "http://localhost:8888"
        
    def reset(self):
         self.name = ""
         self.key = ""
         self.ownerPrivateKey = ""
         self.ownerPublicKey = ""
         self.activePrivateKey = ""
         self.activePublicKey = ""
         self.locked = False
        

class Account():
    
    def __init__(self):
        self.name = ""
        self.creator = ""
        self.creatorOwnerKey = ""
        self.creatorActiveKey = ""
                            
        
    def reset(self):
        self.name = ""
    
class Order():
    def __init__(self):
        self.to = ""
        self.amount = 0.0000
        self.contract = ""
        self.currency = ""
        self.contractAccountName = ""
        self.stakeCPU = ""
        self.stakeBandWidth = ""
        self.buyRam = 0
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
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)  
        self.wallet = Wallet()
        self.order = Order()
        self.account = Account()
        self.blockchain = BlockChain()
        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel
        self.openContractButton = QtGui.QPushButton("Open Contract")    
        self.setWalletNameButton = QtGui.QPushButton("Wallet Name") 
        self.openWalletNameButton = QtGui.QPushButton("Open Wallet") 
        self.setWalletPublicKeysButton = QtGui.QPushButton("Set Wallet Public Keys")
        self.restartButton = QtGui.QPushButton("Reset Local Chain")
        self.startButton = QtGui.QPushButton("Start Local Chain")
        self.stopButton = QtGui.QPushButton("Stop Local Chain")
        self.flushButton = QtGui.QPushButton("Flush Wallets")
        self.createWalletButton = QtGui.QPushButton("Create Wallet")
        self.setOwnerKeyButton = QtGui.QPushButton("Create Owner Keys")
        self.setActiveKeyButton = QtGui.QPushButton("Create Active Keys")
        self.importPrivateKeysButton = QtGui.QPushButton("Import Private Keys")
        self.setAccountNameButton = QtGui.QPushButton("Account Name")
        self.setCreatorAccountNameButton = QtGui.QPushButton("Creator Account Name")
        self.setStakeCPUAmountButton = QtGui.QPushButton("Stake CPU amount")
        self.setStakeBandWidthAmountButton = QtGui.QPushButton("Stake Bandwidth amount")
        self.setBuyRAMAmountButton = QtGui.QPushButton("buy RAM")
        self.createAccountButton = QtGui.QPushButton("Create Account")        
        self.getInfoLabel = QtGui.QLabel()
        self.getInfoLabel.setFrameStyle(frameStyle)
        self.walletNameLabel = QtGui.QLabel()
        self.walletNameLabel.setFrameStyle(frameStyle)
        self.accountNameLabel = QtGui.QLabel()
        self.accountNameLabel.setFrameStyle(frameStyle)
        self.contractNameLabel = QtGui.QLabel()
        self.contractNameLabel.setFrameStyle(frameStyle)    
        self.openFileNameButton = QtGui.QPushButton("Set Contract Steps")
        self.issueButton = QtGui.QPushButton("Issue Currency")
        self.recipientNameButton = QtGui.QPushButton("Set Recipient Name")
        self.amountButton = QtGui.QPushButton("Amount")
        self.issueToAccountButton = QtGui.QPushButton("Issue To Account")
        self.transferToAccountButton = QtGui.QPushButton("Transfer To Account")
        self.chooseCurrencyButton = QtGui.QPushButton("Set Token Name")
        self.getInfoButton = QtGui.QPushButton("Get Info")        
        self.getBalanceButton = QtGui.QPushButton("Get Balance")    
        self.getAccountDetailsButton = QtGui.QPushButton("Get Account Details")
       
        self.listWalletsButton = QtGui.QPushButton("List Wallets")
        self.getBlockInfoButton = QtGui.QPushButton("Block Info")
        self.setBlockNumberButton = QtGui.QPushButton("Set Block Number")
        self.getActionsButton = QtGui.QPushButton("Get Actions")
        self.showKeysButton = QtGui.QPushButton("Show Keys")
        self.listProducersButton = QtGui.QPushButton("Get Block Producers")
        self.getProducerInfoButton = QtGui.QPushButton("Get Block Producer Info")
        self.producerBox = QtGui.QComboBox()
        self.testProducerBox = QtGui.QComboBox()
        self.producerBox.setObjectName(("Access to Main Net"))
        self.testProducerBox.setObjectName(("Access To Test Net"))
        for i in self.blockchain.producerList:
            self.producerBox.addItem(i)
        for i in self.blockchain.testProducerList:
            self.testProducerBox.addItem(i)
    
        self.toggleMainNet = QtGui.QCheckBox("Main Net")
        self.toggleTestNet = QtGui.QCheckBox("Test Net")
        self.toggleLocalNet = QtGui.QCheckBox("Local Net")
        self.toggleWalletLock = QtGui.QCheckBox("Lock Wallet")
        
        self.toggleMainNet.toggled.connect(self.mainNet)
        self.toggleTestNet.toggled.connect(self.testNet)
        self.toggleLocalNet.toggled.connect(self.localNet)
        self.toggleWalletLock.toggled.connect(self.lockWallet)
        self.listProducersButton.clicked.connect(self.listProducers)
        
        self.setWalletPublicKeysButton.clicked.connect(self.setWalletPublicKeys)
        self.listWalletsButton.clicked.connect(self.listWallets)
        self.getBalanceButton.clicked.connect(self.getBalance)    
        self.getAccountDetailsButton.clicked.connect(self.getAccountDetails)
        self.getInfoButton.clicked.connect(self.getInfo)
        self.stopButton.clicked.connect(self.stopChain)
        self.startButton.clicked.connect(self.startChain)
        self.restartButton.clicked.connect(self.resetChain)    
        self.setWalletNameButton.clicked.connect(self.setWalletName)
        self.openWalletNameButton.clicked.connect(self.openWalletName)
        self.createWalletButton.clicked.connect(self.createWallet)
        self.setOwnerKeyButton.clicked.connect(self.setOwnerKey)
        self.setActiveKeyButton.clicked.connect(self.setActiveKey)
        self.importPrivateKeysButton.clicked.connect(self.importPrivateKeys)
        self.setAccountNameButton.clicked.connect(self.createAccountName)
        self.setCreatorAccountNameButton.clicked.connect(self.createCreatorAccountName)
        self.setStakeCPUAmountButton.clicked.connect(self.setStakeCPUAmount)
        self.setStakeBandWidthAmountButton.clicked.connect(self.setStakeBandWidthAmount)
        self.setBuyRAMAmountButton.clicked.connect(self.setBuyRAMAmount)
        self.createAccountButton.clicked.connect(self.createAccount)
        self.openContractButton.clicked.connect(self.LoadContract)
        self.openFileNameButton.clicked.connect(self.setContractSteps)
        self.issueButton.clicked.connect(self.issueCurrency)
        self.flushButton.clicked.connect(self.flushWallets)
        self.amountButton.clicked.connect(self.setAmount)
        self.recipientNameButton.clicked.connect(self.setRecipientName)
        self.issueToAccountButton.clicked.connect(self.issueToAccount)
        self.transferToAccountButton.clicked.connect(self.transferToAccount)
        self.chooseCurrencyButton.clicked.connect(self.chooseCurrency)
        self.getBlockInfoButton.clicked.connect(self.getBlockInfo)
        self.setBlockNumberButton.clicked.connect(self.setBlockNumber)
        self.getActionsButton.clicked.connect(self.getActions)
        self.showKeysButton.clicked.connect(self.showKeys)
        self.listProducersButton.clicked.connect(self.listProducers)
        self.getProducerInfoButton.clicked.connect(self.getProducerInfo)
         
        self.native = QtGui.QCheckBox()
        self.native.setText("EZEOS")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QtGui.QGridLayout()
        layout.addWidget(self.toggleMainNet, 6, 0)
        layout.addWidget(self.toggleTestNet, 5, 0)
        layout.addWidget(self.toggleLocalNet, 4, 0)
        layout.addWidget(self.contractNameLabel, 3, 0)
        layout.addWidget(self.accountNameLabel, 2, 0)    
        layout.addWidget(self.walletNameLabel, 1, 0)
        layout.addWidget(self.getInfoLabel,  0, 0, 1, 7)
        
        
        self.tabs = QtGui.QTabWidget()
        self.tab1 = QtGui.QWidget()	
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()	
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        self.tab6 = QtGui.QWidget()
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
        self.tab1.layout.addWidget(self.listProducersButton)
        self.label = QtGui.QLabel("Main Net")
        self.tab1.layout.addWidget(self.label)
        self.tab1.layout.addWidget(self.producerBox)
        self.label2 = QtGui.QLabel("Test Net")
        self.tab1.layout.addWidget(self.label2)
        self.tab1.layout.addWidget(self.testProducerBox)
        self.tab1.layout.addWidget(self.getProducerInfoButton)            
        self.tab1.setLayout(self.tab1.layout)
 
       
        self.tab2.layout = QtGui.QVBoxLayout(self)
        self.tab2.layout.addWidget(self.flushButton)
        self.tab2.layout.addWidget(self.setWalletNameButton)
        self.tab2.layout.addWidget(self.openWalletNameButton)
        self.tab2.layout.addWidget(self.createWalletButton)
        self.tab2.layout.addWidget(self.listWalletsButton)
        self.tab2.layout.addWidget(self.setOwnerKeyButton)
        self.tab2.layout.addWidget(self.setActiveKeyButton)
        self.tab2.layout.addWidget(self.importPrivateKeysButton)
        self.tab2.layout.addWidget(self.setWalletPublicKeysButton)
        self.tab2.layout.addWidget(self.showKeysButton)
        self.tab2.layout.addWidget(self.toggleWalletLock)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QtGui.QVBoxLayout(self)
        self.tab3.layout.addWidget(self.setAccountNameButton)
        self.tab3.layout.addWidget(self.setCreatorAccountNameButton)
        self.tab3.layout.addWidget(self.setStakeCPUAmountButton)
        self.tab3.layout.addWidget(self.setStakeBandWidthAmountButton)
        self.tab3.layout.addWidget(self.setBuyRAMAmountButton)
        self.tab3.layout.addWidget(self.createAccountButton)
        self.tab3.layout.addWidget(self.getAccountDetailsButton)
        self.tab3.layout.addWidget(self.getActionsButton)
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
        self.getActionsButton.clicked.connect(self.getActions)
        self.tab5.layout.addWidget(self.transferToAccountButton)
        self.tab5.setLayout(self.tab5.layout)
        
        self.tab6.layout = QtGui.QVBoxLayout(self) 
    
        self.tab6.setLayout(self.tab6.layout)

        layout.addWidget(self.tabs)
        self.setLayout(layout)
        self.setWindowTitle("EZEOS")
        self.showMaximized()
 
    
    def showKeys(self):
        out = 'Owner Public Key: ' + '\n' + str(self.wallet.ownerPublicKey) + '\n'  + 'Active Public Key: ' + '\n' + str(self.wallet.activePublicKey) + '\n' + 'Creator Key: ' + '\n' + self.account.creatorActiveKey 
        self.getInfoLabel.setText(str(out))
    
    def update_label(self):
        self.walletNameLabel.setText('Wallet name: ' + self.wallet.name)
        self.accountNameLabel.setText('Account name: ' + self.account.name)
        self.contractNameLabel.setText('Contract name: ' + self.order.contract)
        self.toggleLocalNet.setChecked(self.blockchain.running)
        if self.blockchain.running:
            self.toggleMainNet.setChecked(False)
            self.toggleTestNet.setChecked(False)
        self.blockchain.producer = self.producerBox.currentText()
        self.blockchain.testProducer = self.testProducerBox.currentText()
        
       
    def getActions(self):
        out = subprocess.check_output(['cleos','get', 'actions', self.account.name])   
        self.getInfoLabel.setText(out)
        
    
    def lockWallet(self):
        if self.wallet.locked == False:
            print('Lock')
            subprocess.check_output(['cleos','wallet', 'lock','-n', self.wallet.name])
            self.wallet.locked = True
            self.listWallets()
        else:
            print('unLock')
            child = pexpect.spawn('cleos', ['wallet', 'unlock', '-n', self.wallet.name])
            print('unLock2')
            child.expect('password:')
            print('unLock3')
            out = subprocess.check_output(['cat', os.environ['EZEOS_SOURCE'] +'/'+ self.wallet.name]) 
            child.sendline(out)
            child.expect(pexpect.EOF)
            child.close()
            self.listWallets()
            self.wallet.locked = False
        
    def stopChain(self):
         
        try:
            subprocess.check_output(['killall','nodeos'])
            self.getInfoLabel.setText('Chain stopped')
            self.blockchain.running = False
        except:
            self.getInfoLabel.setText('No chain running')
            self.blockchain.running = False
           
     
    def startChain(self):
        subprocess.Popen(['xterm', '-e', 'nodeos --resync'])
        self.getInfoLabel.setText('chain started')
        self.blockchain.running = True
        self.blockchain.net = 'local'
        
        
        
    def resetChain(self):
        out = ''
        try:
            out = subprocess.check_output(['rm', '-rf', '$EOS_NODEOS' + 'data'])          
        except:
            print('Already reset')
        self.blockchain.running = False   
        self.getInfoLabel.setText('Chain reset' + str(out))
        self.account.reset()
        self.wallet.reset()
        self.order.reset()
        
    def setWalletName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.wallet.name = text
            self.getInfoLabel.setText(text)
    def openWalletName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            out = subprocess.check_output(['cleos','wallet', 'open', '-n', text])
            self.getInfoLabel.setText(out)
    
    def setWalletPublicKeys(self):
       ownerPublicKey = self.wallet.name + 'ownerPublicKeys'
       activePublicKey = self.wallet.name + 'ActivePublicKey'
       self.wallet.ownerPublicKey = subprocess.check_output(['cat', ownerPublicKey]) 
       self.wallet.activePublicKey = subprocess.check_output(['cat', activePublicKey]) 
       out = 'Owner Public Key: ' + '\n' + self.wallet.ownerPublicKey + '\n'  + 'Active Public Key: ' + '\n' + self.wallet.activePublicKey + '\n' + 'Creator Key: ' + '\n' + self.account.creatorActiveKey 
       self.getInfoLabel.setText(out)
    
    def createWallet(self):
        createAccount = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(createAccount):
            os.makedirs(createAccount)
        if self.blockchain.net == 'test' or self.blockchain.net == 'main':
            out = subprocess.check_output(['cleos','-u', '"' + str(self.blockchain.producer) + '"' ,'wallet', 'create', '-n', self.wallet.name])
        else:
            out = subprocess.check_output(['cleos','wallet', 'create', '-n', self.wallet.name])
        f = open( self.wallet.name, 'w' )
        f.write(out)
        f.close()
        line = subprocess.check_output(['tail', '-1', self.wallet.name])
        line = line.replace('"', '')
        f = open( self.wallet.name, 'w' )
        f.write(line)
        f.close()
        self.wallet.key = line
        self.wallet.locked = False
        cwd = os.getcwd()
        text = ' saved to ' + cwd
        self.getInfoLabel.setText(line + text)
    

    def setOwnerKey(self):    
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( self.wallet.name + "ownerPrivateKeys", 'w' )
        f.write(key)
        f.close()
        f = open( self.wallet.name + "ownerPublicKeys", 'w' )
        f.write(key2)
        f.close()
        self.wallet.ownerPrivateKey= key
        self.wallet.ownerPublicKey = key2
        self.getInfoLabel.setText(out)
       

    def setActiveKey(self):
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( self.wallet.name + "ActivePrivateKey", 'w' )
        f.write(key)
        f.close()
        f = open( self.wallet.name + "ActivePublicKey", 'w' )
        f.write(key2)
        f.close()
        self.wallet.activePrivateKey = key
        self.wallet.activePublicKey = key2
        self.getInfoLabel.setText(out)
        
    def importPrivateKeys(self):
        out = subprocess.check_output(['cleos', 'wallet', 'import', '-n', self.wallet.name, self.wallet.ownerPrivateKey])
        out1 = subprocess.check_output(['cleos', 'wallet', 'import', '-n', self.wallet.name, self.wallet.activePrivateKey])
        self.getInfoLabel.setText(self.wallet.ownerPrivateKey +"\n"+ self.wallet.activePrivateKey + "\n" + out + "\n" + out1)
        
    def createAccountName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Account name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.name = text
            self.getInfoLabel.setText(text)
            
    def createCreatorAccountName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Creator name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.account.creator = text
            self.getInfoLabel.setText(text)
        
        
    def createAccount(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['cleos', 'create', 'account', 'eosio', self.account.name, self.wallet.ownerPublicKey, self.wallet.activePublicKey])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            permission = self.account.creator + '@active'
            out = subprocess.check_output(['cleos', '-u', self.blockchain.producer, 'system', 'newaccount', self.account.creator, self.account.name, self.wallet.ownerPublicKey , self.wallet.activePublicKey, '--stake-net', self.order.stakeBandWidth, '--stake-cpu', self.order.stakeCPU, '--buy-ram-kbytes', self.order.buyRam, '--transfer', '-p', permission])
        self.getInfoLabel.setText(out)
    
    def LoadContract(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                "Load Contract",
                self.getInfoLabel.text(), options)
        self.order.contract = directory
        self.order.contractAccountName = os.path.basename(directory)
        self.getInfoLabel.setText(directory)
        
    def setContractSteps(self):
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['cleos', 'set', 'contract', self.account.name,  self.order.contract, '-p', self.account.name ])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main': 
            permission = self.account.creator + '@active'
            out = subprocess.check_output(['cleos', '-u', self.blockchain.producer, 'system', 'newaccount', self.account.creator, self.account.name, self.wallet.ownerPublicKey , self.wallet.activePublicKey, '--stake-net', self.order.stakeBandWidth, '--stake-cpu', self.order.stakeCPU, '--buy-ram-kbytes', self.order.buyRam, '--transfer', '-p', permission])
        self.getInfoLabel.setText(out)
        
    def chooseCurrency(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Token name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.currency = text
            self.getInfoLabel.setText(text)
 
    def issueCurrency(self):
        token1 = '{"issuer": "'
        token2 = self.account.name
        token3 = '", "maximum_supply": "1000000.0000 '
        token4 = self.order.currency
        token5 = '", "can_freeze": 1, "can_recall": 1, "can_whitelist": 1}'
        finalToken = token1 + token2 + token3 + token4 + token5
        print(finalToken)
        out = subprocess.check_output(['cleos', 'push', 'action', self.account.name, 'create', finalToken, '-p', self.account.name + '@active']) 
        self.getInfoLabel.setText(out)
    
    def setRecipientName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Recipient name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.name = text
            self.getInfoLabel.setText(text)
    
    def setAmount(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Currency Amount:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.amount = text 
            self.getInfoLabel.setText(self.order.amount)
            
    def setStakeCPUAmount(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "CPU Amount:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.stakeCPU = text 
            self.getInfoLabel.setText(self.order.stakeCPU)
            
    def setStakeBandWidthAmount(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "BandWith Amount:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.stakeBandWidth = text 
            self.getInfoLabel.setText(self.order.stakeBandWidth)
            
    def setBuyRAMAmount(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Ram Amount:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            self.order.buyRam = text 
            self.getInfoLabel.setText(self.order.buyRam)
           
    def issueToAccount(self):
        out = subprocess.check_output(['cleos', 'get', 'account', self.account.name])
        token1 = '{"to": "'
        token2 = self.order.name
        token3 = '", "quantity": "'
        token4 = self.order.amount
        token5 = '", "memo": "testing"}'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        out = subprocess.check_output(['cleos', 'push', 'action', self.account.name, 'issue', finalToken, '-p', self.account.name]) # + '@active']) 
        self.getInfoLabel.setText(out)
        
    def transferToAccount(self):
        out = subprocess.check_output(['cleos', 'get', 'account', self.account.name ])
        token1 = '{"to": "'
        token2 = self.order.name
        token3 = '", "quantity": "'
        token4 = self.order.amount
        token5 = '", "memo": "testing"}'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        out = subprocess.check_output(['cleos', 'push', 'action', self.account.name, 'transfer', finalToken, '-p', self.account.name]) # + '@active']) 
        self.getInfoLabel.setText(out)
    
    def flushWallets(self):
        #subprocess.check_output(['rm', '-rf', os.environ['HOME'] + '/eosio-wallet/'])
        #self.getInfoLabel.setText("Deleted Wallets")
        self.getInfoLabel.setText("Are you sure you want to do this? How about you go and delete ~/eosio-wallet/ by hand" + "\n" + "This version is used to prototype with accounts on the main net")
        
    def getInfo(self):
        out = subprocess.check_output(['cleos', 'get', 'info'])
        self.getInfoLabel.setText(out)
        
    def getAccountDetails(self):    
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['cleos', 'get', 'account', self.account.name ])
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'account', self.account.name ])
        self.getInfoLabel.setText(out)    
        
    
    def getBalance(self):   
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(['cleos', 'get', 'currency', 'balance', self.order.contractAccountName, self.account.name, self.order.currency ])
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'currency', 'balance', 'eosio.token', self.account.name, self.order.currency ])       
        self.getInfoLabel.setText(out)    
    
    def listWallets(self):
        out = subprocess.check_output(['cleos', 'wallet', 'list'])
        self.getInfoLabel.setText(str(out))
        
    def setBlockNumber(self):    
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Block number:", QtGui.QLineEdit.Normal,
                self.blockchain.block.number)
        if ok and text != '':
            self.account.name = text
            self.getInfoLabel.setText(text)
        
    def getBlockInfo(self):    
        out = subprocess.check_output(['cleos', 'get', 'block', self.blockchain.block.number])
        self.getInfoLabel.setText(out)
        
    def listProducers(self):
        out = ''
        if self.blockchain.net == 'test':
            producerConv = 'https://' + self.blockchain.testProducer
            print(producerConv)
            out = subprocess.check_output(['cleos', '--url', 'https://dc1.eosemerge.io:5443' , 'system', 'listproducers'])
        elif self.blockchain.net == 'main' :
            producerConv = self.blockchain.producer
            print(producerConv)
            out = subprocess.check_output(['cleos', '--url', 'https://dc1.eosemerge.io:5443', 'system', 'listproducers'])
        self.getInfoLabel.setText(out)    
     
    def getProducerInfo(self): 
        out = ''
        if self.blockchain.net == 'test':
            producerConv = 'https://' + self.blockchain.testProducer
            print(producerConv)
            out = subprocess.check_output(['cleos', '--url', 'https://dc1.eosemerge.io:5443', 'get', 'info'])
            self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)   
        elif self.blockchain.net == 'main' :
            out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'info'])
            self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)   
    def mainNet(self):
        if self.toggleMainNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.blockchain.net = 'main'
            self.blockchain.running = False
            self.toggleTestNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to main net')
        else:
            self.getInfoLabel.setText("Off the main net")
            #self.blockchain.running = False
    def localNet(self):
        if self.toggleLocalNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.startChain()
            self.blockchain.net = 'local'
            self.blockchain.running = True
            self.getInfoLabel.setText('Switched to local net')
        else:
            self.blockchain.running = False
            self.stopChain()
            self.getInfoLabel.setText("Off local net")
            
    def testNet(self):
        if self.toggleTestNet.checkState() != 0:
            self.stopChain()
            self.resetChain()
            self.blockchain.running = False
            self.blockchain.net = 'test'
            self.toggleMainNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to test net')
        else:
            self.getInfoLabel.setText("Off test net")
        
        
    
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    
    
    sys.exit(dialog.exec_())
