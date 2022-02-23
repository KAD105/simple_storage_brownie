from brownie import accounts


def simple_storage_deplpoy():
    # account = accounts[0]
    account = accounts.load("freecodecamp-account")
    print(account)


def main():
    simple_storage_deplpoy()
