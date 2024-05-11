from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrive()
    expected = 5
    #Assert
    assert starting_value == expected

def test_update_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    expected = 15
    simple_storage.store(expected, {"from":account})
    value = simple_storage.retrive()
    assert value == expected
