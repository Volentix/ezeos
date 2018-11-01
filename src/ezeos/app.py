import os, sys, subprocess, pexpect, random
from PyQt5.QtCore import QProcess, QDir, Qt
from PyQt5.QtCore import QTimer
import PyQt5.QtCore as QtCore
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *  # QScrollArea, QVBoxLayout, QGridLayout, QTabWidget, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, QLineEdit, QFrame, QComboBox, QCheckBox, QInputDialog, QLineEdit
from subprocess import Popen, PIPE
from PyQt5 import QtPrintSupport
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import pyte
import json
import psutil
from pprint import pprint
import uuid

import src.util


class GUI(QProcess):

    def __init__(self, parent=None):
        super(GUI, self).__init__(parent=None)

        self.wallet = src.util.Wallet()
        self.order = src.util.Order()
        self.account = src.util.Account()
        self.table = src.util.Table()
        self.blockchain = src.util.BlockChain()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)
        self.dialog = Dialog(self)
        frameStyle = QFrame.Sunken | QFrame.Panel
        # Create an instance variable here (of type QTextEdit)
        self.startBtn = QPushButton('OK')
        self.setTableNameButton = QPushButton('Set Table Name')
        self.setContractNameButton = QPushButton('Set Contract Name')
        self.image = QLabel()
        # pixmap = pixmap.scaledToWidth(150)
        self.image_path = src.util.resource_path("../resources/volentix.gif")
        self.image.setPixmap(QtGui.QPixmap(self.image_path).scaledToWidth(50))
        # pixmap = pixmap.scaledToWidth(100)
        # self.image.setPixmap(pixmap)
        self.startBtn = QPushButton('OK')
        self.stopBtn = QPushButton('Cancel')
        self.label2 = QLabel("Test Net")
        self.label = QLabel("Main Net")
        self.setMessageButton = QPushButton("Set Message")
        self.vtxTransferButton = QPushButton("Vtx Distribution Account to Trust Account/VDex Public Key")
        self.getVtxBalanceButton = QPushButton("Get Vtx Balance")
        self.setVDexPublicKeyButton = QPushButton("Set VDex Public Key")
        self.setPermissionObjectButton = QPushButton("Set Permission Object")
        self.stakeBandwidthButton = QPushButton("Set Stake Bandwidth")
        self.testEncryptionButton = QPushButton("Test Encryption")
        self.TestFunctionButton = QPushButton("Test Function")
        self.createEosioWalletButton = QPushButton("Create Eosio Wallet and account")
        self.createEosioTokenAccountButton = QPushButton("Create eosio.token wallet and account")
        self.openContractButton = QPushButton("Open Contract")
        self.setWalletNameButton = QPushButton("Set Wallet Name")
        self.openWalletButton = QPushButton("Open Wallet")
        # self.setWalletPublicKeysButton = QPushButton("Set Wallet Public Keys")
        self.restartButton = QPushButton("Reset Local Chain")
        self.startButton = QPushButton("Start Local Chain")
        self.stopButton = QPushButton("Stop Local Chain")
        self.flushButton = QPushButton("Rename wallet directory (Do not click this unless you know what you are doing)")
        self.createWalletButton = QPushButton("Create Wallet")
        #         self.setOwnerKeyButton = QPushButton("Create Owner Keys")
        #         self.setActiveKeyButton = QPushButton("Create Active Keys")
        self.importKeysButton = QPushButton("Import Keys To Wallet")
        self.setAccountNameButton = QPushButton("Set Account Name")
        self.getTableButton = QPushButton("Get Table")
        self.setAccountOwnerButton = QPushButton("Set Account Owner")
        self.setCreatorAccountNameButton = QPushButton("Set Creator Account Name")
        self.setStakeCPUAmountButton = QPushButton("Set CPU Stake")
        self.setStakeBandWidthAmountButton = QPushButton("Stake Bandwidth")
        self.buyRAMButton = QPushButton("Buy RAM")
        self.setBuyRAMAmountButton = QPushButton("Set RAM Stake")
        self.createAccountButton = QPushButton("Create Account")
        self.setSendAmountButton = QPushButton("Set Send Amount")
        self.setSendRecipientAccountButton = QPushButton("Set Recipient Account")
        self.sendAmountButton = QPushButton("Send Funds")

        self.getInfoLabel = QTextEdit()
        self.getInfoLabel.setFrameStyle(frameStyle)
        self.walletNameLabel = QLabel()
        self.walletNameLabel.setFrameStyle(frameStyle)
        self.accountNameLabel = QLabel()
        self.accountNameLabel.setFrameStyle(frameStyle)
        self.contractNameLabel = QLabel()
        self.contractNameLabel.setFrameStyle(frameStyle)
        self.creatorNameLabel = QLabel()
        self.creatorNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton = QPushButton("Load Contract")
        self.loadEosioContractButton = QPushButton("Load EosioContract")
        self.issueButton = QPushButton("Issue Currency")
        self.recipientNameButton = QPushButton("Set Recipient Name")
        self.amountButton = QPushButton("Amount")
        self.issueToAccountButton = QPushButton("Issue To Account")
        self.transferToAccountButton = QPushButton("Transfer To Account")
        self.chooseCurrencyButton = QPushButton("Set Token Name")
        self.getInfoButton = QPushButton("Get Info")
        self.getBalanceButton = QPushButton("Get Balance")
        self.getAccountDetailsButton = QPushButton("Get Account Details")

        self.listWalletsButton = QPushButton("List Wallets")
        self.getBlockInfoButton = QPushButton("Block Info")
        self.setBlockNumberButton = QPushButton("Set Block Number")
        self.getActionsButton = QPushButton("Get Actions")
        self.showKeysButton = QPushButton("Show Keys")
        self.listProducersButton = QPushButton("Get Block Producers")
        self.getProducerInfoButton = QPushButton("Get Block Producer Info")
        self.setNodeosPathButton = QPushButton("Set Nodeos Path -default:/usr/local/eosio/bin/nodeos)")
        self.producerBox = QComboBox()
        self.testProducerBox = QComboBox()
        self.producerBox.setObjectName(("Access to Main Net"))
        self.testProducerBox.setObjectName(("Access To Test Net"))
        self.toggleMainNet = QCheckBox("Main Net")
        self.toggleTestNet = QCheckBox("Test Net")
        self.toggleLocalNet = QCheckBox("Local Net")
        self.togglePasswordToConsole = QCheckBox("To Console(1) / To File(0)")
        self.toggleWalletLock = QCheckBox("Wallet Lock/Unlock")
        for i in self.blockchain.producerList:
            self.producerBox.addItem(i)
        for i in self.blockchain.testProducerList:
            self.testProducerBox.addItem(i)
        self.setMessageButton.clicked.connect(self.dialog.setMessage)
        self.getVtxBalanceButton.clicked.connect(self.getVtxBalance)
        self.setVDexPublicKeyButton.clicked.connect(self.dialog.setVdexKey)
        self.setNodeosPathButton.clicked.connect(self.dialog.setNodeosPath)
        self.setPermissionObjectButton.clicked.connect(self.setPermissionObject)
        self.toggleMainNet.toggled.connect(self.mainNet)
        self.toggleTestNet.toggled.connect(self.testNet)
        self.toggleLocalNet.toggled.connect(self.localNet)
        self.setTableNameButton.clicked.connect(self.dialog.setTableName)
        self.setContractNameButton.clicked.connect(self.dialog.setContractName)
        self.toggleWalletLock.toggled.connect(self.lockWallet)
        self.listProducersButton.clicked.connect(self.listProducers)
        self.testEncryptionButton.clicked.connect(self.testEncryption)
        # self.setWalletPublicKeysButton.clicked.connect(self.setWalletPublicKeys)
        self.listWalletsButton.clicked.connect(self.listWallets)
        self.getBalanceButton.clicked.connect(self.getBalance)
        self.getAccountDetailsButton.clicked.connect(self.getAccountDetails)
        self.getInfoButton.clicked.connect(self.getInfo)
        self.stopButton.clicked.connect(self.stopChain)
        self.startButton.clicked.connect(self.startChain)

        self.setWalletNameButton.clicked.connect(self.dialog.setWalletName)
        self.openWalletButton.clicked.connect(self.openWallet)
        self.createWalletButton.clicked.connect(self.createWallet)
        #         self.setOwnerKeyButton.clicked.connect(self.setOwnerKey)
        #         self.setActiveKeyButton.clicked.connect(self.setActiveKey)
        self.importKeysButton.clicked.connect(self.importKeys)
        self.vtxTransferButton.clicked.connect(self.recordTransfer)
        self.setAccountNameButton.clicked.connect(self.dialog.setAccountName)
        self.getTableButton.clicked.connect(self.getTable)
        self.setAccountOwnerButton.clicked.connect(self.dialog.setAccountOwner)
        self.setCreatorAccountNameButton.clicked.connect(self.dialog.setCreatorAccountName)
        self.setStakeCPUAmountButton.clicked.connect(self.dialog.setStakeCPUAmount)
        self.setStakeBandWidthAmountButton.clicked.connect(self.dialog.setStakeBandWidthAmount)
        self.setBuyRAMAmountButton.clicked.connect(self.dialog.setBuyRAMAmount)
        self.buyRAMButton.clicked.connect(self.buyRAM)
        self.createAccountButton.clicked.connect(self.createAccount)
        self.openContractButton.clicked.connect(self.dialog.LoadContract)
        self.openFileNameButton.clicked.connect(self.setContractSteps)
        self.issueButton.clicked.connect(self.issueCurrency)
        self.flushButton.clicked.connect(self.flushWallets)
        self.amountButton.clicked.connect(self.dialog.setAmount)
        self.recipientNameButton.clicked.connect(self.dialog.setRecipientName)
        self.issueToAccountButton.clicked.connect(self.issueToAccount)
        self.transferToAccountButton.clicked.connect(self.transferToAccount)
        self.chooseCurrencyButton.clicked.connect(self.dialog.chooseCurrency)
        self.getBlockInfoButton.clicked.connect(self.getBlockInfo)
        self.setBlockNumberButton.clicked.connect(self.dialog.setBlockNumber)
        self.getActionsButton.clicked.connect(self.getActions)
        self.showKeysButton.clicked.connect(self.showKeys)
        self.listProducersButton.clicked.connect(self.listProducers)
        self.getProducerInfoButton.clicked.connect(self.getProducerInfo)
        self.setSendAmountButton.clicked.connect(self.dialog.setSendAmount)
        self.setSendRecipientAccountButton.clicked.connect(self.dialog.setRecipientAccount)
        self.sendAmountButton.clicked.connect(self.sendToAccount)
        self.loadEosioContractButton.clicked.connect(self.loadEosioContract)
        self.createEosioWalletButton.clicked.connect(self.createEosioWallet)
        self.createEosioTokenAccountButton.clicked.connect(self.createEosioTokenAccount)
        self.stakeBandwidthButton.clicked.connect(self.stakeBandwidth)
        self.layout = QGridLayout()
        self.getInfoLabel.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.getInfoLabel.adjustSize()
        self.layout.addWidget(self.getInfoLabel)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.tabs.addTab(self.tab1, "Block chain")
        self.tabs.addTab(self.tab2, "Wallets")
        self.tabs.addTab(self.tab3, "Accounts")
        self.tabs.addTab(self.tab4, "VolentixTGE")
        #         self.tabs.addTab(self.tab5, "eosio.token")
        #         self.tabs.addTab(self.tab6, "test")
        #
        self.tab1.layout = QVBoxLayout()
        # self.tab1.layout.addWidget(self.stopButton)
        # self.tab1.layout.addWidget(self.restartButton)
        # self.tab1.layout.addWidget(self.startButton)
        self.tab1.layout.addWidget(self.toggleMainNet)
        self.tab1.layout.addWidget(self.producerBox)
        self.tab1.layout.addWidget(self.toggleTestNet)
        self.tab1.layout.addWidget(self.testProducerBox)
        self.tab1.layout.addWidget(self.getBlockInfoButton)
        self.tab1.layout.addWidget(self.setBlockNumberButton)
        self.tab1.layout.addWidget(self.listProducersButton)
        self.tab1.layout.addWidget(self.getProducerInfoButton)
        # self.tab1.layout.addWidget(self.setNodeosPathButton)
        # self.tab1.layout.addWidget(self.toggleLocalNet)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addWidget(self.togglePasswordToConsole)
        #         self.tab2.layout.addWidget(self.walletNameLabel)
        self.tab2.layout.addWidget(self.toggleWalletLock)
        self.tab2.layout.addWidget(self.setWalletNameButton)

        self.tab2.layout.addWidget(self.openWalletButton)
        self.tab2.layout.addWidget(self.createWalletButton)
        self.tab2.layout.addWidget(self.listWalletsButton)
        #         self.tab2.layout.addWidget(self.setOwnerKeyButton)
        #         self.tab2.layout.addWidget(self.setActiveKeyButton)
        self.tab2.layout.addWidget(self.importKeysButton)
        # self.tab2.layout.addWidget(self.setWalletPublicKeysButton)
        self.tab2.layout.addWidget(self.showKeysButton)
        # self.tab2.layout.addWidget(self.flushButton)
        # self.tab2.layout.addWidget(self.createEosioWalletButton)

        self.tab2.setLayout(self.tab2.layout)
        self.tab3.layout = QVBoxLayout()
        self.tab3.layout.addWidget(self.accountNameLabel)

        self.tab3.layout.addWidget(self.setAccountNameButton)
        self.tab3.layout.addWidget(self.setSendAmountButton)
        self.tab3.layout.addWidget(self.setMessageButton)
        self.tab3.layout.addWidget(self.getBalanceButton)
        self.tab3.layout.addWidget(self.getAccountDetailsButton)
        self.tab3.layout.addWidget(self.getActionsButton)

        self.tab3.layout.addWidget(self.creatorNameLabel)
        self.tab3.layout.addWidget(self.setCreatorAccountNameButton)
        self.tab3.layout.addWidget(self.setAccountOwnerButton)
        self.tab3.layout.addWidget(self.setStakeCPUAmountButton)
        self.tab3.layout.addWidget(self.setStakeBandWidthAmountButton)
        self.tab3.layout.addWidget(self.setBuyRAMAmountButton)
        self.tab3.layout.addWidget(self.buyRAMButton)
        self.tab3.layout.addWidget(self.createAccountButton)

        self.tab3.layout.addWidget(self.setSendRecipientAccountButton)
        self.tab3.layout.addWidget(self.sendAmountButton)
        # self.tab3.layout.addWidget(self.createEosioTokenAccountButton)
        self.tab3.layout.addWidget(self.stakeBandwidthButton)
        self.tab3.setLayout(self.tab3.layout)

        self.tab4.layout = QVBoxLayout()
        # self.tab4.layout.addWidget(self.setAccountNameButton)

        self.tab4.layout.addWidget(self.vtxTransferButton)
        self.tab4.layout.addWidget(self.getVtxBalanceButton)
        self.tab4.layout.addWidget(self.getTableButton)
        self.tab4.layout.addWidget(self.setContractNameButton)
        self.tab4.layout.addWidget(self.setVDexPublicKeyButton)
        self.tab4.layout.addWidget(self.setTableNameButton)

        # self.tab4.layout.addWidget(self.contractNameLabel)
        #         self.tab4.layout.addWidget(self.openContractButton)
        #         self.tab4.layout.addWidget(self.openFileNameButton)
        #         self.tab4.layout.addWidget(self.loadEosioContractButton)
        self.tab4.setLayout(self.tab4.layout)

        self.tab5.layout = QVBoxLayout()

        self.tab5.layout.addWidget(self.chooseCurrencyButton)
        self.tab5.layout.addWidget(self.issueButton)
        self.tab5.layout.addWidget(self.recipientNameButton)
        self.tab5.layout.addWidget(self.amountButton)
        self.tab5.layout.addWidget(self.issueToAccountButton)
        self.getActionsButton.clicked.connect(self.getActions)
        self.tab5.layout.addWidget(self.transferToAccountButton)
        self.tab5.setLayout(self.tab5.layout)

        self.tab6.layout = QVBoxLayout()
        self.tab6.layout.addWidget(self.setPermissionObjectButton)
        self.tab6.layout.addWidget(self.testEncryptionButton)
        self.tab6.setLayout(self.tab6.layout)

        self.layout.addWidget(self.tabs)
        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.image)

        self.vbox.addLayout(self.layout)

        # self.vbox.addWidget(self.edit)
        self.vbox.addLayout(self.hbox)
        self.startBtn.clicked.connect(self.startNodeos)
        self.stopBtn.clicked.connect(self.kill)
        self.stateChanged.connect(self.slotChanged)

        self.central = QWidget()

        self.central.setLayout(self.vbox)
        self.central.setWindowTitle("Volentix")
        self.central.show()
        self.scrollAreaWidgetContents = self.tabs
        self.scrollArea = QScrollArea()
        self.layout.addWidget(self.scrollArea)
        self.scrollArea.setGeometry(QtCore.QRect(5000, 5000, 5000, 5000))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def recordTransfer(self):
        object = ['112vtxledger', 'vtxdistrib', 'vtxtrust', 100.12345678, '',
                  'EOS81gkcgHo6Q12m8tjd2Ye5m18zbr4wGWh2bqU3XuLYrburgEf2T', 'test', 'nonce']
        object[0] = self.account.name
        object[3] = self.order.amount
        object[5] = self.order.vDexKey
        object = json.dumps(object)
        out = ''
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['c0leos', '--url', self.blockchain.testProducer, 'push', 'action', self.account.name, 'rcrdtfr',
                     object, '-p', '112vtxledger' + '@active'])
            else:
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'push', 'action', self.account.name, 'rcrdtfr', object,
                     '-p', '112vtxledger' + '@active'])
        except:
            print('could not transfer')

        self.getInfoLabel.setText(str(out) + " VTX")

    def getVtxBalance(self):
        out = ""
        iAmount = 0.0
        fAmount = 0.0
        for i in self.table.body:
            for j in i:
                if (j['sToKey'] == self.order.vDexKey):
                    iAmount += j['iVal']
                    fAmount += j['fVal']

        out = iAmount + fAmount
        self.getInfoLabel.setText(str(out) + " VTX")

    def getTable(self):
        out = ""
        accum = ""
        entries = []
        if self.blockchain.testProducer == '' or self.account.name == '' or self.table.contract == '' or self.table.table == '':
            return
        try:
            ub = 1000
            lb = 0
            count = 1

            while (1):

                if self.blockchain.net == 'test':

                    out = subprocess.check_output(
                        ['cleos', '--url', self.blockchain.testProducer, 'get', 'table', self.account.name,
                         self.table.contract, self.table.table, '-L', str(lb), '-U', str(ub), '-l', '1000000'])
                    accum = accum + str(out)
                    o = json.loads(out)
                    d = o['rows']
                    entries.append(d)
                    if len(d) == 0:
                        break

                elif self.blockchain.net == 'main':
                    out = subprocess.check_output(
                        ['cleos', '--url', self.blockchain.producer, 'get', 'table', self.account.name,
                         self.table.contract, self.table.table, '-U', {}, '-L', {}]).format(str(ub), str(lb))
                    accum = accum + str(out)
                    o = json.loads(out)
                    d = o['rows']
                    if len(d) == 0:
                        break
                ub = ub * (count + 1)
                lb = ub - 1000
        except:
            print('could not get table')
        self.table.body = entries
        self.getInfoLabel.setText(str(accum))

    def openWallet(self):
        out = ''
        try:
            out = subprocess.check_output(['cleos', 'wallet', 'open', '-n', self.wallet.name])

        except:
            print('could not open wallet')

        self.getInfoLabel.setText(str(out))

    def slotChanged(self, newState):
        if newState == QProcess.NotRunning:
            self.startBtn.setDisabled(False)
        elif newState == QProcess.Running:
            self.startBtn.setDisabled(True)

    def startNodeos(self):
        cmd = self.blockchain.path + '&'
        out = subprocess.check_output([cmd, '--delete-all-blocks'])
        screen = pyte.Screen(80, 24)
        stream = pyte.Stream(screen)
        stream.feed(out)

    def readStdOutput(self):
        string = self.readAllStandardOutput()

    #         printer = QtPrintSupport.QPrinter()
    #         # Create painter
    #         painter = QtGui.QPainter()
    #         # Start painter
    #         painter.begin(printer)
    #         # Grab a widget you want to print
    #         screen = self.editor.grab()
    #         # Draw grabbed pixmap
    #         painter.drawPixmap(10, 10, screen)
    #         # End painting
    # #        painter.end()
    #         self.edit.append(string)

    def createPermissionObject(self, actor, permission):
        permissionobject = {'actor': actor, 'permission': permission}
        return permissionobject

    def setPermissionObject(self):
        self.createTestAccounts()
        actors = ['partner11111', 'partner22222', 'partner33333']
        multiSigPermissionObject = json.dumps(self.createMultiSigAccountObject(2, 1, actors, 'active'))
        self.account.name = 'mymultisig11'
        subprocess.check_output(
            ['cleos', 'set', 'account', 'permission', self.account.name, 'active', multiSigPermissionObject, 'owner',
             '-p', self.account.name + '@owner', ])
        # cleos set account permission mymultisig11 owner
        # '{"threshold":2,"keys":[],"accounts":[{"permission":{"actor":"partner11111","permission":"owner"},"weight":1},{"permission":{"actor":"partner22222","permission":"owner"},"weight":1},{"permission":{"actor":"partner33333","permission":"owner"},"weight":1}],"waits":[]}'
        # -p mymultisig11@owner
        multiSigPermissionObject = json.dumps(self.createMultiSigAccountObject(2, 1, actors, 'owner'))
        self.account.name = 'mymultisig11'
        out = subprocess.check_output(
            ['cleos', 'set', 'account', 'permission', self.account.name, 'owner', multiSigPermissionObject, '-p',
             self.account.name + '@owner', ])
        self.getInfoLabel.setText(out)

    def createPermissionObjectPK(self, threshold, weight):
        token1 = '{"threshold":"'
        token2 = threshold
        token3 = '","keys":[{"key":"'
        token4 = self.wallet.activePublicKey
        token5 = '","weight":"'
        token6 = weight
        token7 = '"}'
        finalToken = token1 + token2 + token3 + token4 + token5 + token6 + token7
        print(finalToken)
        return finalToken

    def setOwnerPermission(self):
        out = subprocess.check_output(['cleos', 'set', 'account', 'permission', self.account.name, self.account.creator,
                                       self.wallet.activePublicKey, '-p', self.account.name, '@', self.account.creator])
        self.getInfoLabel.setText(out)

    def stakeBandwidth(self):
        out = ''
        try:
            out = subprocess.check_output(
                ['cleos', '--url', self.blockchain.producer, 'system', 'delegatebw', self.account.creator,
                 self.account.name, self.order.stakeBandWidth, self.order.stakeCPU])
        except:
            print('could not stake bw')
        self.getInfoLabel.setText(out)

    def testEncryption(self):
        key = ''
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                                        "Enter private Key:", QLineEdit.Normal,
                                        QtCore.QDir.home().dirName())
        if ok and text != '':
            key = text
        child = pexpect.spawn(['seccure-key'])
        child.expect('Enter private key:')
        child.sendline(key)
        child.expect(pexpect.EOF)
        out = child.before
        self.getInfoLabel.setText(out)
        child.close()

    def createEosioTokenAccount(self):
        self.wallet.name = 'eosio.token'
        self.createWallet()
        #         self.setOwnerKey()
        #         self.setActiveKey()
        self.importKeys()
        subprocess.check_output(['cleos', 'create', 'account', 'eosio', 'eosio.token', self.wallet.ownerPublicKey,
                                 self.wallet.activePublicKey])
        # cleos create account eosio eosio.token EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4 EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4

    def createEosioWallet(self):

        self.wallet.name = 'eosio'
        self.createWallet()
        self.setOwnerKey()
        self.setActiveKey()
        self.showKeys()
        # self.importKeys()
        subprocess.check_output(['cleos', 'wallet', 'import', '-n', 'eosio', '--private-key',
                                 '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'])
        self.account.name = 'eosio'
        out = self.createAccount()
        self.getInfoLabel.setText(out)

    def loadEosioContract(self):
        # cleos set contract eosio build/contracts/eosio.bios -p eosio
        out = subprocess.check_output(
            ['cleos', 'set', 'contract', 'eosio', os.environ['EOS_SOURCE'] + '/build/contracts/eosio.bios', '-p',
             'eosio@active'])
        self.getInfoLabel.setText(out)

    def showKeys(self):
        try:
            out = subprocess.check_output(['cleos', 'wallet', 'keys'])
            self.getInfoLabel.setText(str(out))
        except:
            print('could not show keys')

    def update_label(self):
        self.walletNameLabel.setText('Wallet Name: ' + self.wallet.name)
        self.accountNameLabel.setText('Account Name: ' + self.account.name)
        self.creatorNameLabel.setText('Creator Account Name: ' + self.account.creator)
        self.contractNameLabel.setText('Contract name: ' + self.order.contract)

        #         self.toggleLocalNet.setChecked(self.blockchain.running)
        #         if self.blockchain.running:
        #             self.toggleMainNet.setChecked(False)
        #             self.toggleTestNet.setChecked(False)
        self.blockchain.producer = self.producerBox.currentText()
        self.blockchain.testProducer = self.testProducerBox.currentText()

        if (self.togglePasswordToConsole.isChecked()):
            self.wallet.toFile = False
            self.wallet.toConsole = True
        else:
            self.wallet.toConsole = False
            self.wallet.toFile = True
        try:
            if self.isWalletLocked():
                self.wallet.locked = True
                # self.toggleWalletLock.setChecked(True)
            else:
                self.wallet.locked = False
                # self.toggleWalletLock.setChecked(True)
        except:
            print('No Wallets')

    def isWalletLocked(self):
        out = subprocess.check_output(['cleos', 'wallet', 'list'])
        out = out.decode("utf-8")
        index = out.find(self.wallet.name)
        if (out[index + len(self.wallet.name) + 1] == '*'):
            return False
        else:
            return True

    def lockWallet(self):
        if self.wallet.name == '':
            self.getInfoLabel.setText('Please set wallet name:')
            return
        try:
            if not self.wallet.locked:
                subprocess.check_output(['cleos', 'wallet', 'lock', '-n', self.wallet.name])
                self.wallet.locked = True

            else:
                word = self.dialog.getWord()
                out = subprocess.check_output(['cleos', 'wallet', 'unlock', '-n', self.wallet.name, '--password', word])
                word = ''
                self.wallet.locked = False

        except:
            print('could not unlock wallet')

    def getActions(self):
        out = ''
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.testProducer, 'get', 'actions', self.account.name])
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'get', 'actions', self.account.name])

        except:
            print('could not get actions')
        self.getInfoLabel.setText(str(out))

    def stopChain(self):
        try:
            subprocess.check_output(['killall', '/usr/local/eosio/bin/nodeos'])
            self.getInfoLabel.setText('Chain stopped')
            self.blockchain.running = False
        except:
            self.getInfoLabel.setText('No chain running')
            self.blockchain.running = False

    def startChain(self):

        self.startNodeos()
        self.readStdOutput()
        self.getInfoLabel.setText('chain started')
        self.blockchain.running = True
        self.blockchain.net = 'local'

    def setWalletPublicKeys(self):
        out = 'Owner Public Key: ' + '\n' + self.wallet.ownerPublicKey + '\n' + 'Active Public Key: ' + '\n' + self.wallet.activePublicKey + '\n' + 'Creator Key: ' + '\n' + self.account.creatorActiveKey
        self.getInfoLabel.setText(out)

    def createWallet(self):

        walletDir = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(walletDir):
            os.makedirs(walletDir)
        try:
            if self.wallet.toConsole:
                out = subprocess.check_output(['cleos', 'wallet', 'create', '-n', self.wallet.name, '--to-console'])
                self.getInfoLabel.setText(str(out))
                self.wallet.locked = False
            else:
                out = subprocess.check_output(
                    ['cleos', 'wallet', 'create', '-n', self.wallet.name, '--file', home + "/" + self.wallet.name])
                self.getInfoLabel.setText(str(out))
                self.getInfoLabel.setText("Created wallet and saved password to home directory")
                self.wallet.locked = False

        except:
            out = "could not create wallet"
            self.getInfoLabel.setText(str(out))

    def setOwnerKey(self):
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        self.wallet.ownerPrivateKey = key
        self.wallet.ownerPublicKey = key2
        self.getInfoLabel.setText('Creating owner keys')

    def setActiveKey(self):
        try:
            if self.wallet.toConsole:
                subprocess.check_output(
                    ['cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.ownerPrivateKey,
                     '--to-console'])
                subprocess.check_output(
                    ['cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.activePrivateKey,
                     '--to-console'])
            else:
                subprocess.check_output(
                    ['cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.ownerPrivateKey,
                     '--file', home + "/owner" + self.wallet.name])
                subprocess.check_output(
                    ['cleos', 'wallet', 'import', '-n', self.wallet.name, '--private-key', self.wallet.activePrivateKey,
                     '--file', home + "/owner" + self.wallet.name])
            self.getInfoLabel.setText('Creating active keys')
        except:
            print('cannot create keys')

    def importKeys(self):
        try:
            subprocess.check_output(['cleos', 'wallet', 'create_key', '-n', self.wallet.name])
            subprocess.check_output(['cleos', 'wallet', 'create_key', '-n', self.wallet.name])
        except:
            print('could not import keys')

        self.getInfoLabel.setText('Imported keys to wallet')

    def createAccount(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(
                ['cleos', 'create', 'account', 'eosio', self.account.name, self.wallet.ownerPublicKey,
                 self.wallet.activePublicKey, '-p', 'eosio'])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main':
            permission = self.account.creator + '@active'
            out = subprocess.check_output(
                ['cleos', '-u', self.blockchain.producer, 'system', 'newaccount', self.account.creator,
                 self.account.name, self.wallet.ownerPublicKey, self.wallet.activePublicKey, '--stake-net',
                 self.order.stakeBandWidth, '--stake-cpu', self.order.stakeCPU, '--buy-ram-kbytes', self.order.buyRam,
                 '--transfer', '-p', permission])
        self.getInfoLabel.setText(str(out))

    def setContractSteps(self):
        out = ''
        if self.blockchain.net == 'local':
            out = subprocess.check_output(
                ['cleos', 'set', 'contract', self.account.name, self.order.contract, '-p', self.account.name])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main':
            out = subprocess.check_output(
                ['cleos', '-u', self.blockchain.producer, 'set', 'contract', self.account.name, self.order.contract,
                 '-p', self.account.name])
        self.getInfoLabel.setText(out)

    def issueCurrency(self):
        token1 = '{"issuer": "'
        token2 = self.account.name
        token3 = '", "maximum_supply": "1000000.0000 '
        token4 = self.order.currency
        token5 = '", "can_freeze": 1, "can_recall": 1, "can_whitelist": 1}'
        finalToken = token1 + token2 + token3 + token4 + token5
        print(finalToken)
        out = subprocess.check_output(
            ['cleos', 'push', 'action', self.account.name, 'create', finalToken, '-p', self.account.name + '@active'])
        self.getInfoLabel.setText(out)

    def buyRAM(self):
        try:
            if self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '-u', self.blockchain.producer, 'system', 'buyram', self.account.name,
                     self.account.receiver, self.order.buyRam])
            elif self.blockchain.net == 'test' or self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '-u', self.blockchain.testProducer, 'system', 'buyram', self.account.name,
                     self.account.receiver, self.order.buyRam])
            self.getInfoLabel.setText(out)
        except:
            self.getInfoLabel.setText('Could not buy RAM')

    def issueToAccount(self):
        # cleos push action eosio.token issue '[ "user", "100.0000 SYS", "memo" ]' -p eosio
        token1 = '[ "'
        token2 = self.order.name
        token3 = '", "'
        token4 = self.order.amount
        token5 = '", "memo"]'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        try:
            out = subprocess.check_output(['cleos', 'push', 'action', self.account.name, 'issue', finalToken, '-p',
                                           self.account.name])  # + '@active'])
        except:
            print('Could not issue to Account')
        self.getInfoLabel.setText(out)

    def transferToAccount(self):
        token1 = '{"to": "'
        token2 = self.order.name
        token3 = '", "quantity": "'
        token4 = self.order.amount
        token5 = '", "memo": "testing"}'
        finalToken = token1 + token2 + token3 + str(token4) + token5
        if self.blockchain.net == 'local':
            out = subprocess.check_output(
                ['cleos', 'push', 'action', self.account.name, 'transfer', finalToken, '-p', self.account.name])
        elif self.blockchain.net == 'test' or self.blockchain.net == 'main':
            out = subprocess.check_output(
                ['cleos', '-u', self.blockchain.producer, 'push', 'action', self.account.name, 'transfer', finalToken,
                 '-p', self.account.name])
        self.getInfoLabel.setText(out)

    def sendToAccount(self):
        out = ''
        try:
            if self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'transfer', self.account.name, self.account.receiver,
                     self.order.amount])
            elif self.blockchain.net == 'test' or self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '-u', self.blockchain.testProducer, 'transfer', self.account.name, self.account.receiver,
                     self.order.amount])
        except:
            print('cannot send funds')
        self.getInfoLabel.setText(out)

    def flushWallets(self):
        text, ok = QInputDialog.getText(self.dialog, "Move wallets directory", "save wallets to:", QLineEdit.Normal,
                                        'Absolute Path To Directory')
        if ok and text != '':
            subprocess.check_output(['mv', os.environ['HOME'] + '/eosio-wallet/', text])
            self.getInfoLabel.setText("Moved Wallets" + os.environ['HOME'] + "/" + text)
        elif ok and text == '':
            rand = random.randint(1, 1000000)
            subprocess.check_output(
                ['mv', os.environ['HOME'] + '/eosio-wallet/', os.environ['HOME'] + '/eosio-wallet.save' + str(rand)])
            self.getInfoLabel.setText("Moved Wallets" + os.environ['HOME'] + "/" + '~/eosio-wallet.save' + str(rand))
            subprocess.check_output(['killall', 'keosd'])

    def getInfo(self):
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(['cleos', '--url', self.blockchain.testProducer, 'get', 'info'])
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'info'])
        except:
            print('Could not get account details')
        self.getInfoLabel.setText(str(out))

    def getAccountDetails(self):
        out = ''
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.testProducer, 'get', 'account', self.account.name])
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'get', 'account', self.account.name])
            out = out.decode("utf-8")
        except:
            print('Could not get account details')
        self.getInfoLabel.setText(str(out))

    def getBalance(self):
        out = ''
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.testProducer, 'get', 'currency', 'balance', 'eosio.token',
                     self.account.name, self.order.currency])
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'get', 'currency', 'balance', 'eosio.token',
                     self.account.name, self.order.currency])
        except:
            print('could not get account info')
        self.getInfoLabel.setText(str(out))

    def listWallets(self):
        try:
            out = subprocess.check_output(['cleos', 'wallet', 'list'])
            out = out.decode("utf-8")
            self.getInfoLabel.setText(str(out))

        except:
            print('cannot list wallets')

    def getBlockInfo(self):
        out = ''
        self.getInfoLabel.setText(str(out))
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.testProducer, 'get', 'block', self.blockchain.block.number])
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.producer, 'get', 'block', self.blockchain.block.number])
            out = out.decode("utf-8")
        except:
            print('Could not get block info')
        self.getInfoLabel.setText(str(out))

    def getProducerInfo(self):
        out = ''
        try:
            if self.blockchain.net == 'test':
                producerConv = 'https://' + self.blockchain.testProducer
                print(producerConv)
                out = subprocess.check_output(['cleos', '--url', self.blockchain.testProducer, 'get', 'info'])
                out = out.decode("utf-8")
                self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'info'])
                out = out.decode("utf-8")
                self.getInfoLabel.setText(self.blockchain.producer + '\n' + out)
        except:
            print('Could not get producer info')

    def mainNet(self):
        if self.toggleMainNet.checkState() != 0:
            self.stopChain()

            self.blockchain.net = 'main'
            self.blockchain.running = False
            self.toggleTestNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to main net')
        else:
            self.getInfoLabel.setText("Off the main net")

            # self.blockchain.running = False

    def localNet(self):
        if self.toggleLocalNet.checkState() != 0:
            self.stopChain()

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

            self.blockchain.running = False
            self.blockchain.net = 'test'
            self.toggleMainNet.setChecked(False)
            self.toggleLocalNet.setChecked(False)
            self.getInfoLabel.setText('Switched to test net')
        else:
            self.getInfoLabel.setText("Off test net")

    def getProducerInfo(self):
        out = ''
        if self.blockchain.net == 'test':
            out = subprocess.check_output(['cleos', '--url', self.blockchain.testProducer, 'get', 'info'])
            self.blockchain.producer
            self.getInfoLabel.setText(str(out))
        elif self.blockchain.net == 'main':
            out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'get', 'info'])
            self.blockchain.producer
            self.getInfoLabel.setText(str(out))

    def listProducers(self):
        out = ''
        try:
            if self.blockchain.net == 'test':
                out = subprocess.check_output(
                    ['cleos', '--url', self.blockchain.testProducer, 'system', 'listproducers'])
                self.blockchain.producer
                self.getInfoLabel.setText(str(out))
            elif self.blockchain.net == 'main':
                out = subprocess.check_output(['cleos', '--url', self.blockchain.producer, 'system', 'listproducers'])
                self.blockchain.producer
                self.getInfoLabel.setText(str(out))
        except:
            print("Could not get producer list")


