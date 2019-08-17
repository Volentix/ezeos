#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI
from core import DOCKER_CONTAINER_NAME
from core import TIMEOUT
from core import btc, bch, dash, eth, ltc, neo, xmr
import subprocess
import os
import signal


def run():
    global app
    root = Tk()
    app = UI(root)
    # Application
    getCleosCommand()
    # print(app.tabPanel.producer.get())
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)
    root.mainloop()


def handler(signum, frame):
    raise RuntimeError("End of time")


def getCleosCommand():
    # TODO The docker has to be removed since was deprecated.
    global DOCKER_COMMAND

    DOCKER_COMMAND = ['docker', 'exec', DOCKER_CONTAINER_NAME]
    CLEOS_COMMAND = ['/opt/eosio/bin/cleos', '-h']
    global cleos

    # try:
    #     subprocess.check_output(DOCKER_COMMAND+CLEOS_COMMAND)
    # except OSError as e:
    #     cleos = ['cleos']
    # except Exception as e:
    #     cleos = ['cleos']
    # else:
    #     cleos = ['docker', 'exec', DOCKER_CONTAINER_NAME, '/opt/eosio/bin/cleos']

    try:
        subprocess.check_output(['cleos', '-h'])
    except OSError as e:
        app.outputPanel.logger('Can not find the cleos command.\n' + str(e))
    except Exception as e:
        app.outputPanel.logger('Something went wrong \n' + str(e))
    else:
        cleos = ['cleos']


# Logic functions
def getProducerInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'info'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Producer is not available\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not get info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(),
                                      'get', 'block', app.tabPanel.blockNumber.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get block info\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not get block info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockProducers():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(),
                                      'system', 'listproducers'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get producer list\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get producer list.\n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getWalletList():
    try:
        out = subprocess.run(cleos + ['wallet', 'list'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get wallet list\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get wallet list. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getWalletListFilesystem():
    if 'docker' in cleos:
        # docker exec eos ls /root/eosio-wallet | egrep '\.wallet$'
        out = b"Found wallets in filesystem inside docker container:\n> /root/eosio-wallet\n\n"
        com = " ".join(DOCKER_COMMAND + ['ls', '/root/eosio-wallet', '|', 'egrep', '\.wallet$'])
        out += subprocess.check_output(com, shell=True)
    else:
        # ls ~/eosio-wallet | egrep '\.wallet$'
        out = b"Found wallets in filesystem:\n> ~/eosio-wallet\n\n"
        com = " ".join(['ls', '~/eosio-wallet', '|', 'egrep', '\.wallet$'])
        out += subprocess.check_output(com, shell=True)

    app.outputPanel.logger(out)


def createWallet():
    toConsole = app.tabPanel.toConsole.get()

    if 'docker' in cleos:
        # docker - cleos wallet create -n twal --file /root/twal saved indide docker /root/
        try:
            if toConsole == '--to-console':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--to-console'],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--file', "/root/" + app.tabPanel.walletName.get()],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not create wallet\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.tabPanel.openWalletName.insert(0, app.tabPanel.walletName.get())
            app.outputPanel.logger(out)
    else:
        walletDir = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(walletDir):
            os.makedirs(walletDir)
        try:
            if toConsole == '--to-console':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--to-console'],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--file', walletDir + "/" + app.tabPanel.walletName.get()],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not create wallet\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.tabPanel.openWalletName.insert(0, app.tabPanel.walletName.get())
            app.outputPanel.logger(out)


