from constants import *
import subprocess
import json
import os
from dotenv import load_dotenv
load_dotenv()
mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')
print(mnemonic)
def derive_wallets(coin,numderive,mnemonic):
    command =f'php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json --coin={coin} --numderive={numderive}'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys
coins = {BTCTEST: derive_wallets(BTCTEST,3,mnemonic),
         ETH:derive_wallets(ETH,3,mnemonic)}
print(coins[BTCTEST][0]['privkey'])

#constants
BTC = 'btc'
ETH = 'eth'
BTCTEST = 'btc-test'
