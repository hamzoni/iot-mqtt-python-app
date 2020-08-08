from fastapi import APIRouter

from api.monitor.endpoints import monitor_moisture_endpoints as MME
from api.monitor.endpoints import monitor_temperature_endpoints as MTE

router = APIRouter()

router.include_router(
    MTE.router,
    prefix='/temperature',
    tags=['Temperature']
)

router.include_router(
    MME.router,
    prefix='/moisture',
    tags=['Moisture']
)
