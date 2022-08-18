import os
import json
from brownie import accounts, Contract
from dotenv import load_dotenv
from app.db import schemas
from datetime import datetime , timedelta
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.base import STATE_STOPPED

load_dotenv()

scheduler = BlockingScheduler()


def call_scheduler(auction: schemas.AuctionEndBase):
    duration = (auction.auction_start_time - auction.auction_created_time) + timedelta(hours=auction.duration)
    auction_end_time: datetime = datetime.utcnow() + timedelta(seconds=duration.total_seconds())
    scheduler.add_job(auction_end, 'date', run_date = auction_end_time, args = [auction])
    if not scheduler.state != STATE_STOPPED:
        scheduler.start()

def auction_end(auction: schemas.AuctionEndBase):
    abi_dir = "{}/build/contracts/{}.json".format(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.getenv("AUCTION_MARKET_CONTRACT_NAME")
    )
    if abi_dir.is_exist():
        file = open(abi_dir)
        abi = json.loads(file.read())["abi"] 
        contract_owner = accounts.add(os.getenv('PRIVATE_KEY'))
        auction_contract = Contract.from_abi(
            os.getenv("AUCTION_MARKET_CONTRACT_NAME"), 
            os.getenv('AUCTION_MARKET_CONTRACT_ADDRESS'), 
            abi 
        )
        auction_contract.auctionEnd(
            auction.auction_id,
            auction.token_address,
            auction.nft_contract,
            {"from": contract_owner}
        )
    else:
        return "Missing abi file"
    # scheduler.shutdown(wait=False)