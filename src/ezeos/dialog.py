import os
from PyQt5.QtWidgets import *


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
            self.blockchain.path = text

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
