from fastapi import APIRouter, Depends

from api.signal.models.pin_model import Pin
from services.container import ServiceContainer
from services.signal.pin_registry_service import PinRegistryService

router = APIRouter()

services = ServiceContainer.container()


@router.get('')
def list_all(
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.list_all()


@router.post('')
def add(
        pin: Pin,
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return {
        'result': service.add(pin)
    }


@router.delete('/{board_name}/{pin_name}')
def remove(
        board_name: str, pin_name: str,
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.remove(board_name, pin_name)
