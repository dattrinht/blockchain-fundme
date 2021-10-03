from brownie import MockV3Aggregator, network, config, accounts

DECIMALS = 8
STARTING_PRICE = 281700000000

def get_account():
    if is_development():
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

def is_development():
    return network.show_active() in ["development", "ganache-local"]