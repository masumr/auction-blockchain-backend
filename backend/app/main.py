from typing import Optional

import uvicorn
from fastapi import FastAPI, Depends
from fastapi_pagination import add_pagination


from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import routers
from app.core import config


# scheduler = BackgroundScheduler()

app = FastAPI(
    title=str(config.PROJECT_NAME), docs_url="/api/docs", openapi_url="/api"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    routers.auction_router,
    prefix=config.MAP_URL('auction'),
    tags=["Auction"]
)



# add_pagination(app)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8860)
