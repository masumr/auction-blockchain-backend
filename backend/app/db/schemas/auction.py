from pydantic import BaseModel, validator
from datetime import datetime, timedelta


class AuctionEndBase(BaseModel):
    auction_id: str
    token_address: str
    nft_contract: str
    auction_created_time: datetime = datetime.today()
    auction_start_time: datetime = datetime.today() 
    duration: float = 1.0
    
    
    
