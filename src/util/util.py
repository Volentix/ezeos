#!/bin/env python3
# coding: utf-8

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

import src.ezeos


def run():
    app = QApplication(sys.argv)
    app.setStyleSheet("QPushButton { background: white }")

    qProcess = src.ezeos.GUI()
    qProcess.setProcessChannelMode(QProcess.MergedChannels)
    qProcess.readyReadStandardOutput.connect(qProcess.readStdOutput)
    killkeosd()

    # out = subprocess.Popen(["keosd"], stdout=subprocess.PIPE)
    return app.exec_()


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def killkeosd():
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if 'keosd' in p.info['name']:
            pid = str(p.info['pid'])
            out = subprocess.check_output(['kill', pid])


home = os.environ['HOME']
os.environ['EOS_SOURCE'] = home + "/eos"
os.environ['EOS_NODEOS'] = home + "/.local/share/eosio/nodeos/"
os.environ['EZEOS_SOURCE'] = home + "/eclipse-workspace/ezeos/src"
# os.environ['CLEOS'] = "cleos"


class BlockChain:
    class Block:

        def __init__(self):
            self.number = "1"

    def __init__(self):
        self.net = ['main', 'test']
        self.block = self.Block()
        self.producer = "https://api.eosnewyork.io:443"
        self.testProducer = "http://api.kylin.alohaeos.com"
        self.producerList = [
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
            'http://api.kylin.alohaeos.com',
            'http://127.0.0.1:8888',
            'http://35.183.129.78:8080'
        ]


class Wallet:

    def __init__(self):
        self.name = ""
        self.key = ""
        self.ownerPrivateKey = ""
        self.ownerPublicKey = ""
        self.activePrivateKey = ""
        self.activePublicKey = ""
        self.locked = False
        self.toConsole = True


class Account:

    def __init__(self):
        self.name = ""
        self.creator = ""
        self.owner = ""
        self.receiver = ""
        self.creatorOwnerKey = ""
        self.creatorActiveKey = ""
        self.eosioPublicKey = "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
        self.eosioPrivateKey = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"


class Order:

    def __init__(self):
        self.to = ""
        self.amount = 0.00000000
        self.contract = ""
        self.currency = ""
        self.contractAccountName = ""
        self.stakeCPU = ""
        self.stakeBandWidth = ""
        self.buyRam = 0
        self.vDexKey = ""
        self.message = ""


class Table:

    def __init__(self):
        self.contract = ""
        self.table = ""
        self.body = []

