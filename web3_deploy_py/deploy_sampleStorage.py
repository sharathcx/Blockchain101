from solcx import compile_standard
import json
from web3 import Web3
from dotenv import load_dotenv

# import solcx
# solcx.install_solc('0.6.0')

with open("./simplestorage.sol", "r") as file:
    simple_storage_file = file.read()

# Setting Blockchain
w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/eab9f2aff8984a57ac11c6043cf87d78"))  
chainID = 11155111
myAddress = "0xf22756f18828b857c8252b4B735907fA9Ba24C9b"
privatKey = "f8bebbb1097a07223bc9b265f0f747501760accdefdf53822700558ec075b047"

# Compile the solidity code

compiled_sol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"simplestorage.sol":{"content":simple_storage_file}},
        "settings":{
            "outputSelection":{
                "*":{
                    "*":["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version ="0.6.0"
)

# print(compiled_sol)

with open("comiledcode.json", "w") as file:
    json.dump(compiled_sol, file)

# Get bytcode
bytecode = compiled_sol["contracts"]["simplestorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# Get abi
abi = compiled_sol["contracts"]["simplestorage.sol"]["SimpleStorage"]["abi"]


# Deploy to Ganache
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.get_transaction_count(myAddress)
print(nonce)

# Build a transaction
transaction = SimpleStorage.constructor().build_transaction({"chainId":chainID, "from":myAddress, "nonce":nonce})

# Sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, privatKey)

# Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

# wait for transaction to finish
tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)

# Creating a SimpleStorage Contract
simple_storage = w3.eth.contract(tx_reciept.contractAddress, abi=abi)
print(simple_storage.functions.retrive().call())
print(simple_storage.functions.store(15).call())
# This is just a function call . It won't make any changes in the chain. So we need to make a transaction for that
print(simple_storage.functions.retrive().call())

transaction_store = simple_storage.functions.store(15).build_transaction({"chainId":chainID, "from":myAddress, "nonce":nonce+1})
signed_transaction_store = w3.eth.account.sign_transaction(transaction_store, privatKey)
tx_hash_store = w3.eth.send_raw_transaction(signed_transaction_store.rawTransaction)
tx_reciept_store = w3.eth.wait_for_transaction_receipt(tx_hash_store)
print(simple_storage.functions.retrive().call())
