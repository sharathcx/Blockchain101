from brownie import accounts, config, SimpleStorage, network
import os

def get_account():
    if(network.show_active=="development"):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("sepoliatest") one way
    # account = accounts.add(os.getenv("PRIVAT_KEY")) exports from .env file
    # account = accounts.add(config["wallets"]["from_key"]) # adding from yaml file
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrive()
    print(stored_value)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_value = simple_storage.retrive()
    print(updated_value)

def main():
    deploy_simple_storage()