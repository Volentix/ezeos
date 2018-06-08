
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
import subprocess
import os
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
    
class Dialog(QtGui.QDialog):
    MESSAGE = "VTX"

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QtGui.QErrorMessage(self)

        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.Panel

        self.integerLabel = QtGui.QLabel()
        self.integerLabel.setFrameStyle(frameStyle)
        self.integerButton = QtGui.QPushButton("Wallet name")
        
        
        self.doubleLabel = QtGui.QLabel()
        self.doubleLabel.setFrameStyle(frameStyle)
        self.doubleButton = QtGui.QPushButton("Create wallet")

        self.itemLabel = QtGui.QLabel()
        self.itemLabel.setFrameStyle(frameStyle)
        self.itemButton = QtGui.QPushButton("Set owner Key")
        self.textLabel = QtGui.QLabel()
        self.textLabel.setFrameStyle(frameStyle)
        self.textButton = QtGui.QPushButton("Set active key")

        self.colorLabel = QtGui.QLabel()
        self.colorLabel.setFrameStyle(frameStyle)
        self.colorButton = QtGui.QPushButton("Import private keys")

        self.fontLabel = QtGui.QLabel()
        self.fontLabel.setFrameStyle(frameStyle)
        self.fontButton = QtGui.QPushButton("Account name")

        self.directoryLabel = QtGui.QLabel()
        self.directoryLabel.setFrameStyle(frameStyle)
        self.directoryButton = QtGui.QPushButton("Create account")

        

        self.integerButton.clicked.connect(self.setWalletName)
        self.doubleButton.clicked.connect(self.createWallet)
        self.itemButton.clicked.connect(self.setOwnerKey)
        self.textButton.clicked.connect(self.setActiveKey)
        self.colorButton.clicked.connect(self.importPrivateKeys)
        self.fontButton.clicked.connect(self.createAccountName)
        self.directoryButton.clicked.connect(self.createAccount)

        self.native = QtGui.QCheckBox()
        self.native.setText("Create Wallet and account")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QtGui.QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.integerButton, 0, 0)
        layout.addWidget(self.integerLabel, 0, 1)
        layout.addWidget(self.doubleButton, 1, 0)
        layout.addWidget(self.doubleLabel, 1, 1)
        layout.addWidget(self.itemButton, 2, 0)
        layout.addWidget(self.itemLabel, 2, 1)
        layout.addWidget(self.textButton, 3, 0)
        layout.addWidget(self.textLabel, 3, 1)
        layout.addWidget(self.colorButton, 4, 0)
        layout.addWidget(self.colorLabel, 4, 1)
        layout.addWidget(self.fontButton, 5, 0)
        layout.addWidget(self.fontLabel, 5, 1)
        layout.addWidget(self.directoryButton, 6, 0)
        layout.addWidget(self.directoryLabel, 6, 1)
    
        
        
        self.setLayout(layout)

        self.setWindowTitle("Create wallet and account")
        
         
    def setWalletName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Wallet name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Wallet.name = text
            self.integerLabel.setText(text)
        
                
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
        self.createWalletLabel.setText(out)
        

    def setOwnerKey(self):    
        out = subprocess.check_output(['cleos', 'create', 'key'])
        key = out[13:]
        key = key[:-67]
        key2 = out[77:]
        key2 = key2[:-1]
        f = open( Wallet.name + "OwnerKeys", 'w' )
        f.write(key)
        f.close()
        Wallet.OwnerKey1 = key
        Wallet.PublicKey1 = key2
        self.itemLabel.setText(out)

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
        self.textLabel.setText(out)

    def importPrivateKeys(self):
        #cleos wallet import -n sylvain38 5J7CB6zshNPRbEMwxnAkVEdYdPoPs1owwH9LscKdRTK7qzPPC2Z
        out = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.OwnerKey1])
        out1 = subprocess.check_output(['cleos', 'wallet', 'import', '-n', Wallet.name, Wallet.OwnerKey2])
        self.colorLabel.setText(Wallet.OwnerKey1 +"\n"+ Wallet.OwnerKey2 + "\n" + out + "\n" + out1)
        
    def createAccountName(self):
        text, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Account name:", QtGui.QLineEdit.Normal,
                QtCore.QDir.home().dirName())
        if ok and text != '':
            Account.name = text
            self.fontLabel.setText(text)
    
    def createAccount(self): 
        #cleos create account eosio <account_name> <public key from step 1> <public key from step 2>
        out = subprocess.check_output(['cleos', 'create', 'account', 'eosio', Account.name, Wallet.PublicKey1, Wallet.PublicKey2])
        self.directoryLabel.setText(out)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())


