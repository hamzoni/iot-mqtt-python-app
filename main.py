from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.monitor import api_monitor as monitor
from api.signal import api_signal as signal
from services.queues.queue_subscribe_service import QueueSubscribeService

# run queue service
QueueSubscribeService.run()

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

app.include_router(
    signal.router,
    prefix='/signal',
    tags=['Signal'],
)


@app.get('/?')
def health_check():
    return 'OK'
