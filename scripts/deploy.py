from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account, get_price_feed


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to FundMe contract
    # if we are on the rinkeby chain, use the associated address
    # otherwise, deploys mocks
    price_feed = get_price_feed()
    fund_me = FundMe.deploy(
        price_feed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
