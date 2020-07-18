from fastapi import APIRouter

from api.monitor.endpoints import monitor_temperature_endpoints as MTE

router = APIRouter()

router.include_router(
    MTE.router,
    prefix='/temperature',
    tags=['Temperature']
)
