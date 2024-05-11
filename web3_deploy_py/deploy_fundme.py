import json
from web3 import Web3
from solcx import compile_standard
import solcx


solcx.install_solc('0.6.0')
with open("fundme.sol", "r") as file:
    sourceFundMe = file.read()

w3 = Web3.HTTPProvider("https://sepolia.infura.io/v3/eab9f2aff8984a57ac11c6043cf87d78")
chainID = 11155111
myAddress = "0xf22756f18828b857c8252b4B735907fA9Ba24C9b"
privatKey = "f8bebbb1097a07223bc9b265f0f747501760accdefdf53822700558ec075b047"

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"fundme.sol": {"content": sourceFundMe}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.6.0"
)

with open("fundme.json", "w") as file:
    json.dump(compiled_sol, file)

# bytecode = compiled_sol["contracts"]["fundme.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]



