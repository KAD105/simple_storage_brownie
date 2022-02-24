from brownie import accounts, config, SimpleStorage


def simple_storage_deplpoy():
    account = accounts[0]
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    simple_storage_deplpoy()
