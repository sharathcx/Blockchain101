from solcx import compile_standard
import json
from web3 import Web3
# import solcx
# solcx.install_solc('0.6.0')

with open("./simplestorage.sol", "r") as file:
    simple_storage_file = file.read()

# Setting Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))  
chainID = 1337
myAddress = "0xb113Cc746050f7b23abaC3Ce579CB9D25ea6383f"
privatKey = "0xa7a64330a5a3829a195437a21ffb92b8abd62edf786e000ddc238d16aac1ebe0"

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
signed_transaction = w3.eth.account.sign_transaction(transaction, privat_key = privatKey)

