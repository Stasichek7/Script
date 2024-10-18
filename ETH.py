from web3 import Web3

ankr_url = "https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(ankr_url))

if web3.is_connected():
    print("Підключено до Ethereum")
    wallet_address = "0xf2F305D14DCD8aaef887E0428B3c9534795D0d60"
    balance_wei = web3.eth.get_balance(wallet_address)
    balance_ether = web3.from_wei(balance_wei, 'ether')

    print(f"Баланс гаманця {wallet_address}: {balance_ether} ETH")
else:
    print("Не вдалося підключитися до мережі Ethereum")
