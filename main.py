from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/ВАШ_API_KEY"
web3 = Web3(Web3.HTTPProvider(infura_url))

print("Подключен:", web3.is_connected())

address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

balance_wei = web3.eth.get_balance(address)

balance_eth = web3.from_wei(balance_wei, "ether")
print(f"Баланс: {balance_eth} ETH")
