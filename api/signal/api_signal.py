from fastapi import APIRouter

from api.signal.endpoints import signal_pin_control_endpoints as SPC
from api.signal.endpoints import signal_pin_registry_endpoints as SPR

router = APIRouter()

router.include_router(
    SPC.router,
    prefix='/pin-control',
    tags=['Pin Control']
)

router.include_router(
    SPR.router,
    prefix='/pin-registry',
    tags=['Pin Registry']
)