class Dialog(QDialog):
    MESSAGE = ""

    def __init__(self, parent):
        super(Dialog, self).__init__()
        self.parent = parent

    def setCreatorAccountName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Account Creator Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.account.creator = text
            self.parent.getInfoLabel.setText('Creator: ' + text)

    def setAccountOwner(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Account Owner Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.account.owner = text
            self.parent.getInfoLabel.setText('Owner: ' + text)

    def setAccountName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Account Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.account.name = text
            self.parent.getInfoLabel.setText('Account name: ' + text)

    def setBlockNumber(self):
        value, ok = QInputDialog.getText(self, "EZEOS", "Set Block Number ", QLineEdit.Normal, '1')
        if ok and value != 0:
            self.parent.blockchain.block.number = value
            self.parent.getInfoLabel.setText(str(value))

    def setWalletName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Wallet Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.wallet.name = text
            self.parent.getInfoLabel.setText(text)

    def getWord(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "", QLineEdit.Normal, "")
        if ok and text != '':
            return text
        self.parent.getInfoLabel.setText(text)

    def setRecipientName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Recipient Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.name = text
            self.parent.getInfoLabel.setText(text)

    def setAmount(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Amount:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.amount = text
            self.parent.getInfoLabel.setText(self.parent.order.amount)

    def setSendAmount(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Send Amount:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.amount = text
            self.parent.getInfoLabel.setText(self.parent.order.amount)

    def setStakeCPUAmount(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set CPU Stake:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.stakeCPU = text
            self.parent.getInfoLabel.setText(self.parent.order.stakeCPU)

    def setStakeBandWidthAmount(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Bandwidth Stake:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.stakeBandWidth = text
            self.parent.getInfoLabel.setText(self.parent.order.stakeBandWidth)

    def setBuyRAMAmount(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Ram Stake:", QLineEdit.Normal, '')
        if ok and text != '':
            self.parent.order.buyRam = text
            self.parent.getInfoLabel.setText(self.parent.order.buyRam)

    def setRecipientAccount(self):
        text, ok = QInputDialog.getText(self, "Receipent Account:", "Recipient Account Name:", QLineEdit.Normal, '')
        if ok and text != '':
            self.parent.account.receiver = text
            self.parent.getInfoLabel.setText(text)

    def LoadContract(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "EZEOS", "Load Contact", options)
        self.parent.order.contract = directory
        self.parent.order.contractAccountName = os.path.basename(directory)
        self.parent.getInfoLabel.setText(directory)

    def chooseCurrency(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Token Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.currency = text
            self.parent.getInfoLabel.setText(text)

    def setNodeosPath(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Nodeos Path:", QLineEdit.Normal, "")
        if ok and text != '':
            blockchain.path = text

    def setTableName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Table Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.table.table = text

    def setContractName(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set Contract Name:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.table.contract = text

    def setVdexKey(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set VDex Key:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.vDexKey = text

    def setMessage(self):
        text, ok = QInputDialog.getText(self, "EZEOS", "Set VDex Message:", QLineEdit.Normal, "")
        if ok and text != '':
            self.parent.order.message = text
