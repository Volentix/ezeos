# create project dir
mkdir myproject
cd myproject

# create virtual environment using Python 3.7 and activate or skip to the next step for Python 3.6
python3.7 -m venv venv
source venv/bin/activate

# create virtual environment using Python 3.6 and activate
python3.6 -m venv venv
source venv/bin/activate

(venv) pip install neo-python


np-prompt

create wallet {wallet_path}
open wallet {wallet_path}
wallet close

wallet (verbose)
wallet rebuild (start block)
wallet create_addr {number of addresses}
wallet delete_addr {addr}

export wif {address}
import wif {wif}

export nep2 {address}
import nep2 {nep2_encrypted_key}

send {assetId or name} {address} {amount} (--from-addr={addr}) (--fee={priority_fee}) (--owners=[{addr}, ...]) (--tx-attr=[{"usage": <value>,"data":"<remark>"}, ...])
