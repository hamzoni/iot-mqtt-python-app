from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from services.queues.queue_service import QueueService

from api.monitor import api_monitor as monitor

# run queue service
QueueService.run()

# run web service
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    # expose_headers=['x-total-items', 'x-file-name']
)

app.include_router(
    monitor.router,
    prefix='/monitor',
    tags=['Monitor'],
)