def openWallet():
    try:
        out = subprocess.run(cleos + ['wallet', 'open', '-n', app.tabPanel.openWalletName.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not open the wallet\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not open the wallet.\n' + str(e)
    finally:
        if 'Opened' in out:
            out += "\nRemember this wallet as default for this core session!"
        app.outputPanel.logger(out)


def unlockWallet(password):
    try:
        out = subprocess.run(cleos + ['wallet', 'unlock', '-n', app.tabPanel.openWalletName.get(), '--password', password],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Unlock the wallet\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not unlock the wallet.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def showKeys():
    try:
        out = subprocess.run(cleos + ['wallet', 'keys'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not show keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not show keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def showPrivateKeys(password):
    try:
        out = subprocess.run(cleos + ['wallet', 'private_keys', '-n', app.tabPanel.openWalletName.get(), '--password', password],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not show private keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not show private keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def importKey(key):
    try:
        out = subprocess.run(cleos + ['wallet', 'import', '-n', app.tabPanel.openWalletName.get(), '--private-key', key],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not import the key\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not import the key.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def createKeys():
    # TODO add --tofile feature
    try:
        out = subprocess.run(cleos + ['create', 'key', '--to-console'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not create keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not create keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def compileContract():
    cpp = app.tabPanel.contractFileCPP.get()
    wasm = app.tabPanel.contractFileWASM.get()
    wast = app.tabPanel.contractFileWAST.get()
    abi = app.tabPanel.contractFileABI.get()

    try:
        out = subprocess.run(['eosio-cpp', '-o', wasm, cpp, '--abigen'],
                             timeout=TIMEOUT+60, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not compile contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not compile contract.\n' + str(e)
    finally:
        if 'error' in out:
            app.outputPanel.logger(out)
        else:
            app.outputPanel.logger("Compile successful\n\n" + out)

    try:
        out = subprocess.run(['eosio-cpp', '-o', wast, cpp, '--abigen'],
                             timeout=TIMEOUT+60, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not compile contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not compile contract.\n' + str(e)
    finally:
        if 'error' in out:
            app.outputPanel.logger(out)
        else:
            app.outputPanel.logger("Compile successful\n\n" + out)


def setContract():
    cpp = app.tabPanel.contractFileCPP.get()
    wasm = app.tabPanel.contractFileWASM.get()
    wast = app.tabPanel.contractFileWAST.get()
    abi = app.tabPanel.contractFileABI.get()

    try:
        out_code = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'set', 'code', app.tabPanel.accountName.get(), wasm],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out_abi = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'set', 'abi', app.tabPanel.accountName.get(), abi],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out_code = out_code.stdout.decode('utf-8')
        out_abi = out_abi.stdout.decode('utf-8')
        out = str(out_code) + str(out_abi)
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not set contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not set contract.\n' + str(e)
    finally:
        app.outputPanel.logger("Contract successfully pished to the net.\n\n" + out)


def getAccountBalance():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get() ,'get', 'currency', 'balance', 'eosio.token', app.tabPanel.accountName.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account balance\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account balance. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getAccountDetails():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get() ,'get', 'account', app.tabPanel.accountName.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account details\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account details. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getAccountActions():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'actions', app.tabPanel.accountName.get()],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account actions\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account actions. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getAccountCode():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'code', app.tabPanel.accountName.get()],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account code\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account code. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getAccountAbi():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'abi', app.tabPanel.accountName.get()],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account abi\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account abi. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getAccountTable():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'table', app.tabPanel.accountName.get(), app.tabPanel.accountScope.get(), app.tabPanel.accountTable.get(), '-L', app.tabPanel.accountLower.get(), '-l', app.tabPanel.accountLimit.get()],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get account table\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get account table. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def buyRam():
    creator = app.tabPanel.accountCreator.get()
    owner = app.tabPanel.accountOwner.get()
    ram = app.tabPanel.ram.get()
    # #buy ram for yourself
    # cleos system buyram someaccount1 someaccount1 "10 EOS"
    #
    # #buy ram for someone else
    # cleos system buyram someaccount1 someaccount2 "1 EOS"
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'system', 'buyram', creator, owner, ram],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not buy RAM\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get but RAM. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def stakeNet():
    creator = app.tabPanel.accountCreator.get()
    owner = app.tabPanel.accountOwner.get()
    net = app.tabPanel.net.get()
    cpu = app.tabPanel.cpu.get()
    # cleos system delegatebw accountname1 accountname2 "1 SYS" "1 SYS"
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'system', 'delegatebw', creator, owner, net, cpu],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not stake NET\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get stake NET. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def createAccount():
    creator = app.tabPanel.accountCreator.get()
    owner = app.tabPanel.accountOwner.get()
    activeKey = app.tabPanel.accountActiveKey.get()
    ownerKey = app.tabPanel.accountOwnerKey.get()
    cpu = app.tabPanel.cpu.get()
    net = app.tabPanel.net.get()
    ram = app.tabPanel.ram.get()
    permission = creator + '@active'
    # cleos -u http://IP-HERE:8888 system newaccount --stake-net "0.1000 EOS" --stake-cpu "0.1000 EOS" --buy-ram-kbytes 8 eosio myDesiredAccountName Public key Public key

    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'system', 'newaccount', creator, owner, ownerKey, activeKey, '--stake-net', net, '--stake-cpu', cpu, '--buy-ram', ram, '--transfer', '-p', permission],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not stake NET\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get stake NET. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def setWalletDir():
    stop = stopKeosd(False)
    run = runKeosd(False)
    app.outputPanel.logger(stop + '\n' + run)


def stopKeosd(flag):
    if flag:
        try:
            out = subprocess.run(cleos + ['wallet', 'stop'],
                timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not stop keosd\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not stop keosd. \n" + str(e)
        finally:
            app.outputPanel.logger(out)
    else:
        try:
            out = subprocess.run(cleos + ['wallet', 'stop'],
                                 timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not stop keosd\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not stop keosd. \n" + str(e)
        finally:
            return out


def runKeosd(flag):
    # TODO rewrite function
    if flag:
        try:
            out = os.spawnl(os.P_NOWAIT, 'keosd', '--wallet-dir', '~/eosio-wallet')
        except Exception as e:
            print('Could not run keosd by default path: ' + str(e))
            out = "Could not run keosd by default path: " + str(e)
        finally:
            app.outputPanel.logger(str(out))
    else:
        try:
            out = os.spawnl(os.P_NOWAIT, 'keosd', '--wallet-dir', app.tabPanel.walletDir.get())
        except Exception as e:
            print('Could not run keosd ' + str(e))
            out = "Could not run keosd " + str(e)
        finally:
            return str(out)


# Currency operations
def getBtcBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = btc.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get BTC balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get BTC balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getEthBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = eth.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get ETH balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get ETH balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getXmrBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = xmr.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get XMR balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get XMR balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getNeoBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = neo.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get NEO balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get NEO balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getLtcBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = ltc.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get LTC balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get LTC balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getBchBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = bch.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get BCH balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get BCH balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)


def getDashBalance(address):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT)
    try:
        out = dash.getBalance(address)
    except RuntimeError as e:
        print(e)
        out = 'Can not get DASH balance. Timeout error.\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Can not get DASH balance.\n' + str(e)
    finally:
        signal.alarm(0)
        app.outputPanel.logger(out)
