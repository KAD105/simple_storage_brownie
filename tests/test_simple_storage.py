from brownie import SimpleStorage, accounts, network, config


def test_deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    assert starting_value == expected


def test_updating():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected_value = 15
    simple_storage.store(expected_value, {"from": account})

    assert simple_storage.retrieve() == expected_value
