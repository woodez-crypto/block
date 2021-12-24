from web3 import Web3

ganache_url = "http://192.168.2.222:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0xA503bD1dC22Fe075dC8096123C8eca07E57509c6' # Fill me in
account_2 = '0x57Ee7B3C7838c789591e3DdCFb5044d1aA523AEF' # Fill me in


private_key = '0xe14c440deb344ccc101438c61fa840babf5d36657f9db851b9f6c77b594a6da9' # Fill me in

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

balance1 = web3.eth.get_balance(account_1)
balance2 = web3.eth.get_balance(account_2)

print ("Account1 Balance: {}".format(web3.fromWei(balance1, "wei")))
print ("Account2 Balance: {}".format(web3.fromWei(balance2, "ether")))
# print(web3.fromWei(balance, "ether"))
