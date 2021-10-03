from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helper import get_account, deploy_mocks, is_development

def deploy():
    account = get_account()
    if is_development() == False:
        eth_usd_price_feed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        eth_usd_price_feed = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        eth_usd_price_feed, 
        {"from": account}, 
        publish_source=config["networks"][network.show_active()]["verify"]
        )
    print(f"Contract Deploy on address: {fund_me.address}")

def main():
    deploy()