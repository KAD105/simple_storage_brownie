from brownie import SimpleStorage, accounts, config

# reading the contract basesd on what has been saved into build/deployments/4
def read_contract():
    simple_storage = SimpleStorage[-1]
    # brownie already knows what the abi and address is, since it's been saved in build folder
    print(simple_storage.retrieve())


def main():
    read_contract()
