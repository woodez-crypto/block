import json
from web3 import Web3

# Set up web3 connection with Ganache
# 0x9D2B3a54a45001bf9d749ab6B0e9f52008298008
# 0x9D2B3a54a45001bf9d749ab6B0e9f52008298008
# 0x840bFF2C87864D9Fd5EBf25877A7cb3861274c0b
ganache_url = "http://192.168.2.222:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

address = web3.toChecksumAddress('0xCA738e45E92ea5aCA76a1dE79c7c83fB06A33c35')
contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())