from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])


def get_price_feed():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        # Deploy mock
        price_feed_address = deploy_mocks()

    return price_feed_address


def deploy_mocks():
    print(f"Active network is {network.show_active()}")
    print("Deploying mocks...")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks deployed!")

    return price_feed_address
