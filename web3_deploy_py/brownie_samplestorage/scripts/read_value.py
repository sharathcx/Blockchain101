from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # get most recent one
    print(simple_storage.retrive())


def main():
    read_contract()