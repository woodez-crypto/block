from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/9be35a78f8d64b7aa7735840f9ed9e0c"
web3 = Web3(Web3.HTTPProvider(infura_url))

# print(web3.isConnected())

# print(web3.eth.blockNumber)

# Fill in your account here
balance = web3.eth.get_balance("0x3D27Da1Ed4F2C35F593a3Baf7367a693152daf4C")
print(web3.fromWei(balance, "wei"))