#!/usr/bin/env python
# coding: utf-8

import os
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from core import MAIN_PRODUCERS
from core import TEST_PRODUCERS
from core import CONTRACT_FOLDER
import core.app as ezeos


class TabPanel(object):
    def __init__(self, parent):
        self.parent = parent

        # Variables tab 1
        self.netState = IntVar()
        self.producer = StringVar()
        self.blockNumber = StringVar()

        # Variables tab 2
        self.toConsole = StringVar()
        self.walletName = StringVar()
        self.walletDir = StringVar()
        self.openWalletName = StringVar()

        # Variables tab 3
        self.accountName = StringVar()
        self.accountScope = StringVar()
        self.accountTable = StringVar()
        self.accountLower = IntVar()
        self.accountLimit = IntVar()
        self.accountCreator = StringVar()
        self.accountActiveKey = StringVar()
        self.accountOwner = StringVar()
        self.accountOwnerKey = StringVar()
        self.stakeCPU = StringVar()
        self.stakeNET = StringVar()
        self.ram = StringVar()

        # Variables tab 4
        self.contractFileCPP = StringVar()
        self.contractFileWASM = StringVar()
        self.contractFileWAST = StringVar()
        self.contractFileABI = StringVar()

        self.tabPanel()
        self.fillTab1()
        self.fillTab2()
        self.fillTab3()
        self.fillTab4()
        self.fillTab5()

    def tabPanel(self):
        self.notebook = ttk.Notebook(self.parent.root, height=1)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Block Chain')
        self.notebook.add(self.tab2, text='Wallets')
        self.notebook.add(self.tab3, text='Accounts')
        self.notebook.add(self.tab4, text='Contracts')
        self.notebook.add(self.tab5, text='Currencies')

        self.notebook.pack(expand=True, fill='both')
        # self.notebook.select(self.tab5)

    def fillTab1(self):
        self.netState.set(2)

        # TODO move everything to the label frames
        networkFrame = ttk.LabelFrame(self.tab1, text="Network")
        networkFrame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        mainNet = ttk.Radiobutton(networkFrame, text='Main Net', value=1, variable=self.netState, command=self.update_tab1)
        testNet = ttk.Radiobutton(networkFrame, text='Test Net', value=2, variable=self.netState, command=self.update_tab1)
        self.mainNetList = ttk.OptionMenu(networkFrame, self.producer, *MAIN_PRODUCERS)
        self.mainNetList.configure(state="disabled")

        self.testNetList = ttk.OptionMenu(networkFrame, self.producer, *TEST_PRODUCERS)
        self.testNetList.configure(state="normal")

        mainNet.grid(row=0, column=0, padx=2, pady=2)
        self.mainNetList.grid(row=0, column=1, columnspan=2, padx=2, pady=2)
        testNet.grid(row=1, column=0, padx=2, pady=2)
        self.testNetList.grid(row=1, column=1, columnspan=2, padx=2, pady=2)

        currentProducer = ttk.Button(networkFrame, text="Show current producer", command=self.show_current_producer)
        currentProducer.grid(row=0, column=3, rowspan=2, padx=2, pady=2, ipady=2)

        # Block
        blockFrame = ttk.LabelFrame(self.tab1, text="Block")
        blockFrame.grid(row=0, column=1, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        blockNumberLabel = ttk.Label(blockFrame, text="Enter block number:")
        blockNumberLabel.grid(row=0, column=0)
        self.blockNumber = ttk.Entry(blockFrame)
        self.blockNumber.insert(END, '1')
        self.blockNumber.grid(row=0, column=1, ipadx=2, padx=2, ipady=2, sticky=EW)

        blockInfo = ttk.Button(blockFrame, text="Block info", command=ezeos.getBlockInfo)
        blockInfo.grid(row=0, column=2, ipady=2, sticky=EW)

        info = ttk.Button(blockFrame, text="Get producer info", command=ezeos.getProducerInfo)
        info.grid(row=1, column=0, padx=2, pady=2, ipady=2, sticky=EW)

        blockProducers = ttk.Button(blockFrame, text="Get producers list", command=ezeos.getBlockProducers)
        blockProducers.grid(row=1, column=1, padx=2, pady=2, ipady=2, sticky=EW)

    def fillTab2(self):
        self.toConsole.set('--to-console')
        self.walletDir.set('~/eosio-wallet')

        walletDirFrame = ttk.LabelFrame(self.tab2, text="Wallet directory")
        walletDirFrame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2, columnspan=2)
        ttk.Label(walletDirFrame, text="Directory: ").grid(row=0, column=0)
        ttk.Label(walletDirFrame, textvariable=self.walletDir).grid(row=0, column=1)
        self.setWalletDirButton = ttk.Button(walletDirFrame, text="Set wallet dir", command=self.setWalletDir)
        self.setWalletDirButton.grid(row=0, column=2, padx=2, ipady=2)
        stopKeosd = ttk.Button(walletDirFrame, text="Stop keosd", command=self.stopKeosd)
        stopKeosd.grid(row=0, column=3, padx=2, ipady=2)
        runKeosd = ttk.Button(walletDirFrame, text="Run keosd", command=self.runKeosd)
        runKeosd.grid(row=0, column=4, padx=2, ipady=2)

        createWalletFrame = ttk.LabelFrame(self.tab2, text="Create wallet")
        createWalletFrame.grid(row=1, column=0, sticky=NSEW, padx=2,pady=2, ipady=2, ipadx=2, columnspan=2)

        walletNameLabel = ttk.Label(createWalletFrame, text="Enter wallet name: ")
        walletNameLabel.grid(row=0, column=0)
        self.walletName = ttk.Entry(createWalletFrame)
        self.walletName.insert(END, 'default')
        self.walletName.grid(row=0, column=1, ipady=2, ipadx=2)

        toConsole = ttk.Radiobutton(createWalletFrame, text='To console', value='--to-console', variable=self.toConsole)
        toFile = ttk.Radiobutton(createWalletFrame, text='To file', value='--file', variable=self.toConsole, state=DISABLED)
        toConsole.grid(row=0, column=2, padx=2, pady=2)
        toFile.grid(row=0, column=3, padx=2, pady=2)

        createWallet = ttk.Button(createWalletFrame, text="Create wallet", command=ezeos.createWallet)
        createWallet.grid(row=0, column=4, padx=2, ipady=2)

        walletFrame = ttk.LabelFrame(self.tab2, text="Wallet operations")
        walletFrame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        walletListFilesystem = ttk.Button(walletFrame, text="List wallets (filesystem)", command=ezeos.getWalletListFilesystem)
        walletListFilesystem.grid(row=0, column=0, padx=2, ipady=2, sticky=EW)

        walletList = ttk.Button(walletFrame, text="List wallets", command=ezeos.getWalletList)
        walletList.grid(row=0, column=1, padx=2, ipady=2, sticky=EW)

        currentWallet = ttk.Button(walletFrame, text="Get current wallet", command=self.currentWallet)
        currentWallet.grid(row=0, column=2, padx=2, ipady=2, sticky=EW)

        self.openWalletName = ttk.Entry(walletFrame)
        self.openWalletName.grid(row=1, column=0, ipadx=2, ipady=2, padx=2, pady=2, sticky=EW)

        openWallet = ttk.Button(walletFrame, text="Open wallet", command=ezeos.openWallet)
        openWallet.grid(row=1, column=1, padx=2, ipady=2, pady=2, sticky=EW)

        unlockWallet = ttk.Button(walletFrame, text="Unlock wallet", command=self.unlockWallet)
        unlockWallet.grid(row=1, column=2, padx=2, ipady=2, pady=2, sticky=EW)

        self.walletKeyFrame = ttk.LabelFrame(self.tab2, text="Keys operations")
        self.walletKeyFrame.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)

        showKeys = ttk.Button(self.walletKeyFrame, text="Show public keys", command=ezeos.showKeys)
        showKeys.grid(row=0, column=0, padx=2, ipady=2, pady=2, sticky=W)

        showPrivateKeys = ttk.Button(self.walletKeyFrame, text="Show private keys", command=self.showPrivateKeys)
        showPrivateKeys.grid(row=0, column=1, padx=2, ipady=2, pady=2, sticky=EW)

        createKeys = ttk.Button(self.walletKeyFrame, text="Create key pair", command=ezeos.createKeys)
        createKeys.grid(row=1, column=0, padx=2, ipady=2, pady=2, sticky=EW)

        importPrivateKeys = ttk.Button(self.walletKeyFrame, text="Import key", command=self.importKey)
        importPrivateKeys.grid(row=1, column=1, padx=2, ipady=2, pady=2, sticky=EW)

    def fillTab3(self):
        # Account operations
        self.accountFrame = ttk.LabelFrame(self.tab3, text="Account details")
        self.accountFrame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        accountNameLabel = ttk.Label(self.accountFrame, text="Account name: ")
        accountNameLabel.grid(row=0, column=0)

        self.accountName = ttk.Entry(self.accountFrame)
        self.accountName.insert(END, 'volentixfrst')
        self.accountName.grid(row=0, column=1, ipady=2, ipadx=2)

        accountBalance = ttk.Button(self.accountFrame, text="Get account balance",command=ezeos.getAccountBalance)
        accountBalance.grid(row=0, column=2, padx=2, pady=2, ipady=2, sticky=EW)

        accountDetails = ttk.Button(self.accountFrame, text="Get account details", command=ezeos.getAccountDetails)
        accountDetails.grid(row=0, column=3, padx=2, pady=2, ipady=2, sticky=EW)

        accountActions = ttk.Button(self.accountFrame, text="Get account actions", command=ezeos.getAccountActions)
        accountActions.grid(row=0, column=4, padx=2, pady=2, ipady=2, sticky=EW)

        accountCode = ttk.Button(self.accountFrame, text="Get account code", command=ezeos.getAccountCode)
        accountCode.grid(row=0, column=5, padx=2, pady=2, ipady=2, sticky=EW)

        accountAbi = ttk.Button(self.accountFrame, text="Get account abi", command=ezeos.getAccountAbi)
        accountAbi.grid(row=0, column=6, padx=2, pady=2, ipady=2, sticky=EW)

        ttk.Separator(self.accountFrame).grid(row=1, column=0, columnspan=10, pady=5, sticky="ew")

        accountScopeLabel = ttk.Label(self.accountFrame, text="Scope name: ")
        accountScopeLabel.grid(row=2, column=0)

        self.accountScope = ttk.Entry(self.accountFrame)
        self.accountScope.insert(END, self.accountName.get())
        self.accountScope.grid(row=2, column=1, pady=2, ipady=2, ipadx=2)

        accountTableLabel = ttk.Label(self.accountFrame, text="Table name: ")
        accountTableLabel.grid(row=3, column=0)

        self.accountTable = ttk.Entry(self.accountFrame)
        self.accountTable.insert(END, 'entry')
        self.accountTable.grid(row=3, column=1, pady=2, ipady=2, ipadx=2)

        accountLowerLabel = ttk.Label(self.accountFrame, text="Lower bound: ")
        accountLowerLabel.grid(row=4, column=0)

        self.accountLower = ttk.Entry(self.accountFrame)
        self.accountLower.insert(END, 0)
        self.accountLower.grid(row=4, column=1, pady=2, ipady=2, ipadx=2)

        accountLimitLabel = ttk.Label(self.accountFrame, text="Limit: ")
        accountLimitLabel.grid(row=5, column=0)

        self.accountLimit = ttk.Entry(self.accountFrame)
        self.accountLimit.insert(END, 5)
        self.accountLimit.grid(row=5, column=1, pady=2, ipady=2, ipadx=2)

        accountTable = ttk.Button(self.accountFrame, text="Get account table", command=ezeos.getAccountTable)
        accountTable.grid(row=2, column=2, rowspan=4, padx=2, pady=2, ipady=2, sticky=EW)

        # Creating an account options
        self.accountFrameEx = ttk.LabelFrame(self.tab3, text="Creating an account")
        self.accountFrameEx.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        ttk.Label(self.accountFrameEx, text="Stake CPU: ").grid(row=0, column=0)
        self.cpu = ttk.Entry(self.accountFrameEx)
        self.cpu.insert(END, '0.1000 EOS')
        self.cpu.grid(row=1, column=0, ipady=2, ipadx=2)

        ttk.Label(self.accountFrameEx, text="Stake NET: ").grid(row=0, column=1)
        self.net = ttk.Entry(self.accountFrameEx)
        self.net.insert(END, '0.1000 EOS')
        self.net.grid(row=1, column=1, ipady=2, ipadx=2)

        ttk.Label(self.accountFrameEx, text="RAM: ").grid(row=0, column=2)
        self.ram = ttk.Entry(self.accountFrameEx)
        self.ram.insert(END, '1 EOS')
        self.ram.grid(row=1, column=2, ipady=2, ipadx=2)

        buyRam = ttk.Button(self.accountFrameEx, text="Buy Ram", command=self.buyRam)
        buyRam.grid(row=0, column=3, rowspan=2, padx=2, pady=2, ipady=2, sticky=EW)
        stakeNet = ttk.Button(self.accountFrameEx, text="Stake NET", command=self.stakeNet)
        stakeNet.grid(row=0, column=4, rowspan=2, padx=2, pady=2, ipady=2, sticky=EW)

        ttk.Separator(self.accountFrameEx).grid(row=2, column=0, columnspan=5, pady=5, sticky="ew")

        accountCreatorLabel = ttk.Label(self.accountFrameEx, text="Creator: ")
        accountCreatorLabel.grid(row=3, column=0)
        self.accountCreator = ttk.Entry(self.accountFrameEx)
        self.accountCreator.insert(END, 'volentixcrtr')
        self.accountCreator.grid(row=4, column=0, ipady=2, ipadx=2)
        accountOwnerLabel = ttk.Label(self.accountFrameEx, text="Owner: ")
        accountOwnerLabel.grid(row=3, column=1)
        self.accountOwner = ttk.Entry(self.accountFrameEx)
        self.accountOwner.insert(END, 'volentixownr')
        self.accountOwner.grid(row=4, column=1, ipady=2, ipadx=2)

        accountActiveKeyLabel = ttk.Label(self.accountFrameEx, text="Active Key: ")
        accountActiveKeyLabel.grid(row=3, column=2)
        self.accountActiveKey = ttk.Entry(self.accountFrameEx)
        self.accountActiveKey.insert(END, 'key')
        self.accountActiveKey.grid(row=4, column=2, ipady=2, ipadx=2)

        accountOwnerKeyLabel = ttk.Label(self.accountFrameEx, text="Owner Key: ")
        accountOwnerKeyLabel.grid(row=3, column=3)
        self.accountOwnerKey = ttk.Entry(self.accountFrameEx)
        self.accountOwnerKey.insert(END, 'key')
        self.accountOwnerKey.grid(row=4, column=3, ipady=2, ipadx=2)

        createAccount = ttk.Button(self.accountFrameEx, text="Create", command=self.createAccount)
        createAccount.grid(row=3, column=4, rowspan=2, padx=2, pady=2, ipady=2, sticky=EW)

    def fillTab4(self):
        # Contract operations
        self.contractFrame = ttk.LabelFrame(self.tab4, text="Contract operations")
        self.contractFrame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2, ipady=2, ipadx=2)

        openContract = ttk.Button(self.contractFrame, text="Open contract", command=self.openContract)
        openContract.grid(row=0, column=0, padx=2, ipady=2, sticky=EW)

        compileContract = ttk.Button(self.contractFrame, text="Compile contract", command=ezeos.compileContract)
        compileContract.grid(row=0, column=1, padx=2, ipady=2, sticky=EW)

        setContract = ttk.Button(self.contractFrame, text="Set contract", command=ezeos.setContract)
        setContract.grid(row=0, column=2, padx=2, ipady=2, sticky=EW)

    def fillTab5(self):
        self.btc = "1DwzjjBvHCtr5Hn5kZs72KABfKnoFjJSMy"
        self.eth = "0x0366BfD5eDd7C257f2dcf4d4f1AB6196F03A0Bf6"
        self.xmr = "To Do"
        self.ltc = "LiBqkbnoVeRnrXCNetNDftYCE7Q3DDeDPL"
        self.bch = "CZ9bAtUBNkH3hzStsZr2283bRgPoGaqyuK"
        self.dash = "Xnn7aVPqxkqs8gDLZq1sNEU9v5A17HskM9"
        self.neo = "To do"

        # BTC
        self.btcFrame = ttk.LabelFrame(self.tab5, text="BTC")
        self.btcFrame.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        btcAddress = ttk.Entry(self.btcFrame)
        btcAddress.insert(END, self.btc)
        btcAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        btcGetBalance = ttk.Button(self.btcFrame, text="Get Balance", command=lambda: ezeos.getBtcBalance(btcAddress.get()))
        btcGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # ETH
        self.ethFrame = ttk.LabelFrame(self.tab5, text="ETH")
        self.ethFrame.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        ethAddress = ttk.Entry(self.ethFrame)
        ethAddress.insert(END, self.eth)
        ethAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        ethGetBalance = ttk.Button(self.ethFrame, text="Get Balance", command=lambda: ezeos.getEthBalance(ethAddress.get()))
        ethGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # XMR
        self.xmrFrame = ttk.LabelFrame(self.tab5, text="XMR")
        self.xmrFrame.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        xmrAddress = ttk.Entry(self.xmrFrame)
        xmrAddress.insert(END, self.xmr)
        xmrAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        xmrGetBalance = ttk.Button(self.xmrFrame, text="Get Balance", command=lambda: ezeos.getXmrBalance(xmrAddress.get()))
        xmrGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # NEO
        self.neoFrame = ttk.LabelFrame(self.tab5, text="NEO")
        self.neoFrame.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        neoAddress = ttk.Entry(self.neoFrame)
        neoAddress.insert(END, self.neo)
        neoAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        neoGetBalance = ttk.Button(self.neoFrame, text="Get Balance", command=lambda: ezeos.getNeoBalance(neoAddress.get()))
        neoGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # LTC
        self.ltcFrame = ttk.LabelFrame(self.tab5, text="LTC")
        self.ltcFrame.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        ltcAddress = ttk.Entry(self.ltcFrame)
        ltcAddress.insert(END, self.ltc)
        ltcAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        ltcGetBalance = ttk.Button(self.ltcFrame, text="Get Balance", command=lambda: ezeos.getLtcBalance(ltcAddress.get()))
        ltcGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # BCH
        self.bchFrame = ttk.LabelFrame(self.tab5, text="BCH")
        self.bchFrame.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        bchAddress = ttk.Entry(self.bchFrame)
        bchAddress.insert(END, self.bch)
        bchAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        bchGetBalance = ttk.Button(self.bchFrame, text="Get Balance", command=lambda: ezeos.getBchBalance(bchAddress.get()))
        bchGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

        # DASH
        self.dashFrame = ttk.LabelFrame(self.tab5, text="DASH")
        self.dashFrame.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2, ipady=2, ipadx=2)
        dashAddress = ttk.Entry(self.dashFrame)
        dashAddress.insert(END, self.dash)
        dashAddress.grid(row=0, column=0, pady=2, padx=2, ipady=2, ipadx=2)
        dashGetBalance = ttk.Button(self.dashFrame, text="Get Balance", command=lambda: ezeos.getDashBalance(dashAddress.get()))
        dashGetBalance.grid(row=2, column=0, pady=2, padx=2, ipady=2, ipadx=2, sticky=EW)

    def update_tab1(self):
        if self.netState.get() == 1:
            self.testNetList.configure(state="disabled")
            self.mainNetList.configure(state="normal")
        elif self.netState.get() == 2:
            self.testNetList.configure(state="normal")
            self.mainNetList.configure(state="disabled")

    def show_current_producer(self):
        mes = self.producer.get()
        self.parent.log(mes)

    def currentWallet(self):
        mes = self.openWalletName.get()
        self.parent.log(mes)

    def showPrivateKeys(self):
        password = simpledialog.askstring("Password", "Password from wallet", parent=self.walletKeyFrame)
        if password is not None:
            ezeos.showPrivateKeys(password)
        else:
            self.parent.log("Something went wrong!")

    def buyRam(self):
        payer = self.accountCreator.get()
        receiver = self.accountOwner.get()
        tokens = self.ram.get()
        if 'EOS' in tokens:
            answer = messagebox.askyesno("Validation", "The '%s' will pay '%s' to RAM for '%s'? Is that correct?" % (payer, tokens, receiver))
            if answer:
                ezeos.buyRam()
            else:
                self.parent.log("Rechecking the inputs!")
        else:
            messagebox.askokcancel("Error", "The EOS must be in the field RAM.")
            self.parent.log("Rechecking the inputs!")

    def stakeNet(self):
        payer = self.accountCreator.get()
        receiver = self.accountOwner.get()
        net = self.net.get()
        cpu = self.cpu.get()
        if 'EOS' in net and 'EOS' in cpu:
            answer = messagebox.askyesno("Validation", "The '%s' will pay '%s' for CPU and '%s' for NET for the '%s'? Is that correct?" % (payer, cpu, net, receiver))
            if answer:
                ezeos.stakeNet()
            else:
                self.parent.log("Rechecking the inputs!")
        else:
            messagebox.askokcancel("Error", "The EOS must be in the fields CPU and RAM.")
            self.parent.log("Rechecking the inputs!")

    def setWalletDir(self):
        path = simpledialog.askstring("Wallet directory", "New directory for keosd should be full, for example:\n/Users/username/Desktop", parent=self.setWalletDirButton)
        if path is not None:
            self.walletDir.set(path)
            ezeos.setWalletDir()
        else:
            self.parent.log("Something went wrong!")

    def runKeosd(self):
        answer = messagebox.askyesno("Validation", "Run the keosd with default wallet path?\n ~/eosio-wallet")
        if answer:
            self.walletDir.set("~/eosio-wallet")
            ezeos.runKeosd(True)
        else:
            self.parent.log("Abort")

    def stopKeosd(self):
        ezeos.stopKeosd(True)

    def createAccount(self):
        creator = self.accountCreator.get()
        owner = self.accountOwner.get()
        activeKey = self.accountActiveKey.get()
        ownerKey = self.accountOwnerKey.get()
        cpu = self.cpu.get()
        net = self.net.get()
        ram = self.ram.get()
        if 'EOS' in cpu and 'EOS' in net and 'EOS' in ram:
            answer = messagebox.askyesno("Validation", "Creating an account with the following data: \n Creator: %s \n Owner: %s \n Creator key: %s \n Owner Key: %s \n CPU: %s \n NET: %s \n RAM: %s \n Is that correct?" % (creator, owner, activeKey, ownerKey, cpu, net, ram))
            if answer:
                ezeos.createAccount()
            else:
                self.parent.log("Rechecking the inputs!")
        else:
            messagebox.askokcancel("Error", "The EOS must be in the fields CPU and RAM and NET.")
            self.parent.log("Rechecking the inputs!")

    def unlockWallet(self):
        password = simpledialog.askstring("Password", "Password from wallet", parent=self.walletKeyFrame)
        if password is not None:
            ezeos.unlockWallet(password)
        else:
            self.parent.log("Something went wrong!")

    def importKey(self):
        key = simpledialog.askstring("Import key", "Put import key", parent=self.walletKeyFrame)
        if key is not None:
            ezeos.importKey(key)
        else:
            self.parent.log("Something went wrong!")

    def openContract(self):
        # self.parent.style.theme_use('ubuntu')
        filetypes = [('C++', '.cpp')]
        file = filedialog.askopenfilename(parent=self.contractFrame,
                                          initialdir=CONTRACT_FOLDER,
                                          title="Please select a contract:",
                                          filetypes=filetypes)
        if file is not None:
            # self.parent.style.theme_use('default')
            self.contractFileCPP.set(file)
            self.contractFileWASM.set(file.replace('.cpp', '.wasm'))
            self.contractFileWAST.set(file.replace('.cpp', '.wast'))
            self.contractFileABI.set(file.replace('.cpp', '.abi'))
            self.parent.log("Opened contract:\n\n"+self.contractFileCPP.get())
        else:
            self.parent.log("Something went wrong!")

    # delete
    def test(self):
        mes = self.toConsole.get()+" "+self.walletName.get()
        self.parent.log(mes)