from fastapi import APIRouter, Depends

from services.containers.database_container import DatabaseContainer
from services.containers.service_container import ServiceContainer
from services.signal.pin_control_service import PinControlService

router = APIRouter()

services = ServiceContainer.container()
db = DatabaseContainer.container()


@router.post('/{board_name}/{pin_name}/on')
def digital_on(
        board_name: str, pin_name: str,
        collection=Depends(db.get_pin_collection),
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.on(collection, board_name, pin_name)


@router.post('/{board_name}/{pin_name}/off')
def digital_off(
        board_name: str, pin_name: str,
        collection=Depends(db.get_pin_collection),
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.off(collection, board_name, pin_name)


@router.post('/{board_name}/{pin_name}')
def analog_set_value(
        board_name: str, pin_name: str, value: float,
        collection=Depends(db.get_pin_collection),
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.set_value(collection, board_name, pin_name, value)
