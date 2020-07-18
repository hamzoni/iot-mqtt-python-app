from fastapi import APIRouter, Depends

from services.container import ServiceContainer
from services.signals.pin_control_service import PinControlService

router = APIRouter()

services = ServiceContainer.container()


@router.post('digital/{board_name}/{pin_name}/on')
def digital_on(
        board_name: str, pin_name: str,
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.on(board_name, pin_name)


@router.post('digital/{board_name}/{pin_name}/off')
def digital_off(
        board_name: str, pin_name: str,
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.off(board_name, pin_name)


@router.post('analog/{board_name}/{pin_name}')
def analog_set_value(
        board_name: str, pin_name: str, value: float,
        service: PinControlService = Depends(services.get_pin_control_service)
):
    return service.set_value(board_name, pin_name, value)
