from fastapi import APIRouter, Depends

from services.container import ServiceContainer
from services.signals.entities import Pin
from services.signals.pin_registry_service import PinRegistryService

router = APIRouter()

services = ServiceContainer.container()


@router.get('')
def list_all(
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.list_all()


@router.post('')
def add(
        record: Pin,
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.add(record)


@router.delete('{board_name}/{pin_name}')
def remove(
        board_name: str, pin_name: str,
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.remove(board_name, pin_name)
