from fastapi import (
    APIRouter, 
    status,
    BackgroundTasks
)
from app.db.crud.auction import call_scheduler
from app.db import models, schemas

auction_router = ar = APIRouter()

@ar.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def auction_end(
    auction: schemas.AuctionEndBase,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(call_scheduler, auction)
    return "Successfully start auction"
    