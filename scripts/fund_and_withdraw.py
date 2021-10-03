from brownie import FundMe, MockV3Aggregator
from scripts.helper import get_account

ACCOUNT = get_account()

def fund():
    fund_me = FundMe[-1]
    entrance_free = fund_me.getEntranceFee()
    fund_me.fund({"from": ACCOUNT, "value": entrance_free})

def withdraw():
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": ACCOUNT})

def main():
    fund()
    withdraw()