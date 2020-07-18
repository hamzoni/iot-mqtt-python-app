from fastapi import APIRouter

from api.monitor.endpoints import monitor_temperature_endpoints as MTE

router = APIRouter()
__api_v2_version__ = '/v1'

router.include_router(
    MTE.router,
    prefix='/temperature',
    tags=['Temperature Monitoring']
)
